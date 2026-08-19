# IGCSE 0478 Paper 2 Mixed Review — Set A

> **Original practice paper:** this is an independently written revision resource, not an official Cambridge paper and not copied from a past paper.

---

## Instructions

- Recommended time: **1 hour 45 minutes**
- Total: **75 marks**
- Do not use a calculator.
- Answer all seven questions.
- Spend about **30 minutes** on Question 7.
- Use clear pseudocode unless a question asks for another representation.
- For Question 7, use pseudocode or Python. Do not mix the two syntaxes in one solution.
- Attempt the complete paper before opening the mark scheme.

### Coverage Map

| Question | Main topic | Marks |
|---:|---|---:|
| 1 | Algorithm design, validation and testing | 10 |
| 2 | Trace tables and standard methods | 10 |
| 3 | Programming and two-dimensional arrays | 12 |
| 4 | Databases and SQL | 10 |
| 5 | Boolean logic | 10 |
| 6 | File handling and maintainability | 8 |
| 7 | Integrated programming scenario | 15 |
| **Total** | **Topics 7–10** | **75** |

---

## Question 1 — Problem Analysis and Testing [10]

A parcel locker accepts parcels with a mass from 0.10 kg to 20.00 kg inclusive. The user enters a locker code and parcel mass. The system calculates a charge and displays a collection receipt.

1. State one input and one output. **[2]**
2. Give two suitable subsystems for this solution. **[2]**
3. State a suitable validation check for:
   - the parcel mass
   - the locker code, which must contain exactly six characters. **[2]**
4. Give four mass test values:
   - one normal value
   - the lower extreme value
   - one value immediately below the lower boundary
   - one value immediately above the upper boundary.  
   Label each value with its test type. **[4]**

---

## Question 2 — Trace Table [10]

The array contains:

```text
Values = [4, 7, 2, 9, 6, 3]
```

The algorithm is:

```text
Total <- 0
Count <- 0
Maximum <- Values[1]

FOR Index <- 1 TO 6
    IF Values[Index] MOD 2 = 0 THEN
        Total <- Total + Values[Index]
        Count <- Count + 1
    ENDIF

    IF Values[Index] > Maximum THEN
        Maximum <- Values[Index]
    ENDIF
NEXT Index

OUTPUT Total
OUTPUT Count
OUTPUT Maximum
```

1. Complete the trace table. **[6]**

   | Index | Values[Index] | Total | Count | Maximum |
   |---:|---:|---:|---:|---:|
   | 1 | 4 | | | |
   | 2 | 7 | | | |
   | 3 | 2 | | | |
   | 4 | 9 | | | |
   | 5 | 6 | | | |
   | 6 | 3 | | | |

2. State the three values output. **[3]**
3. State the purpose of `Count`. **[1]**

---

## Question 3 — Programming with Arrays [12]

`Visitors[1:3, 1:5]` stores the number of visitors to three exhibitions on five days. Every value must be an integer from 0 to 200 inclusive.

1. Write pseudocode to input and validate all 15 values. **[4]**
2. Write a function `ExhibitionTotal` that receives an exhibition number and returns its five-day total. **[4]**
3. Write pseudocode that uses the function to output the number of the exhibition with the highest total. If totals are equal, keep the first exhibition. **[4]**

---

## Question 4 — Database and SQL [10]

The table `Visits` stores:

| VisitID | VisitorName | Age | Member | Cost | VisitDate |
|---|---|---:|---|---:|---|
| V101 | Lin | 17 | TRUE | 4.50 | 03/06/2026 |
| V102 | Omar | 22 | FALSE | 8.00 | 04/06/2026 |
| V103 | Mei | 16 | FALSE | 6.00 | 04/06/2026 |
| V104 | Sara | 31 | TRUE | 5.50 | 05/06/2026 |
| V105 | Theo | 19 | FALSE | 4.00 | 05/06/2026 |

1. Identify the primary key and give one reason for your choice. **[2]**
2. State the data type of `Age` and `Member`. **[2]**
3. Write a query to display `VisitorName` and `Cost` for non-members younger than 20, ordered from highest to lowest cost. **[4]**
4. Write a query to output the number of members. **[2]**

---

## Question 5 — Boolean Logic [10]

The output is:

```text
Q = (A XOR B) AND (NOT C)
```

1. State the three gates required and describe how they are connected. **[3]**
2. Complete the final output column. **[4]**

   | A | B | C | A XOR B | NOT C | Q |
   |---:|---:|---:|---:|---:|---:|
   | 0 | 0 | 0 | | | |
   | 0 | 0 | 1 | | | |
   | 0 | 1 | 0 | | | |
   | 0 | 1 | 1 | | | |
   | 1 | 0 | 0 | | | |
   | 1 | 0 | 1 | | | |
   | 1 | 1 | 0 | | | |
   | 1 | 1 | 1 | | | |

3. A selector should activate when exactly one of buttons A and B is pressed and safety switch C is off. Explain how the expression represents this requirement. **[3]**

---

## Question 6 — File Handling [8]

The file `readings.txt` contains one valid real temperature on each line. The number of lines is not known.

1. Write pseudocode to:
   - open the file
   - read every temperature
   - calculate the total and count
   - close the file
   - output the average if at least one value was read. **[6]**
2. Explain why a `WHILE NOT EOF` loop is suitable. **[1]**
3. State one way to make this program easier to maintain. **[1]**

---

## Question 7 — Integrated Programming Scenario [15]

A small library stores 20 book codes in `BookCode[1:20]`. The matching Boolean value in `Available[1:20]` is `TRUE` when that book can be borrowed.

Write one complete solution that:

- inputs a member code and rejects an empty value
- repeatedly inputs a requested book code
- stops when `"END"` is entered or three books have been borrowed
- uses a linear search to find each requested code
- if the code is found and the book is available:
  - changes its availability to `FALSE`
  - increases the number borrowed
  - displays `"Loan recorded"`
- displays `"Not available"` when the code exists but is already unavailable
- displays `"Code not found"` when the code is absent
- outputs the final number of books borrowed

Use pseudocode or Python. **[15]**

---

## Mark Scheme

### Question 1 Mark Scheme [10]

1. Input: locker code or parcel mass **[1]**; output: calculated charge or collection receipt information **[1]**. **[2]**
2. Any two appropriate decomposed parts, for example input parcel details, validate data, calculate charge, allocate/store locker data, display receipt. **[2]**
3. Mass: range check from 0.10 to 20.00 inclusive **[1]**; locker code: length check of six characters **[1]**. **[2]**
4. Example values:
   - normal: `5.00` kg
   - lower extreme: `0.10` kg
   - lower-boundary abnormal: a representable value below 0.10, such as `0.09` kg
   - upper-boundary abnormal: a representable value above 20.00, such as `20.01` kg  
   Award one mark for each suitable, correctly labelled value. **[4]**

---

### Question 2 Mark Scheme [10]

1.

   | Index | Values[Index] | Total | Count | Maximum |
   |---:|---:|---:|---:|---:|
   | 1 | 4 | 4 | 1 | 4 |
   | 2 | 7 | 4 | 1 | 7 |
   | 3 | 2 | 6 | 2 | 7 |
   | 4 | 9 | 6 | 2 | 9 |
   | 5 | 6 | 12 | 3 | 9 |
   | 6 | 3 | 12 | 3 | 9 |

   One mark for each completely correct row. **[6]**
2. `12`, `3`, `9`, in that order. **[3]**
3. It counts how many values are even. **[1]**

---

### Question 3 Mark Scheme [12]

1. Example:

   ```text
   FOR Exhibition <- 1 TO 3
       FOR Day <- 1 TO 5
           REPEAT
               INPUT Visitors[Exhibition, Day]
           UNTIL Visitors[Exhibition, Day] >= 0
                 AND Visitors[Exhibition, Day] <= 200
       NEXT Day
   NEXT Exhibition
   ```

   Award for correct outer loop **[1]**, inner loop and indexed input **[1]**, lower limit **[1]**, upper limit and correct repetition **[1]**. **[4]**

2. Example:

   ```text
   FUNCTION ExhibitionTotal(ExhibitionNumber : INTEGER) RETURNS INTEGER
       Total <- 0
       FOR Day <- 1 TO 5
           Total <- Total + Visitors[ExhibitionNumber, Day]
       NEXT Day
       RETURN Total
   ENDFUNCTION
   ```

   Function header and parameter **[1]**, initialise total **[1]**, traverse and total correct row **[1]**, return total **[1]**. **[4]**

3. Example:

   ```text
   HighestExhibition <- 1
   HighestTotal <- ExhibitionTotal(1)

   FOR Exhibition <- 2 TO 3
       CurrentTotal <- ExhibitionTotal(Exhibition)
       IF CurrentTotal > HighestTotal THEN
           HighestTotal <- CurrentTotal
           HighestExhibition <- Exhibition
       ENDIF
   NEXT Exhibition

   OUTPUT HighestExhibition
   ```

   Initialise from exhibition 1 **[1]**, loop remaining exhibitions and call function **[1]**, update both values only for a strictly greater total **[1]**, output exhibition number **[1]**. **[4]**

---

### Question 4 Mark Scheme [10]

1. `VisitID` **[1]** because it uniquely identifies each visit/record **[1]**. **[2]**
2. `Age`: integer **[1]**; `Member`: Boolean **[1]**. **[2]**
3.

   ```sql
   SELECT VisitorName, Cost
   FROM Visits
   WHERE Member = FALSE AND Age < 20
   ORDER BY Cost DESC;
   ```

   Correct selected fields **[1]**, table **[1]**, both conditions joined by `AND` **[1]**, descending cost order **[1]**. **[4]**

   The result would be Mei at 6.00 followed by Theo at 4.00.

4.

   ```sql
   SELECT COUNT(VisitID)
   FROM Visits
   WHERE Member = TRUE;
   ```

   Correct count and table **[1]**, correct condition **[1]**. **[2]**

---

### Question 5 Mark Scheme [10]

1. Connect `A` and `B` to an `XOR` gate **[1]**; connect `C` to a `NOT` gate **[1]**; connect both intermediate outputs to an `AND` gate **[1]**. **[3]**
2.

   | A | B | C | A XOR B | NOT C | Q |
   |---:|---:|---:|---:|---:|---:|
   | 0 | 0 | 0 | 0 | 1 | 0 |
   | 0 | 0 | 1 | 0 | 0 | 0 |
   | 0 | 1 | 0 | 1 | 1 | 1 |
   | 0 | 1 | 1 | 1 | 0 | 0 |
   | 1 | 0 | 0 | 1 | 1 | 1 |
   | 1 | 0 | 1 | 1 | 0 | 0 |
   | 1 | 1 | 0 | 0 | 1 | 0 |
   | 1 | 1 | 1 | 0 | 0 | 0 |

   Award one mark for each pair of correct final `Q` values. **[4]**
3. `A XOR B` is 1 only when exactly one button is pressed **[1]**; `NOT C` is 1 only when safety switch C is off **[1]**; the final `AND` requires both conditions **[1]**. **[3]**

---

### Question 6 Mark Scheme [8]

1. Example:

   ```text
   Total <- 0
   Count <- 0

   OPENFILE "readings.txt" FOR READ

   WHILE NOT EOF("readings.txt") DO
       READFILE "readings.txt", Temperature
       Total <- Total + Temperature
       Count <- Count + 1
   ENDWHILE

   CLOSEFILE "readings.txt"

   IF Count > 0 THEN
       Average <- Total / Count
       OUTPUT Average
   ENDIF
   ```

   Initialise total and count **[1]**; open correct file for reading **[1]**; loop to end of file **[1]**; read each value **[1]**; total and count correctly **[1]**; close file and safely output average **[1]**. **[6]**
2. The number of records is unknown, and the loop stops when no unread line remains. **[1]**
3. Any one: meaningful identifiers, useful comments, consistent indentation, a function for average, or a procedure for file processing. **[1]**

---

### Question 7 Mark Scheme [15]

Example pseudocode:

```text
CONSTANT MaxLoans <- 3
Borrowed <- 0

REPEAT
    INPUT MemberCode
UNTIL LENGTH(MemberCode) > 0

REPEAT
    INPUT RequestedCode

    IF RequestedCode <> "END" THEN
        Found <- FALSE
        Index <- 1

        WHILE Index <= 20 AND Found = FALSE DO
            IF BookCode[Index] = RequestedCode THEN
                Found <- TRUE
            ELSE
                Index <- Index + 1
            ENDIF
        ENDWHILE

        IF Found = TRUE THEN
            IF Available[Index] = TRUE THEN
                Available[Index] <- FALSE
                Borrowed <- Borrowed + 1
                OUTPUT "Loan recorded"
            ELSE
                OUTPUT "Not available"
            ENDIF
        ELSE
            OUTPUT "Code not found"
        ENDIF
    ENDIF
UNTIL RequestedCode = "END" OR Borrowed = MaxLoans

OUTPUT Borrowed
```

Award marks for:

| Requirement | Marks |
|---|---:|
| initialise borrowed count and use a three-loan limit | 1 |
| reject an empty member code | 1 |
| repeat requests and stop on `"END"` or three successful loans | 2 |
| initialise and perform a bounded linear search | 3 |
| distinguish found and available states correctly | 2 |
| set availability false and increase count only on a valid loan | 2 |
| produce the two distinct failure messages | 2 |
| output final count and maintain coherent control structure | 2 |
| **Total** | **15** |

Equivalent correct solutions in an allowed language receive credit. Exact syntax may vary, but the logic and array matching must be correct.

---

## Result Review

| Score | Interpretation | Next action |
|---:|---|---|
| 60–75 | Secure across most Paper 2 objectives | redo only lost-mark sections under time |
| 45–59 | Functional but inconsistent | revisit the two weakest chapters, then retry |
| 30–44 | Important gaps remain | redo worked examples before another full paper |
| 0–29 | Foundations are not yet secure | study Chapters 7–10 in order before retesting |

Do not treat the band as a predicted examination grade. Use it only to choose the next revision action.

**Total: 75 marks**
