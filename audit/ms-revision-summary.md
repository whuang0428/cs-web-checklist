# 2023–2025 MS revision audit

Checked: 2026-10-15. Maintainer record; excluded from student navigation and search.

## Scope and evidence

Reviewed the revision definitions, processes, features, comparisons and summaries in all 30 chapters: IGCSE 0478 Chapters 1–10, AS 9618 Chapters 1–12 and A2 9618 Chapters 13–20. Worked examples, drills, assessment questions/answers and the independent review papers were outside this task.

| Course | Chapters | Topic records | Recent QP/MS pairs |
| --- | ---: | ---: | ---: |
| IGCSE 0478 | 10 | 155 | 42 |
| AS 9618 | 12 | 155 | 36 |
| A2 9618 | 8 | 139 | 36 |
| Total | 30 | 449 | 114 |

- The recent corpus comprises 228 PDFs and 3,774 extracted pages: February/March 0478 and May/June plus October/November 0478/9618, 2023–2025, all relevant components and available variants. Combined variants can share content; these totals count paper identifiers, not distinct question content.
- [Recent corpus manifest](ms-corpus-2023-2025.csv) records URLs, identity checks, page counts and SHA-256 hashes. The downloaded files identify themselves as Cambridge QPs/MS; third-party hosting is identified separately from the document publisher. File identity verification does not by itself establish semantic support for a topic.
- Earlier papers were searched only for gaps left by the recent corpus. [Fallback manifest](ms-corpus-fallback.csv) records 67 successfully retrieved older documents, including search candidates not ultimately cited. This is a targeted search, not a claim of complete older-year coverage.
- Topic decisions and corresponding question/MS links are recorded in [IGCSE](ms-revision-ig.csv), [AS](ms-revision-as.csv) and [A2](ms-revision-a2.csv). Broader topic-family inventories include application questions; they must not be read as evidence that every question supports every sentence. The direct references and decision/limitation fields identify the relevant support.
- Student pages use concise synthesis with exam keywords and usually one or two direct source links per topic. Related answers were consolidated, repetitions removed and question-specific conditions preserved. Long official questions or complete mark schemes were not inserted into the site.

## Findings and changes

The supplied magnetic-hard-disk screenshot is substantially traceable to **9618/11 May/June 2025 Q6(a)(i)**, rather than evidence of fabrication. The [QP](https://bestexamhelp.com/exam/cambridge-international-a-level/computer-science-9618/2025/9618_s25_qp_11.pdf#page=10) and [MS](https://bestexamhelp.com/exam/cambridge-international-a-level/computer-science-9618/2025/9618_s25_ms_11.pdf#page=10) show four missing terms for four marks. The revision section now supplies provenance, condenses the process and distinguishes the source question's four marked blanks from the number of explanatory sentences.

Other substantive changes include:

- IGCSE: magnetic storage, HTTPS certificate verification, shift overflow, parity/checksum limitations, normal/boundary testing, local variables and database types. Removed unsupported fixed-mark promises and generalised device-price claims; recovered older printer-operation points.
- AS: CSMA/CD collision handling, monitoring versus feedback control, device mechanisms, signatures, relative addressing, database keys and development methods. Restricted broad claims to the relevant scenario and separated general technical explanations from directly evidenced answers.
- A2: user-defined/enumerated types, BitTorrent, pipeline interruptions, scheduling, compiler stages, TLS, machine learning and ADTs. Corrected array-linked-list references so they point to the matching implementation rather than an object-based list question.
- Cross-review corrected topic/source mismatches and refined references to the actual subquestion and PDF page, including cases where the relevant answer follows the start of a multi-page question.

## Explicit evidence limits

Not every syllabus topic has a directly located answer in the reviewed papers. Such material is labelled as supplementary instead of being presented as official scoring language. Examples include IGCSE DAC explanation, EOF programming technique and constructing a full circuit from a truth table and the SQL OR illustration; AS AI environmental impacts, indexing mechanisms, general algorithm/ADT definitions; A2 page replacement, code generation, general AI definition, regression and dictionary semantics. The topic registers also distinguish partially supported sections from fully direct evidence.

Supplementary references include the current syllabus/pseudocode guide and identified technical primary sources such as NIST, PostgreSQL, IEA, LLVM, Oracle and relevant component documentation. Earlier syllabus codes are labelled where used. The AS laser-printer source is a published 2020 predecessor-syllabus paper; the page explicitly states that the examination was not held.

## Verification

- Structural checker: `python3 scripts/check_site.py`.
- Checker regression suite: `python3 scripts/test_check_site_negative.py`.
- Runtime syntax: `node --check assets/site.js`; whitespace check: `git diff --check`.
- All four checks passed. The regression suite passed 29 expected-rejection controls and its documented semantic-blind-spot control; this is why source-content review was performed separately.
- Browser: all 30 chapter routes at 1440px and 390px, root chooser and three course hubs; no document-level horizontal overflow, Mermaid errors or page-script errors. Search returned 34 matches for `magnetic`; result navigation and previous/next chapter navigation passed.
- Inspected rendered source lines and the magnetic-hard-disk section. The changed USB diagram was rendered and inspected separately at mobile width.
- Compared 481 protected example/assessment blocks with the starting revision: unchanged. All 381 non-Mermaid fenced code blocks and all review-paper files remained unchanged.
- All 857 public MS references are present in the topic and corpus registers. Source-link checks validate document identity, question heading and page range; manual cross-review additionally checks that the cited subquestion concerns the stated topic. A valid URL alone is not treated as sufficient evidence.

No commits, pushes, publishing or deployment were performed.

## Outside-scope observation

The IGCSE Chapter 2 parity worked-example tables label nine-bit strings as “Final byte”. These examples were deliberately left unchanged under the agreed scope; this audit does not certify excluded practice material.
