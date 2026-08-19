# IGCSE 0478 Chapter 8: Programming

<div class="chapter-meta"><strong>IGCSE 0478 · Paper 2</strong><span>0478 · 2026–2028 · Version 5</span></div>

## Official Syllabus Checklist

Revise: data types and control structures; strings; arrays; subroutines; files and maintainable programs.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.

> **Paper 2 focus:** translate an algorithm into clear pseudocode or program code by choosing suitable data, control structures, arrays, subroutines and file operations.

---

## Syllabus Map

| Objective | Where it is covered |
|---|---|
| Variables, constants and primitive data types | Data and Basic Statements |
| Input, output and assignment | Data and Basic Statements |
| Sequence, selection and iteration | Sequence, Selection and Iteration |
| Arithmetic, relational and logical operators | Operators and Library Routines |
| String handling | String Handling |
| Procedures, functions, parameters and scope | Procedures, Functions and Scope |
| One-dimensional and two-dimensional arrays | Arrays |
| File handling | File Handling |
| Maintainable programs | Maintainable Programs |
| Library routines: MOD, DIV, ROUND and RANDOM | Operators and Library Routines; Worked Example 1 — Menu, Validation and Function |

---

## Data and Basic Statements

### Variables and constants

- A **variable** is a named storage location whose value can change.
- A **constant** is a named value that remains unchanged while the program runs.

```text
CONSTANT MaxStudents <- 30
StudentCount <- 0
```

Use constants for fixed values such as tax rates, array limits and conversion factors. This avoids unexplained “magic numbers”.

### Primitive data types

| Type | Example | Suitable use |
|---|---|---|
| Integer | `-4`, `27` | counts, whole-number scores |
| Real | `3.75` | measurements, averages |
| Character | `'Y'` | one symbol |
| String | `"Aisha"` | names and text |
| Boolean | `TRUE`, `FALSE` | flags and conditions |

Do not store a phone number as an integer if it may begin with zero or contain formatting characters. A string is safer.

### Input, output and assignment

```text
INPUT Width
Area <- Width * Width
OUTPUT "Area = ", Area
```

Assignment replaces the previous value of a variable. It is not the same as mathematical equality.

---

## Sequence, Selection and Iteration

### Sequence

Statements run in order.

```text
INPUT Price
Discount <- Price * 0.10
FinalPrice <- Price - Discount
OUTPUT FinalPrice
```

### IF selection

```text
IF Temperature < 0 THEN
    OUTPUT "Freezing"
ELSE
    OUTPUT "Not freezing"
ENDIF
```

Nested selections may be used, but keep the indentation clear.
Questions may include statements nested up to three levels. Indent once for each
open block and close the blocks in reverse order.

```text
IF Mark >= 40 THEN
    IF Mark >= 70 THEN
        Grade <- "Distinction"
    ELSE
        Grade <- "Pass"
    ENDIF
ELSE
    Grade <- "Retry"
ENDIF
```

### CASE selection

Use `CASE` when one expression is compared with several distinct choices.

```text
CASE OF MenuChoice
    1 : OUTPUT "Add"
    2 : OUTPUT "Search"
    3 : OUTPUT "Exit"
    OTHERWISE OUTPUT "Invalid"
ENDCASE
```

### Count-controlled loop

Use `FOR` when the number of repetitions is known.

```text
FOR Index <- 1 TO 10
    OUTPUT Index
NEXT Index
```

### Pre-condition loop

A `WHILE` loop may run zero times because its condition is tested first.

```text
WHILE Balance > 0 DO
    Balance <- Balance - Payment
ENDWHILE
```

### Post-condition loop

A `REPEAT ... UNTIL` loop runs at least once because its condition is tested after the body.

```text
REPEAT
    INPUT Choice
UNTIL Choice >= 1 AND Choice <= 3
```

---

## Operators and Library Routines

### Arithmetic operators

| Operator | Meaning | Example result |
|---|---|---|
| `+` | addition | `7 + 2 = 9` |
| `-` | subtraction | `7 - 2 = 5` |
| `*` | multiplication | `7 * 2 = 14` |
| `/` | real division | `7 / 2 = 3.5` |
| `^` | exponent | `3 ^ 2 = 9` |
| `DIV` | integer quotient | `7 DIV 2 = 3` |
| `MOD` | remainder | `7 MOD 2 = 1` |

### Relational and logical operators

- relational: `=`, `<`, `<=`, `>`, `>=`, `<>`
- logical: `AND`, `OR`, `NOT`

```text
IF Age >= 12 AND Age <= 17 THEN
    OUTPUT "Teen ticket"
ENDIF
```

`AND` requires both conditions to be true. `OR` requires at least one. `NOT` reverses a Boolean value.

### ROUND and RANDOM

- `ROUND(Number, Places)` rounds a value to a stated number of decimal places.
- `RANDOM()` produces a pseudo-random value; the exact range or calling form will be stated by the question or language.

```text
Average <- ROUND(Total / Count, 2)
```

Do not assume an unstated `RANDOM` range. Convert it only according to the definition supplied in the question.

---

## String Handling

Common string operations include:

| Operation | Example purpose |
|---|---|
| Length | find the number of characters |
| Substring | extract part of a string |
| Upper case | convert letters to upper case |
| Lower case | convert letters to lower case |

```text
CodeLength <- LENGTH(Code)
Prefix <- SUBSTRING(Code, 1, 2)
UpperCode <- UCASE(Code)
LowerName <- LCASE(Name)
```

Questions may number the first character as position 0 or position 1. Use the convention stated in the question and do not mix conventions.

Example: if the first character is position 1, then:

```text
Code <- "AB407"
Prefix <- SUBSTRING(Code, 1, 2)
```

gives `"AB"`.

---

## Procedures, Functions and Scope

### Procedure

A procedure performs a task and does not return a value directly.

```text
PROCEDURE DisplayResult(Name : STRING, Score : INTEGER)
    OUTPUT Name, " scored ", Score
ENDPROCEDURE
```

Call:

```text
CALL DisplayResult("Mina", 72)
```

### Function

A function returns one value.

```text
FUNCTION IsValidMark(Mark : INTEGER) RETURNS BOOLEAN
    RETURN Mark >= 0 AND Mark <= 100
ENDFUNCTION
```

Call:

```text
Valid <- IsValidMark(InputMark)
```

### Parameters

Parameters carry values into a procedure or function. Use their order and data types consistently. Paper 2 tasks may use up to three parameters.

### Local and global variables

- a **local variable** exists only inside its subroutine
- a **global variable** can be accessed by multiple parts of the program

Prefer local variables unless several subroutines genuinely need shared state. Local scope reduces accidental changes and makes testing easier.

---

## Arrays

An array stores multiple values of the same type under one identifier.

### One-dimensional array

```text
DECLARE Scores : ARRAY[1:5] OF INTEGER

FOR Index <- 1 TO 5
    INPUT Scores[Index]
NEXT Index
```

The index may begin at 0 or 1. Follow the declaration given.

### Two-dimensional array

A two-dimensional array uses a row index and a column index.

```text
DECLARE Rainfall : ARRAY[1:4, 1:7] OF REAL

FOR Week <- 1 TO 4
    FOR Day <- 1 TO 7
        INPUT Rainfall[Week, Day]
    NEXT Day
NEXT Week
```

Nested loops are normally required to process every cell. The inner loop completes all columns for one row before the outer loop advances.

### Variable indexes

```text
Highest <- Scores[1]
HighestIndex <- 1

FOR Index <- 2 TO 5
    IF Scores[Index] > Highest THEN
        Highest <- Scores[Index]
        HighestIndex <- Index
    ENDIF
NEXT Index
```

Here, `Index` is a variable index. `HighestIndex` preserves the position of the best value.

---

## File Handling

Files preserve data after a program stops.

### Write lines

```text
OPENFILE "results.txt" FOR WRITE
WRITEFILE "results.txt", StudentName
WRITEFILE "results.txt", Score
CLOSEFILE "results.txt"
```

### Read lines until end of file

```text
OPENFILE "results.txt" FOR READ

WHILE NOT EOF("results.txt") DO
    READFILE "results.txt", DataLine
    OUTPUT DataLine
ENDWHILE

CLOSEFILE "results.txt"
```

Always:

1. open the file in the correct mode
2. read or write using the same file identifier
3. stop at end of file when reading an unknown number of records
4. close the file

Opening an existing file for writing may replace its contents. Use the mode stated in the question.

---

## Maintainable Programs

A maintainable program is easier to understand, test and change.

Use:

- meaningful identifiers such as `TotalPrice`, not `x`
- consistent indentation
- short procedures and functions with one purpose
- comments that explain non-obvious intent
- named constants for fixed values
- local variables where practical

Avoid comments that merely repeat an instruction.

```text
// Apply loyalty reduction after all item prices have been totalled
FinalCost <- TotalCost * LoyaltyRate
```

This comment adds useful context.

---

## Worked Example 1 — Menu, Validation and Function

A program repeatedly displays three menu options. It must reject other choices and use a function to calculate the area of a rectangle.

```text
FUNCTION RectangleArea(Width : REAL, Height : REAL) RETURNS REAL
    RETURN Width * Height
ENDFUNCTION

REPEAT
    OUTPUT "1 Area"
    OUTPUT "2 Help"
    OUTPUT "3 Exit"
    INPUT Choice

    CASE OF Choice
        1 :
            REPEAT
                INPUT Width
            UNTIL Width > 0
            REPEAT
                INPUT Height
            UNTIL Height > 0
            Area <- RectangleArea(Width, Height)
            OUTPUT ROUND(Area, 2)
        2 :
            OUTPUT "Enter positive dimensions"
        3 :
            OUTPUT "Goodbye"
        OTHERWISE
            OUTPUT "Invalid choice"
    ENDCASE
UNTIL Choice = 3
```

Why it is robust:

- the menu is post-condition controlled, so it appears at least once
- width and height are validated
- `CASE` matches one variable against several choices
- calculation is isolated in a reusable function

---

## Worked Example 2 — Two-Dimensional Array

`Sales[1:3, 1:4]` stores four weekly sales totals for three stores. Find each store total and the largest single value.

```text
Largest <- Sales[1, 1]

FOR Store <- 1 TO 3
    StoreTotal <- 0

    FOR Week <- 1 TO 4
        StoreTotal <- StoreTotal + Sales[Store, Week]

        IF Sales[Store, Week] > Largest THEN
            Largest <- Sales[Store, Week]
        ENDIF
    NEXT Week

    OUTPUT "Store ", Store, StoreTotal
NEXT Store

OUTPUT "Largest weekly value ", Largest
```

`StoreTotal` is reset inside the outer loop because each store needs a separate total. `Largest` is initialised once because it covers the whole array.

---

## Worked Example 3 — Read a File with a Procedure

The file `temperatures.txt` contains one real temperature per line. Display each temperature with the word `"Cold"` if it is below 10.

```text
PROCEDURE DisplayTemperature(Value : REAL)
    IF Value < 10 THEN
        OUTPUT Value, " Cold"
    ELSE
        OUTPUT Value
    ENDIF
ENDPROCEDURE

OPENFILE "temperatures.txt" FOR READ

WHILE NOT EOF("temperatures.txt") DO
    READFILE "temperatures.txt", Temperature
    CALL DisplayTemperature(Temperature)
ENDWHILE

CLOSEFILE "temperatures.txt"
```

The file loop handles an unknown number of lines. The procedure separates display logic from file access.

---

## Required Ideas and Exam Language

Use technical terms as part of a complete statement: identify the component or method, state what it does, then link its effect to the question context. A keyword without a correct relationship is not a complete marking point.

## Common Confusions

- [ ] I choose a data type based on how data is used, not how it looks.
- [ ] I use assignment and equality in the correct contexts.
- [ ] I choose `FOR`, `WHILE` or `REPEAT` deliberately.
- [ ] I write the valid stopping condition after `UNTIL`.
- [ ] I use brackets so mixed logical conditions are unambiguous.
- [ ] I follow the stated string and array indexing convention.
- [ ] I reset a subtotal at the correct loop level.
- [ ] I distinguish a procedure from a value-returning function.
- [ ] I distinguish local from global scope.
- [ ] I open and close files and test for end of file.

---

## Worked Examples

The worked calculations, process templates and scenario answers above model the chain of reasoning expected in examination responses. Rework each example before reading its answer.

## 10-Mark Quick Check

1. State a suitable data type for each value: number of students, average height, one menu letter and a login flag. **[4]**
2. State one difference between a `WHILE` loop and a `REPEAT ... UNTIL` loop. **[2]**
3. Evaluate `17 DIV 5` and `17 MOD 5`. **[2]**
4. State one benefit of a local variable and one benefit of using a function. **[2]**

**Total: 10 marks**

## Quick Check Answers

1. Integer; real; character; Boolean. **[4]**
2. `WHILE` tests before its body and may run zero times; `REPEAT ... UNTIL` tests after its body and therefore runs at least once. **[2]**
3. `17 DIV 5 = 3`; `17 MOD 5 = 2`. **[2]**
4. A local variable reduces unintended access/change outside its subroutine; a function packages reusable logic and returns a value. **[2]**

---

## 20-Mark Exam Practice

A wildlife station stores the number of birds seen at four sites on seven days in `Birds[1:4, 1:7]`. A valid daily count is from 0 to 500 inclusive.

1. Declare the two-dimensional integer array. **[2]**
2. Write pseudocode to input and validate every count. **[5]**
3. Write a function `SiteTotal` that receives a site number and returns the total for its seven days. **[4]**
4. Use the function to output the total for each of the four sites. **[3]**
5. Output the site number with the highest total. If totals are equal, keep the first site. **[4]**
6. State two ways to make the program maintainable. **[2]**

**Total: 20 marks**

### 20 Marks Practice Mark Scheme

1.

   ```text
   DECLARE Birds : ARRAY[1:4, 1:7] OF INTEGER
   ```

   Correct dimensions **[1]** and type **[1]**. **[2]**

2.

   ```text
   FOR Site <- 1 TO 4
       FOR Day <- 1 TO 7
           REPEAT
               INPUT Birds[Site, Day]
           UNTIL Birds[Site, Day] >= 0 AND Birds[Site, Day] <= 500
       NEXT Day
   NEXT Site
   ```

   Correct outer loop **[1]**; inner loop **[1]**; indexed input **[1]**; lower limit **[1]**; upper limit and correct loop ending **[1]**. **[5]**

3.

   ```text
   FUNCTION SiteTotal(SiteNumber : INTEGER) RETURNS INTEGER
       Total <- 0
       FOR Day <- 1 TO 7
           Total <- Total + Birds[SiteNumber, Day]
       NEXT Day
       RETURN Total
   ENDFUNCTION
   ```

   Function header/parameter **[1]**; initialise total **[1]**; correct traversal and accumulation **[1]**; return value **[1]**. **[4]**

4.

   ```text
   FOR Site <- 1 TO 4
       CurrentTotal <- SiteTotal(Site)
       OUTPUT Site, CurrentTotal
   NEXT Site
   ```

   Correct loop **[1]**; function call with site argument **[1]**; both outputs **[1]**. **[3]**

5.

   ```text
   HighestSite <- 1
   HighestTotal <- SiteTotal(1)

   FOR Site <- 2 TO 4
       CurrentTotal <- SiteTotal(Site)
       IF CurrentTotal > HighestTotal THEN
           HighestTotal <- CurrentTotal
           HighestSite <- Site
       ENDIF
   NEXT Site

   OUTPUT HighestSite
   ```

   Initialise from site 1 **[1]**; loop remaining sites **[1]**; strict greater-than update of total and site **[1]**; output site **[1]**. **[4]**

6. Any two: meaningful identifiers, consistent indentation, useful comments, named constants, small procedures/functions, appropriate local variables. **[2]**

---

## Final Revision Checklist

- [ ] I can select and justify primitive data types.
- [ ] I can write sequence, `IF`, `CASE` and all three loop types.
- [ ] I can apply arithmetic, relational and logical operators.
- [ ] I can handle strings using length, substring and case conversion.
- [ ] I can write procedures and functions with up to three parameters.
- [ ] I can reason about local and global scope.
- [ ] I can process one-dimensional and two-dimensional arrays.
- [ ] I can read and write file data safely.
- [ ] I can improve maintainability without changing program behaviour.
- [ ] I completed both practice sets without looking at the answers first.
