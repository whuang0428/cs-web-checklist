# IGCSE 0478 Paper 2 Mixed Review — Set B

> **Original practice paper:** an independent second set for timed retesting. It does not reproduce official questions or mark schemes.

## Instructions

- Recommended time: **1 hour 45 minutes**
- Total: **75 marks**
- Do not use a calculator.
- Answer all seven questions.
- Use pseudocode for coding answers; Question 7 may instead be answered in Python. Do not mix syntaxes.
- Complete this set without referring to Set A.

### Coverage Map

| Question | Main topic | Marks |
|---:|---|---:|
| 1 | Problem analysis, validation and testing | 8 |
| 2 | Trace tables and bubble sort | 10 |
| 3 | Two-dimensional arrays and functions | 12 |
| 4 | Database structure and SQL | 10 |
| 5 | Boolean logic | 10 |
| 6 | Strings, files and maintainability | 10 |
| 7 | Integrated programming scenario | 15 |
| **Total** | **Topics 7–10** | **75** |

---

## Question 1 — Design and Testing [8]

A bicycle-hire kiosk inputs a bicycle code, hire duration from 1 to 8 hours inclusive and whether a helmet is required. It calculates a charge and displays a confirmation.

1. State two inputs and one output. **[3]**
2. Give two suitable program modules and the purpose of each. **[2]**
3. Give one normal, one lower-extreme and one abnormal-boundary value for hire duration. Label each value. **[3]**

---

## Question 2 — Bubble Sort Trace [10]

The array begins as:

```text
Scores = [41, 27, 35, 18, 50]
```

The following code performs an ascending bubble sort.

```text
Upper <- 5
Swapped <- TRUE

WHILE Upper > 1 AND Swapped = TRUE
    Swapped <- FALSE
    FOR Index <- 1 TO Upper - 1
        IF Scores[Index] > Scores[Index + 1] THEN
            Temp <- Scores[Index]
            Scores[Index] <- Scores[Index + 1]
            Scores[Index + 1] <- Temp
            Swapped <- TRUE
        ENDIF
    NEXT Index
    Upper <- Upper - 1
ENDWHILE
```

1. State the array after the first complete pass. **[4]**
2. State the array after the second complete pass. **[3]**
3. State the final sorted array. **[2]**
4. Explain the purpose of `Swapped`. **[1]**

---

## Question 3 — Arrays and Functions [12]

`Sales[1:4, 1:3]` stores sales for four products over three months. Every value is an integer from 0 to 500 inclusive.

1. Write pseudocode to input and validate all 12 values. **[4]**
2. Write a function `ProductTotal(ProductNumber : INTEGER) RETURNS INTEGER` that returns the three-month total for one product. **[4]**
3. Write pseudocode that calls the function for all four products and outputs the product number with the lowest total. If totals are equal, keep the first product. **[4]**

---

## Question 4 — Database and SQL [10]

The table `Bookings` contains:

| BookingID | Customer | Activity | Participants | Paid | Cost |
|---|---|---|---:|---|---:|
| B201 | Ava | Climbing | 2 | TRUE | 38.00 |
| B202 | Noah | Kayaking | 4 | FALSE | 72.00 |
| B203 | Imani | Climbing | 1 | TRUE | 19.00 |
| B204 | Luis | Cycling | 3 | FALSE | 45.00 |
| B205 | Mina | Kayaking | 2 | TRUE | 36.00 |

1. Identify the primary key and justify the choice. **[2]**
2. State suitable data types for `Participants`, `Paid` and `Cost`. **[3]**
3. Write SQL to display `Customer`, `Activity` and `Cost` for unpaid bookings costing at least 40, ordered by cost ascending. **[3]**
4. Write SQL to output the total cost of all climbing bookings. **[2]**

---

## Question 5 — Boolean Logic [10]

A warning output is defined by:

```text
W = (A NAND B) AND (C OR NOT D)
```

1. Name the four gate operations used. **[2]**
2. Calculate `W` for each input set. **[4]**

   | A | B | C | D | W |
   |---:|---:|---:|---:|---:|
   | 0 | 0 | 0 | 0 | |
   | 1 | 1 | 0 | 0 | |
   | 1 | 0 | 0 | 1 | |
   | 1 | 0 | 1 | 1 | |

3. Describe how to construct the circuit, including the intermediate connections. **[4]**

---

## Question 6 — Strings and Files [10]

The file `Codes.txt` contains one code per line. A valid code has exactly eight characters and begins with `"X"`.

1. Write pseudocode to open the file, read every line, count valid codes, close the file and output the count. **[6]**
2. State the two string operations needed to test length and first character. **[2]**
3. Give two ways the solution is made maintainable. **[2]**

---

## Question 7 — Integrated Programming Scenario [15]

A school event stores 12 activity records. Each record has:

- `Code : STRING`
- `Places : INTEGER`
- `Price : REAL`

Write one complete solution that:

- repeatedly inputs an activity code
- stops when `"END"` is entered or four places have been booked in total
- uses linear search to find the activity
- displays `"Unknown code"` when absent
- when found, inputs a required number of places from 1 to 3 and validates it
- displays `"Insufficient places"` if the activity does not have enough places
- otherwise subtracts the required places, adds them to the total booked, adds `required places * price` to total cost and displays `"Booking accepted"`
- never allows the total booked to exceed four
- finally outputs total places booked and total cost

Use pseudocode or Python. **[15]**

---

## Mark Scheme

### Question 1 Mark Scheme [8]

1. Any two of bicycle code, hire duration, helmet choice **[2]**; calculated charge or confirmation details **[1]**. **[3]**
2. Any two distinct modules plus linked purpose, for example `GetHireDetails`, `ValidateHire`, `CalculateCharge`, `DisplayConfirmation`. **[2]**
3. Normal such as `4` **[1]**; lower extreme `1` **[1]**; abnormal boundary `0` or `9` **[1]**. **[3]**

### Question 2 Mark Scheme [10]

1. `[27, 35, 18, 41, 50]`; one mark for each correctly positioned value except the unchanged final value. **[4]**
2. `[27, 18, 35, 41, 50]`; one mark for each of the first three positions. **[3]**
3. `[18, 27, 35, 41, 50]`. **[2]**
4. It records whether a swap occurred so the algorithm can stop early when a complete pass makes no swaps. **[1]**

### Question 3 Mark Scheme [12]

1.

```text
FOR Product <- 1 TO 4
    FOR Month <- 1 TO 3
        REPEAT
            INPUT Sales[Product, Month]
        UNTIL Sales[Product, Month] >= 0 AND Sales[Product, Month] <= 500
    NEXT Month
NEXT Product
```

Nested loops **[2]**; input correct element **[1]**; both validation limits **[1]**. **[4]**

2.

```text
FUNCTION ProductTotal(ProductNumber : INTEGER) RETURNS INTEGER
    Total <- 0
    FOR Month <- 1 TO 3
        Total <- Total + Sales[ProductNumber, Month]
    NEXT Month
    RETURN Total
ENDFUNCTION
```

Header/return type **[1]**; initialisation and loop **[1]**; correct accumulation **[1]**; return **[1]**. **[4]**

3.

```text
LowestProduct <- 1
LowestTotal <- ProductTotal(1)

FOR Product <- 2 TO 4
    CurrentTotal <- ProductTotal(Product)
    IF CurrentTotal < LowestTotal THEN
        LowestTotal <- CurrentTotal
        LowestProduct <- Product
    ENDIF
NEXT Product

OUTPUT LowestProduct
```

Initial first product **[1]**; loop/calls function **[1]**; strict comparison preserves first tie **[1]**; updates/outputs correct identifier **[1]**. **[4]**

### Question 4 Mark Scheme [10]

1. `BookingID` **[1]** because it is unique for every record **[1]**. **[2]**
2. Participants: INTEGER; Paid: BOOLEAN; Cost: REAL. **[3]**
3.

```sql
SELECT Customer, Activity, Cost
FROM Bookings
WHERE Paid = FALSE AND Cost >= 40
ORDER BY Cost ASCENDING;
```

Fields/table **[1]**; both conditions **[1]**; ascending order **[1]**. **[3]**
4.

```sql
SELECT SUM(Cost)
FROM Bookings
WHERE Activity = 'Climbing';
```

Correct aggregate **[1]** and condition **[1]**. **[2]**

### Question 5 Mark Scheme [10]

1. NAND, AND, OR and NOT; all four for two marks, two or three for one. **[2]**
2.

   | A | B | C | D | W |
   |---:|---:|---:|---:|---:|
   | 0 | 0 | 0 | 0 | 1 |
   | 1 | 1 | 0 | 0 | 0 |
   | 1 | 0 | 0 | 1 | 0 |
   | 1 | 0 | 1 | 1 | 1 |

   One mark per row. **[4]**
3. Connect A and B to NAND **[1]**; invert D with NOT **[1]**; connect C and `NOT D` to OR **[1]**; connect NAND output and OR output to final AND **[1]**. **[4]**

### Question 6 Mark Scheme [10]

1.

```text
DECLARE Code : STRING
DECLARE ValidCount : INTEGER

ValidCount <- 0
OPENFILE "Codes.txt" FOR READ
WHILE NOT EOF("Codes.txt")
    READFILE "Codes.txt", Code
    IF LENGTH(Code) = 8 AND SUBSTRING(Code, 1, 1) = "X" THEN
        ValidCount <- ValidCount + 1
    ENDIF
ENDWHILE
CLOSEFILE "Codes.txt"
OUTPUT ValidCount
```

Initialise/open **[1]**; EOF loop/read **[1]**; length test **[1]**; first-character test **[1]**; count **[1]**; close/output **[1]**. **[6]**
2. `LENGTH` **[1]** and `SUBSTRING` **[1]**. **[2]**
3. Any two: meaningful identifiers, indentation, comments, named function/procedure, constant for required length, avoiding repeated logic. **[2]**

### Question 7 Mark Scheme [15]

- repetition and input with both stop conditions **[2]**
- linear search with found/index state **[3]**
- absent-code message **[1]**
- input and validation of required places **[2]**
- prevents activity stock and overall limit from being exceeded **[2]**
- insufficient-places message **[1]**
- updates places and total booked **[2]**
- calculates total cost **[1]**
- final outputs **[1]**

Indicative pseudocode:

```text
TotalBooked <- 0
TotalCost <- 0

REPEAT
    INPUT RequiredCode
    IF RequiredCode <> "END" THEN
        Found <- FALSE
        Index <- 1
        WHILE Index <= 12 AND Found = FALSE
            IF Activity[Index].Code = RequiredCode THEN
                Found <- TRUE
            ELSE
                Index <- Index + 1
            ENDIF
        ENDWHILE

        IF Found = FALSE THEN
            OUTPUT "Unknown code"
        ELSE
            REPEAT
                INPUT RequiredPlaces
            UNTIL RequiredPlaces >= 1 AND RequiredPlaces <= 3

            IF RequiredPlaces > Activity[Index].Places OR TotalBooked + RequiredPlaces > 4 THEN
                OUTPUT "Insufficient places"
            ELSE
                Activity[Index].Places <- Activity[Index].Places - RequiredPlaces
                TotalBooked <- TotalBooked + RequiredPlaces
                TotalCost <- TotalCost + RequiredPlaces * Activity[Index].Price
                OUTPUT "Booking accepted"
            ENDIF
        ENDIF
    ENDIF
UNTIL RequiredCode = "END" OR TotalBooked = 4

OUTPUT TotalBooked
OUTPUT TotalCost
```

**Total: 75 marks**
