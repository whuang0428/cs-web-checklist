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

The following string functions are supplied for this question: `LENGTH(Text : STRING) RETURNS INTEGER`; `CHAR_AT(Text : STRING, Position : INTEGER) RETURNS CHAR` returns the character at a one-based position; `TO_UPPER(Text : STRING) RETURNS STRING` returns the whole string in uppercase, leaving non-letters unchanged. The latter two are functions supplied by this question, not additional standard Cambridge pseudocode keywords.

1. Write `ValidCode(Code : STRING) RETURNS BOOLEAN`. A code has exactly six characters: the first two must be uppercase letters A–Z and the remaining four must be digits 0–9. Reject every other character. **[5]**
2. Write `NormaliseCode(BYREF Code : STRING, BYREF Valid : BOOLEAN)`. Convert the whole string to uppercase, then call `ValidCode` and store its Boolean result in `Valid`. **[3]**
3. Trace the call with `Code="ab0123"` and `Valid=FALSE`. State the two final caller values, explain why they change, and give one test that violates only the digit rule. **[4]**

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

A sensor log `Events.txt` contains one line per reading. Each valid line has exactly eight characters: a two-digit sensor ID, a colon, a three-digit non-negative reading, a colon and status `V` or `E`. For example `03:127:V`. Sensor IDs must be 01–12. Other lines are malformed. Status `E` records are well-formed but must not contribute to averages.

The supplied functions `STRING_TO_INTEGER(Text : STRING) RETURNS INTEGER`, `INTEGER_TO_STRING(Value : INTEGER) RETURNS STRING` and `REAL_TO_STRING(Value : REAL) RETURNS STRING` convert valid numeric text/values. Do not attempt numeric conversion before validating the characters. Also use the supplied `CHAR_AT` function from Question 5, `LENGTH(Text : STRING) RETURNS INTEGER` and `MID(Text : STRING, Start : INTEGER, Count : INTEGER) RETURNS STRING`, with one-based positions.

Write a complete program that:

- reads to end of file, including an empty file
- validates each line's length, separators, status and digit positions before conversion
- rejects IDs outside 01–12 and counts malformed lines
- accumulates a total and count for each sensor's valid `V` readings
- counts well-formed `E` records separately
- writes exactly twelve lines to `Summary.txt` in sensor-ID order, each containing ID and mean, or ID and `No valid readings`
- closes both files and outputs malformed-line count and `E`-record count. **[15]**

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

1. Typed header and Boolean result **[1]**; exact length check before indexing **[1]**; checks both letter positions **[1]**; checks all four digit positions **[1]**; rejects invalid characters and accepts only a complete match **[1]**. **[5]**

```text
FUNCTION ValidCode(Code : STRING) RETURNS BOOLEAN
    DECLARE Position : INTEGER
    DECLARE Symbol : CHAR
    IF LENGTH(Code) <> 6 THEN
        RETURN FALSE
    ENDIF
    FOR Position <- 1 TO 2
        Symbol <- CHAR_AT(Code, Position)
        IF Symbol < 'A' OR Symbol > 'Z' THEN
            RETURN FALSE
        ENDIF
    NEXT Position
    FOR Position <- 3 TO 6
        Symbol <- CHAR_AT(Code, Position)
        IF Symbol < '0' OR Symbol > '9' THEN
            RETURN FALSE
        ENDIF
    NEXT Position
    RETURN TRUE
ENDFUNCTION
```

2. Correct reference modes/types **[1]**; conversion of the string **[1]**; calls the function and assigns its result **[1]**. **[3]**

```text
PROCEDURE NormaliseCode(BYREF Code : STRING, BYREF Valid : BOOLEAN)
    Code <- TO_UPPER(Code)
    Valid <- ValidCode(Code)
ENDPROCEDURE
```

3. `Code="AB0123"` **[1]**, `Valid=TRUE` **[1]**. Both parameters refer to caller variables, so the procedure's assignments update them **[1]**. For example `"AB01X3"` has the correct length and uppercase prefix, but a non-digit in the suffix, so it is rejected **[1]**. **[4]**

### Question 6 Mark Scheme [8]

1. Waterfall **[1]**; stable/formally approved requirements **[1]**; documentation, traceability or safety evidence **[1]**. **[3]**
2. White-box; integration; acceptance. **[3]**
3. Dosage fault: corrective **[1]**; new OS: adaptive **[1]**. **[2]**

### Question 7 Mark Scheme [15]

- Initialises twelve sensor totals/counts and both diagnostic counters **[2]**.
- Opens/reads/closes the input using an EOF loop **[2]**.
- Validates length before indexing, both separators and status **[2]**.
- Validates all digit positions before conversion and validates ID range **[2]**.
- Counts malformed and well-formed E records separately **[2]**.
- Accumulates only V readings into the correct sensor's total/count **[2]**.
- Writes all twelve IDs in order, calculates means with an empty-count guard **[2]**.
- Closes output and outputs both diagnostic counts **[1]**.

```text
DECLARE Totals : ARRAY[1:12] OF INTEGER
DECLARE Counts : ARRAY[1:12] OF INTEGER
DECLARE Sensor, Reading, Position, Malformed, ErrorRecords : INTEGER
DECLARE Line, Result : STRING
DECLARE Valid : BOOLEAN

FOR Sensor <- 1 TO 12
    Totals[Sensor] <- 0
    Counts[Sensor] <- 0
NEXT Sensor
Malformed <- 0
ErrorRecords <- 0
OPENFILE "Events.txt" FOR READ
WHILE NOT EOF("Events.txt")
    READFILE "Events.txt", Line
    Valid <- FALSE
    IF LENGTH(Line) = 8 THEN
        Valid <- CHAR_AT(Line, 3) = ':' AND CHAR_AT(Line, 7) = ':'
                 AND (CHAR_AT(Line, 8) = 'V' OR CHAR_AT(Line, 8) = 'E')
        FOR Position <- 1 TO 6
            IF Position <> 3 THEN
                IF CHAR_AT(Line, Position) < '0' OR CHAR_AT(Line, Position) > '9' THEN
                    Valid <- FALSE
                ENDIF
            ENDIF
        NEXT Position
        IF Valid = TRUE THEN
            Sensor <- STRING_TO_INTEGER(MID(Line, 1, 2))
            IF Sensor < 1 OR Sensor > 12 THEN
                Valid <- FALSE
            ENDIF
        ENDIF
    ENDIF
    IF Valid = FALSE THEN
        Malformed <- Malformed + 1
    ELSE
        IF CHAR_AT(Line, 8) = 'E' THEN
            ErrorRecords <- ErrorRecords + 1
        ELSE
            Reading <- STRING_TO_INTEGER(MID(Line, 4, 3))
            Totals[Sensor] <- Totals[Sensor] + Reading
            Counts[Sensor] <- Counts[Sensor] + 1
        ENDIF
    ENDIF
ENDWHILE
CLOSEFILE "Events.txt"

OPENFILE "Summary.txt" FOR WRITE
FOR Sensor <- 1 TO 12
    IF Counts[Sensor] = 0 THEN
        Result <- "No valid readings"
    ELSE
        Result <- REAL_TO_STRING(Totals[Sensor] / Counts[Sensor])
    ENDIF
    WRITEFILE "Summary.txt", INTEGER_TO_STRING(Sensor) & "," & Result
NEXT Sensor
CLOSEFILE "Summary.txt"
OUTPUT Malformed, ErrorRecords
```

Check `03:127:V`, `03:129:V`, `03:999:E`, `13:100:V` and an empty line: sensor 3 mean = 128, malformed = 2, E records = 1; the other eleven sensors have no valid readings. For an empty input, both diagnostic counts are zero and all twelve summaries say `No valid readings`.

**Total: 75 marks**
