# IGCSE 0478 Computer Science - Chapter 7 Updated Checklist
## Algorithm Design and Problem-Solving｜Syllabus-Aligned Paper 2 Revision Sheet

> **Version:** Syllabus-aligned revision for Paper 2  
> **Target:** Cambridge IGCSE Computer Science 0478  
> **Chapter:** 7 Algorithm design and problem-solving  
> **Main audience:** Students  
> **Style:** Chinese explanation + English pseudocode keywords

---

# 0. How to Use This Sheet

Chapter 7 是 Paper 2 的核心。复习目标不是背定义，而是能把题目场景变成清晰的 algorithm。

Use this order:

1. understand the problem and identify inputs, processing and outputs
2. decompose the task into smaller steps
3. write or trace pseudocode
4. test with normal, boundary and abnormal data
5. improve the algorithm when a trace table shows an error

---

# 1. Core Problem-Solving Ideas

| Idea | What it means | Exam phrase |
| --- | --- | --- |
| decomposition | split a large problem into smaller sub-problems | break down the problem |
| abstraction | keep important details and ignore irrelevant detail | remove unnecessary detail |
| algorithm | finite sequence of steps to solve a problem | ordered steps |
| input | data entered into the algorithm | value supplied by user/sensor/file |
| output | result produced by the algorithm | display, store or print result |
| validation | check data is reasonable before processing | range, type, length, presence, format |
| verification | check data has been entered accurately | double entry, visual check |

Common mistake:

- Writing a program in natural language only, with no clear sequence.
- Using validation to mean "checking the answer is correct". Validation only checks whether input is acceptable.

---

# 2. Standard Pseudocode Building Blocks

## 2.1 Input and Output

```text
INPUT name
OUTPUT "Enter mark"
OUTPUT total
```

Use meaningful variable names:

- good: `studentMark`, `total`, `highestScore`
- weak: `x`, `thing`, `number1` when the context is clear

## 2.2 Assignment

```text
total <- total + mark
count <- count + 1
average <- total / count
```

Important: `=` compares values in conditions, while `<-` assigns a new value.

---

# 3. Selection

## 3.1 IF Statement

```text
IF mark >= 50 THEN
    OUTPUT "Pass"
ELSE
    OUTPUT "Fail"
ENDIF
```

## 3.2 Nested Selection

```text
IF mark >= 80 THEN
    grade <- "A"
ELSE
    IF mark >= 60 THEN
        grade <- "B"
    ELSE
        grade <- "C"
    ENDIF
ENDIF
```

Common mistake: using several separate `IF` statements when the categories are mutually exclusive. Use `ELSE IF` logic or nested selection.

---

# 4. Iteration

| Loop | When to use it | Example |
| --- | --- | --- |
| `FOR` | fixed number of repetitions | process 30 students |
| `WHILE` | may run zero times | repeat while input is invalid |
| `REPEAT ... UNTIL` | must run at least once | keep asking until valid |

## 4.1 Count-Controlled Loop

```text
FOR i <- 1 TO 10
    INPUT score
    total <- total + score
NEXT i
```

## 4.2 Pre-Condition Loop

```text
WHILE password <> "CS2028" DO
    INPUT password
ENDWHILE
```

## 4.3 Post-Condition Loop

```text
REPEAT
    INPUT age
UNTIL age >= 11 AND age <= 19
```

---

# 5. Arrays

Arrays store multiple values under one name.

```text
DECLARE names : ARRAY[1:30] OF STRING
DECLARE scores : ARRAY[1:30] OF INTEGER

FOR i <- 1 TO 30
    INPUT names[i]
    INPUT scores[i]
NEXT i
```

Exam skills:

- choose a suitable array size
- use the index correctly
- search through an array
- find total, average, highest and lowest values
- update one element

---

# 6. Searching and Counting Patterns

## 6.1 Linear Search

```text
found <- FALSE
position <- 0

FOR i <- 1 TO 30
    IF names[i] = searchName THEN
        found <- TRUE
        position <- i
    ENDIF
NEXT i

IF found = TRUE THEN
    OUTPUT position
ELSE
    OUTPUT "Not found"
ENDIF
```

## 6.2 Counting Matches

```text
count <- 0
FOR i <- 1 TO 30
    IF scores[i] >= 50 THEN
        count <- count + 1
    ENDIF
NEXT i
```

Common mistake: resetting `count` or `total` inside the loop. Initialise before the loop.

---

# 7. Trace Tables

A trace table shows how variable values change when an algorithm runs.

Checklist:

1. make one column for each variable
2. update values only when an assignment happens
3. include loop counter changes
4. record output separately
5. stop exactly when the loop condition becomes false

Example:

```text
total <- 0
FOR i <- 1 TO 3
    INPUT mark
    total <- total + mark
NEXT i
OUTPUT total
```

If the inputs are `5, 7, 4`, the final output is `16`.

---

# 8. Testing and Dry Runs

| Test type | Meaning | Example for age 11 to 19 |
| --- | --- | --- |
| normal | accepted value in the middle | 15 |
| boundary | value at or just around the limit | 11, 19, 10, 20 |
| abnormal | wrong type or impossible value | "abc", -5 |

Good test data includes expected results. Do not only list inputs.

---

# 9. Common Exam Mistakes

- No initialisation before using `total`, `count`, `highest` or `found`.
- Loop runs one time too many or one time too few.
- Validation checks are written after the invalid data has already been used.
- Array index starts at the wrong value.
- Boolean flag is set but never tested.
- Output is inside the loop when the question expects one final result.

---

# 10. Mini Practice

1. Write pseudocode to input 20 temperatures and output the highest temperature.
2. Write validation for a mark from 0 to 100 inclusive.
3. Trace an algorithm that counts how many numbers in an array are greater than 50.
4. Explain the difference between validation and verification.
5. Write a linear search for a product code in an array of 100 codes.

---

