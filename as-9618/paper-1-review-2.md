# AS 9618 Paper 1 Mixed Review — Set B

> **Original practice paper:** an independent second set with new scenarios, data and question combinations.

## Instructions

- Syllabus: **9618, examinations 2027–2029, Version 2**
- Recommended time: **1 hour 30 minutes**
- Total: **75 marks**
- Do not use a calculator.
- Answer all eight questions.
- Show working and develop explanations in the context given.

### Coverage and assessment objectives

| Question | Section | Marks | AO1 | AO2 |
|---:|---|---:|---:|---:|
| 1 | 1 Information representation | 9 | 6 | 3 |
| 2 | 2 Communication | 9 | 5 | 4 |
| 3 | 3 Hardware | 10 | 6 | 4 |
| 4 | 4 Processor fundamentals | 9 | 5 | 4 |
| 5 | 5 System software | 9 | 5 | 4 |
| 6 | 6 Security, privacy and data integrity | 9 | 6 | 3 |
| 7 | 7 Ethics and ownership | 10 | 6 | 4 |
| 8 | 8 Databases | 10 | 6 | 4 |
| **Total** | **Sections 1–8** | **75** | **45** | **30** |

## Question 1 — Information Representation [9]

1. Convert denary `-52` to 8-bit two's complement. **[2]**
2. Subtract binary `00110101` from `10010110`, giving an 8-bit binary result. **[2]**
3. A bitmap is `800 × 600` pixels with 24-bit colour. Calculate its uncompressed size in MiB using binary prefixes. **[3]**
4. Explain one reason to choose vector graphics for a logo and one reason not to use lossy compression for source program text. **[2]**

## Question 2 — Communication [9]

A research station sends data to a city laboratory.

1. Explain why client-server networking is appropriate for centrally managed user accounts. **[2]**
2. Compare circuit switching and packet switching when the station sends data to the laboratory. **[3]**
3. Describe how a router uses an IP address and a routing table to forward a packet. **[2]**
4. Give one benefit and one limitation of using satellite communication at the remote station. **[2]**

## Question 3 — Hardware [10]

1. Describe how a microphone converts speech into data that can be stored by a computer. **[3]**
2. Describe how a solid-state drive stores and retrieves a bit using a floating-gate transistor. **[3]**
3. A simulator uses a VR headset. Explain how stereoscopic displays and motion tracking create an updated view. **[3]**
4. State the purpose of a buffer when data is sent to an output device. **[1]**

## Question 4 — Processor Fundamentals [9]

1. Explain the role of the status register after a comparison instruction. **[2]**
2. Write one instruction to load immediate value `18` and one to store the accumulator at address `42`. **[2]**
3. After a compare, explain how `JPE` and `JPN` select different control-flow paths. **[2]**
4. A new monitor accepts HDMI and VGA. Explain which port should be selected for digital video and audio, and why VGA is unsuitable for this requirement. **[3]**

## Question 5 — System Software [9]

1. Explain how backup software and disk defragmentation software perform different utility tasks. **[3]**
2. Explain how a program library and a dynamically linked library (DLL) can support application development and execution. **[3]**
3. Explain why Java is described as partially compiled and partially interpreted/executed by a virtual machine. **[3]**

## Question 6 — Security, Privacy and Data Integrity [9]

An examination centre transfers candidate records between two authorised offices.

1. State two differences between validation and verification. **[2]**
2. Explain how a check digit can detect an incorrectly entered candidate number. **[2]**
3. Explain how access rights, encryption and versioned backups protect against three different risks. **[3]**
4. State one privacy principle for collecting candidate data and explain its use. **[2]**

## Question 7 — Ethics and Ownership [10]

A recruitment system ranks applicants using a machine-learning model.

1. Explain two ways biased training data could create an unfair outcome. **[4]**
2. Explain two controls that would make use of the ranking more accountable. **[4]**
3. Distinguish between free software and freeware. **[2]**

## Question 8 — Databases [10]

The database contains `MEMBER(MemberID, Name, Region)` and `LOAN(LoanID, MemberID, ItemID, LoanDate, Returned)`.

1. Identify the primary key and foreign key in `LOAN`. **[2]**
2. Explain how an index on `MemberID` can improve a query and state one cost of maintaining it. **[2]**
3. Write SQL to display `LoanID` and `LoanDate` for unreturned loans by member `M104`, newest date first. **[4]**
4. Explain how referential integrity applies when a `LOAN` row is inserted. **[2]**

## Mark Scheme

### Question 1 Mark Scheme [9]

1. `52 = 00110100`; invert/add one gives `11001100`. **[2]**
2. `10010110 - 00110101 = 01100001`; correct binary subtraction method **[1]**, answer **[1]**. **[2]**
3. `800 × 600 × 24 = 11 520 000` bits **[1]**; `÷ 8 = 1 440 000` bytes **[1]**; `÷ 1 048 576 ≈ 1.37 MiB` **[1]**. **[3]**
4. Vector shapes scale without pixelation / usually suit simple geometric logos **[1]**; lossy compression could remove/change source characters so the exact program cannot be reconstructed **[1]**. **[2]**

### Question 2 Mark Scheme [9]

1. Server centrally stores/authenticates account data **[1]**, so policies, permissions and backups can be applied consistently to clients **[1]**. **[2]**
2. Circuit switching reserves one end-to-end communication path for the session **[1]**; packet switching divides data into addressed packets that may use different routes **[1]**; packet switching shares network capacity efficiently, whereas a reserved circuit gives predictable capacity but may be idle **[1]**. **[3]**
3. Router reads destination IP **[1]** and uses the routing table/next-hop entry to select an outgoing interface **[1]**. **[2]**
4. Benefit such as coverage where cables are unavailable **[1]**; limitation such as high latency, weather interference or cost **[1]**. **[2]**

### Question 3 Mark Scheme [10]

1. Sound vibrates a diaphragm **[1]**; transducer converts movement into a varying analogue electrical signal **[1]**; ADC samples/quantises it into digital data **[1]**. **[3]**
2. Charge is trapped or removed from a floating gate **[1]**; stored charge changes transistor threshold/conductivity to represent a bit state **[1]**; controller senses that state when reading **[1]**. **[3]**
3. Slightly different images are shown to each eye to produce depth **[1]**; sensors track head position/orientation **[1]**; processor renders a new viewpoint with low delay **[1]**. **[3]**
4. Temporarily holds data to compensate for different producer/device transfer rates. **[1]**

### Question 4 Mark Scheme [9]

1. It stores condition flags as bits **[1]**; flags record the comparison result for a later conditional jump **[1]**. **[2]**
2. `LDM #18` **[1]**; `STO 42` **[1]**. **[2]**
3. `JPE` jumps when the previous comparison is true/equal **[1]**; `JPN` jumps when it is false/not equal **[1]**. **[2]**
4. Select HDMI because it carries digital video and digital audio **[2]**; VGA carries analogue video only and therefore cannot carry the required audio **[1]**. **[3]**

### Question 5 Mark Scheme [9]

1. Backup software copies selected data so it can be restored after loss or corruption **[1]**; disk defragmentation software rearranges file fragments into contiguous blocks on a magnetic disk **[1]**; this reduces head movement and can improve access speed **[1]**. **[3]**
2. A program library supplies pre-written, tested routines that can be reused rather than rewritten **[1]**; a DLL is linked/loaded when the program runs instead of being copied into every executable **[1]**; one shared DLL can therefore reduce duplicated storage or be updated independently for applications that use its compatible interface **[1]**. **[3]**
3. Java source is compiled to platform-independent bytecode **[1]**; the JVM interprets/executes or just-in-time compiles bytecode **[1]**; the same bytecode can run where a compatible JVM exists **[1]**. **[3]**

### Question 6 Mark Scheme [9]

1. Validation checks acceptability/rules while verification checks accurate transfer/entry **[1]**; validation can reject an invalid format/range but cannot prove a plausible value is correct, whereas verification compares with the source/second entry **[1]**. **[2]**
2. A calculation is applied to number digits and a check digit is stored **[1]**; entry is recalculated and mismatch indicates an error **[1]**. **[2]**
3. Access rights restrict which authorised role can read/change records **[1]**; encryption protects confidentiality if data is intercepted/stolen **[1]**; versioned backups restore data after deletion or corruption **[1]**. **[3]**
4. One explained principle: collect only necessary data, use it only for stated purpose, keep it only as long as needed, keep it accurate, or secure it. **[2]**

### Question 7 Mark Scheme [10]

1. Two developed effects, two marks each: under-represented groups may have less accurate patterns **[1]** causing qualified applicants to be ranked lower **[1]**; historic biased decisions can be learned **[1]** and repeated at scale **[1]**. **[4]**
2. Two developed controls, two marks each: test outcomes/error rates by relevant group and retrain when disparities appear; document data/model limits; provide human review and an appeal; log reasons/version; do not use protected attributes or close proxies without justification. **[4]**
3. Free software gives freedoms to inspect, modify and redistribute source under its licence **[1]**; freeware is available without payment but may remain closed-source/restrict modification **[1]**. **[2]**

### Question 8 Mark Scheme [10]

1. Primary key `LoanID` **[1]**; foreign key `MemberID` referencing `MEMBER.MemberID` **[1]**. **[2]**
2. Key/pointer index locates matching rows without scanning every row **[1]**; it uses storage and must be updated when indexed values/rows change **[1]**. **[2]**
3.

   ```sql
   SELECT LoanID, LoanDate
   FROM LOAN
   WHERE MemberID = 'M104' AND Returned = FALSE
   ORDER BY LoanDate DESC;
   ```

   Correct fields/table **[1]**; member condition **[1]**; returned condition joined by `AND` **[1]**; descending date order **[1]**. **[4]**
4. The inserted `MemberID` must match an existing primary-key value in `MEMBER` **[1]**; otherwise the DBMS rejects the row/prevents an orphan record **[1]**. **[2]**
