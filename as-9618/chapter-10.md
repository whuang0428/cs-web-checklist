# AS 9618 Chapter 10: Data Types and Structures

> **Paper 2 focus:** select, declare and process records, arrays and text files, then reason accurately about stack, queue and linked-list operations.

---

## 1. Syllabus Coverage

| Syllabus objective | Where it is covered |
|---|---|
| Select suitable data types | Section 2 |
| Define, read and update records | Section 3 |
| Use array terminology, bounds and indexes | Section 4 |
| Select and write 1D/2D arrays | Section 4 |
| Bubble sort and linear search array data | Section 5 |
| Explain the need for files and process text files | Section 6 |
| Define an abstract data type | Section 7 |
| Describe and justify stacks, queues and linked lists | Sections 8–10 |
| Add, edit and delete ADT data | Sections 8–10 and Worked Example 3 |
| Describe array implementations of stacks, queues and linked lists | Section 11 |

---

## 2. Data Types

Choose a data type from what the value represents and how it will be processed.

| Type | Example | Suitable use |
|---|---|---|
| `INTEGER` | `-12`, `40` | counts and whole numbers |
| `REAL` | `18.75` | measurements and averages |
| `CHAR` | `'Y'` | one character |
| `STRING` | `"AB014"` | text and mixed-character codes |
| `BOOLEAN` | `TRUE` | two-state flags |
| `DATE` | `22/07/2026` | dates that need date operations |
| `ARRAY` | multiple same-type elements | lists and grids |
| `FILE` | persistent line data | data retained between runs |

Examples:

- store a telephone number as `STRING`, because arithmetic is not required and leading zeros matter
- store a count as `INTEGER`
- store a measured mass as `REAL`
- store one menu letter as `CHAR`

---

## 3. Records

A **record** stores related fields of different data types under one identifier.

```text
TYPE BookRecord
    DECLARE BookCode : STRING
    DECLARE Title : STRING
    DECLARE Price : REAL
    DECLARE Available : BOOLEAN
ENDTYPE

DECLARE CurrentBook : BookRecord
```

### Read and update fields

```text
INPUT CurrentBook.BookCode
INPUT CurrentBook.Title
INPUT CurrentBook.Price
CurrentBook.Available <- TRUE

OUTPUT CurrentBook.Title
CurrentBook.Price <- CurrentBook.Price + 1.50
```

### Array of records

```text
DECLARE Catalogue : ARRAY[1:100] OF BookRecord

Catalogue[1].BookCode <- "BK101"
Catalogue[1].Available <- TRUE
```

Use a record when one entity has several related properties. An array of records keeps many entities in one coherent structure.

---

## 4. Arrays

An array stores elements of the same data type.

### Terminology

| Term | Meaning |
|---|---|
| index | position used to access an element |
| lower bound | smallest valid index |
| upper bound | largest valid index |
| element | one stored value |
| dimension | number of indexes required |

### One-dimensional array

```text
DECLARE Score : ARRAY[1:30] OF INTEGER

FOR Index <- 1 TO 30
    INPUT Score[Index]
NEXT Index
```

### Two-dimensional array

```text
DECLARE Temperature : ARRAY[1:4, 1:7] OF REAL

FOR Week <- 1 TO 4
    FOR Day <- 1 TO 7
        INPUT Temperature[Week, Day]
    NEXT Day
NEXT Week
```

Select:

- 1D for a single sequence
- 2D for rows and columns
- an array of records for repeated entities with mixed field types

Always use the declared bounds. Do not assume the first index is 0 or 1.

---

## 5. Processing Array Data

### Linear search

```text
Found <- FALSE
Index <- 1

WHILE Index <= 30 AND Found = FALSE
    IF StudentID[Index] = SearchID THEN
        Found <- TRUE
    ELSE
        Index <- Index + 1
    ENDIF
ENDWHILE
```

After the loop:

- if `Found = TRUE`, `Index` is the matching position
- otherwise the target is absent

### Bubble sort

```text
FOR Pass <- 1 TO 29
    FOR Index <- 1 TO 30 - Pass
        IF Score[Index] > Score[Index + 1] THEN
            Temp <- Score[Index]
            Score[Index] <- Score[Index + 1]
            Score[Index + 1] <- Temp
        ENDIF
    NEXT Index
NEXT Pass
```

For ascending order, the largest unsorted value reaches its final position after each pass.

If parallel arrays or records are used, swap the entire associated item, not just the sort key.

---

## 6. Text Files

A file preserves data after program execution ends and can hold an unknown number of lines.

### Read every line

```text
DECLARE DataLine : STRING

OPENFILE "Readings.txt" FOR READ

WHILE NOT EOF("Readings.txt")
    READFILE "Readings.txt", DataLine
    OUTPUT DataLine
ENDWHILE

CLOSEFILE "Readings.txt"
```

### Write lines

```text
OPENFILE "Summary.txt" FOR WRITE
WRITEFILE "Summary.txt", ReportTitle
WRITEFILE "Summary.txt", Total
CLOSEFILE "Summary.txt"
```

### Append a line

```text
OPENFILE "Audit.txt" FOR APPEND
WRITEFILE "Audit.txt", NewEntry
CLOSEFILE "Audit.txt"
```

File checklist:

- correct filename
- correct mode
- read/write uses the opened file
- `EOF` prevents reading beyond the file
- file is closed
- empty-file cases are handled before division or average calculations

---

## 7. Abstract Data Types

An **abstract data type (ADT)** is:

- a collection of data
- together with a defined set of operations on that data

The logical behaviour is separated from the implementation.

Examples:

- stack
- queue
- linked list

At AS Level, you must:

- describe their features
- justify their use
- trace adding, editing and deleting data
- describe how arrays and pointers can implement them

You are not required to write full pseudocode implementations for these ADTs.

---

## 8. Stacks

A stack is **LIFO**: last in, first out.

| Operation | Effect |
|---|---|
| push | add an item at the top |
| pop | remove and return the top item |
| peek | inspect the top item without removing it |
| is empty | test whether no item is stored |
| is full | test whether a fixed implementation has no free position |

Example:

```text
Start: [A, B] where B is top
PUSH C: [A, B, C]
POP: returns C, leaves [A, B]
```

Suitable uses:

- undo history
- browser back history
- matching brackets
- returning from nested subroutine calls

Errors:

- **overflow:** push when full
- **underflow:** pop when empty

---

## 9. Queues

A queue is **FIFO**: first in, first out.

| Operation | Effect |
|---|---|
| enqueue | add an item at the rear |
| dequeue | remove and return the front item |
| inspect front | view the next item without removing it |
| is empty | test whether no item is stored |
| is full | test whether a fixed implementation has no free position |

Example:

```text
Front -> [A, B] <- Rear
ENQUEUE C: [A, B, C]
DEQUEUE: returns A, leaves [B, C]
```

Suitable uses:

- print jobs
- network packets awaiting processing
- customer requests
- keyboard buffers

A circular queue reuses array positions released at the front.

---

## 10. Linked Lists

A linked list contains nodes. Each node stores:

- data
- a pointer to the next node

A start pointer identifies the first node. A null pointer marks the end.

```text
Start -> [A | 4] -> [C | 1] -> [F | NULL]
```

The physical array positions do not have to match the logical order.

### Insert

To insert `B` between `A` and `C`:

1. obtain a free node
2. store `B`
3. set `B.Next` to the node containing `C`
4. set `A.Next` to the new node

### Delete

To delete `C`:

1. find the previous node `B`
2. set `B.Next` to `C.Next`
3. return the removed node to the free list

### Edit

Change the data field of the target node without changing pointers unless its logical order also needs to change.

Benefits:

- nodes can be inserted/deleted without shifting every following element
- storage need not be contiguous

Costs:

- pointer storage is required
- direct indexed access is not available
- traversal must follow links from the start

---

## 11. Array Implementations of ADTs

### Stack

Required components:

- `StackData` array
- `TopPointer`

`TopPointer` identifies the current top or the next free position, depending on the stated convention. Never mix conventions.

### Queue

Required components:

- `QueueData` array
- `FrontPointer`
- `RearPointer`
- sometimes a count to distinguish full from empty

In a circular queue, incrementing beyond the upper bound wraps to the lower bound.

### Linked list

One possible node record:

```text
TYPE Node
    DECLARE Data : STRING
    DECLARE NextPointer : INTEGER
ENDTYPE

DECLARE List : ARRAY[1:10] OF Node
DECLARE StartPointer : INTEGER
DECLARE FreeListPointer : INTEGER
```

The active list and free list are both chains of array positions.

Pointer diagrams should show:

- array index
- data
- next pointer
- start pointer
- free-list pointer
- null-pointer value

---

## 12. Worked Example 1 — Array of Records

Store four runners. Each runner has an ID, name and time. Display the ID of the fastest runner.

```text
TYPE RunnerRecord
    DECLARE RunnerID : STRING
    DECLARE Name : STRING
    DECLARE Time : REAL
ENDTYPE

DECLARE Runner : ARRAY[1:4] OF RunnerRecord

FOR Index <- 1 TO 4
    INPUT Runner[Index].RunnerID
    INPUT Runner[Index].Name
    REPEAT
        INPUT Runner[Index].Time
    UNTIL Runner[Index].Time > 0
NEXT Index

FastestIndex <- 1

FOR Index <- 2 TO 4
    IF Runner[Index].Time < Runner[FastestIndex].Time THEN
        FastestIndex <- Index
    ENDIF
NEXT Index

OUTPUT Runner[FastestIndex].RunnerID
```

The complete record remains together, while `FastestIndex` identifies the winning entity.

---

## 13. Worked Example 2 — File Summary

`Codes.txt` contains one workshop code string per line. Copy every non-empty
code to `CleanCodes.txt` and output how many codes were copied.

```text
DECLARE CodeLine : STRING
DECLARE Count : INTEGER

Count <- 0

OPENFILE "Codes.txt" FOR READ
OPENFILE "CleanCodes.txt" FOR WRITE

WHILE NOT EOF("Codes.txt")
    READFILE "Codes.txt", CodeLine
    IF CodeLine <> "" THEN
        WRITEFILE "CleanCodes.txt", CodeLine
        Count <- Count + 1
    ENDIF
ENDWHILE

CLOSEFILE "Codes.txt"
CLOSEFILE "CleanCodes.txt"

OUTPUT Count
IF Count = 0 THEN
    OUTPUT "No codes"
ENDIF
```

The variable receiving `READFILE` data is a string, matching the official text-file model.

---

## 14. Worked Example 3 — Trace Three ADTs

### Stack trace

Start bottom-to-top: `[K, L]`

| Operation | Result | Returned value |
|---|---|---|
| PUSH M | [K, L, M] | |
| POP | [K, L] | M |
| PUSH N | [K, L, N] | |
| PEEK | [K, L, N] | N |

### Queue trace

Start front-to-rear: `[P, Q]`

| Operation | Result | Returned value |
|---|---|---|
| ENQUEUE R | [P, Q, R] | |
| DEQUEUE | [Q, R] | P |
| ENQUEUE S | [Q, R, S] | |

### Linked-list deletion

Before:

```text
Start -> A -> B -> C -> NULL
```

Delete `B`:

```text
A.Next <- B.Next
return B node to free list
```

After:

```text
Start -> A -> C -> NULL
```

Only links change; `C` does not need to move physically.

---

## 15. Common Mistakes Checklist

- [ ] I use a record for related mixed-type fields.
- [ ] I distinguish an array element from its index.
- [ ] I follow the stated lower and upper bounds.
- [ ] I swap complete associated records when sorting by one field.
- [ ] I stop a linear search at the upper bound.
- [ ] I open, process and close text files correctly.
- [ ] I guard against an empty file before division.
- [ ] I distinguish LIFO from FIFO.
- [ ] I update pointers in the correct order when inserting/deleting.
- [ ] I describe array implementation without assuming a hidden pointer convention.

---

## 16. 10 Marks Quick Check

1. State suitable types for a product code, quantity and measured mass. **[3]**
2. State why a record is suitable for storing one student's ID, name and mark. **[2]**
3. Define an ADT. **[2]**
4. State the processing order of a stack and a queue, and name the queue operation that removes an item. **[3]**

**Total: 10 marks**

### Quick Check Answers

1. STRING, INTEGER and REAL. **[3]**
2. It groups related fields under one identifier **[1]** and allows the fields to have different data types **[1]**. **[2]**
3. A collection of data **[1]** together with a defined set of operations on the data **[1]**. **[2]**
4. Stack: LIFO **[1]**; queue: FIFO **[1]**; `dequeue` **[1]**. **[3]**

---

## 17. 20 Marks Practice

A clinic stores six appointments in an array of records. Each appointment has a unique code, patient name, duration in minutes and attended flag.

1. Define a suitable record type and declare `Appointment[1:6]`. **[5]**
2. Write pseudocode to use a linear search for an input appointment code and output the matching patient name or `"Not found"`. **[6]**
3. A queue contains appointments front-to-rear as `[A1, A2, A3]`. State the queue after `ENQUEUE A4`, `DEQUEUE`, `DEQUEUE`; also state both returned codes. **[4]**
4. Explain how an array can implement a linked list, naming three required components. **[3]**
5. State two actions required after opening a text file for reading an unknown number of lines. **[2]**

**Total: 20 marks**

### 20 Marks Practice Mark Scheme

1. Example:

   ```text
   TYPE AppointmentRecord
       DECLARE Code : STRING
       DECLARE PatientName : STRING
       DECLARE Duration : INTEGER
       DECLARE Attended : BOOLEAN
   ENDTYPE

   DECLARE Appointment : ARRAY[1:6] OF AppointmentRecord
   ```

   Correct type structure **[1]**; four suitable field declarations **[3]**; correct array declaration **[1]**. **[5]**

2. Example:

   ```text
   INPUT SearchCode
   Found <- FALSE
   Index <- 1

   WHILE Index <= 6 AND Found = FALSE
       IF Appointment[Index].Code = SearchCode THEN
           Found <- TRUE
       ELSE
           Index <- Index + 1
       ENDIF
   ENDWHILE

   IF Found = TRUE THEN
       OUTPUT Appointment[Index].PatientName
   ELSE
       OUTPUT "Not found"
   ENDIF
   ```

   Input target **[1]**; initialise flag and index **[1]**; bounded loop **[1]**; correct field comparison **[1]**; progress/termination **[1]**; correct two-way output **[1]**. **[6]**

3. After enqueue: `[A1, A2, A3, A4]` **[1]**; first dequeue returns `A1` **[1]**; second returns `A2` **[1]**; final queue `[A3, A4]` **[1]**. **[4]**
4. An array stores nodes/records **[1]**; each node contains data and a next pointer/index **[1]**; a start pointer identifies the first node, with a free-list pointer or null value also named **[1]**. **[3]**
5. Any two: loop until `EOF`, read each line with `READFILE`, process/store each value, close the file after the loop. **[2]**

---

## 18. Final Self-Assessment

- [ ] I can select every required AS pseudocode data type.
- [ ] I can define and process records and arrays of records.
- [ ] I can process 1D and 2D arrays within their bounds.
- [ ] I can write linear-search and bubble-sort pseudocode.
- [ ] I can read, write and append text-file lines.
- [ ] I can trace stack, queue and linked-list operations.
- [ ] I can describe how arrays and pointers implement each ADT.
- [ ] I completed both practice sets before checking the answers.
