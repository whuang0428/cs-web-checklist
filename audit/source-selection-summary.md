# 2023–2025 topic-source selection

Checked: 2026-10-16. Maintainer record; excluded from student navigation and search.

## Scope and selection rules

This follow-up expands the source links for the 449 topic records across all 30 chapters. It supersedes the earlier one-or-two-link display policy in [the MS revision audit](ms-revision-summary.md). The revision explanations, examples and practice tasks are outside this source-selection change.

- The recent corpus is the 114 QP/MS pairs in [the corpus manifest](ms-corpus-2023-2025.csv): IGCSE February/March, May/June and October/November; AS/A2 May/June and October/November; 2023–2025. All 228 cached PDF SHA-256 values were rechecked against the manifest on 2026-10-16, with no mismatches.
- A source must support the specific topic. A broad main-question reference is narrowed to the relevant subquestions; a shared scenario or a matching keyword alone is insufficient.
- Related subquestions within one paper's main question form one source group. Splitting a question into several links does not turn it into several examination occurrences. Identical combined-variant tasks are not independent evidence.
- For topics with at most five located independent recent source groups, retain all relevant groups. With more than five, prefer the five groups with the longest relevant MS answer content; additional sources can be retained where needed for a distinct subtopic. This is an editorial display threshold, not a prediction of examination likelihood.
- `answer_words` is a length proxy for the relevant answer text after removing headers, footers, generic marking instructions and unrelated subquestions. It is not the number of marks or independent marking points. Tables, code, alternative answers, repeated gap-fill stems and extraction-order anomalies require contextual review; a whole PDF's page count is never used for ranking.
- Older papers remain supplementary where recent direct evidence is absent or incomplete. An older source does not count toward 2023–2025 frequency. Where the user has requested related past-paper support for a topic without a direct question, show the relevant QP/MS source and state its actual coverage; keep any unsupported explanation explicitly supplementary. Related support does not increase direct-topic frequency.
- The three selection registers record candidates, precise question/page references, selection decisions, scope and limitations: [IGCSE](source-selection-ig.csv), [AS](source-selection-as.csv), [A2](source-selection-a2.csv). Candidate counts describe the evidence located and reviewed, not a guarantee that every differently worded occurrence has been recovered.

## AS virtual-reality check

The answer depends on what is being counted. There is **one directly located question about a VR headset's principal operation**, but **two papers use a VR headset as a scenario**.

All 18 AS Paper 1 QPs and their 18 MS from 2023–2025 were searched for `virtual reality`, `VR` and `headset` (including whitespace variants). The 18 Paper 2 pairs were also checked. A fresh extraction from the verified PDFs reproduced the same hits; the relevant QP and MS pages were inspected visually.

| Paper and question | What is assessed | Marks | Evidence |
| --- | --- | ---: | --- |
| 9618/12 May/June 2024 Q2(a) | VR headset principal operation: displays, motion sensors, movement data and eye tracking | 4 | [QP p.3](https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/9618_s24_qp_12.pdf#page=3), [MS p.4](https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/9618_s24_ms_12.pdf#page=4) |
| 9618/13 October/November 2023 Q7(b) | Reasons for EEPROM in a VR headset | 2 | [QP p.10](https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/9618_w23_qp_13.pdf#page=10), [MS p.7](https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/9618_w23_ms_13.pdf#page=7) |
| 9618/13 October/November 2023 Q7(d) | A suitable connection port and justification | 3 | [QP p.11](https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/9618_w23_qp_13.pdf#page=11), [MS p.8](https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/9618_w23_ms_13.pdf#page=8) |

The other parts of 2024 Q2 assess buffers, EEPROM, bitmap/vector representation and compression. They are not additional headset-operation questions. No VR/headset occurrence was found in the 2025 AS papers in this corpus. The operation section therefore keeps its one direct source and labels related application references separately, rather than inflating its direct frequency.

## Corrections made during source review

- IGCSE: recovered omitted RLE and abstraction evidence, narrowed broad database/logic references, and separated SQL result layout from actual `ORDER BY` questions. The 2024 October/November Paper 22 Q11(d) has no `ORDER BY` clause and is not used as sorting evidence. The five located problem-to-expression questions and two circuit-to-expression questions are recorded separately.
- AS: removed logical-gate questions from wired/wireless-network candidates, firewall/proxy questions from password/access-rights evidence, and entity/attribute questions from normalisation evidence. Function, built-in-function and efficiency source lengths count only the relevant scoring content, not a whole surrounding algorithm. The VR length measure counts the four gap-fill answers, not the prefilled question stem.
- A2: excluded a pipeline-only question from the RISC-feature subsection. Pipeline length measurement excludes repeated equivalent example diagrams. Matching tables and practical papers were checked for extraction-order errors; repeated language implementations or unrelated algorithm work do not make a source richer for a narrower topic.
- Diagram-only sources have an explicit limitation: extracted word count cannot fully measure a circuit, truth table or matching diagram. Graphical mappings were inspected where text extraction misplaced labels or omitted connections.

These corrections affect source selection and its audit trail. They do not rewrite the revision explanations or practice material.

## Initial expansion inventory

| Course | Topics reviewed | Topics with changed Sources | Previous MS links | MS links after initial expansion |
| --- | ---: | ---: | ---: | ---: |
| IGCSE 0478 | 155 | 152 | 303 | 683 |
| AS 9618 | 155 | 135 | 281 | 588 |
| A2 9618 | 139 | 100 | 273 | 436 |
| **Total** | **449** | **387** | **857** | **1,707** |

These are link occurrences across topic sections, not unique papers or examination frequencies. At this initial snapshot, AS had 587 selected Sources links plus one separately labelled VR application link. A source may legitimately support more than one topic. The three selection registers then contained 3,495 candidate/decision rows; the A2 register also recorded 12 selected supplementary resources that were not MS links. The follow-up below supersedes these display counts.

Across the topic records, 241 have at most five located independent recent source groups, 182 exceed five, and 26 have no located direct recent group. The last category includes older-paper-only and supplementary-resource-only topics. It is not a claim that those topics never appear under another wording.

## Past-paper-only Sources for ten remaining topics

The user's follow-up requires past-paper QP/MS references in the Sources of the ten topics previously displayed with only external or syllabus support. All ten now have related past-paper references. External explanatory provenance remains in the maintainer registers, but is no longer presented as the student-facing Sources for these ten topics. Revision explanations, code and practice tasks are unchanged.

| Topic | Selected paper/question groups | Actual coverage and limit |
| --- | --- | --- |
| IG Chapter 8: Read lines until end of file | s24/21 Q7(b); w25/21 Q9 | Text-file reading; neither assesses an EOF-controlled loop. |
| IG Chapter 10: Truth table to circuit | w23/23 Q6(a)–(c); s24/21 Q8(a), (b) | Description-to-gates/table and expression-to-circuit/table; neither starts from a supplied complete truth table. |
| AS Chapter 7: Environmental impacts | w24/12 Q2(a); s24/13 Q5(c)(ii) | Electronic waste and networking power consumption; not specifically AI's environmental effects. |
| AS Chapter 8: Indexing | s23/13 Q4(b), secondary-key row | Locating data with an alternative key; not index structure, efficiency or maintenance costs. |
| AS Chapter 9: Algorithms | s23/21 Q3(b); w25/21 Q5(b)(i), (ii) | Stepwise solution design and search termination; not the standalone definition. |
| AS Chapter 10: Abstract Data Types | s24/21 Q3(b); s25/22 Q6(b) | Array/pointer implementation of a linked list and identifying insertion; not the standalone ADT definition. |
| A2 Chapter 16: Page replacement | w23/32 Q5(a), (b); w24/31 Q8(b) | Why virtual memory is needed and page swapping; not FIFO/LRU selection policies. |
| A2 Chapter 18: What is Artificial Intelligence? | s25/31 Q10(a), (b); w23/31 Q12 | Graph applications and learning/prediction with neural networks; not the general AI definition. |
| A2 Chapter 18: Directed and undirected graphs | w25/33 Q8 | An undirected weighted graph and Dijkstra distances; not comparison with directed graphs. |
| A2 Chapter 19: Dictionary ADT | w25/41 Q3(c), (d), (f); s23/31 Q3(b) | Keyed storage/retrieval and hashing/collisions; not dictionary terminology, deletion or tombstones. |

The 18 added MS source-group links bring the public totals to **687 IGCSE + 595 AS + 443 A2 = 1,725**. AS includes one separately labelled VR application link. A2 also provides the seven corresponding QP links for these four topics. Every topic's note states the actual support and its limits; these related questions do not change the earlier count of 26 topics with no located direct recent group. This follow-up does not claim that a direct definition or comparison question has now been found.

## Initial expansion verification

- `python3 scripts/check_site.py`: passed, including all 30 chapter contracts, navigation/search paths, original practice totals, Java 17 execution and Python checks.
- `python3 scripts/test_check_site_negative.py`: all 29 expected rejection controls passed; the existing documented semantic blind spot remains. Structural checks do not establish a source's subject relevance.
- `node --check assets/site.js` and `git diff --check`: passed. Runtime code was unchanged.
- All 1,707 public MS link occurrences were checked against the cached PDFs for document identity, PDF page range, question labels and paper/year labels. The two legacy MS layouts that omit repeated parent question numbers were visually confirmed: `0478_s15_ms_12` p.3 Q2(ii), and `0478_w15_ms_11` p.6 Q5(a)(ii).
- All 449 topics are represented in the selection registers, and every selected MS URL occurs in its course chapter. No unexplained non-source chapter changes were found; all fenced code blocks are unchanged.
- All 30 chapter routes were rendered at 1440 px and 390 px (60 chapter/viewport checks). Rendered MS link counts matched the Markdown counts on every route. No page-level horizontal overflow, JavaScript page errors or Mermaid error indicators were found. The home chooser, three course hubs, sidebars, search results and previous/next navigation were checked; source wrapping and the VR scope note were inspected visually.
- No commit, push, publication or deployment was performed. Live deployment behaviour and continued availability of external PDF mirrors are outside this local verification.

## Ten-topic follow-up verification

- Compared with the saved pre-follow-up workspace: exactly ten source/scope blocks in nine chapter files changed; all other chapter text, headings, fenced code and practice content are identical.
- All ten Sources blocks contain only past-paper links: 18 MS links and seven companion QP links. Relevant QP/MS pages were checked for the stated support and limitations; independent cross-review covered the six IG/AS mappings.
- Rechecked all 1,725 public MS occurrences for PDF identity, page range, paper/year labels and question labels: no issues. Rebuilt the public-reference inventory and confirmed every selected MS URL occurs in its course chapter; all ten new mappings were also checked in their specific topic sections.
- The three registers still cover 449 topics and now contain 3,508 candidate/decision rows. Five A2 sources reuse previously excluded related-question rows, two add rows; IG adds four rows and AS seven. Earlier explanatory provenance and the direct-evidence gaps remain recorded.
- `python3 scripts/check_site.py` and `git diff --check`: passed. The negative-checker suite was not repeated because this follow-up changes content/source records only; its 29 passing controls above belong to the initial expansion verification.
- Rendered the ten sections at 1440 px and 390 px: 20 checks across nine routes passed, with no page errors, page-level overflow or non-paper Sources links. Source wrapping was visually inspected; the home chooser, sidebar, search and previous/next navigation passed.
- No commit, push, publication or deployment was performed.
