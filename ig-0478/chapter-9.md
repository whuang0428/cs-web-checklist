# IGCSE 0478 Computer Science - Chapter 9 Updated Checklist
## Databases｜Syllabus-Aligned Paper 2 Revision Sheet

> **Version:** Syllabus-aligned revision for Paper 2  
> **Target:** Cambridge IGCSE Computer Science 0478  
> **Chapter:** 9 Databases  
> **Main audience:** Students  
> **Style:** Chinese explanation + English database keywords

---

# 0. How to Use This Sheet

Database questions usually reward precise vocabulary. Learn the structure first, then practise queries.

Core path:

1. table, record, field
2. data types and validation
3. primary key
4. search, sort and query
5. simple SQL-style thinking

---

# 1. Database Structure

| Term | Meaning | Example |
| --- | --- | --- |
| table | stores data about one type of item | Students |
| record | one row in a table | one student's details |
| field | one column / attribute | StudentID, Name, Mark |
| field name | name of a field | `DateOfBirth` |
| data type | kind of data stored in a field | INTEGER, STRING, DATE |
| primary key | field that uniquely identifies each record | StudentID |

Common mistake:

- Saying a primary key "stores the most important data". It uniquely identifies a record.

---

# 2. Good Field Design

Choose field names that are:

- meaningful
- unique within the table
- short but clear
- not full sentences

Example:

| Weak field | Better field |
| --- | --- |
| `thing` | `ProductName` |
| `date` | `OrderDate` |
| `number` | `StudentID` |

---

# 3. Data Types and Validation

| Field | Suitable type | Possible validation |
| --- | --- | --- |
| StudentID | STRING or INTEGER | length check / presence check |
| Mark | INTEGER | range check 0 to 100 |
| DateOfBirth | DATE | format check |
| Email | STRING | format check / presence check |
| Member | BOOLEAN | true/false |

Validation checks:

- range check
- type check
- length check
- presence check
- format check
- lookup check

---

# 4. Searching and Sorting

| Task | Meaning |
| --- | --- |
| search/query | find records that match conditions |
| sort ascending | A to Z / smallest to largest / oldest to newest |
| sort descending | Z to A / largest to smallest / newest to oldest |

Example conditions:

- `Mark >= 50`
- `House = "Blue"`
- `DateJoined > 01/09/2026`
- `Mark >= 80 AND House = "Red"`

---

# 5. Simple SQL-Style Queries

The exam may not require full SQL syntax, but query thinking is useful.

```sql
SELECT Name, Mark
FROM Students
WHERE Mark >= 50
ORDER BY Mark DESC;
```

Meaning:

- show only `Name` and `Mark`
- use the `Students` table
- include only passing students
- sort highest mark first

Common SQL keywords:

| Keyword | Meaning |
| --- | --- |
| `SELECT` | choose fields to display |
| `FROM` | choose table |
| `WHERE` | filter records |
| `ORDER BY` | sort results |
| `ASC` | ascending |
| `DESC` | descending |

---

# 6. Forms and Reports

| Feature | Purpose |
| --- | --- |
| form | easier data entry and editing |
| report | formatted output for viewing or printing |
| query | selects data using criteria |

Exam phrasing:

- A form can reduce input errors by using controls such as drop-down lists.
- A report presents selected data in a clear layout.
- A query can filter records that match conditions.

---

# 7. Common Exam Mistakes

- Confusing record and field.
- Choosing a non-unique field as a primary key.
- Sorting text and numbers the wrong way.
- Forgetting that validation does not prove data is true.
- Writing `WHERE Mark = > 50` instead of `WHERE Mark >= 50`.
- Selecting all fields when the question asks for specific fields.

---

# 8. Mini Practice

1. A library database stores books. Suggest a primary key and justify it.
2. Choose suitable data types for `BookID`, `Title`, `Price`, `Available`.
3. Write a query to show books cheaper than 10.00 sorted by title.
4. Explain the difference between a field and a record.
5. Give two validation checks for an email address field.

---

