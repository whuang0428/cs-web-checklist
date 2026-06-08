# IGCSE 0478 Computer Science - Chapter 8 Updated Checklist
## Programming｜Syllabus-Aligned Paper 2 Revision Sheet

> **Version:** Syllabus-aligned revision for Paper 2  
> **Target:** Cambridge IGCSE Computer Science 0478  
> **Chapter:** 8 Programming  
> **Main audience:** Students  
> **Teacher Appendix:** optional; kept at the end for teachers  
> **Style:** Chinese explanation + English programming keywords

---

# 0. How to Use This Sheet

Chapter 8 turns algorithms into real programming ideas. The exam may use pseudocode, but the thinking is programming thinking:

- variables and constants
- data types
- operators
- selection and loops
- arrays
- subroutines
- file handling
- errors and testing

---

# 1. Data Types

| Data type | Meaning | Example |
| --- | --- | --- |
| INTEGER | whole number | `42`, `-7` |
| REAL | decimal number | `3.14` |
| CHAR | single character | `"A"` |
| STRING | sequence of characters | `"Cambridge"` |
| BOOLEAN | true or false | `TRUE`, `FALSE` |
| DATE | date value | `08/06/2026` |

Common mistake:

- Treating `"123"` as a number. It is a string if it is stored with quotation marks.

---

# 2. Variables, Constants and Assignment

| Term | Meaning | Example |
| --- | --- | --- |
| variable | named storage value that can change | `score <- score + 1` |
| constant | named value that should not change | `CONSTANT MaxMark <- 100` |
| assignment | storing a value in a variable | `total <- 0` |

Use constants for values that should stay fixed:

```text
CONSTANT PassMark <- 50
IF mark >= PassMark THEN
    OUTPUT "Pass"
ENDIF
```

---

# 3. Operators

## 3.1 Arithmetic Operators

| Operator | Meaning |
| --- | --- |
| `+` | addition |
| `-` | subtraction |
| `*` | multiplication |
| `/` | division |
| `DIV` | integer division |
| `MOD` | remainder |

Example:

```text
hours <- totalMinutes DIV 60
minutes <- totalMinutes MOD 60
```

## 3.2 Comparison and Boolean Operators

| Operator | Meaning |
| --- | --- |
| `=` | equal to |
| `<>` | not equal to |
| `<`, `>`, `<=`, `>=` | comparison |
| `AND` | both conditions true |
| `OR` | at least one condition true |
| `NOT` | reverses a Boolean value |

---

# 4. String Handling

Typical operations:

| Operation | Use |
| --- | --- |
| length | find number of characters |
| substring | take part of a string |
| concatenation | join strings |
| comparison | check if two strings match |

Example:

```text
initials <- LEFT(firstName, 1) & LEFT(lastName, 1)
```

Exam tip: be clear about whether the first character position is 1 or 0 if the question gives a specific convention.

---

# 5. Procedures and Functions

| Subroutine | Returns a value? | Example use |
| --- | --- | --- |
| procedure | no | display a menu, update an array |
| function | yes | calculate average, validate input |

## 5.1 Procedure

```text
PROCEDURE DisplayMenu()
    OUTPUT "1 Add score"
    OUTPUT "2 Show average"
ENDPROCEDURE
```

## 5.2 Function

```text
FUNCTION IsValidMark(mark : INTEGER) RETURNS BOOLEAN
    IF mark >= 0 AND mark <= 100 THEN
        RETURN TRUE
    ELSE
        RETURN FALSE
    ENDIF
ENDFUNCTION
```

Common mistake: writing a function that never returns a value.

---

# 6. Parameters

Parameters pass data into a subroutine.

```text
PROCEDURE PrintGrade(name : STRING, mark : INTEGER)
    OUTPUT name
    IF mark >= 50 THEN
        OUTPUT "Pass"
    ELSE
        OUTPUT "Fail"
    ENDIF
ENDPROCEDURE
```

Benefits:

- avoids repeated code
- makes code easier to test
- allows the same subroutine to work with different data

---

# 7. File Handling

Core operations:

| Operation | Meaning |
| --- | --- |
| open file | prepare the file for reading or writing |
| read file | get data from the file |
| write file | store data in the file |
| close file | save changes and release the file |

Example pattern:

```text
OPENFILE "Scores.txt" FOR READ
WHILE NOT EOF("Scores.txt")
    READFILE "Scores.txt", score
    total <- total + score
ENDWHILE
CLOSEFILE "Scores.txt"
```

Common mistake: forgetting to close the file.

---

# 8. Errors and Testing

| Error type | Meaning | Example |
| --- | --- | --- |
| syntax error | code breaks language rules | missing `ENDIF` |
| logic error | program runs but gives wrong result | average formula uses wrong divisor |
| runtime error | error occurs while running | division by zero |

Testing checklist:

1. use normal, boundary and abnormal data
2. record expected output
3. compare actual output with expected output
4. fix errors and retest

---

# 9. Maintainable Programs

Good programming style:

- meaningful identifiers
- indentation
- comments for complex logic
- constants instead of repeated magic numbers
- subroutines for repeated tasks
- clear validation before processing

Bad style:

- one giant block of code
- variables called `a`, `b`, `c` with no meaning
- repeated code copied many times
- comments that only repeat the code

---

# 10. Mini Practice

1. Write a function that returns `TRUE` if a password has at least 8 characters.
2. Write a procedure that displays a student's name and grade.
3. Use `DIV` and `MOD` to convert seconds into minutes and seconds.
4. Explain one difference between a syntax error and a logic error.
5. Write pseudocode to read all numbers from a file and output the total.

---

# 11. Teacher Appendix

> Optional teacher-facing planning notes. Students can skip this appendix during normal revision.

## 11.1 Suggested teaching order

1. Teach data types and operators through tiny trace tasks.
2. Teach functions only after students can write a clear `IF`.
3. Use file handling as a pattern students practise repeatedly.
4. Mark pseudocode for clarity and correctness, not for matching one exact style.

