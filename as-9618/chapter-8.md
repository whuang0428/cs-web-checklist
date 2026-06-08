# AS 9618 Computer Science — Chapter 8 Updated Notes
## Databases｜Syllabus-Aligned Paper 1 Revision Sheet

> **Version:** Syllabus-aligned revision; informed by recent Paper 1 patterns  
> **Target:** Cambridge International AS & A Level Computer Science 9618  
> **Chapter:** 8 Databases  
> **Main audience:** Students  
> **Style:** 中文解释 + English mark scheme keywords  
> **Docsify:** ready for static webpage display  
> **Important:** 本章只覆盖 AS Paper 1 理论部分的数据库要求，不加入 A2 / 大学数据库中过深内容。

---

# 0. How to Use This Sheet

本章不是单纯背定义。2024 和 2025 的题目趋势非常明显：

1. **给一个真实场景数据库**
2. **要求判断 primary key / foreign key / relationship**
3. **写 SQL DDL 或 DML**
4. **解释 normalisation / file-based approach / DBMS features**
5. **用 mark scheme phrases 精准拿分**

复习顺序建议如下：

```mermaid
flowchart LR
A[File-based approach<br/>limitations] --> B[Relational database<br/>tables / records / fields]
B --> C[Keys and relationships<br/>PK / FK / E-R diagram]
C --> D[Normalisation<br/>1NF / 2NF / 3NF]
D --> E[DBMS features<br/>dictionary / security / integrity]
E --> F[SQL<br/>DDL + DML]
```

---

# 1. Recent Paper 1 Pattern Map

| Area | Recent exam pattern | What students must practise |
| --- | --- | --- |
| File-based approach vs relational database | High | limitation + how relational database solves it |
| Primary key / foreign key | Very high | identify keys from table design and explain purpose |
| E-R relationship | High | one-to-many / many-to-many implemented using linking table |
| SQL DDL `CREATE TABLE` | Very high | field type, `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, sensible constraints |
| SQL DML `SELECT` queries | Very high | `SUM`, `COUNT`, `WHERE`, date condition, `GROUP BY`, simple join |
| Database terminology | High | tuple, attribute, entity, candidate key, referential integrity |
| Normalisation | Medium-high | purpose and benefits; remove redundancy and update/insert/delete anomalies |
| DBMS features | Medium | data dictionary, access rights, backup, query processor, developer interface |
| Complex relational theory | Low | do not over-study beyond 3NF and syllabus wording |
| Very advanced SQL | Low | no nested queries, no stored procedures, no triggers required |

---

# 2. Content Update Decision

## 2.1 Keep and Strengthen

| Kept content | Reason |
| --- | --- |
| file-based approach limitations | 2024 database question starts from file-based approach |
| relational database benefits | frequently asked as “explain how relational database addresses limitation” |
| primary key / foreign key / candidate key | repeated across 2024 and 2025 |
| referential integrity | direct definition question and useful in relationship explanation |
| E-R diagram relationships | often tested with given tables |
| many-to-many linking table | common when two entities can link to many of each other |
| SQL `CREATE TABLE` | high-value 4–5 mark DDL question |
| SQL aggregate functions | `SUM`, `COUNT`, `AVG` appear in Paper 1 database scripts |
| `WHERE`, `GROUP BY`, `INNER JOIN` | practical mark scheme phrases |
| normalisation to 3NF | syllabus requirement and scenario question topic |
| DBMS features | can appear as explain/describe questions |

## 2.2 Downweight

| Downweighted content | Why |
| --- | --- |
| very detailed database indexing | not central in AS 9618 Paper 1 |
| transaction processing / ACID | beyond AS Chapter 8 expectation |
| SQL subqueries | not required by syllabus subset |
| triggers, stored procedures, views in depth | may confuse students and not common for marks |
| entity-attribute modelling theory beyond E-R diagrams | too abstract for Paper 1 |
| full commercial DBMS architecture | only developer interface and query processor are needed |

## 2.3 Delete / Avoid

| Avoided content | Reason |
| --- | --- |
| NoSQL databases | not in AS 9618 Chapter 8 |
| recursive SQL / window functions | beyond syllabus |
| advanced normal forms such as BCNF / 4NF / 5NF | not required |
| brand-specific SQL syntax | Cambridge says no brand names; keep generic SQL |

---

# 3. Syllabus Scope

Chapter 8 contains three syllabus sections:

| Syllabus section | Main focus |
| --- | --- |
| **8.1 Database Concepts** | file-based approach, relational model, keys, E-R diagrams, normalisation |
| **8.2 Database Management Systems** | DBMS features, data dictionary, data security, data integrity, query processor |
| **8.3 DDL and DML** | SQL as DDL and DML, `CREATE TABLE`, `ALTER TABLE`, `SELECT`, `INSERT`, `DELETE`, `UPDATE` |

---

# 4. One-Page Mind Map

```mermaid
mindmap
  root((Chapter 8<br/>Databases))
    Database Concepts
      File-based approach
      Relational database
      Entity
      Attribute
      Tuple
      Primary key
      Candidate key
      Foreign key
      Referential integrity
    Relationships
      One-to-one
      One-to-many
      Many-to-many
      Linking table
      E-R diagram
    Normalisation
      1NF
      2NF
      3NF
      Redundancy
      Anomalies
    DBMS
      Data dictionary
      Data modelling
      Logical schema
      Access rights
      Backup
      Query processor
      Developer interface
    SQL
      DDL
        CREATE DATABASE
        CREATE TABLE
        ALTER TABLE
        PRIMARY KEY
        FOREIGN KEY
      DML
        SELECT FROM
        WHERE
        ORDER BY
        GROUP BY
        INNER JOIN
        SUM COUNT AVG
        INSERT DELETE UPDATE
```

---

# 5. 8.1 Database Concepts

## 5.1 File-based approach

### Meaning

A **file-based approach** stores data in separate files, usually created for one specific application.

中文理解：  
就是每个程序自己管自己的文件。比如 repair data 一个文件，customer data 一个文件，invoice data 又一个文件。这样简单，但容易重复、难维护。

### Limitations

| Limitation | 中文解释 | Mark scheme phrase |
| --- | --- | --- |
| Data duplication / redundancy | 同一数据在多个文件重复存储 | same data stored more than once |
| Data inconsistency | 一个文件更新了，另一个没更新 | data may become inconsistent |
| Data isolation | 数据分散在不同文件中 | data stored in separate files |
| Program-data dependence | 文件结构变了，程序也要改 | file structure is dependent on program |
| Difficult to query | 很难跨文件查找复杂信息 | difficult to search / retrieve related data |
| Poor security | 权限不好统一控制 | difficult to control access rights |
| Poor integrity | 不容易统一验证数据正确性 | difficult to maintain data integrity |

### 2024-style answer

> A file-based approach can cause data redundancy because the same customer data may be stored in several files. A relational database reduces redundancy by storing customer data once in a CUSTOMER table and linking it to other tables using a foreign key.

---

## 5.2 Relational database

### Definition

> A relational database stores data in tables. Tables are linked using primary keys and foreign keys.

中文理解：  
relational database 的核心就是 **分表 + 关联**。不是把所有数据塞进一个大表，而是把 customer、repair、part、invoice 等分开放，再用 key 连接。

### Core terms

| Term | Meaning | 中文解释 |
| --- | --- | --- |
| Entity | something about which data is stored | 要存储的对象，如 CUSTOMER / REPAIR |
| Table / relation | a set of records about one entity | 表 |
| Attribute / field | one item of data stored for an entity | 字段 / 列 |
| Tuple / record | one row in a table | 一条记录 / 一行 |
| Domain | set of allowed values for an attribute | 一个字段允许的值范围 |
| Primary key | attribute(s) that uniquely identify a record | 主键，唯一识别一行 |
| Candidate key | attribute(s) that could be chosen as primary key | 候选键，可以当主键 |
| Foreign key | attribute that references primary key in another table | 外键，连接另一张表 |
| Referential integrity | foreign key values must match existing primary key values or be null | 外键必须引用真实存在的主键 |

---

## 5.3 Primary key

### Mark scheme answer

> A primary key is an attribute or set of attributes that uniquely identifies each record in a table.

### Important points

+ must be **unique**
+ cannot normally be **NULL**
+ each table should have a primary key
+ can be one field or a **composite key**

### Example

```sql
CUSTOMER(CustomerID, FirstName, LastName, ContactNumber)
```

`CustomerID` is suitable because each customer has a different ID.

---

## 5.4 Candidate key

### Mark scheme answer

> A candidate key is an attribute or set of attributes that could be used as the primary key because it uniquely identifies each record.

### Example

In a table:

```text
STUDENT(StudentID, Email, PassportNumber, FirstName, LastName)
```

Possible candidate keys:

+ `StudentID`
+ `Email`
+ `PassportNumber`

Only one is chosen as the **primary key**, but all three could uniquely identify a student.

---

## 5.5 Foreign key

### Mark scheme answer

> A foreign key is an attribute in one table that refers to the primary key in another table.

### Example

```text
REPAIR(RepairNumber, StartDate, EndDate, CustomerID, Device)
CUSTOMER(CustomerID, FirstName, LastName, ContactNumber)
```

`CustomerID` in `REPAIR` is a foreign key because it references `CustomerID` in `CUSTOMER`.

### Common 2024-style task

Given:

```text
SALE(SaleID, BatchID, CustomerID, Quantity, Date)
BATCH(BatchID, Type, Flavour, Size, SellingPrice, EndDate)
CUSTOMER(CustomerID, CompanyName, EmailAddress, TelephoneNumber)
```

Foreign keys in `SALE`:

| Foreign key | References table |
| --- | --- |
| `BatchID` | `BATCH` |
| `CustomerID` | `CUSTOMER` |

---

## 5.6 Referential integrity

### Mark scheme answer

> Referential integrity ensures that a foreign key value in one table must match an existing primary key value in the referenced table.

### 中文解释

如果 `REPAIR.CustomerID = "C102"`，那么 `CUSTOMER` 表里必须真的有 `CustomerID = "C102"`。  
不能出现 repair 记录属于一个不存在的 customer。

### Why it matters

+ prevents orphan records
+ keeps relationships valid
+ improves data consistency
+ prevents invalid foreign key values

---

## 5.7 Relationships

### One-to-one

One record in table A links to one record in table B.

Example:

```text
EMPLOYEE ---- LOGIN_DATA
```

Each employee has one login record; each login record belongs to one employee.

### One-to-many

One record in table A links to many records in table B.

Example:

```text
CUSTOMER ---- REPAIR
```

One customer can have many repairs, but each repair belongs to one customer.

### Many-to-many

Many records in table A link to many records in table B.

Example:

```text
REPAIR ---- PART
```

One repair can use many parts.  
One part can be used in many repairs.

This is implemented using a **linking table**:

```text
REPAIR_PART(PartID, RepairNumber, Quantity)
```

### Mark scheme style

> A many-to-many relationship is implemented by creating a linking table that contains the primary keys from both tables as foreign keys.

---

## 5.8 E-R diagrams

### What to show

An E-R diagram normally shows:

+ entities / tables
+ relationships between entities
+ one-to-many / many-to-many relationships
+ linking tables where needed

### Example

```mermaid
erDiagram
    CUSTOMER ||--o{ REPAIR : makes
    REPAIR ||--o{ REPAIR_PART : uses
    PART ||--o{ REPAIR_PART : included_in
```

### Exam advice

If you see a table like:

```text
REPAIR_PART(PartID, RepairNumber, Quantity)
```

that usually means it is a **linking table** between `REPAIR` and `PART`.

---

# 6. Normalisation

## 6.1 Why normalise?

### Mark scheme answer

> Normalisation reduces data redundancy and helps avoid update, insert and delete anomalies.

中文理解：  
normalisation 就是把“乱的大表”拆成“结构清楚的小表”，减少重复，避免数据改一处漏一处。

### Benefits

| Benefit | 中文解释 | Mark scheme phrase |
| --- | --- | --- |
| Reduces redundancy | 减少重复数据 | reduces data duplication |
| Improves consistency | 数据更一致 | improves data consistency |
| Avoids update anomaly | 修改数据时不用改很多地方 | avoids update anomalies |
| Avoids insert anomaly | 可以插入某类数据而不依赖其他数据 | avoids insert anomalies |
| Avoids delete anomaly | 删除一条记录不会误删其他重要信息 | avoids delete anomalies |
| Improves integrity | 数据更准确完整 | improves data integrity |

---

## 6.2 First Normal Form: 1NF

### Rule

> A table is in 1NF if it has no repeating groups and each field contains atomic values.

中文理解：  
一格里面只能放一个值，不能放列表。

### Bad example

| StudentID | Name | Subjects |
| --- | --- | --- |
| S01 | Amy | Maths, CS, Physics |

Problem: `Subjects` contains a repeating group.

### Better design

| StudentID | Name |
| --- | --- |
| S01 | Amy |

| StudentID | Subject |
| --- | --- |
| S01 | Maths |
| S01 | CS |
| S01 | Physics |

---

## 6.3 Second Normal Form: 2NF

### Rule

> A table is in 2NF if it is in 1NF and every non-key attribute is fully dependent on the whole primary key.

中文理解：  
如果主键是 composite key，那么非主键字段必须依赖整个主键，而不能只依赖其中一部分。

### Example

```text
ORDER_ITEM(OrderID, ProductID, ProductName, Quantity)
```

Composite key: `(OrderID, ProductID)`

Problem:

+ `Quantity` depends on both `OrderID` and `ProductID`
+ `ProductName` only depends on `ProductID`

So `ProductName` should be moved to `PRODUCT`.

---

## 6.4 Third Normal Form: 3NF

### Rule

> A table is in 3NF if it is in 2NF and has no non-key attribute depending on another non-key attribute.

中文理解：  
非主键字段不能依赖另一个非主键字段。

### Example

```text
STUDENT(StudentID, Name, TutorID, TutorName)
```

Problem:

+ `TutorName` depends on `TutorID`
+ `TutorID` is not the primary key of `STUDENT`

Better design:

```text
STUDENT(StudentID, Name, TutorID)
TUTOR(TutorID, TutorName)
```

---

## 6.5 Normalisation quick exam wording

| Question asks | Best answer structure |
| --- | --- |
| “Give one benefit of normalisation” | reduces redundancy + improves consistency |
| “Why is this table not in 1NF?” | repeating group / non-atomic values |
| “How to remove many-to-many?” | create linking table with foreign keys |
| “Why split table?” | remove partial/transitive dependency |
| “What problem can occur without normalisation?” | update / insert / delete anomaly |

---

# 7. 8.2 Database Management Systems DBMS

## 7.1 DBMS definition

### Mark scheme answer

> A DBMS is software used to define, create, maintain and control access to a database.

中文理解：  
DBMS 就是管理数据库的软件层。它不是数据本身，而是用来创建表、修改数据、查询数据、控制权限、备份数据的软件系统。

---

## 7.2 DBMS features

| Feature | What it does | Mark scheme phrase |
| --- | --- | --- |
| Data dictionary | stores metadata about database structure | stores data about data |
| Data management | maintains data in tables | stores / updates / deletes data |
| Data modelling | helps design database structure | produces E-R model / logical schema |
| Logical schema | overall logical structure of database | independent of physical storage |
| Data integrity | keeps data accurate and consistent | validation / referential integrity |
| Data security | protects data from unauthorised access | access rights / passwords / encryption |
| Backup and recovery | makes copies and restores data | recover after data loss |
| Developer interface | allows developers to write commands / SQL | interface for database development |
| Query processor | processes SQL queries | interprets / optimises / executes queries |

---

## 7.3 Data dictionary

### Definition

> A data dictionary stores metadata about the database, such as table names, field names, data types, relationships and validation rules.

### Examples of metadata

+ table names
+ field / attribute names
+ data types
+ field lengths
+ primary keys
+ foreign keys
+ relationships
+ validation rules
+ access rights

### Common weak answer

> A data dictionary stores data.

Too vague. It stores **data about data**, not normal user records.

---

## 7.4 Data integrity in DBMS

DBMS can improve integrity by:

+ enforcing data types
+ applying validation rules
+ enforcing referential integrity
+ preventing invalid foreign keys
+ using constraints such as `NOT NULL`
+ controlling concurrent updates

### Mark scheme phrase

> The DBMS can enforce validation rules and referential integrity to ensure data remains accurate, complete and consistent.

---

## 7.5 Data security in DBMS

DBMS can improve security by:

+ username and password
+ access rights
+ user groups
+ different permissions for read/write/delete
+ encryption
+ audit logs
+ backup procedures

### Example answer

> A DBMS can use access rights so that different users can only view or modify the data they are authorised to access.

---

## 7.6 Developer interface

### Meaning

A developer interface lets developers create and modify database structures and write SQL queries.

### Mark scheme style

> The developer interface allows a developer to write SQL commands to define, query and maintain the database.

---

## 7.7 Query processor

### Meaning

A query processor deals with SQL queries.

It may:

+ parse the query
+ check syntax
+ optimise the query
+ execute the query
+ return results

### Mark scheme style

> The query processor interprets and executes SQL queries and may optimise them before execution.

---

# 8. 8.3 DDL and DML

## 8.1 DDL vs DML

| Type | Full name | Purpose | Examples |
| --- | --- | --- | --- |
| DDL | Data Definition Language | create / change database structure | `CREATE DATABASE`, `CREATE TABLE`, `ALTER TABLE` |
| DML | Data Manipulation Language | query / insert / update / delete data | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |

### Mark scheme answer

> DDL is used to define or modify the structure of a database. DML is used to query and maintain the data stored in the database.

---

## 8.2 SQL data types

| Data type | Use | Example |
| --- | --- | --- |
| `CHARACTER` | fixed-length text | code with fixed length |
| `VARCHAR(n)` | variable-length text up to n characters | names, emails |
| `BOOLEAN` | true/false value | paid / active |
| `INTEGER` | whole number | quantity |
| `REAL` | decimal number | price |
| `DATE` | date value | start date |
| `TIME` | time value | appointment time |

### Exam advice

Use sensible types:

| Field | Good type |
| --- | --- |
| ID with letters/numbers | `VARCHAR(n)` or `CHARACTER(n)` |
| price / amount | `REAL` |
| quantity | `INTEGER` |
| paid true/false | `BOOLEAN` |
| date sent / end date | `DATE` |
| contact number | `VARCHAR(n)`, not integer |

Contact numbers should not be `INTEGER` because they may start with `0` and are not used for arithmetic.

---

## 8.3 SQL DDL: `CREATE TABLE`

### General structure

```sql
CREATE TABLE TableName (
    Field1 DataType NOT NULL,
    Field2 DataType,
    PRIMARY KEY (Field1)
);
```

### With foreign key

```sql
CREATE TABLE REPAIR (
    RepairNumber VARCHAR(6) NOT NULL,
    StartDate DATE,
    EndDate DATE,
    CustomerID VARCHAR(6),
    Device VARCHAR(30),
    PRIMARY KEY (RepairNumber),
    FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID)
);
```

---

## 8.4 2024-style DDL example: linking table

Given:

```text
REPAIR_PART(PartID, RepairNumber, Quantity)
```

A good answer:

```sql
CREATE TABLE REPAIR_PART (
    PartID VARCHAR(10) NOT NULL,
    RepairNumber VARCHAR(4) NOT NULL,
    Quantity INTEGER,
    PRIMARY KEY (PartID, RepairNumber),
    FOREIGN KEY (PartID) REFERENCES PART(PartID),
    FOREIGN KEY (RepairNumber) REFERENCES REPAIR(RepairNumber)
);
```

### Why this is strong

| Part | Why it gets marks |
| --- | --- |
| `CREATE TABLE REPAIR_PART` | correct table creation |
| `PartID VARCHAR(...)` | text ID with letters/numbers |
| `RepairNumber VARCHAR(...)` | leading zero possible, so not integer |
| `Quantity INTEGER` | quantity is whole number |
| `PRIMARY KEY (PartID, RepairNumber)` | composite key for linking table |
| two `FOREIGN KEY` lines | correctly links to parent tables |

---

## 8.5 SQL DML: `SELECT`

### Basic structure

```sql
SELECT FieldName
FROM TableName
WHERE condition;
```

### Example

```sql
SELECT FirstName, LastName
FROM CUSTOMER
WHERE CustomerID = 'C102';
```

---

## 8.6 `SUM`, `COUNT`, `AVG`

| Function | Purpose | Example use |
| --- | --- | --- |
| `SUM` | total of numeric values | total amount due |
| `COUNT` | number of records | number of customers |
| `AVG` | average of numeric values | average price |

### Example: total unpaid invoices

```sql
SELECT SUM(AmountDue)
FROM INVOICE
WHERE SupplierID = 'JK675'
AND Paid = FALSE;
```

This is a very common Paper 1 style: **aggregate function + WHERE condition**.

---

## 8.7 Date conditions

Different SQL systems format dates slightly differently. In Cambridge answers, focus on logic.

Example:

```sql
SELECT SUM(Quantity)
FROM SALE
WHERE CustomerID = '0034E'
AND Date >= '2023-01-01'
AND Date <= '2023-12-31';
```

Alternative accepted style may use:

```sql
AND Date BETWEEN '2023-01-01' AND '2023-12-31'
```

### Exam warning

If the field is called `Date`, keep it exactly as shown in the question unless the question uses another name such as `DateSent`.

---

## 8.8 `GROUP BY`

Use `GROUP BY` when the question asks for totals/counts **for each group**.

### Example

Show number of birds for each size:

```sql
SELECT Size, COUNT(BirdID)
FROM BIRD_TYPE
GROUP BY Size;
```

### Common mistake

Writing `COUNT(Size)` when the question wants count of records.  
Usually safer: `COUNT(*)` or `COUNT(PrimaryKey)`.

---

## 8.9 `INNER JOIN`

Use `INNER JOIN` when data is needed from two tables.

### Example

```sql
SELECT CUSTOMER.FirstName, REPAIR.Device
FROM CUSTOMER
INNER JOIN REPAIR
ON CUSTOMER.CustomerID = REPAIR.CustomerID;
```

### Mark scheme style

You can also see comma-style join:

```sql
SELECT CUSTOMER.FirstName, REPAIR.Device
FROM CUSTOMER, REPAIR
WHERE CUSTOMER.CustomerID = REPAIR.CustomerID;
```

Both express the same basic relationship.

---

## 8.10 DML maintenance commands

### `INSERT INTO`

```sql
INSERT INTO CUSTOMER(CustomerID, FirstName, LastName)
VALUES('C105', 'Amy', 'Chen');
```

### `UPDATE`

```sql
UPDATE INVOICE
SET Paid = TRUE
WHERE InvoiceID = '000002';
```

### `DELETE FROM`

```sql
DELETE FROM INVOICE
WHERE InvoiceID = '000003';
```

### Exam warning

Never write:

```sql
DELETE FROM INVOICE;
```

unless you want to delete every row.

---

# 9. Mark Scheme Keywords

## 9.1 Database concept keywords

| Concept | Must-have keywords |
| --- | --- |
| Primary key | uniquely identifies each record |
| Candidate key | could be used as primary key |
| Foreign key | references primary key in another table |
| Referential integrity | foreign key matches existing primary key |
| Tuple | row / record |
| Attribute | field / column |
| Entity | object about which data is stored |
| Relational database | data stored in linked tables |
| File-based limitation | redundancy / inconsistency / difficult access |
| Normalisation | reduces redundancy / removes anomalies |
| 1NF | no repeating groups / atomic values |
| 2NF | full dependency on whole key |
| 3NF | no non-key dependency |
| DBMS | define / create / maintain / control database |
| Data dictionary | metadata / data about data |
| Query processor | processes / optimises / executes SQL |
| Developer interface | allows developer to write SQL commands |

## 9.2 SQL keywords

| SQL task | Keywords to include |
| --- | --- |
| Create table | `CREATE TABLE`, field names, data types |
| Primary key | `PRIMARY KEY(field)` |
| Foreign key | `FOREIGN KEY(field) REFERENCES Table(field)` |
| Query table | `SELECT ... FROM ...` |
| Filter rows | `WHERE` |
| Total | `SUM(field)` |
| Count | `COUNT(field)` / `COUNT(*)` |
| Average | `AVG(field)` |
| Sort | `ORDER BY` |
| Group | `GROUP BY` |
| Join tables | `INNER JOIN ... ON ...` |
| Add data | `INSERT INTO ... VALUES` |
| Change data | `UPDATE ... SET ... WHERE` |
| Remove data | `DELETE FROM ... WHERE` |

---

# 10. Common Mistakes 易错表

| Mistake | Why it loses marks | Correct version |
| --- | --- | --- |
| saying primary key is “important field” | too vague | uniquely identifies each record |
| saying foreign key is “another primary key” | not precise | references primary key in another table |
| using `INTEGER` for IDs like `0022` | leading zero may be lost | use `VARCHAR` / `CHARACTER` |
| forgetting `PRIMARY KEY` in `CREATE TABLE` | loses DDL constraint mark | add `PRIMARY KEY(...)` |
| forgetting foreign key references | table not linked | add `FOREIGN KEY(...) REFERENCES ...` |
| using `SUM(*)` | invalid for total field | use `SUM(AmountDue)` |
| using `COUNT(Price)` for total price | count counts rows, not sum | use `SUM(Price)` |
| missing `WHERE` in update/delete | changes all rows | always include condition |
| confusing tuple and attribute | row vs column confusion | tuple = row, attribute = field |
| saying normalisation “makes database faster” only | weak and not always true | reduces redundancy and anomalies |
| drawing many-to-many directly without linking table | implementation missing | use linking table |
| saying data dictionary stores “words” | wrong context | stores metadata |

---

# 11. Scenario Answer Bank 场景迁移答题模板

## Scenario 1: File-based approach limitation

**Question:**  
A shop stores repair data using separate files. Give one limitation and explain how a relational database addresses it.

**Answer template:**

> A file-based approach can cause **data redundancy**, because the same customer details may be stored in several files. A relational database can store customer details once in a CUSTOMER table and link the data to repair records using a **foreign key**, reducing duplication and improving consistency.

---

## Scenario 2: Identify foreign keys

**Question:**  
Given:

```text
SALE(SaleID, BatchID, CustomerID, Quantity, Date)
BATCH(BatchID, Type, Flavour)
CUSTOMER(CustomerID, CompanyName)
```

**Answer template:**

> `BatchID` in `SALE` is a foreign key referencing `BATCH(BatchID)`.  
> `CustomerID` in `SALE` is a foreign key referencing `CUSTOMER(CustomerID)`.

---

## Scenario 3: Many-to-many relationship

**Question:**  
A repair can use many parts. A part can be used in many repairs. Explain how this relationship is implemented.

**Answer template:**

> This is a many-to-many relationship. It can be implemented using a linking table, such as `REPAIR_PART`, which stores `RepairNumber` and `PartID` as foreign keys. These two fields can also form a composite primary key.

---

## Scenario 4: Normalisation benefit

**Question:**  
Explain one benefit of normalisation.

**Answer template:**

> Normalisation reduces data redundancy because repeated data is moved into separate linked tables. This also improves data consistency because a value only needs to be updated in one place.

---

## Scenario 5: Write total SQL query

**Question:**  
Return the total amount due for supplier `JK675` for unpaid invoices.

**Answer template:**

```sql
SELECT SUM(AmountDue)
FROM INVOICE
WHERE SupplierID = 'JK675'
AND Paid = FALSE;
```

---

## Scenario 6: Create linking table SQL

**Question:**  
Write SQL to create `REPAIR_PART(PartID, RepairNumber, Quantity)`.

**Answer template:**

```sql
CREATE TABLE REPAIR_PART (
    PartID VARCHAR(10) NOT NULL,
    RepairNumber VARCHAR(4) NOT NULL,
    Quantity INTEGER,
    PRIMARY KEY (PartID, RepairNumber),
    FOREIGN KEY (PartID) REFERENCES PART(PartID),
    FOREIGN KEY (RepairNumber) REFERENCES REPAIR(RepairNumber)
);
```

---

## Scenario 7: DBMS security

**Question:**  
Explain how a DBMS can protect data.

**Answer template:**

> A DBMS can use usernames and passwords to authenticate users. It can also use access rights so that each user can only read or modify the data they are authorised to access.

---

## Scenario 8: Data dictionary

**Question:**  
Describe the purpose of a data dictionary.

**Answer template:**

> A data dictionary stores metadata about the database, such as table names, field names, data types, primary keys, foreign keys, relationships and validation rules.

---

# 12. Mermaid Process Diagram: From Scenario to SQL

```mermaid
flowchart TD
A[Read scenario] --> B[Identify entities]
B --> C[Convert entities to tables]
C --> D[Choose primary key for each table]
D --> E[Identify relationships]
E --> F{Many-to-many?}
F -- Yes --> G[Create linking table]
F -- No --> H[Place foreign key on many side]
G --> I[Apply referential integrity]
H --> I
I --> J[Write SQL DDL or DML]
J --> K[Check field names, types, conditions]
```

---

# 13. 10 Marks Quick Check

## Questions

1. Define **primary key**. `[1]`
2. Define **foreign key**. `[1]`
3. State what is meant by **referential integrity**. `[1]`
4. Give one limitation of a file-based approach. `[1]`
5. Give one benefit of normalisation. `[1]`
6. State the purpose of a data dictionary. `[1]`
7. Identify a suitable SQL data type for a price such as `22.50`. `[1]`
8. Write the SQL keyword used to sort query results. `[1]`
9. Write the SQL aggregate function used to total values. `[1]`
10. State what `DML` is used for. `[1]`

## Answers

1. An attribute / set of attributes that uniquely identifies each record.
2. An attribute in one table that references the primary key in another table.
3. Foreign key values must match existing primary key values in the referenced table.
4. Data redundancy / inconsistency / difficult access / poor security.
5. Reduces redundancy / improves consistency / avoids anomalies.
6. Stores metadata / data about data.
7. `REAL`.
8. `ORDER BY`.
9. `SUM`.
10. Querying and maintaining data stored in a database.

---

# 14. 20 Marks Exam-Style Practice

## Question

A sports centre uses a relational database to store data about members, classes and class bookings.

The database has the following tables:

```text
MEMBER(MemberID, FirstName, LastName, ContactNumber)

CLASS(ClassID, ClassName, Instructor, Fee)

BOOKING(MemberID, ClassID, BookingDate, Paid)
```

### (a) Define the term **primary key**. `[1]`

### (b) Identify the foreign keys in `BOOKING` and state which table each one references. `[2]`

### (c) Explain why `BOOKING` is needed in this database design. `[3]`

### (d) Write an SQL script to create the table `BOOKING`. Include suitable data types and constraints. `[5]`

### (e) Write an SQL script to return the number of unpaid bookings for the class with `ClassID = 'YOGA01'`. `[3]`

### (f) Explain two benefits of using a relational database instead of a file-based approach. `[4]`

### (g) Describe the purpose of a data dictionary in a DBMS. `[2]`

---

## Mark Scheme

### (a) `[1]`

One mark:

> A primary key uniquely identifies each record in a table.

---

### (b) `[2]`

| Foreign key | References |
| --- | --- |
| `MemberID` | `MEMBER(MemberID)` |
| `ClassID` | `CLASS(ClassID)` |

One mark for each correct foreign key + referenced table.

---

### (c) `[3]`

Award up to 3 marks:

+ `MEMBER` and `CLASS` have a many-to-many relationship.
+ One member can book many classes.
+ One class can be booked by many members.
+ `BOOKING` acts as a linking table.
+ It stores data about each booking, such as `BookingDate` and `Paid`.

Example answer:

> `BOOKING` is needed because a member can book many classes and each class can be booked by many members. This is a many-to-many relationship, so a linking table is used. The linking table also stores data about the relationship, such as the booking date and whether it has been paid.

---

### (d) `[5]`

Example answer:

```sql
CREATE TABLE BOOKING (
    MemberID VARCHAR(6) NOT NULL,
    ClassID VARCHAR(10) NOT NULL,
    BookingDate DATE,
    Paid BOOLEAN,
    PRIMARY KEY (MemberID, ClassID, BookingDate),
    FOREIGN KEY (MemberID) REFERENCES MEMBER(MemberID),
    FOREIGN KEY (ClassID) REFERENCES CLASS(ClassID)
);
```

Award marks:

| Mark | Requirement |
| --- | --- |
| 1 | `CREATE TABLE BOOKING` with brackets |
| 1 | suitable data types for `MemberID`, `ClassID`, `BookingDate`, `Paid` |
| 1 | suitable primary key |
| 1 | foreign key for `MemberID` |
| 1 | foreign key for `ClassID` |

---

### (e) `[3]`

Example answer:

```sql
SELECT COUNT(*)
FROM BOOKING
WHERE ClassID = 'YOGA01'
AND Paid = FALSE;
```

Award marks:

| Mark | Requirement |
| --- | --- |
| 1 | `SELECT COUNT(...) FROM BOOKING` |
| 1 | condition for `ClassID = 'YOGA01'` |
| 1 | condition for unpaid bookings |

---

### (f) `[4]`

Award up to 4 marks:

+ reduces data redundancy
+ because data is stored once in a table
+ improves consistency
+ because updates only need to be made in one place
+ allows relationships between tables using keys
+ improves data integrity through constraints / referential integrity
+ improves security using access rights
+ easier to query related data

Example answer:

> A relational database reduces redundancy because member details can be stored once in the MEMBER table and linked to bookings using `MemberID`. This improves consistency because the member details only need to be updated in one place. It also improves integrity because foreign keys can enforce valid relationships between tables.

---

### (g) `[2]`

Award up to 2 marks:

+ stores metadata / data about data
+ examples: table names, field names, data types, keys, relationships, validation rules

Example answer:

> A data dictionary stores metadata about the database, such as table names, field names, data types, primary keys, foreign keys and validation rules.

---

