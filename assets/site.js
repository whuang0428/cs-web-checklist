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
        foldAnswers();
        prepareTables();
        constrainPagination(path);
        prepareSearch();
      }, 0);
    });
  };
})();
