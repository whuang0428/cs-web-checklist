# A2 9618 Paper 3 Advanced Theory Review — Set A

> **Original practice paper:** an independent cross-chapter review for Sections 13–20. It does not reproduce official questions or mark schemes.

## Instructions

- Syllabus: **9618, examinations 2027–2029, Version 2**
- Recommended time: **1 hour 30 minutes**
- Total: **75 marks**
- Do not use a calculator.
- Answer all eight questions.
- Use precise technical language and link every explanation to the stated context.
- Attempt the complete paper before reading the mark scheme.

### Coverage Map

| Question | Section | Marks | AO1 | AO2 |
|---:|---|---:|---:|---:|
| 1 | 13 Data Representation | 10 | 6 | 4 |
| 2 | 14 Communication and Internet Technologies | 9 | 5 | 4 |
| 3 | 15 Hardware and Virtual Machines | 10 | 6 | 4 |
| 4 | 16 System Software | 9 | 5 | 4 |
| 5 | 17 Security | 9 | 5 | 4 |
| 6 | 18 Artificial Intelligence | 9 | 5 | 4 |
| 7 | 19 Computational Thinking and Problem-Solving | 10 | 7 | 3 |
| 8 | 20 Further Programming | 9 | 6 | 3 |
| **Total** | **Sections 13–20** | **75** | **45** | **30** |

---

## Question 1 — Data Representation [10]

1. Distinguish an enumerated type, a record type and a pointer type. **[3]**
2. Compare serial, sequential and random file organisation in terms of record order and access. **[3]**
3. Explain four reasons why storing a real number in a fixed-size floating-point representation can produce an inaccurate result. **[4]**

---

## Question 2 — Communication [9]

1. State the purpose of the application, transport, internet and link layers in the TCP/IP model. **[4]**
2. Give three differences between circuit switching and packet switching. **[3]**
3. Explain how BitTorrent distributes a file between peers and state one implication of this model. **[2]**

---

## Question 3 — Hardware and Virtual Machines [10]

1. Explain two benefits and two limitations of parallel processing. **[4]**
2. Explain three reasons for using a virtual machine. **[3]**
3. Simplify the Boolean expression `(A AND B) OR (A AND NOT B)` and show the two algebraic steps used. **[3]**

---

## Question 4 — System Software [9]

1. Compare first-come-first-served and round-robin process scheduling. **[3]**
2. Explain how paging and virtual memory allow a program larger than available RAM to execute. **[3]**
3. Describe the purpose of lexical analysis, syntax analysis and code generation during compilation. **[3]**

---

## Question 5 — Security [9]

1. Explain how asymmetric cryptography can provide confidentiality and authenticate the sender of a message. **[4]**
2. Explain the role of a digital certificate when establishing a TLS connection. **[3]**
3. Give one benefit and one limitation of quantum cryptography. **[2]**

---

## Question 6 — Artificial Intelligence [9]

1. Compare Dijkstra's algorithm and A* search, including the role of a heuristic. **[4]**
2. Explain how backpropagation changes an artificial neural network during training. **[3]**
3. Distinguish supervised and unsupervised learning. **[2]**

---

## Question 7 — Algorithms and Recursion [10]

1. State the precondition for binary search and explain why its time complexity is `O(log n)`. **[3]**
2. Explain why insertion sort can perform well on a nearly sorted list. **[2]**
3. A binary search tree is built by inserting already sorted keys. Explain the resulting shape and its effect on search complexity. **[3]**
4. State the purpose of the base case and call-stack unwinding in recursion. **[2]**

---

## Question 8 — Further Programming [9]

Use the low-level instruction set and the declarative notation shown in the question.

1. Write three low-level instructions to load the immediate value `6`, add the value stored at address `25`, and store the result at address `40`. **[3]**
2. Identify the addressing modes used by `LDI 30` and `LDX 30`, and explain how each effective address is obtained. **[2]**
3. The fact `FACT refrigerated("P17")` is supplied. Using `RULE ... IF ...` and `GOAL ...` notation:
   - write a rule stating that every refrigerated parcel is priority **[2]**
   - write a goal asking whether `P17` is priority **[1]**
   - state whether the goal is satisfied **[1]**

---

## Mark Scheme

### Question 1 Mark Scheme [10]

1. Enumerated: a fixed named set of allowed values **[1]**; record: related fields, possibly of different types, grouped into one item **[1]**; pointer: stores/references a memory address or another data item **[1]**. **[3]**
2. Serial: records in arrival order, normally scanned **[1]**; sequential: records stored in key order and processed in that order **[1]**; random: record location is calculated from a key so earlier records need not be read **[1]**. **[3]**
3. Any four: finite mantissa bits; finite exponent range; rounding/truncation of excess bits; many decimal fractions have no finite binary representation; overflow/underflow; accumulated rounding error during repeated operations. **[4]**

### Question 2 Mark Scheme [9]

1. Application: services/protocols used by applications **[1]**; transport: end-to-end delivery, segmentation and reliability/ports **[1]**; internet: logical addressing and routing packets **[1]**; link: local-network framing/media access and physical transfer **[1]**. **[4]**
2. Circuit establishes a dedicated route while packets may take different routes **[1]**; circuit reserves bandwidth while packet switching shares links **[1]**; circuit has predictable order/delay after setup while packets may be delayed, lost or reordered **[1]**. **[3]**
3. Peers download file pieces from other peers and can upload pieces they already hold **[1]**; distribution does not depend on one central file server, although availability depends on peers continuing to share **[1]**. **[2]**

### Question 3 Mark Scheme [10]

1. Benefits: reduced execution time and/or greater throughput, multiple tasks/data items processed together **[2]**. Limitations: problem may not be divisible, communication/synchronisation overhead, serial sections, extra hardware/cost or race conditions **[2]**. **[4]**
2. Any three: run another operating system; isolate applications; consolidate servers; test safely; support legacy software; allocate resources flexibly; create repeatable environments. **[3]**
3. Factor `A`: `A AND (B OR NOT B)` **[1]**; complement law gives `B OR NOT B = 1` **[1]**; identity law gives `A AND 1 = A` **[1]**. **[3]**

### Question 4 Mark Scheme [9]

1. FCFS runs processes in arrival order and may make short jobs wait behind a long job **[1]**; round robin gives each ready process a time slice **[1]**; round robin improves responsiveness/fairness but causes context-switch overhead **[1]**. **[3]**
2. Program is divided into fixed-size pages and RAM into frames **[1]**; only required pages are loaded while other pages remain on secondary storage **[1]**; page faults cause required pages to be loaded/replaced, allowing the logical address space to exceed RAM **[1]**. **[3]**
3. Lexical analysis groups source characters into tokens **[1]**; syntax analysis checks the token sequence against the language grammar **[1]**; code generation produces target/object code from the analysed program **[1]**. **[3]**

### Question 5 Mark Scheme [9]

1. Encrypt message with recipient's public key so only the recipient's private key decrypts it **[2]**; sign a digest with sender's private key and verify using sender's public key **[2]**. **[4]**
2. Certificate binds an identity/domain to a public key **[1]**; it is signed by a trusted certificate authority **[1]**; the client verifies the signature/validity before using the key to establish the secure session **[1]**. **[3]**
3. Benefit: eavesdropping can be detected because measurement disturbs the quantum state **[1]**; limitation: specialised equipment, distance/rate constraints or high cost **[1]**. **[2]**

### Question 6 Mark Scheme [9]

1. Both find least-cost paths through a weighted graph **[1]**; Dijkstra expands by known distance from the start **[1]**; A* also adds a heuristic estimate to the goal **[1]**; an admissible/useful heuristic can reduce explored nodes while retaining an optimal result **[1]**. **[4]**
2. Output is compared with the target to calculate error **[1]**; error contribution is propagated backwards through layers **[1]**; weights/biases are adjusted to reduce future error, usually using a learning rate/gradient **[1]**. **[3]**
3. Supervised learning trains on labelled input-output examples **[1]**; unsupervised learning finds patterns/clusters in unlabelled data **[1]**. **[2]**

### Question 7 Mark Scheme [10]

1. Data is sorted using the search key **[1]**; each comparison removes approximately half the remaining items **[1]**; therefore comparison count grows with the number of halvings, `O(log n)` **[1]**. **[3]**
2. The sorted section needs only a few comparisons/shifts for each new item **[1]**, so behaviour can approach `O(n)` **[1]**. **[2]**
3. Sorted insertion produces a skewed chain with each node on the same side **[1]**; tree height becomes `n` **[1]**; search degrades from average `O(log n)` to worst-case `O(n)` **[1]**. **[3]**
4. Base case terminates recursion without another call **[1]**; unwinding pops saved call frames in reverse order and combines/returns results **[1]**. **[2]**

### Question 8 Mark Scheme [9]

1. `LDM #6` **[1]**; `ADD 25` **[1]**; `STO 40` **[1]**. **[3]**
2. `LDI 30` is indirect: address `30` contains the second address used to obtain the value **[1]**. `LDX 30` is indexed: the effective address is `30 + IX` **[1]**. **[2]**
3. `RULE priority(X) IF refrigerated(X)` contains a variable and applies the supplied relationship to any matching parcel **[2]**; `GOAL priority("P17")` **[1]**; the goal is satisfied because the fact matches the rule condition **[1]**. **[4]**

**Total: 75 marks**
