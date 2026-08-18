# AS 9618 Paper 1 Mixed Review — Set A

> **Original practice paper:** independently written for revision. It is not an official Cambridge paper and does not reproduce a past-paper question.

## Instructions

- Syllabus: **9618, examinations 2027–2029, Version 2**
- Recommended time: **1 hour 30 minutes**
- Total: **75 marks**
- Answer all eight questions.
- Show all working and use precise technical language.
- Attempt the complete paper before opening the mark scheme.

### Coverage and assessment objectives

| Question | Section | Marks | AO1 | AO2 |
|---:|---|---:|---:|---:|
| 1 | 1 Information representation | 10 | 6 | 4 |
| 2 | 2 Communication | 9 | 5 | 4 |
| 3 | 3 Hardware | 9 | 5 | 4 |
| 4 | 4 Processor fundamentals | 10 | 6 | 4 |
| 5 | 5 System software | 9 | 5 | 4 |
| 6 | 6 Security, privacy and data integrity | 9 | 6 | 3 |
| 7 | 7 Ethics and ownership | 9 | 6 | 3 |
| 8 | 8 Databases | 10 | 6 | 4 |
| **Total** | **Sections 1–8** | **75** | **45** | **30** |

## Question 1 — Information Representation [10]

A sound library digitises short recordings.

1. Convert hexadecimal `7D3` to denary. **[2]**
2. Represent denary `-37` as an 8-bit two's complement value. **[2]**
3. Explain how sampling resolution and sampling rate affect sound quality and file size. **[4]**
4. State why run-length encoding is unlikely to compress a complex music recording effectively. **[2]**

## Question 2 — Communication [9]

A college connects two buildings using a network.

1. Distinguish between a LAN and a WAN. **[2]**
2. Explain how packet switching allows a file to travel across the network. **[3]**
3. State the purpose of a MAC address and an IP address. **[2]**
4. Give one reason for using fibre-optic cable and one possible limitation. **[2]**

## Question 3 — Hardware [9]

A delivery company equips drivers with mobile terminals.

1. Explain the role of an input device, an output device and secondary storage in this system. Give one suitable example of each. **[3]**
2. Describe how a laser printer produces a page. **[3]**
3. The company chooses solid-state storage. Give two contextual advantages and one contextual disadvantage compared with magnetic storage. **[3]**

## Question 4 — Processor Fundamentals [10]

A processor executes an instruction to add a value from memory to the accumulator.

1. Describe the roles of the PC, MAR, MDR and CIR during the fetch stage. **[4]**
2. Explain the decode and execute stages for this instruction. **[2]**
3. State two factors, other than clock speed, that can affect processor performance. **[2]**
4. Explain how an interrupt can be handled without losing the current program state. **[2]**

## Question 5 — System Software [9]

A programmer creates a utility that converts image files.

1. State three functions of an operating system. **[3]**
2. Distinguish between a compiler and an interpreter. **[2]**
3. Explain the purpose of a linker and a loader. **[2]**
4. State two ways an integrated development environment can help locate a logic error. **[2]**

## Question 6 — Security, Privacy and Data Integrity [9]

A medical appointment system stores personal data.

1. Distinguish between data security, data privacy and data integrity. **[3]**
2. Explain how asymmetric encryption can establish a secure exchange of a symmetric session key. **[3]**
3. Describe one access-control measure and one backup measure that reduce different risks to the data. **[2]**
4. State one limitation of using a checksum to protect data integrity. **[1]**

## Question 7 — Ethics and Ownership [9]

A navigation application collects journey data and recommends routes.

1. Identify two ethical concerns raised by collecting detailed journey data. **[2]**
2. Explain two measures the developer could use to address those concerns. **[4]**
3. Distinguish between copyright and a software licence. **[2]**
4. State one reason why acknowledging an open-source component may still be required. **[1]**

## Question 8 — Databases [10]

The relation below is used before a database is normalised.

`BOOKING(BookingID, CustomerID, CustomerName, EventID, EventName, VenueID, VenueName, SeatNo)`

Each booking is for one event. An event uses one venue. A customer can make many bookings.

1. State the primary key of the unnormalised relation. **[1]**
2. Give three functional dependencies represented by the data. **[3]**
3. Produce a set of relations in Third Normal Form, showing each primary key and foreign key. **[4]**
4. Explain how referential integrity should be enforced when a booking is added. **[2]**

## Mark Scheme

### Question 1 Mark Scheme [10]

1. `7 × 256 + 13 × 16 + 3 = 2003`. Method/place values **[1]**, answer **[1]**. **[2]**
2. `37 = 00100101`; invert and add one to give `11011011`. **[2]**
3. Higher sampling rate records more measurements per second and can represent higher frequencies/more detail **[1]** but stores more samples and increases file size **[1]**. Greater resolution uses more bits per sample, representing amplitude more precisely/reducing quantisation error **[1]** but increases file size **[1]**. **[4]**
4. RLE is effective for long runs of identical values **[1]**; complex audio changes frequently, so runs are short and run metadata may increase size **[1]**. **[2]**

### Question 2 Mark Scheme [9]

1. LAN covers a limited geographic area and is normally owned/managed by one organisation **[1]**; WAN covers a large area and uses third-party telecommunications infrastructure / connects LANs **[1]**. **[2]**
2. File is divided into packets with addressing/sequence/control data **[1]**; routers can forward packets independently along available routes **[1]**; receiver checks and reorders/reassembles them, requesting retransmission if required **[1]**. **[3]**
3. MAC identifies a network interface on the local network **[1]**; IP provides a logical address used for routing between networks **[1]**. **[2]**
4. Benefit: high bandwidth, low attenuation or immunity to electromagnetic interference **[1]**; limitation: higher installation/equipment cost or more difficult repair/termination **[1]**. **[2]**

### Question 3 Mark Scheme [9]

1. One mark for each correct role with a suitable contextual example: input captures data, such as GPS/touch screen; output communicates information, such as screen/speaker; secondary storage retains programs/data without power, such as flash storage. **[3]**
2. Laser/LED creates an electrostatic image on a charged drum **[1]**; toner is attracted to the image and transferred to paper **[1]**; heated pressure rollers fuse toner to the paper **[1]**. **[3]**
3. Two contextual advantages, such as resistance to vehicle vibration, lower power, smaller mass or faster access **[2]**; one disadvantage, such as higher cost per GiB or finite write endurance **[1]**. **[3]**

### Question 4 Mark Scheme [10]

1. PC holds next instruction address **[1]**; address copies to MAR and memory is read **[1]**; instruction returns through MDR **[1]**; instruction copies to CIR and PC is incremented **[1]**. **[4]**
2. Control unit decodes opcode/operand or addressing mode **[1]**; required data is fetched and ALU performs addition, placing result in accumulator **[1]**. **[2]**
3. Any two: number of cores, cache size/level/speed, bus width, word length, instruction-set/architecture efficiency. **[2]**
4. Processor completes the current instruction and saves register/program state **[1]**; runs the interrupt service routine, restores state and resumes the interrupted program **[1]**. **[2]**

### Question 5 Mark Scheme [9]

1. Any three: process scheduling, memory management, peripheral management, file management, security/user management, user interface, platform for applications. **[3]**
2. Compiler translates a complete program and produces object/executable code **[1]**; interpreter translates and executes one statement at a time without producing a standalone executable **[1]**. **[2]**
3. Linker combines object modules/libraries and resolves references **[1]**; loader places executable code/data in memory and prepares execution **[1]**. **[2]**
4. Any two: breakpoints, single stepping, watch expressions, variable inspection, trace/output window. **[2]**

### Question 6 Mark Scheme [9]

1. Security protects data from unauthorised access/damage **[1]**; privacy controls lawful/appropriate collection and use of personal data **[1]**; integrity means data remains accurate, complete and unaltered except by authorised action **[1]**. **[3]**
2. Recipient publishes public key **[1]**; sender encrypts the session key using that public key **[1]**; only the matching private key can decrypt it, after which the faster symmetric key protects the session **[1]**. **[3]**
3. One explained access control, such as role-based least privilege or multi-factor authentication **[1]**; one backup measure, such as encrypted offline/versioned copies with restoration tests **[1]**. **[2]**
4. Different corruptions can produce the same checksum / a checksum does not stop deliberate alteration / it detects but does not correct an error. **[1]**

### Question 7 Mark Scheme [9]

1. Any two: continuous location surveillance, use beyond original purpose, sharing/sale, re-identification, unfair route decisions, data breach risk. **[2]**
2. Two explained measures, two marks each: data minimisation, informed granular consent, short retention, aggregation/anonymisation with limitations considered, access/deletion controls, transparent purpose, security controls. **[4]**
3. Copyright gives the creator legal rights over copying/distribution/adaptation **[1]**; a licence states the permissions and conditions under which another person may use the software **[1]**. **[2]**
4. The component's licence may require attribution or preservation of notices. **[1]**

### Question 8 Mark Scheme [10]

1. `BookingID`. **[1]**
2. Any three valid dependencies: `BookingID → CustomerID, EventID, SeatNo`; `CustomerID → CustomerName`; `EventID → EventName, VenueID`; `VenueID → VenueName`. **[3]**
3. One mark for each correct relation with keys indicated: `CUSTOMER(CustomerID PK, CustomerName)`; `VENUE(VenueID PK, VenueName)`; `EVENT(EventID PK, EventName, VenueID FK)`; `BOOKING(BookingID PK, CustomerID FK, EventID FK, SeatNo)`. **[4]**
4. The supplied `CustomerID` and `EventID` must already exist as referenced primary-key values **[1]**; the DBMS rejects the insert or requires a valid referenced record, preventing orphan rows **[1]**. **[2]**
