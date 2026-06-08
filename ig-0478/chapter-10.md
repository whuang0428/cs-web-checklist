# IGCSE 0478 Computer Science - Chapter 10 Updated Checklist
## Boolean Logic｜Syllabus-Aligned Paper 2 Revision Sheet

> **Version:** Syllabus-aligned revision for Paper 2  
> **Target:** Cambridge IGCSE Computer Science 0478  
> **Chapter:** 10 Boolean logic  
> **Main audience:** Students  
> **Teacher Appendix:** optional; kept at the end for teachers  
> **Style:** Chinese explanation + English logic keywords

---

# 0. How to Use This Sheet

Boolean logic questions are usually skill questions. You need to:

1. recognise logic gates
2. write Boolean expressions
3. complete truth tables
4. build a logic circuit from an expression
5. simplify simple ideas using careful reasoning

---

# 1. Logic Gates

| Gate | Output is 1 when... | Expression |
| --- | --- | --- |
| NOT | input is 0 | `NOT A` |
| AND | all inputs are 1 | `A AND B` |
| OR | at least one input is 1 | `A OR B` |
| NAND | not all inputs are 1 | `NOT (A AND B)` |
| NOR | no input is 1 | `NOT (A OR B)` |
| XOR | inputs are different | `A XOR B` |

Common mistake:

- XOR is not the same as OR. XOR is false when both inputs are 1.

---

# 2. Two-Input Truth Tables

| A | B | A AND B | A OR B | A XOR B |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

For NAND and NOR:

- `A NAND B` is the opposite of `A AND B`
- `A NOR B` is the opposite of `A OR B`

---

# 3. Building a Truth Table

Method:

1. write all possible input combinations
2. add intermediate columns for brackets
3. calculate NOT before AND/OR when needed
4. complete the final output column

Example:

Expression:

```text
(A AND B) OR (NOT C)
```

Use intermediate columns:

| A | B | C | A AND B | NOT C | Output |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 1 |

---

# 4. Expressions from Scenarios

Scenario: An alarm sounds if the door is open and the system is armed.

```text
Alarm = DoorOpen AND Armed
```

Scenario: A fan turns on if temperature is high or manual override is pressed.

```text
Fan = HighTemp OR Override
```

Scenario: A machine starts only if the safety guard is closed and the stop button is not pressed.

```text
Start = GuardClosed AND NOT StopPressed
```

---

# 5. Circuits from Expressions

For:

```text
Output = (A AND B) OR (NOT C)
```

Circuit steps:

1. send `A` and `B` into an AND gate
2. send `C` into a NOT gate
3. send both results into an OR gate

Exam tip: draw intermediate gate outputs clearly. Avoid crossing lines when possible.

---

# 6. Common Exam Mistakes

- Missing brackets when the expression has two parts.
- Forgetting to invert the final output for NAND or NOR.
- Writing `A AND NOT B` but drawing `NOT (A AND B)`.
- Leaving out intermediate columns in a three-input truth table.
- Using `1` and `0` inconsistently with TRUE and FALSE.

---

# 7. Mini Practice

1. Complete the truth table for `A OR (B AND C)`.
2. Write an expression for a light that turns on when it is dark and motion is detected.
3. Draw a circuit for `(A OR B) AND NOT C`.
4. Explain why XOR is different from OR.
5. Write the expression for a NAND gate using AND and NOT.

---

# 8. Teacher Appendix

> Optional teacher-facing planning notes. Students can skip this appendix during normal revision.

## 8.1 Suggested teaching order

1. Start with AND, OR and NOT using real switches.
2. Add NAND, NOR and XOR only after core gates are secure.
3. Require intermediate truth-table columns for every compound expression.
4. Use scenario-to-expression tasks before drawing circuits.

