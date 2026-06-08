# AS 9618 Computer Science - Chapter 9 Updated Checklist
## Algorithm Design and Problem-Solving｜Syllabus-Aligned Paper 2 Revision Sheet

> **Version:** Syllabus-aligned revision for AS Paper 2  
> **Target:** Cambridge International AS & A Level Computer Science 9618  
> **Chapter:** 9 Algorithm design and problem-solving  
> **Main audience:** Students  
> **Style:** 中文解释 + English pseudocode keywords

---

# 0. How to Use This Sheet

AS Paper 2 wants more than simple pseudocode. You must show computational thinking:

- decompose a problem
- identify inputs, outputs and processing
- choose suitable data structures
- trace and dry-run an algorithm
- design test data
- refine an inefficient or incorrect solution

---

# 1. Computational Thinking

| Skill | Meaning | In an exam answer |
| --- | --- | --- |
| abstraction | remove unnecessary detail | focus on essential data and operations |
| decomposition | split into smaller parts | separate input, processing, output |
| pattern recognition | spot repeated logic | use loops or subroutines |
| algorithmic thinking | write ordered steps | pseudocode with correct control flow |

Weak answer: "make a program to solve it".

Strong answer: "decompose the task into input validation, processing each record, and outputting a summary."

---

# 2. Structure Charts and Modular Design

A structure chart shows how a solution is divided into modules.

Good module names:

- `GetValidatedMark`
- `CalculateAverage`
- `FindHighestScore`
- `DisplayReport`

Benefits of modular design:

- easier to test
- easier to debug
- reusable subroutines
- different programmers can work on different modules
- reduces repeated code

---

# 3. Pseudocode Control Structures

## 3.1 Selection

```text
IF average >= 80 THEN
    grade <- "A"
ELSE
    IF average >= 60 THEN
        grade <- "B"
    ELSE
        grade <- "C"
    ENDIF
ENDIF
```

## 3.2 Iteration

```text
REPEAT
    INPUT mark
UNTIL mark >= 0 AND mark <= 100
```

## 3.3 Nested Loops

```text
FOR row <- 1 TO 3
    FOR col <- 1 TO 4
        OUTPUT grid[row, col]
    NEXT col
NEXT row
```

Common mistake: using one loop when each row and column must be processed.

---

# 4. Trace Tables

Trace tables are used to prove what an algorithm does.

Checklist:

1. include all variables that change
2. include array indexes if they affect output
3. include Boolean flags
4. update values in the order the code executes
5. record output separately

When tracing nested loops, update the inner loop fully before increasing the outer loop.

---

# 5. Searching and Sorting Concepts

## 5.1 Linear Search

Linear search checks each item until a match is found or the list ends.

Best use:

- unsorted data
- small lists
- simple implementation

## 5.2 Binary Search

Binary search repeatedly halves a sorted list.

Requirements:

- data must be sorted
- compare with middle item
- discard half of the search space

Common phrase:

> Binary search is more efficient on a sorted list because each comparison reduces the remaining search area by about half.

## 5.3 Bubble Sort

Bubble sort repeatedly compares adjacent items and swaps them if needed.

Exam skills:

- trace one pass
- identify swaps
- know that the largest item moves to the end after a full ascending pass

---

# 6. Validation and Test Data

| Test type | Purpose |
| --- | --- |
| normal | data that should be accepted |
| boundary | values at and around the limits |
| abnormal | invalid data that should be rejected |
| extreme | largest or smallest valid value |

For every test, include:

- test data
- reason for using it
- expected result

---

# 7. Common Exam Mistakes

- Writing vague English instead of executable pseudocode.
- Forgetting to initialise `total`, `count`, `found`, `highest` or `lowest`.
- Using binary search on unsorted data.
- Giving test data with no expected outcome.
- Describing modular design benefits without linking them to testing or maintenance.

---

# 8. Mini Practice

1. Draw a structure chart for a program that records sports day results.
2. Write pseudocode to validate a percentage from 0 to 100.
3. Trace one pass of bubble sort on `7, 2, 5, 1`.
4. Explain why binary search needs sorted data.
5. Give normal, boundary and abnormal test data for a ticket price input.

---

