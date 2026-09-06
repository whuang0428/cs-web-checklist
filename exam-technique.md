# Cambridge Computer Science Exam Technique

Use the command word, mark allocation and context to decide how much to write. Technical accuracy and a complete relationship earn marks; isolated keywords do not.

## Command Words

| Command word | What your answer must do |
|---|---|
| State / Identify | Give the precise fact(s), value(s) or name(s) requested. |
| Describe | Give the relevant features, stages or behaviour. |
| Explain | State a point and show why or how it produces the result. |
| Compare | Give linked similarities or differences covering both sides. |
| Justify | Choose an option and support it with the stated context. |
| Discuss | Develop relevant arguments, including different sides where appropriate. |
| Evaluate | Weigh evidence or trade-offs and reach a supported judgement. |
| Calculate | Work out the value; show method, substitutions and units when the question or mark allocation requires them. |
| Trace | Follow the algorithm exactly and record each required state change. |
| Write pseudocode | Use consistent Cambridge-style logic, clear identifiers and correct control structures. |

Equivalent technically correct wording is acceptable. A keyword does not earn a mark when the explanation is contradictory or incomplete.

## Build Stronger Explanations

Use this progression when a question asks you to explain, justify or evaluate:

1. **Point** — state the relevant technical fact.
2. **Mechanism** — explain how it works.
3. **Context** — connect it to the scenario.
4. **Consequence** — state the resulting effect.
5. **Judgement** — where required, decide which option is more suitable and why.

### Example

**Weak:** Fibre is faster.

**Improved:** Fibre has higher bandwidth, so more data can be transmitted per second.

**Contextual:** Fibre has higher bandwidth and is not affected by electromagnetic interference, so it is more suitable for a reliable high-volume link between the two school buildings.

## Five High-Mark Answer Patterns

### 1. Calculation: formula → substitution → conversion → unit

**Question pattern:** calculate the size of a `400 × 300` image at 16-bit colour in KiB.

```text
400 × 300 × 16 = 1 920 000 bits
1 920 000 ÷ 8 = 240 000 bytes
240 000 ÷ 1024 = 234.375 KiB
```

Write every conversion. A correct number with no method can lose working marks; a correct method with a final unit slip may retain them. Practise this pattern in [IGCSE Chapter 1](ig-0478/chapter-1.md) and [AS Chapter 1](as-9618/chapter-1.md).

### 2. Trace: record only states that actually change

For binary search, use columns such as `Low`, `High`, `Middle`, `Value` and `Action`. Calculate the middle index, compare once, then update only one boundary. Do not silently jump to the final answer.

| Step | Low | High | Middle | Value | Action |
|---:|---:|---:|---:|---:|---|
| 1 | 0 | 6 | 3 | 21 | target larger, so `Low = 4` |
| 2 | 4 | 6 | 5 | 33 | target smaller, so `High = 4` |

For assembly, record ACC, IX and changed memory after every instruction. For recursion, show calls descending and returned values during unwinding. Practise in [A2 Chapter 19](a2-9618/chapter-19.md) and [AS Chapter 4](as-9618/chapter-4.md).

### 3. Pseudocode: contract → initialise → process → return/output

All three courses require pseudocode. Before writing the body:

1. identify inputs, outputs and return type
2. declare/initialise totals, counters, flags and arrays
3. choose the loop from the stopping condition
4. keep array bounds and indexing consistent
5. close every construct and return on every required path

```text
FUNCTION FindCode(Codes : ARRAY[0:99] OF STRING, Target : STRING, Count : INTEGER) RETURNS INTEGER
    DECLARE Index : INTEGER
    Index <- 0
    WHILE Index < Count
        IF Codes[Index] = Target THEN
            RETURN Index
        ENDIF
        Index <- Index + 1
    ENDWHILE
    RETURN -1
ENDFUNCTION
```

Here `Count` is the number of occupied elements (0–100); `LENGTH` is a string function, not an array-size function in Cambridge pseudocode. The example uses the AS/A2 typed-parameter convention.

For IGCSE Paper 2, the final 15-mark scenario permits pseudocode or an approved programming language; this site's program-code route is Python. For the other questions, follow the requested notation and write pseudocode when required. AS Paper 2 requires Cambridge pseudocode, while AS classroom programming on this site uses Java. A2 retains pseudocode and uses Java for executable work and Paper 4 practice. Do not mix syntax within one answer. See [IGCSE Chapter 7](ig-0478/chapter-7.md), [AS Chapter 11](as-9618/chapter-11.md) and [A2 Chapter 19](a2-9618/chapter-19.md).

### IGCSE 15-Mark Scenario Assessment

Assess the complete response in two areas: **AO2 /9** and **AO3 /6**. Select a level in each area, then a mark within that level; award 0 where there is no creditable evidence. Do not turn a checklist of individual requirements into fifteen automatic points.

| Area | Lower level | Middle level | Upper level |
|---|---|---|---|
| AO2: solution design and application | 1–3: limited suitable techniques; little effective use of the required data | 4–6: several appropriate techniques and useful data handling | 7–9: appropriate techniques work together across the problem, using the required data structures effectively |
| AO3: program quality and accuracy | 1–2: little working logic or readable organisation | 3–4: some requirements work; organisation, identifiers and comments provide some clarity | 5–6: the solution is largely or fully correct, with clear organisation, meaningful identifiers and helpful comments |

Use the paper's task-specific checklist to locate evidence, then judge the whole answer. These are original practice descriptors aligned to the official specimen assessment approach.

Within a level, use the extent and consistency of the evidence to select the mark. The highest mark requires the strongest fulfilment of that area's criteria; merely reaching the upper level does not automatically earn 9 or 6.

### 4. Evaluate: benefits and limitations must lead to a decision

For a 4-mark structure asking for two benefits, one limitation and a conclusion:

- benefit 1: technical mechanism + contextual effect
- benefit 2: a different mechanism + contextual effect
- limitation: how/when the proposal can fail
- judgement: choose, reject or trial it using the evidence above

**Model:** “Automated classification can process items continuously, increasing throughput. It can also apply the same learned criteria consistently. However, dirty or unusual items may be outside the training data and be misclassified. The centre should therefore trial it with sampled human checks until measured accuracy meets its target.”

The conclusion is not a repeated benefit; it is an action supported by the trade-off.

### 5. Paper 4 Java evidence: code → input → expected → actual → result

Paper 4 marks executable behaviour and testing evidence. For every required test, record:

| Test purpose | Input | Expected result | Actual result | Pass? |
|---|---|---|---|---|
| lower boundary | reading `-50.0` | object accepted | object accepted | yes |
| invalid value | reading `150.1` | `IllegalArgumentException` | `IllegalArgumentException` | yes |

Use Java console mode throughout this site's A2 practical route. Include normal, boundary and invalid cases plus empty/full/missing-file paths where relevant. A screenshot without the input and expected outcome is weak evidence. Apply this pattern in [Paper 4 Set A](a2-9618/paper-4-review.md) and [Set B](a2-9618/paper-4-review-2.md).

## Losing Marks: Diagnosis and Repair

| Weak response | Why it loses marks | Repair |
|---|---|---|
| list of keywords | no relationship or mechanism | turn each keyword into subject + action + effect |
| generic advantage | not applied to the scenario | name the data, device, user or constraint |
| trace with final value only | no evidence of correct execution | show each comparison/state change |
| pseudocode with mixed syntax | unclear or invalid constructs | use one consistent course convention |
| “reasonable answer” without condition | cannot be awarded precisely | state the exact fact and causal link |
| Java test says “works” | no reproducible evidence | show input, expected, actual and pass/fail |

## Assessment Objectives

### IGCSE 0478

| Paper | AO1 | AO2 | AO3 |
|---|---:|---:|---:|
| Paper 1 | 60% | 20% | 20% |
| Paper 2 | 20% | 60% | 20% |

### AS & A Level 9618 — 2027–2029

| Paper | AO1 | AO2 | AO3 |
|---|---:|---:|---:|
| Paper 1 | 60% | 40% | 0% |
| Paper 2 | 0% | 40% | 60% |
| Paper 3 | 60% | 40% | 0% |
| Paper 4 | 0% | 0% | 100% |

## Examination Conditions

- IGCSE 0478 Papers 1 and 2 do not permit calculators.
- 9618 Papers 1, 2, 3 and 4 do not permit calculators.
- For 9618 Paper 4, use a centre-provided computer without internet or email access and submit complete program code plus evidence of testing.

## Timed Practice Routine

1. Confirm the correct paper, time and syllabus range in the course hub.
2. Complete the paper without opening the mark scheme.
3. Show working and record testing evidence where required.
4. Open the folded mark scheme only after finishing.
5. Correct each response by adding the missing idea, link or context—not by copying keywords alone.

## High-Mark Practice Route

Use three passes through a topic: explain it without notes, solve a marked task, then transfer the method to a different situation. Keep a short error log with the faulty step, its cause and a fresh test or question that would expose it again.

| Level | Construction and transfer work | Evidence of readiness |
|---|---|---|
| IGCSE | [Python programming route](ig-0478/chapter-8.md#python-programming-route), then both Paper 2 scenarios | handle endpoints, missing items, repeated requests, ties, fouls and empty-data cases; explain each decision in pseudocode |
| AS | [Java testing workshop](as-9618/chapter-12.md#java-testing-workshop), then the [file-processing scenario](as-9618/paper-2-review-2.md#question-7-integrated-pseudocode-scenario-15) | validate before conversion, maintain per-item totals, preserve record associations, and write typed pseudocode with correct parameter modes |
| A2 | [42-mark algorithm construction](a2-9618/chapter-19.md#algorithm-construction-drill), both Paper 3 sets and both Java Paper 4 practicals | derive floating-point/K-map results, construct complete algorithms, justify time and space, and supply reproducible practical test evidence |

For theory answers, check that every claimed advantage has a mechanism and a consequence in the question's context. For programming, test normal data and cases that exercise different branches; a program that works on one typical input is not ready for a new scenario. Retest on the other set after a gap, then use further official papers for unfamiliar applications. This site is a revision and marked-practice hub; the course syllabus and independent examination practice remain the wider study framework.
