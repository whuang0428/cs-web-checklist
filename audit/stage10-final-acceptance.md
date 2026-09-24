# Stage 10 — Final Internal Acceptance

Date: 2026-09-24

## Decision

**Pass for internal review of this working tree; not a publication approval.** The three course registers have traceable teaching, practice and answer evidence for every currently registered syllabus objective. The site does **not** meet, and does not claim to meet, the different proposition that every sentence was extracted from an official Cambridge mark scheme (MS). Student-facing explanations and original practice remain project-authored paraphrases.

## Evidence closed by Stages 5–9

| Course | Current site baseline | Registered objectives | Final semantic status |
|---|---|---:|---|
| IGCSE 0478 | 2026–2028, Version 6 | 133 | 133 verified |
| AS 9618 | 2027–2029, Version 2, Sections 1–12 | 178 | 178 verified |
| A2 9618 | 2027–2029, Version 2, Sections 13–20 | 83 | 83 verified |
| **Total** | | **394** | **394 verified** |

The objective-level links are in `coverage.md`; the finding, repair and official-source references are in the Stage 5–7 semantic CSVs and summaries. `audit/source-manifest.csv` registers 18 Cambridge documents: four current-authority syllabus/update/pseudocode documents and 14 supporting public mark schemes, specimen mark schemes or examiner reports. The supporting samples are not a complete MS corpus and do not override the applicable syllabus.

Stage 8 regression gates passed on 2026-09-24: `python3 scripts/check_site.py`, 29 rejecting mutation controls in `python3 scripts/test_check_site_negative.py`, the documented passing semantic-blind-spot control, and `git diff --check`. The site check validates all 30 chapter files, course navigation and search paths, source/audit registration, teaching–question–answer links, review marks, A/B independence and executable Python/Java examples. These are structural and executable safeguards, not a proof that every explanation is semantically correct.

Stage 9 rendered-browser acceptance passed in local Chrome/Playwright at 1440px and 390px: the cover, all three course hubs and two representative chapters per course loaded; course identity, sidebar, previous/next links, search and result navigation, keyboard answer disclosure, Mermaid rendering, tables and code containers worked. No page-width overflow or repeatable console/page/request error remained in the final run. Mermaid and long code may require horizontal scrolling *inside* their containers on mobile. This was a representative visual sample, not a manual inspection of every page.

## Claim boundaries and residual risk

1. **Syllabus coverage:** all 394 registered objectives have reviewed evidence, but a newly issued syllabus amendment or a later content edit can invalidate a row. The source manifest records the audit snapshot dated 2026-09-21; this stage did not repeat the external document download/hash review or check for a newer publication.
2. **MS provenance:** original explanations, questions and indicative marking points are not official Cambridge MS text. An `MS-aligned explanation` label requires a registered source ID; an unlabelled paragraph is not individually certified against an MS. “All wording comes from official MS” is therefore unsupported and must not be used in site or release claims.
3. **Automation limit:** the negative suite deliberately demonstrates that semantically diluted prose can still pass structural checks. Material content changes require renewed human comparison with the relevant official syllabus and cited evidence.
4. **Browser limit:** Stage 9 sampled six of 30 chapters. Its clean result cannot certify every route, browser or device.

## Handoff

- Keep this as an uncommitted local review candidate until the user reviews the changes.
- Before any publication, recheck the current official syllabus/update pages for the intended examination years, rerun the checks, and obtain explicit approval for the actual commit/push/deployment step.
- Do not present the site as an official Cambridge publication or its original answers as official mark schemes.
