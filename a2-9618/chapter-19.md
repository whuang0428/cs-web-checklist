# A2 9618 Computer Science - Chapter 19 Updated Checklist
## Computational Thinking and Problem-Solving｜Syllabus-Aligned Paper 4 Revision Sheet

> **Version:** Syllabus-aligned revision for A2 Paper 4  
> **Target:** Cambridge International AS & A Level Computer Science 9618 A2  
> **Chapter:** 19 Computational thinking and problem-solving  
> **Main audience:** Students  
> **Style:** 中文解释 + English algorithm keywords

---

# 0. How to Use This Sheet

Chapter 19 is about designing better solutions, not just writing longer code. It connects Paper 4 programming with algorithmic reasoning.

Focus on:

- abstraction and decomposition
- algorithm design
- recursion
- search and sort strategy
- efficiency and complexity language
- ADT operations
- testing and refinement

---

# 1. Computational Thinking at A2

| Skill | A2 expectation |
| --- | --- |
| abstraction | model the problem using only relevant data |
| decomposition | split a complex task into modules/classes/functions |
| algorithm design | choose a method that solves the task reliably |
| pattern recognition | reuse known algorithm patterns |
| generalisation | design a solution that works for many inputs |

Strong A2 answers explain why a design choice is suitable for the problem, not only what the code does.

---

# 2. Algorithm Design Patterns

## 2.1 Accumulator

```text
total <- 0
FOR i <- 1 TO NumberOfItems
    total <- total + Value[i]
NEXT i
```

## 2.2 Sentinel-Controlled Input

```text
INPUT value
WHILE value <> -1 DO
    Process(value)
    INPUT value
ENDWHILE
```

## 2.3 Flag-Controlled Search

```text
found <- FALSE
index <- 1
WHILE found = FALSE AND index <= ListSize DO
    IF Items[index] = Target THEN
        found <- TRUE
    ELSE
        index <- index + 1
    ENDIF
ENDWHILE
```

---

# 3. Recursion

Recursion needs:

- base case
- recursive case
- progress toward the base case
- return value or side effect

Example:

```text
FUNCTION SumTo(n : INTEGER) RETURNS INTEGER
    IF n = 0 THEN
        RETURN 0
    ELSE
        RETURN n + SumTo(n - 1)
    ENDIF
ENDFUNCTION
```

Use recursion when the problem naturally breaks into smaller versions of itself, such as tree traversal, factorial-style calculations or divide-and-conquer search.

Common mistake: recursive call does not reduce the problem, so it never reaches the base case.

---

# 4. Searching

| Search | Requirement | Main idea |
| --- | --- | --- |
| linear search | none | check each item |
| binary search | sorted data | repeatedly halve search range |

Binary search outline:

```text
low <- 1
high <- ListSize
found <- FALSE

WHILE found = FALSE AND low <= high DO
    mid <- (low + high) DIV 2
    IF List[mid] = Target THEN
        found <- TRUE
    ELSE
        IF Target < List[mid] THEN
            high <- mid - 1
        ELSE
            low <- mid + 1
        ENDIF
    ENDIF
ENDWHILE
```

---

# 5. Sorting

Know the idea behind common sorting algorithms:

| Sort | Core idea |
| --- | --- |
| bubble sort | repeatedly swap adjacent out-of-order items |
| insertion sort | insert each item into the sorted part |
| quicksort | choose a pivot and partition into smaller/larger parts |

Exam focus:

- trace a pass
- identify the result after a pass
- explain why a method is inefficient or suitable
- compare general behaviour, not memorise every implementation detail

---

# 6. Abstract Data Types

An ADT describes data and operations without exposing implementation details.

## 6.1 Stack

LIFO: last in, first out.

Operations:

- `Push`
- `Pop`
- `Peek`
- `IsEmpty`
- `IsFull`

## 6.2 Queue

FIFO: first in, first out.

Operations:

- `Enqueue`
- `Dequeue`
- `IsEmpty`
- `IsFull`

## 6.3 Linked List

Nodes store data and a pointer/reference to the next node.

Typical tasks:

- insert a node
- delete a node
- traverse the list
- search for a value
- maintain a free list if array-based

---

# 7. Algorithm Efficiency

Use efficiency language carefully:

| Phrase | Meaning |
| --- | --- |
| constant time | does not grow with input size |
| linear time | grows roughly in proportion to input size |
| logarithmic behaviour | search space repeatedly halves |
| nested loop | often processes many combinations |

Avoid vague answers such as "it is faster". Say why:

> Binary search is more efficient than linear search for sorted data because each comparison halves the remaining search interval.

---

# 8. Testing and Refinement

For A2 algorithm questions, testing should include:

- normal cases
- boundary cases
- empty structure cases
- full structure cases
- duplicate values
- not-found cases
- invalid input

Refinement means improving the design after testing or review:

- remove repeated code
- split large modules
- add validation
- improve data structure choice
- handle edge cases

---

# 9. Common Exam Mistakes

- Using binary search on unsorted data.
- Writing recursive code without a base case.
- Explaining stack/queue by example only, without LIFO/FIFO.
- Forgetting empty and full cases for ADTs.
- Saying an algorithm is efficient without comparing input size behaviour.
- Tracing sort algorithms without recording intermediate states.

---

# 10. Mini Practice

1. Write iterative and recursive pseudocode to sum the numbers in an array.
2. Explain why binary search is unsuitable for an unsorted linked list.
3. Trace one partition step of a quicksort-style algorithm.
4. Write operations needed for an array-based queue.
5. Give test data for inserting into an empty linked list and a full array-based list.

---

