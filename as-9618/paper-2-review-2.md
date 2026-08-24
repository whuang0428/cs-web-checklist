# AS 9618 Paper 2 Mixed Review — Set B

> **Original practice paper:** an independent second set for timed retesting. It does not reproduce official questions or mark schemes.

## Instructions

- Recommended time: **2 hours**
- Total: **75 marks**
- Do not use a calculator.
- Answer all seven questions in pseudocode where programming is required.
- Show all trace states and attempt the paper before reading the mark scheme.

### Coverage Map

| Question | Main content | Marks |
|---:|---|---:|
| 1 | Abstraction, decomposition and identifiers | 8 |
| 2 | Algorithm representation and refinement | 10 |
| 3 | Arrays, searching and sorting | 12 |
| 4 | ADT operations and array representation | 10 |
| 5 | Structured programming and parameters | 12 |
| 6 | Development, testing and maintenance | 8 |
| 7 | Integrated pseudocode scenario | 15 |
| **Total** | **Sections 9–12** | **75** |

---

## Question 1 — Computational Thinking [8]

A campsite booking system records a pitch code, arrival date, number of nights, number of guests and whether electricity is required. The description also gives the guest's favourite sport and car colour.

1. Identify three essential details and two irrelevant details for calculating and recording the booking. **[5]**
2. Give three suitable program modules and state the purpose of each. **[3]**

---

## Question 2 — Refinement and Representation [10]

A program repeatedly inputs temperatures until `999` is entered. It outputs the number of valid temperatures from `-30.0` to `50.0` inclusive and their average.

1. Refine `ProcessTemperatures` into five ordered sub-tasks. **[5]**
2. Write structured English for the complete algorithm, including the empty-data case. **[5]**

---

## Question 3 — Search and Sort [12]

Two parallel arrays store eight product codes and matching stock levels.

1. Write pseudocode for a linear search function that receives a product code and returns its index or `-1`. **[5]**
2. Write one complete pass of an ascending bubble sort on stock level, swapping both stock and the matching product code. **[5]**
3. Explain why both arrays must be swapped together. **[2]**

---

## Question 4 — Abstract Data Types [10]

An array-based circular queue uses indexes `0:5`. Initially:

```text
Queue = ["", "", "B", "C", "D", "E"]
Front = 2
Rear = 5
Count = 4
```

1. Trace these operations in order: `Dequeue`, `Enqueue("F")`, `Enqueue("G")`, `Dequeue`. After each operation, record any returned value and the values of `Front`, `Rear` and `Count`. **[6]**
2. Explain how the circular implementation reuses released array positions and how `Count` distinguishes a full queue from an empty queue. **[4]**

---

## Question 5 — Structured Programming [12]

1. Write a function `ValidMark(Mark : INTEGER) RETURNS BOOLEAN` for marks from 0 to 100 inclusive. **[3]**
2. Write a procedure `UpdateStatistics` with:
   - mark passed by value
   - total and count passed by reference
   - highest mark passed by reference. **[5]**
3. Trace the call for `Mark = 72`, `Total = 130`, `Count = 2`, `Highest = 68`. State the final caller values and explain which variable is unchanged. **[4]**

---

## Question 6 — Software Development [8]

A hospital requires a medication system with stable, formally approved requirements and extensive safety evidence.

1. Select a development life cycle and justify it using two scenario details. **[3]**
2. Name the most suitable testing method for checking:
   - each internal decision path
   - communication between prescription and stock modules
   - whether the final system meets the hospital's agreed requirements. **[3]**
3. Classify fixing a dosage-calculation fault and changing the program for a new operating system. **[2]**

---

## Question 7 — Integrated Pseudocode Scenario [15]

An equipment centre stores 20 records in `Equipment[1:20]`:

- `Code : STRING`
- `Available : INTEGER`
- `DailyRate : REAL`

The supplied function `INTEGER_TO_STRING(Value : INTEGER) RETURNS STRING` converts an integer to its decimal string representation.

Write a complete pseudocode program that:

- repeatedly inputs an equipment code
- stops for `"END"` or after six successful hire days have been recorded
- searches for the code using linear search
- displays `"Unknown"` when absent
- when found, inputs and validates requested days from 1 to 4
- rejects the request when the requested days would make the overall successful-day total exceed six
- displays `"Unavailable"` when `Available` is zero
- displays `"Hire-day limit exceeded"` when accepting the request would take the overall successful-day total above six
- otherwise decreases `Available`, adds requested days to the successful-day total and adds `days * daily rate` to total income
- writes each successful hire as one line containing code and days to `Hires.txt`
- closes the file and outputs hire count, successful-day total and total income. **[15]**

---

## Mark Scheme

### Question 1 Mark Scheme [8]

1. Any three of pitch code, arrival date, nights, guests, electricity choice **[3]**; favourite sport and car colour **[2]**. **[5]**
2. Three distinct modules with purposes, for example input/validate booking, calculate charge, save booking, display confirmation. **[3]**

### Question 2 Mark Scheme [10]

1. Input first temperature; initialise total/count; repeat until sentinel; validate and accumulate; calculate/output average or no-data result. One mark each in a valid order. **[5]**
2. Award one mark each for: initialise total/count; input inside repetition; sentinel excluded; range check before accumulation; conditional average avoiding division by zero. **[5]**

Indicative structured English:

```text
SET total and count to zero
INPUT a temperature
WHILE the temperature is not 999
    IF it is from -30.0 to 50.0 inclusive
        ADD it to total
        INCREASE count
    ENDIF
    INPUT the next temperature
ENDWHILE
OUTPUT count
IF count is greater than zero
    OUTPUT total divided by count
ELSE
    OUTPUT "No valid data"
ENDIF
```

### Question 3 Mark Scheme [12]

1.

```text
FUNCTION FindProduct(Target : STRING) RETURNS INTEGER
    FOR Index <- 1 TO 8
        IF ProductCode[Index] = Target THEN
            RETURN Index
        ENDIF
    NEXT Index
    RETURN -1
ENDFUNCTION
```

Function/header **[1]**; loop **[1]**; comparison **[1]**; found return **[1]**; not-found return **[1]**. **[5]**

2.

```text
FOR Index <- 1 TO 7
    IF Stock[Index] > Stock[Index + 1] THEN
        TempStock <- Stock[Index]
        Stock[Index] <- Stock[Index + 1]
        Stock[Index + 1] <- TempStock

        TempCode <- ProductCode[Index]
        ProductCode[Index] <- ProductCode[Index + 1]
        ProductCode[Index + 1] <- TempCode
    ENDIF
NEXT Index
```

Correct bounds/comparison **[2]**; stock swap **[1]**; code swap **[2]**. **[5]**
3. Each stock level must remain associated with its original product code **[1]**; otherwise records become corrupted/incorrectly matched **[1]**. **[2]**

### Question 4 Mark Scheme [10]

1.

| Operation | Returned value | Front | Rear | Count |
| --- | --- | ---:| ---:| ---:|
| `Dequeue` | `"B"` | 3 | 5 | 3 |
| `Enqueue("F")` | — | 3 | 0 | 4 |
| `Enqueue("G")` | — | 3 | 1 | 5 |
| `Dequeue` | `"C"` | 4 | 1 | 4 |

First dequeue value and state **[2]**; state after enqueueing `F` **[1]**; state after enqueueing `G` **[1]**; final dequeue value and state **[2]**. **[6]**

2. Advancing `Rear` beyond index `5` wraps it to index `0`, so released positions at the start of the array can be reused **[1]**; `Front` wraps in the same way when it passes the upper bound **[1]**; `Count = 0` means empty **[1]**; `Count = 6` means full **[1]**. **[4]**

### Question 5 Mark Scheme [12]

1.

```text
FUNCTION ValidMark(Mark : INTEGER) RETURNS BOOLEAN
    RETURN Mark >= 0 AND Mark <= 100
ENDFUNCTION
```

Header/type **[1]**; both limits **[1]**; Boolean return **[1]**. **[3]**

2.

```text
PROCEDURE UpdateStatistics(
    BYVAL Mark : INTEGER,
    BYREF Total : INTEGER,
    BYREF Count : INTEGER,
    BYREF Highest : INTEGER
)
    Total <- Total + Mark
    Count <- Count + 1
    IF Mark > Highest THEN
        Highest <- Mark
    ENDIF
ENDPROCEDURE
```

Correct modes/types **[2]**; total **[1]**; count **[1]**; highest update **[1]**. **[5]**
3. `Total = 202` **[1]**; `Count = 3` **[1]**; `Highest = 72` **[1]**; caller's `Mark` remains 72 because it is passed by value/not assigned **[1]**. **[4]**

### Question 6 Mark Scheme [8]

1. Waterfall **[1]**; stable/formally approved requirements **[1]**; documentation, traceability or safety evidence **[1]**. **[3]**
2. White-box; integration; acceptance. **[3]**
3. Dosage fault: corrective **[1]**; new OS: adaptive **[1]**. **[2]**

### Question 7 Mark Scheme [15]

- initialise counters/totals and open output file **[2]**
- repetition with both stop conditions **[2]**
- complete linear search including not-found state **[3]**
- validates requested days **[1]**
- enforces overall six-day limit **[1]**
- tests availability and produces correct messages **[1]**
- updates availability, hire count and days **[2]**
- calculates income **[1]**
- writes successful code/days using the supplied conversion function, closes file and outputs totals **[2]**

Indicative solution:

```text
HireCount <- 0
TotalDays <- 0
TotalIncome <- 0
Code <- ""
OPENFILE "Hires.txt" FOR WRITE

WHILE Code <> "END" AND TotalDays < 6
    INPUT Code
    IF Code <> "END" THEN
        Found <- FALSE
        Index <- 1
        WHILE Index <= 20 AND Found = FALSE
            IF Equipment[Index].Code = Code THEN
                Found <- TRUE
            ELSE
                Index <- Index + 1
            ENDIF
        ENDWHILE

        IF Found = FALSE THEN
            OUTPUT "Unknown"
        ELSE
            REPEAT
                INPUT Days
            UNTIL Days >= 1 AND Days <= 4

            IF TotalDays + Days > 6 THEN
                OUTPUT "Hire-day limit exceeded"
            ELSE
                IF Equipment[Index].Available = 0 THEN
                    OUTPUT "Unavailable"
                ELSE
                    Equipment[Index].Available <- Equipment[Index].Available - 1
                    HireCount <- HireCount + 1
                    TotalDays <- TotalDays + Days
                    TotalIncome <- TotalIncome + Days * Equipment[Index].DailyRate
                    WRITEFILE "Hires.txt", Code & "," & INTEGER_TO_STRING(Days)
                ENDIF
            ENDIF
        ENDIF
    ENDIF
ENDWHILE

CLOSEFILE "Hires.txt"
OUTPUT HireCount, TotalDays, TotalIncome
```

**Total: 75 marks**
