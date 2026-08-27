# AS 9618 Paper 2 Mixed Review — Set A

> **Original practice paper:** independently written for revision. It is not an official Cambridge paper and does not reproduce past-paper questions or mark schemes.

---

## Instructions

- Recommended time: **2 hours**
- Total: **75 marks**
- Do not use a calculator.
- Answer all seven questions.
- Write programming answers in **pseudocode**.
- Show intermediate states for traces.
- Attempt the complete paper before opening the mark scheme.

### Coverage Map

| Question | Main syllabus content | Marks |
|---:|---|---:|
| 1 | Abstraction, decomposition and identifiers | 8 |
| 2 | Algorithm representation and refinement | 10 |
| 3 | Records, arrays and files | 12 |
| 4 | Stacks, queues and linked lists | 10 |
| 5 | Constructs and structured programming | 12 |
| 6 | Development, testing and maintenance | 8 |
| 7 | Integrated pseudocode scenario | 15 |
| **Total** | **Sections 9–12** | **75** |

---

## Question 1 — Computational Thinking [8]

A community tool-hire system records a member code, tool code, number of hire days and whether insurance is selected. The scenario also states the member's favourite colour and how they travelled to the centre.

1. Identify two essential details and two irrelevant details for calculating and recording a hire. **[4]**
2. Give two suitable program modules and state the purpose of each. **[2]**
3. Give an identifier, data type and purpose for:
   - number of hire days
   - insurance selected. **[2]**

---

## Question 2 — Algorithm Design [10]

A program inputs a percentage mark, rejects values outside 0–100, and outputs `"Pass"` for a mark of at least 40 or `"Fail"` otherwise.

1. Define stepwise refinement and state why it is used. **[2]**
2. Refine the high-level instruction `ProcessMark` into four ordered sub-tasks. **[4]**
3. Write pseudocode for the input, validation and output behaviour. **[4]**

---

## Question 3 — Records, Arrays and Files [12]

A weather station stores a code, location, active flag and latest real temperature for each station.

1. State suitable data types for the four fields. **[3]**
2. Define a record type and declare an array `Station[1:5]` of these records. **[4]**
3. The text file `Readings.txt` contains one observation string per line. Write pseudocode to copy every non-empty line to `ValidReadings.txt`, close both files and output the number of lines copied. The input file may be empty. **[5]**

---

## Question 4 — Abstract Data Types [10]

1. A stack contains `[A, B]` from bottom to top. Trace:
   - `PUSH C`
   - `PUSH D`
   - `POP`
   - edit the current top item from `C` to `E`
   State the final stack and the value returned by `POP`. **[4]**
2. A queue contains `[J1, J2, J3]` from front to rear. Trace:
   - `ENQUEUE J4`
   - `DEQUEUE`
   - `DEQUEUE`  
   State the final queue and both returned values. **[3]**
3. A linked list is `Start -> K -> M -> P -> NULL`. Apply these changes: insert `L` between `K` and `M`; edit the data in `P` to `Q`; delete `M`. State the resulting list and one pointer change required for the insertion and deletion. **[3]**

---

## Question 5 — Structured Programming [12]

1. State why a `REPEAT ... UNTIL` loop is suitable for input that must occur at least once and continue until valid. **[2]**
2. Write a function `IsValidScore` that receives an integer and returns whether it is from 0 to 100 inclusive. **[3]**
3. Write a procedure `AddScore` that receives a score by value and updates a total and count passed by reference. **[4]**
4. Trace the call when `Score = 12`, `Total = 30` and `Count = 2`. State the final values of all three caller variables. **[3]**

---

## Question 6 — Software Development [8]

A small retailer needs a prototype stock app quickly. Staff are available every week to review it, and requirements are expected to change.

1. Select a suitable development life cycle and justify it with two details from the scenario. **[3]**
2. Name the testing method for:
   - checking every internal branch
   - checking interfaces between two modules
   - staff checking the agreed requirements. **[3]**
3. Classify:
   - fixing an incorrect reorder calculation
   - adding support for a new barcode format. **[2]**

---

## Question 7 — Integrated Pseudocode Scenario [15]

A training centre stores 10 workshops in `Workshop[1:10]`. Each record has:

- `Code : STRING`
- `PlacesLeft : INTEGER`
- `Fee : REAL`

Write one complete pseudocode solution that:

- repeatedly inputs a requested workshop code
- stops when `"END"` is entered or five bookings have been recorded
- uses a linear search to find the workshop
- displays `"Code not found"` when absent
- displays `"Full"` when found with no places left
- for a successful booking:
  - decreases `PlacesLeft` by 1
  - increases the booking count
  - adds the workshop fee to total income
  - displays `"Booked"`
- finally outputs the booking count and total income
- outputs an average fee only when at least one booking was recorded. **[15]**

---

## Mark Scheme

### Question 1 Mark Scheme [8]

1. Essential: any two of member code, tool code, hire days, insurance choice **[2]**. Irrelevant: favourite colour and travel method **[2]**. **[4]**
2. Any two distinct modules with linked purposes, for example `GetHireDetails` inputs the required values; `CalculateCharge` calculates the cost; `SaveHire` stores the record; `DisplayConfirmation` outputs the result. **[2]**
3. Example:

   | Identifier | Data type | Purpose |
   |---|---|---|
   | `HireDays` | INTEGER | stores number of days |
   | `HasInsurance` | BOOLEAN | stores whether insurance is selected |

   One mark for each complete suitable row. **[2]**

---

### Question 2 Mark Scheme [10]

1. Stepwise refinement repeatedly replaces a high-level task with more detailed steps **[1]** until each step can be programmed **[1]**. **[2]**
2. For example: input mark; validate mark; select result; display result. One mark each in a logical order. **[4]**
3.

   ```text
   REPEAT
       INPUT Mark
   UNTIL Mark >= 0 AND Mark <= 100

   IF Mark >= 40 THEN
       OUTPUT "Pass"
   ELSE
       OUTPUT "Fail"
   ENDIF
   ```

   Repetition/input **[1]**; both validation limits **[1]**; correct selection threshold **[1]**; correct two outputs **[1]**. **[4]**

---

### Question 3 Mark Scheme [12]

1. Code: STRING; location: STRING; active flag: BOOLEAN; temperature: REAL. Award all four correct for three marks, three correct for two, two correct for one. **[3]**
2.

   ```text
   TYPE StationRecord
       DECLARE Code : STRING
       DECLARE Location : STRING
       DECLARE Active : BOOLEAN
       DECLARE LatestTemperature : REAL
   ENDTYPE

   DECLARE Station : ARRAY[1:5] OF StationRecord
   ```

   Record structure **[1]**; correct fields **[2]**; correct array declaration **[1]**. **[4]**
3.

   ```text
   DECLARE DataLine : STRING
   DECLARE Count : INTEGER

   Count <- 0
   OPENFILE "Readings.txt" FOR READ
   OPENFILE "ValidReadings.txt" FOR WRITE

   WHILE NOT EOF("Readings.txt")
       READFILE "Readings.txt", DataLine
       IF DataLine <> "" THEN
           WRITEFILE "ValidReadings.txt", DataLine
           Count <- Count + 1
       ENDIF
   ENDWHILE

   CLOSEFILE "Readings.txt"
   CLOSEFILE "ValidReadings.txt"
   OUTPUT Count
   ```

   Initialise count and open input **[1]**; open output **[1]**; EOF loop/read string **[1]**; copy/count only non-empty lines **[1]**; close both files and output count **[1]**. **[5]**

---

### Question 4 Mark Scheme [10]

1. After pushes: `[A, B, C, D]` **[1]**; `POP` returns `D` **[1]**; editing the current top changes `C` to `E` **[1]**; final stack `[A, B, E]` **[1]**. **[4]**
2. After enqueue: `[J1, J2, J3, J4]` **[1]**; dequeues return `J1` then `J2` **[1]**; final queue `[J3, J4]` **[1]**. **[3]**
3. Set `L.Next` to the node containing `M` and `K.Next` to the new `L` node for insertion **[1]**; change `P`'s data to `Q`, then set `L.Next` to the node after `M` / the node now containing `Q` for deletion **[1]**; result `Start -> K -> L -> Q -> NULL` **[1]**. **[3]**

---

### Question 5 Mark Scheme [12]

1. The body executes before the condition is tested **[1]**, so input occurs at least once and stops when the valid condition becomes true **[1]**. **[2]**
2.

   ```text
   FUNCTION IsValidScore(Score : INTEGER) RETURNS BOOLEAN
       RETURN Score >= 0 AND Score <= 100
   ENDFUNCTION
   ```

   Header/type **[1]**; both limits with `AND` **[1]**; Boolean return **[1]**. **[3]**
3.

   ```text
   PROCEDURE AddScore(
       BYVAL Score : INTEGER,
       BYREF Total : INTEGER,
       BYREF Count : INTEGER
   )
       Total <- Total + Score
       Count <- Count + 1
   ENDPROCEDURE
   ```

   Procedure/header **[1]**; parameter modes **[1]**; total update **[1]**; count update **[1]**. **[4]**
4. `Score = 12` because value passing does not change it **[1]**; `Total = 42` **[1]**; `Count = 3` **[1]**. **[3]**

---

### Question 6 Mark Scheme [8]

1. RAD or iterative **[1]**; linked to rapid prototype/short deadline **[1]** and weekly feedback/changing requirements **[1]**. **[3]**
2. White-box; integration; acceptance. **[3]**
3. Corrective; adaptive. **[2]**

---

### Question 7 Mark Scheme [15]

Example:

```text
DECLARE BookingCount : INTEGER
DECLARE TotalIncome : REAL
DECLARE RequestedCode : STRING
DECLARE Found : BOOLEAN
DECLARE Index : INTEGER

BookingCount <- 0
TotalIncome <- 0

REPEAT
    INPUT RequestedCode

    IF RequestedCode <> "END" THEN
        Found <- FALSE
        Index <- 1

        WHILE Index <= 10 AND Found = FALSE
            IF Workshop[Index].Code = RequestedCode THEN
                Found <- TRUE
            ELSE
                Index <- Index + 1
            ENDIF
        ENDWHILE

        IF Found = FALSE THEN
            OUTPUT "Code not found"
        ELSE
            IF Workshop[Index].PlacesLeft = 0 THEN
                OUTPUT "Full"
            ELSE
                Workshop[Index].PlacesLeft <-
                    Workshop[Index].PlacesLeft - 1
                BookingCount <- BookingCount + 1
                TotalIncome <- TotalIncome + Workshop[Index].Fee
                OUTPUT "Booked"
            ENDIF
        ENDIF
    ENDIF
UNTIL RequestedCode = "END" OR BookingCount = 5

OUTPUT BookingCount
OUTPUT TotalIncome

IF BookingCount > 0 THEN
    OUTPUT TotalIncome / BookingCount
ENDIF
```

| Requirement | Marks |
|---|---:|
| initialise count and income | 1 |
| repeat input and stop on `"END"` or five bookings | 2 |
| initialise bounded linear search | 2 |
| compare record code and update search state | 2 |
| distinguish not-found path | 1 |
| distinguish full path | 1 |
| decrease places only for success | 1 |
| update count and income only for success | 2 |
| display correct success message | 1 |
| output final count/income and guard average against zero | 2 |
| **Total** | **15** |

Equivalent correct pseudocode receives credit. The search must not access `Workshop[11]`.

---

## Result Review

| Score | Interpretation | Next action |
|---:|---|---|
| 60–75 | Most AS Paper 2 objectives are secure | redo lost marks under timed conditions |
| 45–59 | Core skills work but are inconsistent | revisit the two weakest chapters |
| 30–44 | Several design/programming gaps remain | redo worked examples before retesting |
| 0–29 | Foundations are not yet secure | study Chapters 9–12 in sequence |

These bands guide revision only; they are not predicted examination grades.

**Total: 75 marks**
