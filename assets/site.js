(function () {
  'use strict';

  var courseRoutes = {
    '/ig-0478/': { className: 'course-ig', label: 'IGCSE 0478' },
    '/as-9618/': { className: 'course-as', label: 'AS 9618' },
    '/a2-9618/': { className: 'course-a2', label: 'A Level 9618' }
  };

  function currentCourse(path) {
    var route = Object.keys(courseRoutes).find(function (prefix) {
      return path.indexOf(prefix) === 0;
    });
    return route ? { prefix: route, data: courseRoutes[route] } : null;
  }

  function applyCourseIdentity(path) {
    document.body.classList.remove('course-ig', 'course-as', 'course-a2');
    var course = currentCourse(path);
    if (course) {
      document.body.classList.add(course.data.className);
    }
  }

  function prepareMain() {
    var main = document.querySelector('main');
    if (main) {
      main.id = 'main-content';
      main.tabIndex = -1;
    }
  }

  function isAnswerHeading(heading) {
    var text = heading.textContent.trim().toLowerCase();
    return text.indexOf('quick check answers') !== -1 ||
      text.indexOf('practice mark scheme') !== -1 ||
      text === 'mark scheme' || text.endsWith(' mark scheme') ||
      text.indexOf('model answers') !== -1;
  }

  function foldAnswers() {
    var section = document.querySelector('.markdown-section');
    if (!section) return;

    Array.from(section.querySelectorAll('h2, h3, h4')).forEach(function (heading) {
      if (!isAnswerHeading(heading) || heading.closest('details')) return;

      var level = Number(heading.tagName.substring(1));
      var details = document.createElement('details');
      details.className = 'answer-disclosure';
      var summary = document.createElement('summary');
      summary.textContent = heading.textContent.trim();
      details.appendChild(summary);
      heading.parentNode.insertBefore(details, heading);

      var node = heading;
      while (node) {
        if (node !== heading && node.matches && node.matches('h2, h3, h4')) {
          var nextLevel = Number(node.tagName.substring(1));
          if (nextLevel <= level) break;
        }
        var next = node.nextSibling;
        details.appendChild(node);
        node = next;
      }
    });
  }

  function headingLevel(heading) {
    return Number(heading.tagName.substring(1));
  }

  function isOverviewHeading(heading) {
    var text = heading.textContent.trim();
    return text.endsWith('Chapter at a Glance') || text.endsWith('Threats at a Glance');
  }

  function prepareChapterOverviews() {
    var content = document.querySelector('.markdown-section');
    if (!content) return;

    Array.from(content.querySelectorAll('h2, h3')).forEach(function (heading) {
      if (!isOverviewHeading(heading) || heading.dataset.overviewReady) return;

      var level = headingLevel(heading);
      var topicSelector = 'H' + (level + 1);
      var nodes = [];
      var node = heading.nextSibling;

      while (node) {
        if (node.nodeType === 1 && node.matches('hr')) break;
        if (node.nodeType === 1 && /^H[1-6]$/.test(node.tagName) && headingLevel(node) <= level) break;
        nodes.push(node);
        node = node.nextSibling;
      }

      if (!nodes.length) return;

      var overview = document.createElement('section');
      overview.className = 'chapter-overview';
      if (heading.id) overview.setAttribute('aria-labelledby', heading.id);
      heading.parentNode.insertBefore(overview, nodes[0]);
      nodes.forEach(function (item) { overview.appendChild(item); });

      var topics = Array.from(overview.children).filter(function (child) {
        return child.tagName === topicSelector;
      });

      topics.forEach(function (topicHeading, index) {
        var nextTopic = topics[index + 1] || null;
        var topic = document.createElement('article');
        topic.className = 'overview-topic';
        overview.insertBefore(topic, topicHeading);

        var topicNode = topicHeading;
        while (topicNode && topicNode !== nextTopic) {
          var next = topicNode.nextSibling;
          topic.appendChild(topicNode);
          topicNode = next;
        }

        Array.from(topic.querySelectorAll('p')).forEach(function (paragraph) {
          if (paragraph.querySelector('[lang="zh-CN"]')) {
            paragraph.classList.add('overview-cn-hint');
          }
          var strong = paragraph.querySelector(':scope > strong:first-child');
          if (strong && strong.textContent.trim() === 'Exam cue:') {
            paragraph.classList.add('overview-exam-cue');
          }
        });
      });

      var intro = Array.from(overview.children).find(function (child) {
        return child.tagName === 'P';
      });
      if (intro) intro.classList.add('overview-intro');
      heading.dataset.overviewReady = 'true';
    });
  }

  function restoreOverviewAnchor() {
    var queryStart = window.location.hash.indexOf('?');
    if (queryStart === -1) return;

    var routeParams = new URLSearchParams(window.location.hash.substring(queryStart + 1));
    var anchorId = routeParams.get('id');
    if (!anchorId) return;

    var target = document.getElementById(anchorId);
    if (!target) return;
    if (!target.classList.contains('legacy-anchor') && !isOverviewHeading(target)) return;

    window.setTimeout(function () {
      target.scrollIntoView({ block: 'start' });
    }, 700);
  }

  function prepareTables() {
    document.querySelectorAll('.markdown-section table').forEach(function (table, index) {
      if (table.parentElement.classList.contains('table-scroll')) return;

      var wrapper = document.createElement('div');
      wrapper.className = 'table-scroll';
      wrapper.tabIndex = 0;
      wrapper.setAttribute('role', 'region');
      wrapper.setAttribute('aria-label', 'Scrollable data table ' + (index + 1));
      table.parentNode.insertBefore(wrapper, table);
      wrapper.appendChild(table);

      var updateOverflow = function () {
        wrapper.classList.toggle('has-overflow', wrapper.scrollWidth > wrapper.clientWidth + 1);
      };
      updateOverflow();
      window.addEventListener('resize', updateOverflow, { passive: true });
    });
  }

  var mermaidObserver = null;
  var mermaidResizeReady = false;
  var mermaidSettleTimer = null;
  var mermaidFinalSettleTimer = null;

  function diagramHeading(container) {
    var node = container.previousElementSibling;
    while (node && !node.matches('h1, h2, h3, h4')) {
      node = node.previousElementSibling;
    }
    return node ? node.textContent.trim() : '';
  }

  function tightenMermaidSvg(svg) {
    if (!svg.matches('.flowchart, .statediagram, .erDiagram')) return;

    var root = svg.querySelector('g.root');
    var viewBox = svg.viewBox && svg.viewBox.baseVal;
    if (!root || !viewBox || viewBox.width <= 0 || viewBox.height <= 0) return;

    var bounds;
    try {
      bounds = root.getBBox();
    } catch (error) {
      return;
    }
    if (bounds.width <= 0 || bounds.height <= 0) return;

    var contentRatio = (bounds.width * bounds.height) / (viewBox.width * viewBox.height);
    var excessWidth = viewBox.width - bounds.width;
    var excessHeight = viewBox.height - bounds.height;
    if (contentRatio >= 0.3 || (excessWidth <= 64 && excessHeight <= 64)) return;

    var padding = 16;
    var width = bounds.width + padding * 2;
    var height = bounds.height + padding * 2;
    svg.setAttribute('viewBox', [
      bounds.x - padding,
      bounds.y - padding,
      width,
      height
    ].join(' '));
    svg.setAttribute('width', width);
    svg.setAttribute('height', height);
    svg.style.removeProperty('max-width');
  }

  function updateMermaidOverflow() {
    document.querySelectorAll('.markdown-section .mermaid').forEach(function (container, index) {
      var hasOverflow = container.scrollWidth > container.clientWidth + 1;
      container.classList.toggle('has-overflow', hasOverflow);

      if (hasOverflow) {
        var heading = diagramHeading(container);
        container.tabIndex = 0;
        container.setAttribute('role', 'region');
        container.setAttribute(
          'aria-label',
          heading ? 'Scrollable diagram: ' + heading : 'Scrollable diagram ' + (index + 1)
        );
        container.dataset.mermaidA11y = 'true';
      } else if (container.dataset.mermaidA11y) {
        container.removeAttribute('tabindex');
        container.removeAttribute('role');
        container.removeAttribute('aria-label');
        delete container.dataset.mermaidA11y;
      }
    });
  }

  function settleMermaidDiagrams() {
    document.querySelectorAll('.markdown-section .mermaid svg').forEach(tightenMermaidSvg);
    updateMermaidOverflow();
  }

  function scheduleMermaidSettle() {
    window.clearTimeout(mermaidSettleTimer);
    window.clearTimeout(mermaidFinalSettleTimer);
    mermaidSettleTimer = window.setTimeout(function () {
      var settle = function () {
        window.requestAnimationFrame(function () {
          window.requestAnimationFrame(function () {
            settleMermaidDiagrams();
            mermaidFinalSettleTimer = window.setTimeout(settleMermaidDiagrams, 160);
          });
        });
      };

      if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(settle, settle);
      } else {
        settle();
      }
    }, 0);
  }

  function prepareMermaidDiagrams() {
    var content = document.querySelector('.markdown-section');
    if (!content) return;

    if (mermaidObserver) mermaidObserver.disconnect();
    mermaidObserver = new MutationObserver(function (mutations) {
      var hasNewDiagram = mutations.some(function (mutation) {
        return Array.from(mutation.addedNodes).some(function (node) {
          return node.nodeType === 1 && (
            node.matches('.mermaid svg') ||
            (node.querySelector && node.querySelector('.mermaid svg'))
          );
        });
      });
      if (hasNewDiagram) scheduleMermaidSettle();
    });
    mermaidObserver.observe(content, { childList: true, subtree: true });

    if (!mermaidResizeReady) {
      window.addEventListener('resize', scheduleMermaidSettle, { passive: true });
      mermaidResizeReady = true;
    }
    scheduleMermaidSettle();
  }

  function constrainPagination(path) {
    var course = currentCourse(path);
    if (!course) return;

    var pagination = document.querySelector('.docsify-pagination-container');
    if (!pagination) return;

    pagination.querySelectorAll('a').forEach(function (link) {
      var href = link.getAttribute('href') || '';
      var normalized = href.replace(/^#/, '');
      if (normalized && normalized.indexOf(course.prefix) !== 0) {
        link.remove();
      }
    });

    if (!pagination.querySelector('.course-hub-return')) {
      var returnLink = document.createElement('a');
      returnLink.className = 'course-hub-return';
      returnLink.href = '#' + course.prefix;
      returnLink.textContent = 'Return to ' + course.data.label + ' hub';
      pagination.appendChild(returnLink);
    }
  }

  function decorateSearchResults() {
    document.querySelectorAll('.matching-post').forEach(function (result) {
      result.querySelectorAll('p').forEach(function (excerpt) {
        if (excerpt.dataset.searchExcerptCleaned) return;

        var rawText = excerpt.textContent || '';
        var hasLeadingEllipsis = /^\s*(?:\.\.\.|…)/.test(rawText);
        var hasTrailingEllipsis = /(?:\.\.\.|…)\s*$/.test(rawText);
        var fragments = rawText
          .replace(/<[^>]*>/g, '')
          .replace(/(?:^|\s)\/?[a-z][a-z0-9-]*>/gi, ' ')
          .replace(/\*{2,3}|__|`/g, '')
          .replace(/^\s*[-+]\s+/gm, '')
          .split(/(?:\.\.\.|…)+/)
          .map(function (fragment) {
            return fragment
              .replace(/^\/?[a-z][a-z0-9-]*>\s*/i, '')
              .replace(/^[\s+*.-]+|[\s+*.-]+$/g, '')
              .replace(/\s+/g, ' ')
              .trim();
          })
          .filter(Boolean);
        var uniqueFragments = [];

        fragments.forEach(function (fragment) {
          var key = fragment.toLowerCase();
          var duplicate = uniqueFragments.some(function (existing, index) {
            var existingKey = existing.toLowerCase();
            if (existingKey === key || (key.length > 15 && existingKey.indexOf(key) !== -1)) {
              return true;
            }
            if (existingKey.length > 15 && key.indexOf(existingKey) !== -1) {
              uniqueFragments[index] = fragment;
              return true;
            }
            return false;
          });
          if (!duplicate) uniqueFragments.push(fragment);
        });

        var cleanedText = uniqueFragments.slice(0, 3).join(' … ');
        if (hasLeadingEllipsis && cleanedText) cleanedText = '… ' + cleanedText;
        if (hasTrailingEllipsis && cleanedText) cleanedText += ' …';
        excerpt.textContent = cleanedText;
        excerpt.dataset.searchExcerptCleaned = 'true';
      });

      if (result.querySelector('.search-course-label')) return;
      var link = result.querySelector('a');
      var href = link ? link.getAttribute('href') || '' : '';
      var identity = href.indexOf('/ig-0478/') !== -1 ? 'IGCSE 0478' :
        href.indexOf('/as-9618/') !== -1 ? 'AS 9618' :
        href.indexOf('/a2-9618/') !== -1 ? 'A Level 9618 · A2' : 'Shared resource';
      var label = document.createElement('span');
      label.className = 'search-course-label';
      label.textContent = identity;
      result.insertBefore(label, result.firstChild);
    });
  }

  function prepareSearch() {
    var input = document.querySelector('.search input');
    if (!input || input.dataset.courseIdentityReady) return;
    input.dataset.courseIdentityReady = 'true';
    var panel = document.querySelector('.results-panel');
    if (panel && !panel.dataset.courseIdentityReady) {
      panel.dataset.courseIdentityReady = 'true';
      new MutationObserver(decorateSearchResults).observe(panel, {
        childList: true,
        subtree: true
      });
    }
    input.addEventListener('input', function () {
      window.setTimeout(decorateSearchResults, 80);
    });
  }

  window.csChecklistPlugin = function (hook, vm) {
    hook.doneEach(function () {
      window.setTimeout(function () {
        var path = vm.route.path || '/';
        prepareMain();
        applyCourseIdentity(path);
        prepareChapterOverviews();
        foldAnswers();
        prepareTables();
        prepareMermaidDiagrams();
        constrainPagination(path);
        prepareSearch();
        restoreOverviewAnchor();
      }, 0);
    });
  };
})();
