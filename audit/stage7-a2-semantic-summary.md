# Stage 7 — A2 9618 Semantic Audit and Repair

## Scope

- A2 9618 Sections 13–20 only.
- Paper 3 (Sections 13–20) and Paper 4 (Sections 19–20, excluding low-level and declarative programming).
- IGCSE and AS content were not changed as part of this stage.
- The objective register is the 83 `A2-*` rows in `coverage.md`.

## Authority used

- Cambridge International AS & A Level Computer Science 9618 syllabus for 2027–2029, Version 2.
- Cambridge 9618 Pseudocode Guide for Teachers for 2027–2029, Version 1.
- Public Cambridge mark schemes for Papers 31 and 41, May/June 2024.
- Public May/June 2024 examiner report.
- Public specimen mark schemes for Papers 3 and 4.

The local source files were checked against the SHA-256 values recorded in `audit/source-manifest.csv` before the audit.

## Initial result

| Initial status | Objectives | Meaning |
|---|---:|---|
| verified | 67 | Complete current teaching and practice evidence was already present. |
| partial | 13 | Teaching was relevant, but practice did not isolate every part of the current objective. |
| missing_teaching | 1 | Chapter 13 did not define and use a class/object type in current pseudocode notation. |
| out_of_scope_practice | 2 | Two Paper 3 review areas tested material outside the listed A2 Section 17/18 content. |
| **Total** | **83** | |

## Repairs

- Added a current-pseudocode class/object definition and use example to Chapter 13, plus marked class construction and two-method hashing practice.
- Added a complete sender-to-receiver four-layer TCP/IP trace to Chapter 14.
- Added focused RISC pipelining/register and multi-input/adder truth-table construction to Chapter 15.
- Added targeted OS resource, scheduling, interrupt, page-replacement and compiler-stage practice to Chapter 16.
- Added certificate acquisition and certificate-backed digital-signature practice to Chapter 17.
- Replaced the Paper 3 password-limitation item with certificate acquisition.
- Replaced the Paper 3 training-bias/human-review items with supervised/unsupervised and deep-learning evidence, and added a four-method selection drill to Chapter 18.
- Added explicit search/sort traces and input-size/initial-order analysis to Chapter 19.
- Added serial, sequential and random file-processing transfer practice to Chapter 20.
- Updated `coverage.md` so each repaired objective links directly to the new targeted question and answer evidence.

## Final result

- `83/83` objectives have final status `verified` in `stage7-a2-semantic-audit.csv`.
- `verified` means the site now has current-syllabus-aligned, original teaching and assessable practice evidence for the objective.
- It does **not** mean that every sentence was copied from an official mark scheme. Public student material remains original; official material was used to establish scope, terminology, answer logic and marking boundaries.
