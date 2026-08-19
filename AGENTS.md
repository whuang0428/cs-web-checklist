# AGENTS.md

This file is for AI coding agents and maintainers working in this repository. Read it before editing, then read `README.md`, `_sidebar.md`, and any affected chapter files.

## Project

`cs-web-checklist` is a Docsify-style static revision website for Computer Science checklist content.

Repository root: the directory containing this `AGENTS.md` file. Do not rely on a machine-specific absolute path.

The site covers:

- IGCSE Computer Science 0478.
- AS Computer Science 9618.
- A2 Computer Science 9618.

## Stack

- Static HTML and Markdown.
- Docsify loaded from CDN in `index.html`.
- Docsify search plugin.
- Docsify pagination plugin.
- Mermaid and docsify-mermaid from CDN.
- Custom CSS in `assets/style.css`.

There is no npm package, build step, React app, or Vite config in this repository. Do not add one unless the user explicitly asks.

## Important Files

- `index.html`: Docsify runtime configuration and CDN scripts.
- `README.md`: concise no-script root fallback.
- `_coverpage.md`: cover-only course chooser.
- `_sidebar.md`: root course/shared-resource navigation.
- `ig-0478/README.md`, `as-9618/README.md`, `a2-9618/README.md`: course hubs.
- Each course folder's `_sidebar.md`: course-scoped navigation.
- `assets/style.css`: custom styling.
- `assets/site.js`: course identity, answer disclosure, table and pagination behaviour.
- `exam-technique.md`: exam technique and the stable Command Words anchor.
- `syllabus-versions.md`: active syllabus-cycle record.
- `coverage.md`: maintainer-only inventory; exclude it from student navigation/search.
- `ig-0478/chapter-*.md`: IGCSE 0478 chapters.
- `ig-0478/paper-1-review*.md`: two independent original 75-mark IGCSE Paper 1 reviews.
- `ig-0478/paper-2-review*.md`: two original 75-mark IGCSE Paper 2 mixed reviews.
- `as-9618/chapter-*.md`: AS 9618 chapters.
- `as-9618/paper-1-review*.md`: two independent original 75-mark AS Paper 1 reviews.
- `as-9618/paper-2-review*.md`: two original 75-mark AS 9618 Paper 2 mixed reviews.
- `a2-9618/chapter-*.md`: A2 9618 chapters.
- `a2-9618/paper-3-review*.md`: two original 75-mark A2 9618 Advanced Theory reviews.
- `a2-9618/paper-4-review*.md`: two original 75-mark A2 9618 Java practical reviews.

Do not edit `.git`, generated browser caches, or temporary files.

## Local Preview

Because Docsify fetches Markdown files, prefer serving the folder over opening `index.html` directly:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/
```

If another server already uses port 8000, choose a different port.

## Content Structure

Current course hubs and sidebars:

- `IGCSE 0478`
  - `ig-0478/chapter-1.md` through `chapter-10.md`
  - `ig-0478/paper-1-review.md`
  - `ig-0478/paper-1-review-2.md`
  - `ig-0478/paper-2-review.md`
  - `ig-0478/paper-2-review-2.md`
- `AS 9618`
  - `as-9618/chapter-1.md` through `chapter-12.md`
  - `as-9618/paper-1-review.md`
  - `as-9618/paper-1-review-2.md`
  - `as-9618/paper-2-review.md`
  - `as-9618/paper-2-review-2.md`
- `A2 9618`
  - `a2-9618/chapter-13.md` through `chapter-20.md`
  - `a2-9618/paper-3-review.md`
  - `a2-9618/paper-3-review-2.md`
  - `a2-9618/paper-4-review.md`
  - `a2-9618/paper-4-review-2.md`

When adding or renaming pages, update the relevant course hub/sidebar and the explicit search paths in `index.html`. Keep the root navigation at course level.

## Maturity And Improvement Priorities

This repository is a revision checklist and marked-practice hub. It should not be presented as a full textbook, full lesson sequence or complete past-paper archive.

Already addressed in the current baseline:

- The root page is a cover-only course chooser; three course hubs and course-specific sidebars separate the levels.
- `coverage.md` is maintainer-only; `exam-technique.md` and `syllabus-versions.md` are shared student resources.
- A dependency-free structural checker and GitHub Actions workflow validate chapter inventory, editorial contracts, versions, headings, links, scoped navigation, explicit search paths, practice totals, A/B independence, runtime hooks and pinned CDN versions.
- Student-facing chapter headings use syllabus-aligned wording instead of `Trend-Based` or `Past Paper Focus` entry titles.
- Teacher-only sections have been removed from student-facing pages.
- All 30 chapters use the shared editorial contract and course/Paper/version metadata.
- IGCSE 0478 checklist coverage includes Chapters 1-10 and two independent 75-mark Paper 1 sets.
- IGCSE Chapters 7-10 include syllabus maps, worked examples, 10-mark checks, 20-mark practice and full answers.
- Two original 75-mark IGCSE Paper 2 mixed reviews and mark schemes cover Topics 7-10.
- AS 9618 checklist coverage includes Chapters 1-12 and two independent 75-mark Paper 1 sets.
- AS Chapters 9-12 include syllabus maps, worked examples, 10-mark checks, 20-mark practice and full answers.
- Two original 75-mark AS Paper 2 mixed reviews and mark schemes cover Sections 9-12.
- A2 9618 checklist coverage now includes Chapters 13-20.
- A2 Chapters 19-20 include syllabus maps, executable Java examples, pseudocode planning, worked examples, 10-mark checks and 20-mark practice.
- Two independent original 75-mark A2 Paper 3 reviews cover Sections 13-20.
- Two original 75-mark A2 Paper 4 Java practicals and reference mark schemes cover Sections 19-20.

Remaining highest-priority improvements:

1. Keep all practice sets independent and avoid duplicating scenarios merely to increase page count.
2. Keep practical Java examples executable and preserve pseudocode across all three course levels.
3. Maintain keyboard, contrast, mobile and long-code-block accessibility.
4. Keep recent-paper references as supporting evidence, but do not make them the main page title or site positioning.
5. Do not add teacher notes, teaching guides, classroom-management advice, or teacher-only appendices to public pages.

## Content Style

Write for students revising Computer Science.

Good checklist pages should be:

- syllabus-aligned
- concise but complete enough for revision
- organized with clear headings
- focused on mark-scheme language and common mistakes
- written in original wording
- suitable for quick scanning before practice questions

Use tables, bullet lists, short explanations, and examples where they improve revision value.

Do not copy official exam questions, markschemes, textbook pages, screenshots, or long official text. You may align structure and emphasis with official syllabuses, but public content must be original.

## Markdown And Docsify Rules

- Keep heading levels consistent; each chapter should have one clear `#` title.
- Use relative links that work from Docsify routes.
- Avoid raw HTML inside chapter pages unless existing styling or layout needs it.
- Mermaid diagrams are allowed if they render clearly in Docsify.
- If Mermaid syntax is added, verify the diagram renders in the browser.
- Keep `_sidebar.md` simple and readable.

## Verification

Run the dependency-free structural checks for every change:

```bash
python3 scripts/check_site.py
```

For Markdown-only edits:

```bash
python3 -m http.server 8000
```

Then manually check:

- Home page loads.
- Sidebar loads.
- Search box works.
- Edited chapter route opens.
- Previous/next pagination still works.
- Mermaid diagrams render if touched.
- Mobile width does not cause table or code overflow.

For CSS or `index.html` changes, check multiple course pages and mobile width.

## Working Rules

- Check `git status --short` before editing.
- Preserve user changes and do not revert unrelated work.
- Keep this repository simple; prefer Markdown/CSS/Docsify changes over new tooling.
- Do not introduce package managers, generated build output, or framework migrations unless explicitly requested.
- Do not push, publish, or deploy unless the user explicitly asks.
