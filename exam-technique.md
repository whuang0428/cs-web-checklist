# Cambridge Computer Science Exam Technique

Use the command word, mark allocation and context to decide how much to write. Technical accuracy and a complete relationship earn marks; isolated keywords do not.

## Command Words

| Command word | What your answer must do |
|---|---|
| State / Identify | Give one precise fact, value or name. |
| Describe | Give the relevant features, stages or behaviour. |
| Explain | State a point and show why or how it produces the result. |
| Compare | Give linked similarities or differences covering both sides. |
| Justify | Choose an option and support it with the stated context. |
| Discuss | Develop relevant arguments, including different sides where appropriate. |
| Evaluate | Weigh evidence or trade-offs and reach a supported judgement. |
| Calculate | Show the method, substitutions, units and final value. |
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
FUNCTION FindCode(Codes, Target) RETURNS INTEGER
    FOR Index <- 0 TO LENGTH(Codes) - 1
        IF Codes[Index] = Target THEN
            RETURN Index
        ENDIF
    NEXT Index
    RETURN -1
ENDFUNCTION
```

IGCSE may also use Python program code; AS Paper 2 uses Cambridge pseudocode; A2 executable examples and Paper 4 practice in this site use Java. Do not mix syntax within one answer. See [IGCSE Chapter 7](ig-0478/chapter-7.md), [AS Chapter 11](as-9618/chapter-11.md) and [A2 Chapter 19](a2-9618/chapter-19.md).

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
