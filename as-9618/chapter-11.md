# AS 9618 Chapter 11: Programming

> **Paper 2 focus:** translate a design into correct, efficient pseudocode using declarations, expressions, suitable control structures and well-defined subroutines.

---

## 1. Syllabus Coverage

| Syllabus objective | Where it is covered |
|---|---|
| Implement pseudocode from a flowchart or structured English | Sections 2 and 6 |
| Declare and initialise constants | Section 2 |
| Declare variables and assign values | Section 2 |
| Use arithmetic and logical expressions | Section 3 |
| Input from keyboard and output to console | Section 2 |
| Use supplied built-in/library/string routines | Section 4 |
| Write IF/ELSE, nested IF and CASE | Section 5 |
| Write count-, pre- and post-condition loops | Section 6 |
| Justify the choice of loop | Section 6 |
| Define and use procedures | Section 7 |
| Pass parameters by value and by reference | Section 8 |
| Define and use functions in expressions | Section 9 |
| Use subroutine terminology correctly | Section 10 |
| Write efficient pseudocode | Section 11 and Worked Example 3 |

---

## 2. Programming Basics

### Constants

```text
CONSTANT MAX_ITEMS = 50
CONSTANT TAX_RATE = 0.08
```

A constant has a meaningful name and is not changed while the program runs.

### Variables

```text
DECLARE ItemCount : INTEGER
DECLARE TotalCost : REAL
DECLARE MenuChoice : CHAR
DECLARE IsValid : BOOLEAN
```

### Assignment

```text
ItemCount <- 0
TotalCost <- TotalCost + CurrentPrice
IsValid <- Score >= 0 AND Score <= 100
```

The assignment arrow stores a new value. The equals sign is used for comparison inside a condition.

### Input and output

```text
OUTPUT "Enter quantity"
INPUT Quantity
OUTPUT "Total: ", Total
```

Prompts should make the required input clear when user interaction is part of the design.

---

## 3. Expressions and Operators

### Arithmetic

| Operator | Meaning | Example |
|---|---|---|
| `+` | addition | `A + B` |
| `-` | subtraction | `A - B` |
| `*` | multiplication | `A * B` |
| `/` | real division | `7 / 2 = 3.5` |
| `DIV` | integer quotient | `7 DIV 2 = 3` |
| `MOD` | remainder | `7 MOD 2 = 1` |

### Relational

```text
=   <>   <   <=   >   >=
```

### Logical

```text
AND   OR   NOT
```

Use brackets when several operations are combined:

```text
IsEligible <- (Age >= 16 AND Age <= 18) OR HasPermit = TRUE
```

Do not assume ambiguous precedence when brackets can state the intention.

---

## 4. Built-In and Library Routines

The question or pseudocode guide defines the routines available. Use their stated:

- name
- parameter order
- parameter type
- return type

Examples of purposes:

- string length
- substring extraction
- upper/lower-case conversion
- rounding
- random value generation

If a question provides:

```text
LENGTH(Text)
SUBSTRING(Text, Start, Count)
```

use exactly that interface. Do not invent a different parameter order.

String manipulation routines needed for a question will be supplied.

---

## 5. Selection

### IF / ELSE

```text
IF Temperature < 0 THEN
    OUTPUT "Frozen"
ELSE
    OUTPUT "Not frozen"
ENDIF
```

### Nested IF

```text
IF Mark >= 40 THEN
    IF Mark >= 70 THEN
        Grade <- "Distinction"
    ELSE
        Grade <- "Pass"
    ENDIF
ELSE
    Grade <- "Fail"
ENDIF
```

### CASE

```text
CASE OF Choice
    1 : CALL AddItem()
    2 : CALL FindItem()
    3 : OUTPUT "Exit"
    OTHERWISE : OUTPUT "Invalid"
ENDCASE
```

Use `CASE` when one expression is matched against distinct choices. Use `IF` for ranges and compound Boolean conditions.

---

## 6. Iteration and Loop Choice

### Count-controlled loop

```text
FOR Index <- 1 TO 20
    OUTPUT Value[Index]
NEXT Index
```

Choose `FOR` when the number of repetitions is known.

### Pre-condition loop

```text
WHILE Index <= UpperBound AND Found = FALSE
    ...
ENDWHILE
```

Choose `WHILE` when:

- the condition must be checked before the first iteration
- zero iterations may be correct
- the number of repetitions is not known

### Post-condition loop

```text
REPEAT
    INPUT Choice
UNTIL Choice >= 1 AND Choice <= 4
```

Choose `REPEAT ... UNTIL` when:

- the body must execute at least once
- the stopping condition is checked afterwards

### Justification pattern

Weak:

> A WHILE loop is best.

Strong:

> A WHILE loop is suitable because the file may contain zero lines, the number of lines is unknown, and the end-of-file condition must be checked before reading.

---

## 7. Procedures

A **procedure** performs a task and does not return a value through a function result.

```text
PROCEDURE DisplayResult(Name : STRING, Score : INTEGER)
    OUTPUT Name, " scored ", Score
ENDPROCEDURE

CALL DisplayResult("Ravi", 72)
```

Use a procedure when:

- a named action is required
- several statements belong together
- the task may be reused
- the main algorithm becomes clearer by hiding detail

---

## 8. Parameters: By Value and By Reference

### By value

A copy of the argument is passed. Changing the parameter does not change the original variable.

```text
PROCEDURE AddOne(BYVAL Number : INTEGER)
    Number <- Number + 1
ENDPROCEDURE
```

If `Score = 8`, calling `AddOne(Score)` leaves `Score = 8`.

### By reference

The parameter refers to the original variable. Changing it changes the argument.

```text
PROCEDURE AddOne(BYREF Number : INTEGER)
    Number <- Number + 1
ENDPROCEDURE
```

If `Score = 8`, calling `AddOne(Score)` changes `Score` to 9.

### Swap using reference parameters

```text
PROCEDURE Swap(BYREF First : INTEGER, BYREF Second : INTEGER)
    Temp <- First
    First <- Second
    Second <- Temp
ENDPROCEDURE
```

Use reference parameters only when the subroutine is intended to update the caller's data.

---

## 9. Functions

A **function** returns one value and its call is used in an expression.

```text
FUNCTION IsValidMark(Mark : INTEGER) RETURNS BOOLEAN
    RETURN Mark >= 0 AND Mark <= 100
ENDFUNCTION
```

Call:

```text
IF IsValidMark(InputMark) = TRUE THEN
    OUTPUT "Accepted"
ENDIF
```

Another example:

```text
FUNCTION CalculateArea(Width : REAL, Height : REAL) RETURNS REAL
    RETURN Width * Height
ENDFUNCTION

TotalArea <- CalculateArea(4.5, 3.0) + CalculateArea(2.0, 1.0)
```

The returned values replace the function calls in the expression.

---

## 10. Subroutine Terminology

| Term | Meaning |
|---|---|
| header | first line defining the name, parameters and return type if applicable |
| interface | how other code communicates with the subroutine |
| parameter | named input in the subroutine definition |
| argument | actual value or variable supplied in a call |
| return value | result produced by a function |
| call | instruction that transfers control to the subroutine |

For:

```text
FUNCTION Larger(First : INTEGER, Second : INTEGER) RETURNS INTEGER
```

- `First` and `Second` are parameters
- in `Larger(Age1, Age2)`, `Age1` and `Age2` are arguments
- the header forms part of the interface

---

## 11. Efficient Pseudocode

Efficiency includes using fewer unnecessary operations and writing a solution that is clear enough to maintain.

Improve efficiency by:

- using one traversal when several results can be calculated together
- stopping a search when a match is found
- moving calculations outside a loop when they do not change
- avoiding repeated code by using a subroutine
- choosing a suitable loop and data structure
- avoiding unnecessary nested loops

Inefficient:

```text
FOR Index <- 1 TO 100
    Total <- Total + Value[Index]
NEXT Index

FOR Index <- 1 TO 100
    IF Value[Index] > Highest THEN
        Highest <- Value[Index]
    ENDIF
NEXT Index
```

One traversal:

```text
Total <- 0
Highest <- Value[1]

FOR Index <- 1 TO 100
    Total <- Total + Value[Index]
    IF Value[Index] > Highest THEN
        Highest <- Value[Index]
    ENDIF
NEXT Index
```

Do not sacrifice correctness or readability for a tiny reduction in instructions.

---

## 12. Worked Example 1 — Structured English to Pseudocode

Design:

> Display a menu at least once. Input a choice from 1 to 3. For choice 1, input a positive radius and display its area. For choice 2, display help. Choice 3 exits. Reject all other choices.

```text
CONSTANT PI = 3.142

REPEAT
    OUTPUT "1 Circle area"
    OUTPUT "2 Help"
    OUTPUT "3 Exit"
    INPUT Choice

    CASE OF Choice
        1 :
            REPEAT
                INPUT Radius
            UNTIL Radius > 0
            Area <- PI * Radius * Radius
            OUTPUT Area
        2 :
            OUTPUT "Enter a positive radius"
        3 :
            OUTPUT "Goodbye"
        OTHERWISE :
            OUTPUT "Invalid choice"
    ENDCASE
UNTIL Choice = 3
```

The post-condition loop is justified because the menu must appear at least once.

---

## 13. Worked Example 2 — Trace Value and Reference Parameters

```text
PROCEDURE Change(BYVAL A : INTEGER, BYREF B : INTEGER)
    A <- A + 2
    B <- B + A
ENDPROCEDURE

X <- 3
Y <- 4
CALL Change(X, Y)
OUTPUT X, Y
```

Trace:

| Step | A | B / Y | X |
|---|---:|---:|---:|
| before call | 3 | 4 | 3 |
| `A <- A + 2` | 5 | 4 | 3 |
| `B <- B + A` | 5 | 9 | 3 |
| after return | local parameter ends | 9 | 3 |

Output: `3, 9`.

`A` was a copy of `X`; `B` referred to `Y`.

---

## 14. Worked Example 3 — Refactor Repeated Logic

Repeated design:

```text
INPUT FirstMark
WHILE FirstMark < 0 OR FirstMark > 100
    INPUT FirstMark
ENDWHILE

INPUT SecondMark
WHILE SecondMark < 0 OR SecondMark > 100
    INPUT SecondMark
ENDWHILE
```

Refactored:

```text
FUNCTION GetValidMark() RETURNS INTEGER
    REPEAT
        INPUT Mark
    UNTIL Mark >= 0 AND Mark <= 100
    RETURN Mark
ENDFUNCTION

FirstMark <- GetValidMark()
SecondMark <- GetValidMark()
```

The function:

- removes duplicated validation
- has one clear purpose
- can be tested once and reused
- keeps the main program concise

---

## 15. Common Mistakes Checklist

- [ ] I declare values before using them.
- [ ] I distinguish assignment from equality.
- [ ] I bracket compound expressions clearly.
- [ ] I choose `CASE` only for discrete choices.
- [ ] I justify loop choice using execution behaviour.
- [ ] I ensure `WHILE` loops make progress.
- [ ] I write the valid stopping condition after `UNTIL`.
- [ ] I distinguish parameters from arguments.
- [ ] I use `BYREF` only when caller data should change.
- [ ] I use a function call inside an expression.
- [ ] I remove unnecessary traversals without changing behaviour.

---

## 16. 10 Marks Quick Check

1. State one difference between a constant and a variable. **[2]**
2. Give one situation suitable for each loop: `FOR`, `WHILE`, `REPEAT ... UNTIL`. **[3]**
3. Distinguish a parameter from an argument. **[2]**
4. State the effect of passing a parameter by reference and state one appropriate use. **[2]**
5. State how a function call is used. **[1]**

**Total: 10 marks**

### Quick Check Answers

1. A constant cannot change during execution, while a variable can; both should be named. **[2]**
2. `FOR`: known repetition count; `WHILE`: condition tested first/zero repetitions possible; `REPEAT`: body must execute at least once. **[3]**
3. A parameter is the named placeholder in a subroutine definition; an argument is the actual value/variable supplied in a call. **[2]**
4. It allows the subroutine to modify the caller's original variable **[1]**; suitable for swapping or returning an additional updated value **[1]**. **[2]**
5. Its return value replaces the call within an expression. **[1]**

---

## 17. 20 Marks Practice

A delivery program processes an unknown number of parcel masses. Entry stops when `-1` is entered. Valid masses are greater than 0 and at most 25.0 kg.

1. Explain why a `WHILE` loop is more suitable than a `FOR` loop for the main input process. **[2]**
2. Write a function `IsValidMass` that receives a real mass and returns a Boolean. **[3]**
3. Write a procedure `UpdateTotals` with:
   - mass passed by value
   - total mass and parcel count passed by reference
   - correct updates to both reference parameters. **[5]**
4. Write the main pseudocode to:
   - initialise total and count
   - input masses until `-1`
   - reject other invalid values with a message
   - call `UpdateTotals` for valid values
   - output the count and average, avoiding division by zero. **[8]**
5. State one reason this modular solution is more maintainable than duplicating the update logic. **[2]**

**Total: 20 marks**

### 20 Marks Practice Mark Scheme

1. The number of parcels is unknown **[1]**, and the stopping value must be tested during execution rather than repeating a fixed number of times **[1]**. **[2]**
2.

   ```text
   FUNCTION IsValidMass(Mass : REAL) RETURNS BOOLEAN
       RETURN Mass > 0 AND Mass <= 25.0
   ENDFUNCTION
   ```

   Correct header/type **[1]**; both limits combined with `AND` **[1]**; returns Boolean result **[1]**. **[3]**

3.

   ```text
   PROCEDURE UpdateTotals(
       BYVAL Mass : REAL,
       BYREF TotalMass : REAL,
       BYREF ParcelCount : INTEGER
   )
       TotalMass <- TotalMass + Mass
       ParcelCount <- ParcelCount + 1
   ENDPROCEDURE
   ```

   Procedure/header **[1]**; correct value parameter **[1]**; two reference parameters **[1]**; total update **[1]**; count update **[1]**. **[5]**

4.

   ```text
   TotalMass <- 0
   ParcelCount <- 0
   INPUT Mass

   WHILE Mass <> -1
       IF IsValidMass(Mass) = TRUE THEN
           CALL UpdateTotals(Mass, TotalMass, ParcelCount)
       ELSE
           OUTPUT "Invalid mass"
       ENDIF
       INPUT Mass
   ENDWHILE

   OUTPUT ParcelCount
   IF ParcelCount > 0 THEN
       OUTPUT TotalMass / ParcelCount
   ELSE
       OUTPUT "No parcels"
   ENDIF
   ```

   Initialise both accumulators **[1]**; priming input **[1]**; correct sentinel loop **[1]**; function call/selection **[1]**; update call for valid data **[1]**; invalid message **[1]**; next input **[1]**; safe count/average output **[1]**. **[8]**

5. Any valid reason, such as one update module can be changed/tested once **[1]** and every call uses the corrected behaviour **[1]**. **[2]**

---

## 18. Final Self-Assessment

- [ ] I can translate structured English or a flowchart into pseudocode.
- [ ] I can declare constants and variables and build expressions.
- [ ] I can choose and justify every selection and loop construct.
- [ ] I can define procedures and functions with clear interfaces.
- [ ] I can trace value and reference parameters.
- [ ] I can use subroutine terminology accurately.
- [ ] I can improve pseudocode efficiency without changing its result.
- [ ] I completed both practice sets before checking the answers.
