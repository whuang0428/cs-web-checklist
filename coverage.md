# Coverage and Maintenance Status

This maintainer page records the current information architecture and assessment inventory. It is intentionally excluded from student navigation and search.

## Syllabus Baselines

| Course area | Baseline | Student hub |
|---|---|---|
| IGCSE 0478 | 2026–2028, Version 5 | `ig-0478/README.md` |
| AS 9618 | 2027–2029, Version 2, Sections 1–12 | `as-9618/README.md` |
| A Level 9618 — A2 / Year 2 | 2027–2029, Version 2, Sections 13–20 | `a2-9618/README.md` |

## Current Inventory

| Course | Chapters | Complete original practice |
|---|---:|---|
| IGCSE 0478 | 1–10 | Paper 1 Set A; Paper 2 Sets A and B |
| AS 9618 | 1–12 | Paper 1 Set A; Paper 2 Sets A and B |
| A Level 9618 — A2 / Year 2 | 13–20 | Paper 3 Sets A and B; Paper 4 Sets A and B |

All 30 chapter pages carry course/Paper/version metadata and the same editorial contract: Official Syllabus Checklist, Core Knowledge, Required Ideas and Exam Language, Common Confusions, Worked Examples, 10-Mark Quick Check with answers, 20-Mark Exam Practice with a mark scheme, and Final Revision Checklist.

## Navigation Contract

- The root cover and fallback home link only to the three course hubs and shared student resources.
- Each course loads its own `_sidebar.md`; course pagination must not cross into another level.
- `exam-technique.md` owns the stable Command Words anchor.
- `syllabus-versions.md` records the examination cycles used by the site.
- Search uses an explicit list of student pages in `index.html`.
- This file remains maintainer-only.

## Runtime and Visual Contract

- Docsify, Markdown, CSS and local native JavaScript only; no build system or account/progress layer.
- `assets/site.js` applies course identity, answer disclosure, focusable table scrolling and course-bounded pagination.
- `assets/style.css` defines the IG blue, AS teal and A2 amber tokens, the approximately 76-character reading measure, responsive layout and A4 print rules.
- Answers remain collapsed by default. Printing a collapsed page produces a student version; opening the answer disclosure before printing includes the mark scheme.

## Verification

Run before any publication decision:

```bash
python3 scripts/check_site.py
git diff --check
```

Then verify the cover, all three hubs, representative theory/practical/Mermaid pages, search, course sidebars, pagination, answer disclosure, wide tables and A4 print output at desktop and mobile widths.

## Maintenance Priorities

1. Keep every practice set independent; do not create new sets by rewording an existing scenario.
2. Recheck syllabus versions and Paper 4 permitted languages when Cambridge publishes a new cycle.
3. Preserve keyboard, contrast, mobile, print, Mermaid and long-code/table accessibility.
4. Keep public wording student-facing and original; do not add teacher-only or trend-ranking material.
