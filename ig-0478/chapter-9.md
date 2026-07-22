# Chapter 9: Databases

> **Paper 2 focus:** design a suitable single-table database, choose fields and data types, select a primary key, and read or complete SQL queries.

---

## 1. Syllabus Coverage

| Objective | Where it is covered |
|---|---|
| Define a single-table database from storage requirements | Sections 2–3 |
| Choose suitable field names and data types | Section 3 |
| Select and explain a primary key | Section 4 |
| Read and complete single-table SQL | Sections 5–6 |
| Use `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `SUM`, `COUNT`, `AND` and `OR` | Sections 5–6 |
| Identify the output of a query | Section 7 and Worked Example 2 |

---

## 2. Database Structure

A **database** is an organised collection of data. In Topic 9, questions use a **single table**.

| Term | Meaning |
|---|---|
| Table | The complete set of related records |
| Record | All stored fields about one item or entity |
| Field | One category of data within every record |
| Field name | The identifier used for a field |
| Data type | The kind of value a field may store |
| Primary key | A field that uniquely identifies each record |

Example table: `Equipment`

| EquipmentID | ItemName | Category | PurchaseDate | Cost | Available |
|---|---|---|---|---:|---|
| EQ101 | Tripod | Camera | 03/09/2025 | 45.50 | TRUE |
| EQ102 | Microphone | Audio | 18/10/2025 | 29.99 | FALSE |
| EQ103 | Light panel | Camera | 07/01/2026 | 61.00 | TRUE |

Each row is one record. `Cost` is one field. `EquipmentID` is a suitable primary key.

---

## 3. From Requirements to a Table Design

Use this method:

1. identify the entity represented by one record
2. list each item of data that must be stored
3. give every field a concise, meaningful name
4. choose the narrowest suitable data type
5. select a field that is unique and always present as the primary key

### Data types

| Data type | Suitable example | Important distinction |
|---|---|---|
| Text / alphanumeric | `"AB107"` | letters, digits or mixed text |
| Character | `'Y'` | exactly one character |
| Boolean | `TRUE` | two logical states |
| Integer | `27` | whole-number quantity |
| Real | `19.95` | value with a fractional part |
| Date/time | `22/07/2026` | date or time value that may be sorted/compared chronologically |

Choose the type according to use:

- an identification code is usually text even when it contains only digits
- a quantity is integer because arithmetic is performed
- a price is real
- an availability state is Boolean
- a date should use a date/time type, not ordinary text

### Example design

A sports centre stores each court's code, sport, hourly charge, indoor status and number of bookings this month.

| Field name | Data type | Reason |
|---|---|---|
| CourtCode | Text | may contain letters and digits |
| Sport | Text | stores a word or phrase |
| HourlyCharge | Real | may contain decimal places |
| IsIndoor | Boolean | only true or false |
| MonthlyBookings | Integer | a whole-number count |

`CourtCode` can be the primary key if every court has a different code.

---

## 4. Primary Keys

A primary key must:

- be unique for every record
- be present for every record
- remain stable enough to identify the record

Good primary keys:

- `StudentID`
- `BookCode`
- `VehicleRegistration`

Weak choices:

- name, because two people or products may share it
- price, because many records may have the same price
- availability, because it has only two possible values

If no natural field is reliably unique, create an ID field.

---

## 5. SQL Building Blocks

SQL queries retrieve or calculate information from a table.

### SELECT and FROM

```sql
SELECT ItemName, Cost
FROM Equipment;
```

This returns the `ItemName` and `Cost` fields from every record.

Use `*` when all fields are required:

```sql
SELECT *
FROM Equipment;
```

### WHERE

```sql
SELECT ItemName
FROM Equipment
WHERE Available = TRUE;
```

`WHERE` filters records before the selected fields are displayed.

### AND and OR

```sql
SELECT ItemName, Cost
FROM Equipment
WHERE Category = 'Camera' AND Cost < 60;
```

Both conditions must be true.

```sql
SELECT ItemName
FROM Equipment
WHERE Category = 'Camera' OR Category = 'Audio';
```

At least one condition must be true.

Text values use quotation marks. Numeric and Boolean values normally do not.

### ORDER BY

```sql
SELECT ItemName, Cost
FROM Equipment
ORDER BY Cost ASC;
```

`ASC` means ascending and `DESC` means descending. Ascending is normally the default, but writing the required direction makes the intention clear.

```sql
SELECT ItemName, Cost
FROM Equipment
ORDER BY Cost DESC;
```

### SUM and COUNT

```sql
SELECT SUM(Cost)
FROM Equipment;
```

This produces the total of all values in `Cost`.

```sql
SELECT COUNT(EquipmentID)
FROM Equipment
WHERE Available = TRUE;
```

This produces the number of available equipment records.

---

## 6. Constructing a Query

Translate the request in a fixed order.

> Show the item names and costs of available camera equipment, ordered from highest to lowest cost.

1. output fields: `ItemName, Cost`
2. table: `Equipment`
3. conditions: category is Camera **and** available is true
4. order: cost descending

```sql
SELECT ItemName, Cost
FROM Equipment
WHERE Category = 'Camera' AND Available = TRUE
ORDER BY Cost DESC;
```

Check that:

- every selected field exists
- the table name is correct
- string values are quoted
- the logical connector matches the wording
- sorting uses the requested field and direction

---

## 7. Predicting Query Output

Use this sequence:

1. apply the `WHERE` condition to remove records
2. calculate `SUM` or `COUNT` if present
3. apply `ORDER BY` to the remaining records
4. display only the fields named after `SELECT`

For the sample `Equipment` table:

```sql
SELECT ItemName, Cost
FROM Equipment
WHERE Available = TRUE
ORDER BY Cost DESC;
```

Output:

| ItemName | Cost |
|---|---:|
| Light panel | 61.00 |
| Tripod | 45.50 |

`Microphone` is excluded before sorting because its `Available` value is false.

For:

```sql
SELECT COUNT(EquipmentID)
FROM Equipment
WHERE Category = 'Camera' OR Cost < 30;
```

all three records satisfy at least one condition, so the output is `3`.

---

## 8. Worked Example 1 — Design a Single Table

A community garden needs to store:

- a unique plot code such as `P-104`
- the gardener's name
- plot area in square metres
- whether a water connection is installed
- the date the plot was allocated

A suitable design is:

| Field name | Data type | Key? | Reason |
|---|---|---|---|
| PlotCode | Text | Primary key | mixed characters and unique |
| GardenerName | Text | No | names are not guaranteed to be unique |
| Area | Real | No | may include a fractional value |
| HasWater | Boolean | No | two logical states |
| AllocationDate | Date/time | No | supports chronological comparison |

Why `GardenerName` is not the key: two gardeners may share a name, and one person's displayed name may change. The allocated plot code is unique for the record.

---

## 9. Worked Example 2 — Query and Output

Use the table `Courses`.

| CourseCode | CourseName | Places | Fee | Online |
|---|---|---:|---:|---|
| C10 | Web Basics | 20 | 35.00 | TRUE |
| C11 | Robotics | 12 | 55.00 | FALSE |
| C12 | Digital Art | 18 | 40.00 | TRUE |
| C13 | Databases | 15 | 30.00 | FALSE |

Query:

```sql
SELECT CourseName, Fee
FROM Courses
WHERE Online = TRUE OR Fee < 35
ORDER BY Fee DESC;
```

Filtering:

- Web Basics: included because `Online = TRUE`
- Robotics: excluded
- Digital Art: included because `Online = TRUE`
- Databases: included because `Fee < 35`

After descending sort and projection:

| CourseName | Fee |
|---|---:|
| Digital Art | 40.00 |
| Web Basics | 35.00 |
| Databases | 30.00 |

The value `35.00` does not satisfy `Fee < 35`, but Web Basics is still included because the two conditions use `OR`.

---

## 10. Common Mistakes Checklist

- [ ] I design one record around one clearly identified entity.
- [ ] I do not use a non-unique name as a primary key.
- [ ] I store codes as text when leading zeros or letters matter.
- [ ] I use a real type for values that may contain a fractional part.
- [ ] I quote text conditions but not numeric values.
- [ ] I do not confuse `AND` with `OR`.
- [ ] I filter records before predicting the displayed fields.
- [ ] I sort using the requested field and direction.
- [ ] I distinguish `SUM` from `COUNT`.
- [ ] I use only fields that actually exist in the table.

---

## 11. 10 Marks Quick Check

1. Define a record and a field. **[2]**
2. State two properties of a suitable primary key. **[2]**
3. Give suitable data types for a product code `"007A"`, a quantity, a price and an in-stock flag. **[4]**
4. State the purpose of `WHERE` and `ORDER BY`. **[2]**

**Total: 10 marks**

### Quick Check Answers

1. A record is all stored fields about one entity; a field is one category/item of data in each record. **[2]**
2. Any two: unique, always present, stable. **[2]**
3. Text/alphanumeric; integer; real; Boolean. **[4]**
4. `WHERE` filters records using a condition; `ORDER BY` sorts the result using a field and direction. **[2]**

---

## 12. 20 Marks Practice

A bicycle-hire company needs one table. For every bicycle it stores a unique code such as `"BK042"`, model name, hourly rate, number of hires and whether it is currently available.

1. Give a suitable field name and data type for each of the five values. **[5]**
2. Identify the primary key and justify your answer. **[2]**
3. Write a query to display the code, model and hourly rate of available bicycles costing less than 12.50 per hour, ordered from lowest to highest rate. **[5]**
4. Write a query to output the number of bicycles that are unavailable. **[3]**
5. Write a query to output the total number of hires for bicycles whose hourly rate is greater than 15.00 or whose hire count is greater than 100. **[4]**
6. State why `ModelName` would be unsuitable as the primary key. **[1]**

**Total: 20 marks**

### 20 Marks Practice Mark Scheme

Assume the table is named `Bicycles` and uses these fields: `BikeCode`, `ModelName`, `HourlyRate`, `HireCount`, `Available`.

1. `BikeCode`: text; `ModelName`: text; `HourlyRate`: real; `HireCount`: integer; `Available`: Boolean. Award one mark for each suitable field/type pair. **[5]**
2. `BikeCode` **[1]** because it is stated to be unique for every bicycle **[1]**. **[2]**
3.

   ```sql
   SELECT BikeCode, ModelName, HourlyRate
   FROM Bicycles
   WHERE Available = TRUE AND HourlyRate < 12.50
   ORDER BY HourlyRate ASC;
   ```

   Correct selected fields **[1]**; table **[1]**; availability condition **[1]**; rate condition joined with `AND` **[1]**; ascending rate order **[1]**. **[5]**

4.

   ```sql
   SELECT COUNT(BikeCode)
   FROM Bicycles
   WHERE Available = FALSE;
   ```

   `COUNT` with a field **[1]**; correct table **[1]**; correct condition **[1]**. **[3]**

5.

   ```sql
   SELECT SUM(HireCount)
   FROM Bicycles
   WHERE HourlyRate > 15.00 OR HireCount > 100;
   ```

   `SUM(HireCount)` **[1]**; correct table **[1]**; both conditions **[1]**; correct `OR` connector **[1]**. **[4]**

6. More than one bicycle may have the same model name, so it is not guaranteed to be unique. **[1]**

---

## 13. Final Self-Assessment

- [ ] I can convert storage requirements into a single-table design.
- [ ] I can justify every field's data type.
- [ ] I can choose and explain a primary key.
- [ ] I can construct queries using the complete required keyword set.
- [ ] I can distinguish `AND` from `OR` in a scenario.
- [ ] I can use `SUM` and `COUNT` correctly.
- [ ] I can predict filtered, sorted and projected query output.
- [ ] I completed both practice sets without looking at the answers first.
