# Stage 6 — AS 9618 Semantic Audit and Repair

## Scope

- AS 9618 Sections 1–12 only.
- Paper 1 (Sections 1–8) and Paper 2 (Sections 9–12).
- A2 Sections 13–20 were not changed as part of this stage.
- The objective register is the 178 `AS-*` rows in `coverage.md`.

## Authority used

- Cambridge International AS & A Level Computer Science 9618 syllabus for 2027–2029, Version 2.
- Cambridge 9618 Pseudocode Guide for Teachers for 2027–2029, Version 1, for Sections 9–12 notation.
- Public Cambridge mark schemes for Papers 11 and 21, May/June 2024.
- Public May/June 2024 examiner report.
- Public specimen mark schemes for Papers 1 and 2.

The local source files were checked against the SHA-256 values recorded in `audit/source-manifest.csv` before the audit.

## Initial result

| Initial status | Objectives | Meaning |
|---|---:|---|
| verified | 122 | Complete current teaching and practice evidence was already present. |
| partial | 50 | Teaching was relevant, but practice did not isolate every part of a compound objective. |
| incorrect_scope | 3 | A practice/checklist example used content outside the current AS list. |
| unsupported_marking_claim | 1 | An answer accepted CPU performance factors outside the current listed set. |
| out_of_scope_practice | 1 | A review item tested a privacy principle instead of the required transfer-verification detail. |
| imprecise_evidence | 1 | DBMS evidence named generic query/report tools instead of the required tools. |
| **Total** | **178** | |

## Repairs

- Added original targeted syllabus drills and answer evidence to Chapters 1–8 and 10. Chapters 9, 11 and 12 already had focused transfer, subroutine, testing and maintenance drills.
- Replaced the AS circuit-switching review item with mesh packet-routing and resilience.
- Restricted CPU performance evidence to processor type, number of cores, bus width, clock speed and cache memory.
- Removed line numbering as a listed current IDE presentation example and tested all four current IDE feature categories.
- Replaced the privacy-principle item with parity-block verification and tested the complete validation/verification list.
- Replaced freeware with the current FSF, OSI, shareware and commercial licence categories.
- Replaced generic DBMS query/report wording with developer-interface and query-processor evidence.
- Updated `coverage.md` so every repaired objective links directly to its targeted drill and answers.

## Final result

- `178/178` objectives have final status `verified` in `stage6-as-semantic-audit.csv`.
- `verified` means the site now has current-syllabus-aligned, original teaching and assessable practice evidence for the objective.
- It does **not** mean that every sentence was copied from an official mark scheme. Public student material remains original; official material was used to establish scope, terminology, answer logic and marking boundaries.
