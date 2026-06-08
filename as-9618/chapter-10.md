# AS 9618 Computer Science - Chapter 10 Updated Checklist
## Data Types and Structures｜Syllabus-Aligned Paper 2 Revision Sheet

> **Version:** Syllabus-aligned revision for AS Paper 2  
> **Target:** Cambridge International AS & A Level Computer Science 9618  
> **Chapter:** 10 Data types and structures  
> **Main audience:** Students  
> **Teacher Appendix:** optional; kept at the end for teachers  
> **Style:** 中文解释 + English pseudocode keywords

---

# 0. How to Use This Sheet

Chapter 10 is about choosing the right way to store data. Focus on:

- primitive data types
- arrays
- records
- files
- stacks and queues
- linked lists at concept level

---

# 1. Primitive Data Types

| Type | Meaning | Example |
| --- | --- | --- |
| INTEGER | whole number | `12` |
| REAL | decimal number | `3.5` |
| CHAR | one character | `"Y"` |
| STRING | several characters | `"Alice"` |
| BOOLEAN | true or false | `TRUE` |
| DATE | date value | `08/06/2026` |

Choose the smallest suitable type that still stores the needed data.

---

# 2. Arrays

An array stores multiple values of the same data type.

```text
DECLARE Scores : ARRAY[1:30] OF INTEGER
Scores[1] <- 76
```

Two-dimensional array:

```text
DECLARE Seats : ARRAY[1:10, 1:20] OF BOOLEAN
Seats[row, column] <- TRUE
```

Common uses:

- lists of marks
- grids
- tables
- repeated records when combined with records

---

# 3. Records

A record groups fields that may have different data types.

```text
TYPE Student
    DECLARE StudentID : STRING
    DECLARE Name : STRING
    DECLARE Mark : INTEGER
ENDTYPE

DECLARE ClassList : ARRAY[1:30] OF Student
```

Use a record when one item has several related attributes.

Common mistake: using several separate arrays when a record would keep related data together more clearly.

---

# 4. Files

| File type | Meaning |
| --- | --- |
| text file | stores readable characters |
| binary file | stores data in binary form |
| serial file | records stored in order received |
| sequential file | records stored in key order |
| random/direct access file | records can be accessed directly |

Pseudocode pattern:

```text
OPENFILE "Students.txt" FOR READ
WHILE NOT EOF("Students.txt")
    READFILE "Students.txt", line
    OUTPUT line
ENDWHILE
CLOSEFILE "Students.txt"
```

Always close files after use.

---

# 5. Stacks

A stack is LIFO: last in, first out.

Operations:

| Operation | Meaning |
| --- | --- |
| push | add item to top |
| pop | remove item from top |
| peek | inspect top item |
| isEmpty | check no items |
| isFull | check no space |

Example uses:

- undo feature
- browser back history
- expression evaluation
- subroutine call stack

Common overflow/underflow language:

- stack overflow: push when full
- stack underflow: pop when empty

---

# 6. Queues

A queue is FIFO: first in, first out.

Operations:

| Operation | Meaning |
| --- | --- |
| enqueue | add item to rear |
| dequeue | remove item from front |
| isEmpty | check no items |
| isFull | check no space |

Example uses:

- printer jobs
- call centre waiting line
- keyboard buffer
- network packet handling

---

# 7. Linked List Concept

A linked list stores data in nodes. Each node stores:

- data
- pointer/reference to the next node

Benefits:

- can grow and shrink more flexibly than a fixed array
- insertion and deletion can avoid shifting many items

Drawback:

- extra storage is needed for pointers
- direct access by index is not as simple as an array

---

# 8. Choosing a Data Structure

| Situation | Suitable structure |
| --- | --- |
| fixed list of same type values | array |
| one item with several fields | record |
| last item must be processed first | stack |
| first item must be processed first | queue |
| data must persist after program closes | file |

---

# 9. Mini Practice

1. Declare a record type for a library book.
2. Explain why a stack is suitable for an undo feature.
3. Explain why a queue is suitable for print jobs.
4. Write pseudocode to read all lines from a text file.
5. Choose a data structure for storing 30 student marks and justify it.

---

# 10. Teacher Appendix

> Optional teacher-facing planning notes. Students can skip this appendix during normal revision.

## 10.1 Suggested teaching order

1. Teach arrays and records together through the same scenario.
2. Use physical cards for stack and queue operations.
3. Ask students to justify a data structure choice, not just name it.
4. Keep linked lists conceptual unless your class is ready for pointer dry runs.

