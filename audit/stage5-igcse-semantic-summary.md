# Stage 5 — IGCSE 0478 Semantic Audit

## Scope

- Course: Cambridge IGCSE Computer Science 0478
- Examination baseline: 2026–2028, syllabus Version 6
- Objectives audited: 133 of 133
- Content checked per objective: official requirement and notes, teaching coverage, practice evidence and answer evidence
- Assessment boundary checked: Paper 2 requires pseudocode except for the final 15-mark scenario, where Python, Visual Basic or Java may be used

## Sources

- Current authority: `0478-SYL-2026-2028-V6`
- Current update: `0478-UPD-2026-2028-V6`
- Supporting samples: `0478-MS-11-MJ24`, `0478-MS-21-MJ24`, `0478-ER-MJ24`, `0478-SMS-1B-2023`, `0478-SMS-2B-2023`
- All downloaded source hashes matched `audit/source-manifest.csv`.

## Findings Before Repair

| Status | Count |
|---|---:|
| verified | 85 |
| partial | 45 |
| missing | 0 |
| incorrect | 1 |
| unsupported_marking_claim | 0 |
| imprecise_evidence | 2 |
| **Total** | **133** |

The partial findings were mainly compound syllabus requirements whose teaching coverage existed but whose cited practice did not independently demonstrate every component. The single incorrect finding was an over-generalised DDoS/botnet statement. No student-facing claim was found that represented this site's original answers as official Cambridge mark-scheme wording.

## Repairs

- Added targeted syllabus drills and full answers where existing evidence did not isolate every requirement component.
- Corrected the DDoS explanation so botnets are described as a common method, not a universal prerequisite.
- Added the explicit Paper 2 pseudocode/program-code response boundary.
- Refined coverage wording for check digits and virtual memory.
- Replaced unqualified “high-scoring” and “full-mark” labels in affected IGCSE material with accurate exam-style or process labels.

## Final Result

| Final status | Count |
|---|---:|
| verified | **133** |
| partial / missing / incorrect / unsupported / imprecise | **0** |

This result means every IGCSE objective has traceable teaching, practice and answer evidence against the current syllabus. It does not mean the site's original answers are copied from, or guaranteed to reproduce, official Cambridge mark-scheme wording.
