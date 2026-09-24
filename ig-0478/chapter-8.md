# IGCSE 0478 Chapter 8: Programming

<div class="chapter-meta"><strong>IGCSE 0478 · Paper 2</strong><span>0478 · 2026–2028 · Version 6</span></div>

## Official Syllabus Checklist

Revise: data types and control structures; strings; arrays; subroutines; files and maintainable programs.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.

> **Paper 2 focus:** choose suitable data, control structures, arrays, subroutines and file operations. Use pseudocode when requested; the final 15-mark scenario also permits program code. This chapter uses Python for the program-code route.

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
IF Temperature < 0
THEN
    OUTPUT "Freezing"
ELSE
    OUTPUT "Not freezing"
ENDIF
```

Nested selections may be used, but keep the indentation clear.
Questions may include statements nested up to three levels. Indent once for each
open block and close the blocks in reverse order.

```text
IF Mark >= 40
THEN
    IF Mark >= 70
    THEN
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
| `DIV(Value1, Value2)` | integer quotient | `DIV(7, 2) = 3` |
| `MOD(Value1, Value2)` | remainder | `MOD(7, 2) = 1` |

### Relational and logical operators

- relational: `=`, `<`, `<=`, `>`, `>=`, `<>`
- logical: `AND`, `OR`, `NOT`

```text
IF Age >= 12 AND Age <= 17
THEN
    OUTPUT "Teen ticket"
ENDIF
```

`AND` requires both conditions to be true. `OR` requires at least one. `NOT` reverses a Boolean value.

### ROUND and RANDOM

- `ROUND(Number, Places)` rounds a value to a stated number of decimal places.
- `RANDOM()` returns a pseudo-random real number between `0` and `1` inclusive.

```text
Average <- ROUND(Total / Count, 2)

RandomValue <- RANDOM()
DiceValue <- 1
IF RandomValue >= 1 / 6
THEN
    DiceValue <- 2
ENDIF
IF RandomValue >= 2 / 6
THEN
    DiceValue <- 3
ENDIF
IF RandomValue >= 3 / 6
THEN
    DiceValue <- 4
ENDIF
IF RandomValue >= 4 / 6
THEN
    DiceValue <- 5
ENDIF
IF RandomValue >= 5 / 6
THEN
    DiceValue <- 6
ENDIF
```

The second example divides the `0` to `1` range into six equal intervals, so `DiceValue` is always from `1` to `6`. Do not confuse IGCSE `RANDOM()` with the 9618 routine `RAND(x)`, which has a different name and range.

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
    IF Scores[Index] > Highest
    THEN
        Highest <- Scores[Index]
        HighestIndex <- Index
    ENDIF
NEXT Index
```

Here, `Index` is a variable index. `HighestIndex` preserves the position of the best value.

---

## File Handling

Files preserve data after a program stops.

Opening and closing control access to the file. Reading and writing may handle either a single data item or a complete line of text. Keep the intended record layout clear: a single numeric item can be read into a numeric variable, while a complete text line may include spaces and is read into a string.

### Read and write single items

```text
OPENFILE "score.txt" FOR READ
READFILE "score.txt", Score
CLOSEFILE "score.txt"

OPENFILE "result.txt" FOR WRITE
WRITEFILE "result.txt", Score
CLOSEFILE "result.txt"
```

Here one file item is transferred to or from one variable.

### Write lines

```text
OPENFILE "results.txt" FOR WRITE
WRITEFILE "results.txt", StudentName
WRITEFILE "results.txt", Score
CLOSEFILE "results.txt"
```

Each `WRITEFILE` statement writes the supplied item as one line in this layout. A program can instead write a complete prepared string, such as `SummaryLine`, as one line of text.

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

### File-operation check

1. Write pseudocode to open `name.txt`, read one complete line into `FullName`, close it, then write `FullName` as one complete line to `copy.txt` and close that file. **[3]**
2. Write pseudocode to open `count.txt`, read the single integer item `Count`, close it, then write that item to `saved-count.txt` and close that file. **[3]**

#### File-operation check answers

1. Open/read/close `name.txt` **[1]**; open `copy.txt` for writing and write `FullName` **[1]**; close `copy.txt` **[1]**. **[3]**
2. Open/read/close `count.txt` into integer variable `Count` **[1]**; open `saved-count.txt` for writing and write `Count` **[1]**; close `saved-count.txt` **[1]**. **[3]**

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

        IF Sales[Store, Week] > Largest
        THEN
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
    IF Value < 10
    THEN
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

## Python Programming Route

Write the algorithm in pseudocode first, then implement it in Python 3. Save each complete block below in its own `.py` file and run it. The assertions check the stated outcomes. For Paper 2, Python is an option for the final 15-mark scenario; use the notation requested in other questions.

| Cambridge pseudocode | Python | Point to check |
|---|---|---|
| `INPUT Value` | `value = input()` | `input()` returns a string; convert before arithmetic |
| `DIV`, `MOD`, `^` | `//`, `%`, `**` | use integer operands for integer division/remainder |
| `AND`, `OR`, `NOT` | `and`, `or`, `not` | Boolean values are `True` and `False` |
| `FOR Index <- 1 TO 5` | `for index in range(5):` | Python indexes here are 0–4; the stop is excluded |
| `SUBSTRING(Code, 2, 3)` | `code[1:4]` | IGCSE start position 2 becomes Python index 1 |
| `LENGTH(Code)` | `len(code)` | Python also permits `len(list)`; Cambridge `LENGTH` is for strings |
| `LCASE(Code)`, `UCASE(Code)` | `code.lower()`, `code.upper()` | the methods return a new string |
| function / procedure | `def`, with / without a result | use `return` for a result; keep names and indentation clear |

### Python Example 1 — Input, Validation and a Menu

This menu repeats until `Q`. Each accepted `A` operation records one integer mark from 0 to 100. The post-condition input loop is written as `while True` with `break` after validation. The two input/output parameters make the same program testable without typing every value again.

```python
def read_mark(read, write):
    while True:
        try:
            mark = int(read("Mark (0–100): "))
            if 0 <= mark <= 100:
                return mark
        except ValueError:
            pass
        write("Invalid mark")


def run_menu(read=input, write=print):
    total = 0
    count = 0
    while True:
        choice = read("A: add mark; Q: quit: ").upper()
        if choice == "Q":
            break
        if choice == "A":
            mark = read_mark(read, write)
            total += mark
            count += 1
            write("Pass" if mark >= 40 else "Fail")
        else:
            write("Unknown option")
    write(total / count if count > 0 else "No marks")
    return count, total


if __name__ == "__main__":
    from sys import argv
    if "--interactive" in argv:
        run_menu()
    else:
        entries = iter(["X", "a", "bad", "-1", "101", "0", "A", "100", "Q"])
        output = []
        assert run_menu(lambda prompt: next(entries), output.append) == (2, 100)
        assert output == ["Unknown option", "Invalid mark", "Invalid mark",
                          "Invalid mark", "Fail", "Pass", 50.0]
        output = []
        assert run_menu(lambda prompt: "Q", output.append) == (0, 0)
        assert output == ["No marks"]
        print("Menu tests passed")
```

Run with `python example.py --interactive` to enter your own data. `try/except` handles a conversion failure; the range check handles a converted integer outside the permitted interval.

### Python Example 2 — Arrays, Search and Sort

Use a list to implement the one-dimensional array. A list of separate row lists represents the two-dimensional array. Do not initialise a matrix with `[[0] * 3] * 4`: its rows refer to the same list.

```python
def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1


def bubble_sort(values):
    high = len(values) - 1
    swapped = True
    while high > 0 and swapped:
        swapped = False
        for index in range(high):
            if values[index] > values[index + 1]:
                temporary = values[index]
                values[index] = values[index + 1]
                values[index + 1] = temporary
                swapped = True
        high -= 1


def row_totals(matrix):
    totals = []
    for row in matrix:
        total = 0
        for value in row:
            total += value
        totals.append(total)
    return totals


if __name__ == "__main__":
    for original, expected in [([], []), ([4], [4]), ([3, -1, 3, 0], [-1, 0, 3, 3])]:
        values = original.copy()
        bubble_sort(values)
        assert values == expected
    assert linear_search([7, 2, 7], 7) == 0
    assert linear_search([7, 2], 8) == -1
    assert linear_search([], 7) == -1
    assert row_totals([[2, 0, 4], [1, 3, 5]]) == [6, 9]
    assert row_totals([]) == []
    print("Array tests passed")
```

### Python Example 3 — File Processing

The input contains one integer mark per line. Count rejected lines, copy valid marks to a new file and return their count and average. Use a different output path: opening a file in `w` mode replaces its previous contents. `with` closes a file when its block finishes, including when an exception is raised.

```python
def summarise_marks(source_path, destination_path):
    count = 0
    total = 0
    rejected = 0
    with open(source_path, "r", encoding="utf-8") as source:
        with open(destination_path, "w", encoding="utf-8") as destination:
            for line in source:
                try:
                    mark = int(line.strip())
                    if not 0 <= mark <= 100:
                        raise ValueError("out of range")
                except ValueError:
                    rejected += 1
                    continue
                destination.write(str(mark) + "\n")
                total += mark
                count += 1
    average = total / count if count > 0 else None
    return count, average, rejected


if __name__ == "__main__":
    from pathlib import Path
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as directory:
        source = Path(directory) / "marks.txt"
        destination = Path(directory) / "accepted.txt"
        source.write_text("0\nwrong\n101\n100\n\n", encoding="utf-8")
        assert summarise_marks(source, destination) == (2, 50.0, 3)
        assert destination.read_text(encoding="utf-8") == "0\n100\n"
        source.write_text("", encoding="utf-8")
        assert summarise_marks(source, destination) == (0, None, 0)
        assert destination.read_text(encoding="utf-8") == ""
    print("File tests passed")
```

### Python Transfer Drill

1. Change the menu's accepted interval to 1–50 and pass threshold to 25. Give tests for both accepted endpoints and the adjacent rejected values. **[4]**
2. Write a function that returns the index of the row with the greatest total, retaining the first row on a tie and returning `-1` for an empty matrix. **[4]**
3. Adapt the file program to append a single summary line to a separate log, including `No marks` for an empty input. Explain why the log must use append mode. **[4]**

**Total: 12 marks**

#### Python Transfer Drill Answers

1. Change the validation to `1 <= mark <= 50` **[1]** and the pass test to `mark >= 25` **[1]**. Accept 1 and 50 **[1]**; reject 0 and 51 **[1]**. Also check 24 gives Fail and 25 gives Pass.
2. The following function handles empty input **[1]**, visits every row **[1]**, replaces the selected index only for a strictly greater total **[1]** and returns the correct index **[1]**.

```python
def greatest_row(matrix):
    best_index = -1
    best_total = 0
    for index in range(len(matrix)):
        total = 0
        for value in matrix[index]:
            total += value
        if best_index == -1 or total > best_total:
            best_index = index
            best_total = total
    return best_index


if __name__ == "__main__":
    assert greatest_row([]) == -1
    assert greatest_row([[-4, -2], [-1, -3], [-2, -2]]) == 1
    assert greatest_row([[2], [2]]) == 0
```

3. Open the separate log with `with open(log_path, "a", encoding="utf-8") as log:` **[1]**; select the average or `No marks` according to the count **[1]**; write the result plus `"\n"` and close via `with` **[1]**. Append preserves previous summaries; write mode would replace them **[1]**. The log must differ from both the input and accepted-mark output paths.

## Targeted Syllabus Drill

1. Write one `IF` statement and one `CASE` statement that output a message for a menu choice from 1 to 3. **[4]**
2. Use a count-controlled loop to output 1 to 3, then write both a pre-condition loop and a post-condition loop that repeatedly input `Choice` until it is from 1 to 3 inclusive. **[6]**
3. For `Code <- "Ab407"`, write statements that obtain its length, extract three characters from position 2, convert it to upper case and convert it to lower case. **[4]**
4. State the results of `DIV(17, 5)`, `MOD(17, 5)` and `ROUND(7 / 3, 2)`, then write an expression using `RANDOM()` that produces a real value in its defined range. **[4]**
5. Distinguish a procedure from a function, explain the purpose of a parameter, and distinguish local from global scope. **[4]**
6. Write one statement that adds `Value` to a total and one selection that increments `Count` only when `Value > 0`. **[2]**
7. Declare `Scores` as a one-dimensional array of five integers, input every element using a variable index, and increase the third element by one. **[4]**

### Targeted Syllabus Drill Answers

1. One correctly formed `IF ... THEN ... ELSE ... ENDIF` selection **[2]** and one correctly formed `CASE OF ... OTHERWISE ... ENDCASE` selection **[2]**. **[4]**
2. For example: `FOR Value <- 1 TO 3 ... NEXT Value` **[2]**; initialise/input `Choice`, then use `WHILE Choice < 1 OR Choice > 3 DO ... ENDWHILE` **[2]**; use `REPEAT INPUT Choice UNTIL Choice >= 1 AND Choice <= 3` **[2]**. **[6]**
3. `LENGTH(Code)`; `SUBSTRING(Code, 2, 3)`; `UCASE(Code)`; `LCASE(Code)`. One mark for each correct operation and arguments. **[4]**
4. `3`; `2`; `2.33`; `RANDOM()` (or assignment from it). **[4]**
5. A procedure performs a task without directly returning a value **[1]**; a function returns one value **[1]**; a parameter passes a value into a subroutine **[1]**; local scope is restricted to its subroutine while global scope is accessible more widely **[1]**. **[4]**
6. `Total <- Total + Value` **[1]**; `IF Value > 0 THEN Count <- Count + 1 ENDIF` **[1]**. **[2]**
7. `DECLARE Scores : ARRAY[1:5] OF INTEGER` **[1]**; a loop from 1 to 5 **[1]** with `INPUT Scores[Index]` **[1]**; `Scores[3] <- Scores[3] + 1` **[1]**. **[4]**

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
2. For `Code <- "AB219"`, state the results of `LENGTH(Code)` and `SUBSTRING(Code, 2, 3)` when the first character is position 1. **[2]**
3. Calculate `DIV(17, 5)` and `MOD(17, 5)`. **[2]**
4. State one benefit of a local variable and one benefit of using a function. **[2]**

**Total: 10 marks**

## Quick Check Answers

1. Integer; real; character; Boolean. **[4]**
2. `5`; `"B21"`. **[2]**
3. `DIV(17, 5) = 3`; `MOD(17, 5) = 2`. **[2]**
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

<span id="20-marks-practice-mark-scheme" class="legacy-anchor" aria-hidden="true"></span>

### 20 Marks Practice Indicative Marking Points

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
       IF CurrentTotal > HighestTotal
       THEN
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
