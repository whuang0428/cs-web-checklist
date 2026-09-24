# IGCSE 0478 Paper 2 Mixed Review — Set B

> **Original practice paper:** an independent second set for timed retesting. It does not reproduce official questions or mark schemes.

## Instructions

- Recommended time: **1 hour 45 minutes**
- Total: **75 marks**
- Do not use a calculator.
- Answer all seven questions.
- Use pseudocode for coding answers; Question 7 may instead be answered in Python, Visual Basic or Java. Use one language consistently.
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

WHILE Upper > 1 AND Swapped = TRUE DO
    Swapped <- FALSE
    FOR Index <- 1 TO Upper - 1
        IF Scores[Index] > Scores[Index + 1]
        THEN
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

`Seats[1:4, 1:6]` stores four rows of six seats: 0 means free and 1 means occupied. The array is already populated.

1. Write `FindPair(RowNumber : INTEGER) RETURNS INTEGER`. Return the column number of the first pair of adjacent free seats in that row, or −1 if no pair exists. **[4]**
2. Write pseudocode that inputs and validates a row number, calls `FindPair`, reserves both seats if possible, and outputs their column numbers or `"No pair"`. **[6]**
3. Give a six-seat row that tests a pair at the final possible position, and state the expected function result. **[2]**

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
W = (A NAND B) AND (C OR NOT A)
```

1. Name the four gate operations used. **[2]**
2. Calculate `W` for each input set. **[4]**

   | A | B | C | W |
   |---:|---:|---:|---:|
   | 0 | 0 | 0 | |
   | 1 | 1 | 0 | |
   | 1 | 0 | 0 | |
   | 1 | 0 | 1 | |

3. Describe how to construct the circuit, including the intermediate connections. **[4]**

---

## Question 6 — Strings and Files [10]

The file `Codes.txt` contains one code per line. A valid code has exactly eight characters and begins with `"X"`.

1. Write pseudocode to open the file, read every line, count valid codes, close the file and output the count. **[6]**
2. State the two string operations needed to test length and first character. **[2]**
3. Give two ways the solution is made maintainable. **[2]**

---

## Question 7 — Integrated Programming Scenario [15]

Six competitors each make three long-jump attempts. Store non-empty names in `Names[1:6]` and real distances in `Attempts[1:6, 1:3]`. A distance from 0.0 to 10.0 inclusive is valid; −1 records a foul. Reject and re-input every other value.

Write a complete solution that:

- inputs and validates all six names and eighteen distances
- finds each competitor's greatest valid distance
- outputs each name with that distance, or `"No valid attempt"` if all three attempts are fouls
- finds the overall winner, retaining the first competitor on a tie
- outputs the winner's name and distance, or `"No winner"` if all attempts are fouls
- calculates and outputs the mean of all valid attempts, excluding fouls and avoiding division by zero.

Use pseudocode, Python, Visual Basic or Java. **[15]**

---

<span id="mark-scheme" class="legacy-anchor" aria-hidden="true"></span>

## Indicative Marking Points

<span id="question-1-mark-scheme-8" class="legacy-anchor" aria-hidden="true"></span>

### Question 1 Indicative Marking Points [8]

1. Any two of bicycle code, hire duration, helmet choice **[2]**; calculated charge or confirmation details **[1]**. **[3]**
2. Any two distinct modules plus linked purpose, for example `GetHireDetails`, `ValidateHire`, `CalculateCharge`, `DisplayConfirmation`. **[2]**
3. Normal such as `4` **[1]**; lower extreme `1` **[1]**; abnormal boundary `0` or `9` **[1]**. **[3]**

<span id="question-2-mark-scheme-10" class="legacy-anchor" aria-hidden="true"></span>

### Question 2 Indicative Marking Points [10]

1. `[27, 35, 18, 41, 50]`; one mark for each correctly positioned value except the unchanged final value. **[4]**
2. `[27, 18, 35, 41, 50]`; one mark for each of the first three positions. **[3]**
3. `[18, 27, 35, 41, 50]`. **[2]**
4. It records whether a swap occurred so the algorithm can stop early when a complete pass makes no swaps. **[1]**

<span id="question-3-mark-scheme-12" class="legacy-anchor" aria-hidden="true"></span>

### Question 3 Indicative Marking Points [12]

1. Correct function and row parameter **[1]**; checks columns 1–5 without exceeding bounds **[1]**; tests both seats and returns the first match **[1]**; returns −1 if none **[1]**. **[4]**

```text
FUNCTION FindPair(RowNumber : INTEGER) RETURNS INTEGER
    FOR Column <- 1 TO 5
        IF Seats[RowNumber, Column] = 0 AND Seats[RowNumber, Column + 1] = 0
        THEN
            RETURN Column
        ENDIF
    NEXT Column
    RETURN -1
ENDFUNCTION
```

2. Repeated input **[1]**; both row limits **[1]**; calls function with selected row **[1]**; handles −1 without indexing it **[1]**; updates both seats **[1]**; correct seat output **[1]**. **[6]**

```text
REPEAT
    INPUT RowNumber
UNTIL RowNumber >= 1 AND RowNumber <= 4
Column <- FindPair(RowNumber)
IF Column = -1
THEN
    OUTPUT "No pair"
ELSE
    Seats[RowNumber, Column] <- 1
    Seats[RowNumber, Column + 1] <- 1
    OUTPUT Column, Column + 1
ENDIF
```

3. For example `[1, 0, 1, 1, 0, 0]` **[1]**; return 5 **[1]**. **[2]**

<span id="question-4-mark-scheme-10" class="legacy-anchor" aria-hidden="true"></span>

### Question 4 Indicative Marking Points [10]

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

### Question 5 Indicative Marking Points [10]

1. NAND, AND, OR and NOT; all four for two marks, two or three for one. **[2]**
2.

   | A | B | C | W |
   |---:|---:|---:|---:|
   | 0 | 0 | 0 | 1 |
   | 1 | 1 | 0 | 0 |
   | 1 | 0 | 0 | 0 |
   | 1 | 0 | 1 | 1 |

   One mark per row. **[4]**
3. Connect A and B to NAND **[1]**; branch A to NOT **[1]**; connect C and `NOT A` to OR **[1]**; connect NAND output and OR output to final AND **[1]**. **[4]**

### Question 6 Indicative Marking Points [10]

1.

```text
DECLARE Code : STRING
DECLARE ValidCount : INTEGER

ValidCount <- 0
OPENFILE "Codes.txt" FOR READ
WHILE NOT EOF("Codes.txt") DO
    READFILE "Codes.txt", Code
    IF LENGTH(Code) = 8 AND SUBSTRING(Code, 1, 1) = "X"
    THEN
        ValidCount <- ValidCount + 1
    ENDIF
ENDWHILE
CLOSEFILE "Codes.txt"
OUTPUT ValidCount
```

Initialise/open **[1]**; EOF loop/read **[1]**; length test **[1]**; first-character test **[1]**; count **[1]**; close/output **[1]**. **[6]**
2. `LENGTH` **[1]** and `SUBSTRING` **[1]**. **[2]**
3. Any two: meaningful identifiers, indentation, comments, named function/procedure, constant for required length, avoiding repeated logic. **[2]**

<span id="question-7-mark-scheme-15" class="legacy-anchor" aria-hidden="true"></span>

### Question 7 Indicative Marking Points [15]

Apply the [IGCSE scenario levels](../exam-technique.md#igcse-15-mark-scenario-assessment): AO2 /9 and AO3 /6. Judge the whole solution, using the following evidence of completeness: correct array storage and nested loops; non-empty names and permitted distances; fouls excluded; per-competitor maximum; first winner retained on ties; all-foul handling; total/count and guarded mean. Treat these as evidence for the level judgement, not as separate automatic points.

```text
DECLARE Names : ARRAY[1:6] OF STRING
DECLARE Attempts : ARRAY[1:6, 1:3] OF REAL
DECLARE Competitor, Attempt, Winner, ValidCount : INTEGER
DECLARE Best, WinningDistance, Total : REAL

Winner <- 0
WinningDistance <- -1
Total <- 0
ValidCount <- 0
FOR Competitor <- 1 TO 6
    // Store each competitor's attempts in a separate row.
    REPEAT
        INPUT Names[Competitor]
    UNTIL LENGTH(Names[Competitor]) > 0
    Best <- -1
    FOR Attempt <- 1 TO 3
        REPEAT
            INPUT Attempts[Competitor, Attempt]
        UNTIL Attempts[Competitor, Attempt] = -1 OR
              (Attempts[Competitor, Attempt] >= 0 AND Attempts[Competitor, Attempt] <= 10)
        IF Attempts[Competitor, Attempt] <> -1
        THEN
            // Exclude fouls from both the mean and the competitor's best result.
            Total <- Total + Attempts[Competitor, Attempt]
            ValidCount <- ValidCount + 1
            IF Attempts[Competitor, Attempt] > Best
            THEN
                Best <- Attempts[Competitor, Attempt]
            ENDIF
        ENDIF
    NEXT Attempt
    IF Best = -1
    THEN
        OUTPUT Names[Competitor], "No valid attempt"
    ELSE
        OUTPUT Names[Competitor], Best
        IF Best > WinningDistance
        THEN
            // A strict comparison retains the first competitor on a tie.
            Winner <- Competitor
            WinningDistance <- Best
        ENDIF
    ENDIF
NEXT Competitor
IF Winner = 0
THEN
    // No name is indexed when every attempt was a foul.
    OUTPUT "No winner"
ELSE
    OUTPUT Names[Winner], WinningDistance
ENDIF
IF ValidCount > 0
THEN
    OUTPUT Total / ValidCount
ELSE
    OUTPUT "No valid attempts for a mean"
ENDIF
```

Python reference program (six competitors by default). The optional smaller size makes boundary cases concise to test; it does not change the algorithm.

```python
def run_competition(read=input, write=print, competitors=6):
    names = [""] * competitors
    attempts = [[0.0] * 3 for index in range(competitors)]
    winner = -1
    winning_distance = -1.0
    total = 0.0
    valid_count = 0
    for competitor in range(competitors):
        # Each row stores the three attempts belonging to this name.
        names[competitor] = read("Name: ")
        while len(names[competitor]) == 0:
            names[competitor] = read("Name: ")
        best = -1.0
        for attempt in range(3):
            while True:
                try:
                    distance = float(read("Distance or -1: "))
                    if distance == -1 or 0 <= distance <= 10:
                        break
                except ValueError:
                    pass
                write("Invalid distance")
            attempts[competitor][attempt] = distance
            if distance != -1:
                # Fouls must not contribute to the mean or the maximum.
                total += distance
                valid_count += 1
                if distance > best:
                    best = distance
        write((names[competitor], best if best != -1 else "No valid attempt"))
        # Strictly greater retains the first competitor on equal distances.
        if best > winning_distance:
            winner = competitor
            winning_distance = best
    write((names[winner], winning_distance) if winner != -1 else "No winner")
    # An all-foul competition has neither a winner nor a defined mean.
    mean = total / valid_count if valid_count > 0 else None
    write(mean if mean is not None else "No valid attempts for a mean")
    return winner, winning_distance, mean, names, attempts


if __name__ == "__main__":
    from sys import argv
    if "--interactive" in argv:
        run_competition()
    else:
        entries = iter(["", "A", "bad", "-2", "11", "0", "10", "-1",
                        "B", "10", "-1", "-1"])
        output = []
        result = run_competition(lambda prompt: next(entries), output.append, 2)
        assert result[:3] == (0, 10.0, 20.0 / 3)
        assert result[3:] == (["A", "B"], [[0.0, 10.0, -1.0], [10.0, -1.0, -1.0]])
        assert output[:3] == ["Invalid distance"] * 3
        assert output[-2] == ("A", 10.0)
        entries = iter(["C", "-1", "-1", "-1"])
        output = []
        assert run_competition(lambda prompt: next(entries), output.append, 1)[:3] == (-1, -1.0, None)
        assert output == [("C", "No valid attempt"), "No winner", "No valid attempts for a mean"]
        entries = iter(sum(([str(index), "0", "0", "0"] for index in range(6)), []))
        assert run_competition(lambda prompt: next(entries), lambda value: None)[:3] == (0, 0.0, 0.0)
        print("Competition tests passed")
```

**Total: 75 marks**
