# AGENTS.md

This file is for AI coding agents and maintainers working in this repository. Read it before editing, then read `README.md`, `_sidebar.md`, and any affected chapter files.

## Project

`cs-web-checklist` is a Docsify-style static revision website for Computer Science checklist content.

Local path:

```bash
/Users/kw/Projects/cs-web-checklist
```

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
- `README.md`: home page and course cards.
- `_coverpage.md`: cover page.
- `_sidebar.md`: navigation structure.
- `assets/style.css`: custom styling.
- `ig-0478/chapter-*.md`: IGCSE 0478 chapters.
- `as-9618/chapter-*.md`: AS 9618 chapters.
- `a2-9618/chapter-*.md`: A2 9618 chapters.

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

Current sidebar sections:

- `IGCSE 0478`
  - `ig-0478/chapter-1.md` through `chapter-10.md`
- `AS 9618`
  - `as-9618/chapter-1.md` through `chapter-12.md`
- `A2 9618`
  - `a2-9618/chapter-13.md` through `chapter-20.md`

When adding or renaming pages, update `_sidebar.md` and any links in `README.md`.

## Maturity And Improvement Priorities

This repository is useful as a revision checklist, but it should not be presented as a complete Cambridge Computer Science course until coverage gaps are fixed.

Already addressed in the current baseline:

- The home page, cover page, and sidebar link to `coverage.md`.
- Student-facing chapter headings use syllabus-aligned wording instead of `Trend-Based` or `Past Paper Focus` entry titles.
- Teacher-only sections are labelled as `Teacher Appendix` and marked optional for students.
- IGCSE 0478 checklist coverage now includes Chapters 1-10.
- AS 9618 checklist coverage now includes Chapters 1-12.
- A2 9618 checklist coverage now includes Chapters 13-20.

Remaining highest-priority improvements:

1. Deepen the newly added IGCSE Paper 2, AS Paper 2 and A2 Paper 4 chapters with more worked examples and mixed practice sets.
2. Add end-of-section review pages for IGCSE, AS and A2.
3. Add a lightweight link/checklist verification workflow before publishing, even if the site remains a no-build Docsify project.
4. Keep recent-paper references as supporting evidence, but do not make them the main page title or site positioning.

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
