# A2 9618 Paper 3 Advanced Theory Review — Set A

> **Original practice paper:** an independent cross-chapter review for Sections 13–20. It does not reproduce official questions or mark schemes.

## Instructions

- Syllabus: **9618, examinations 2027–2029, Version 2**
- Recommended time: **1 hour 30 minutes**
- Total: **75 marks**
- Do not use a calculator.
- Answer all eight questions.
- Use precise technical language and link every explanation to the stated context.
- Attempt the complete paper before reading the indicative marking points.

### Coverage Map

| Question | Section | Marks | AO1 | AO2 |
|---:|---|---:|---:|---:|
| 1 | 13 Data Representation | 10 | 4 | 6 |
| 2 | 14 Communication and Internet Technologies | 9 | 7 | 2 |
| 3 | 15 Hardware and Virtual Machines | 10 | 4 | 6 |
| 4 | 16 System Software | 9 | 7 | 2 |
| 5 | 17 Security | 9 | 6 | 3 |
| 6 | 18 Artificial Intelligence | 9 | 7 | 2 |
| 7 | 19 Computational Thinking and Problem-Solving | 10 | 3 | 7 |
| 8 | 20 Further Programming | 9 | 7 | 2 |
| **Total** | **Sections 13–20** | **75** | **45** | **30** |

---

## Question 1 — Data Representation [10]

A format stores an 8-bit two's-complement mantissa with the binary point immediately after its sign bit, and a 5-bit two's-complement exponent. Value = mantissa × 2^exponent.

1. Represent +6.75 and −6.75 in normalised form. Show the mantissa and exponent for each. **[4]**
2. Explain how to recognise a normalised non-zero mantissa and why normalisation improves the precision available. **[2]**
3. Explain approximation when storing 0.1, overflow, underflow and how repeated arithmetic can accumulate rounding error. Give a distinct explanation for each. **[4]**

---

## Question 2 — Communication [9]

1. State the purpose of the application, transport, internet and link layers in the TCP/IP model. **[4]**
2. Give three differences between circuit switching and packet switching. **[3]**
3. Explain how BitTorrent distributes a file between peers and state one implication of this model. **[2]**

---

## Question 3 — Hardware and Virtual Machines [10]

1. A simulation divides work among several processors. Explain one benefit and one limitation of parallel processing, then give two reasons to run its operating system in a virtual machine. **[4]**
2. A three-input circuit outputs 1 for input values `ABC = 001, 011, 100, 101` and 0 otherwise. Copy and complete this Karnaugh map. **[2]**

   | A \ BC | 00 | 01 | 11 | 10 |
   |---|---:|---:|---:|---:|
   | 0 | | | | |
   | 1 | | | | |

3. Mark the largest valid groups covering all the 1s and derive a minimal sum-of-products expression. Identify the constant variables in each group. **[4]**

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

A binary search tree stores unique integer keys in the global array `Nodes[0:19]`. Each record has integer fields `Key`, `Left` and `Right`; −1 means no child. `Root = -1` and `NextFree = 0` initially. Nodes are allocated consecutively; this task does not delete nodes.

1. Write the complete procedure `InsertKey(BYVAL NewKey : INTEGER, BYREF Inserted : BOOLEAN)`. Reject insertion if the array is full. Otherwise allocate a node, link it into the correct position (including an empty tree), update `NextFree`, and set `Inserted`. Do not call an unspecified insertion helper. Assume the new key is not already present. **[7]**
2. Write recursive `InOrder(Position : INTEGER)` to output the keys in ascending order. Include the empty-subtree case. **[3]**

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

<span id="mark-scheme" class="legacy-anchor" aria-hidden="true"></span>

## Indicative Marking Points

<span id="question-1-mark-scheme-10" class="legacy-anchor" aria-hidden="true"></span>

### Question 1 Indicative Marking Points [10]

1. `6.75 = 110.11₂ = 0.11011₂ × 2³`. Positive mantissa `01101100` **[1]**, exponent `00011` **[1]**. Negate the mantissa using two's complement: `10010100` **[1]**, with the same exponent `00011` **[1]**. The negative mantissa has value −108/128, giving −6.75 after scaling. **[4]**
2. The first two bits differ: `01` for positive and `10` for negative **[1]**; redundant leading sign bits are removed so available positions carry as many significant bits as possible **[1]**. **[2]**
3. 0.1 has a recurring binary expansion and a finite mantissa must approximate it **[1]**; overflow occurs when the result exceeds the representable magnitude/range **[1]**; underflow occurs when a non-zero magnitude is too small for the format's exponent range **[1]**; rounding at successive operations can compound rather than reproduce exact arithmetic **[1]**. **[4]**

<span id="question-2-mark-scheme-9" class="legacy-anchor" aria-hidden="true"></span>

### Question 2 Indicative Marking Points [9]

1. Application: services/protocols used by applications **[1]**; transport: end-to-end delivery, segmentation and reliability/ports **[1]**; internet: logical addressing and routing packets **[1]**; link: local-network framing/media access and physical transfer **[1]**. **[4]**
2. Circuit establishes a dedicated route while packets may take different routes **[1]**; circuit reserves bandwidth while packet switching shares links **[1]**; circuit has predictable order/delay after setup while packets may be delayed, lost or reordered **[1]**. **[3]**
3. Peers download file pieces from other peers and can upload pieces they already hold **[1]**; distribution does not depend on one central file server, although availability depends on peers continuing to share **[1]**. **[2]**

<span id="question-3-mark-scheme-10" class="legacy-anchor" aria-hidden="true"></span>

### Question 3 Indicative Marking Points [10]

1. Independent work can execute simultaneously, reducing elapsed time/increasing throughput **[1]**; serial sections, synchronisation or communication overhead limit the improvement **[1]**. Any two distinct VM uses: isolate the simulation, run a different/legacy OS, restore a test snapshot, or share physical hardware between separate environments **[2]**. **[4]**
2. One mark for each complete row. **[2]**

   | A \ BC | 00 | 01 | 11 | 10 |
   |---|---:|---:|---:|---:|
   | 0 | 0 | 1 | 1 | 0 |
   | 1 | 1 | 1 | 0 | 0 |

3. Group row `A=0`, columns `01` and `11` **[1]**, giving `NOT A AND C` because B varies **[1]**. Group row `A=1`, columns `00` and `01` **[1]**, giving `A AND NOT B` because C varies **[1]**. Combine with OR: `(NOT A AND C) OR (A AND NOT B)`. No valid group of four exists. **[4]**

<span id="question-4-mark-scheme-9" class="legacy-anchor" aria-hidden="true"></span>

### Question 4 Indicative Marking Points [9]

1. FCFS runs processes in arrival order and may make short jobs wait behind a long job **[1]**; round robin gives each ready process a time slice **[1]**; round robin improves responsiveness/fairness but causes context-switch overhead **[1]**. **[3]**
2. Program is divided into fixed-size pages and RAM into frames **[1]**; only required pages are loaded while other pages remain on secondary storage **[1]**; page faults cause required pages to be loaded/replaced, allowing the logical address space to exceed RAM **[1]**. **[3]**
3. Lexical analysis groups source characters into tokens **[1]**; syntax analysis checks the token sequence against the language grammar **[1]**; code generation produces target/object code from the analysed program **[1]**. **[3]**

<span id="question-5-mark-scheme-9" class="legacy-anchor" aria-hidden="true"></span>

### Question 5 Indicative Marking Points [9]

1. Encrypt message with recipient's public key so only the recipient's private key decrypts it **[2]**; sign a digest with sender's private key and verify using sender's public key **[2]**. **[4]**
2. Certificate binds an identity/domain to a public key **[1]**; it is signed by a trusted certificate authority **[1]**; the client verifies the signature/validity before using the key to establish the secure session **[1]**. **[3]**
3. Benefit: eavesdropping can be detected because measurement disturbs the quantum state **[1]**; limitation: specialised equipment, distance/rate constraints or high cost **[1]**. **[2]**

### Question 6 Indicative Marking Points [9]

1. Both find least-cost paths through a weighted graph **[1]**; Dijkstra expands by known distance from the start **[1]**; A* also adds a heuristic estimate to the goal **[1]**; an admissible/useful heuristic can reduce explored nodes while retaining an optimal result **[1]**. **[4]**
2. Output is compared with the target to calculate error **[1]**; error contribution is propagated backwards through layers **[1]**; weights/biases are adjusted to reduce future error, usually using a learning rate/gradient **[1]**. **[3]**
3. Supervised learning trains on labelled input-output examples **[1]**; unsupervised learning finds patterns/clusters in unlabelled data **[1]**. **[2]**

<span id="question-7-mark-scheme-10" class="legacy-anchor" aria-hidden="true"></span>

### Question 7 Indicative Marking Points [10]

1. Full check with false result **[1]**; initialises new key and both child links **[1]**; handles empty root **[1]**; traverses from root and selects left/right by comparison **[2]**; attaches to the correct parent link **[1]**; updates allocation index and success result **[1]**. Equivalent complete algorithms are also valid. **[7]**

```text
PROCEDURE InsertKey(BYVAL NewKey : INTEGER, BYREF Inserted : BOOLEAN)
    DECLARE Current, Parent : INTEGER
    Inserted <- FALSE
    IF NextFree < 20 THEN
        Nodes[NextFree].Key <- NewKey
        Nodes[NextFree].Left <- -1
        Nodes[NextFree].Right <- -1
        IF Root = -1 THEN
            Root <- NextFree
        ELSE
            Current <- Root
            Parent <- -1
            WHILE Current <> -1
                Parent <- Current
                IF NewKey < Nodes[Current].Key THEN
                    Current <- Nodes[Current].Left
                ELSE
                    Current <- Nodes[Current].Right
                ENDIF
            ENDWHILE
            IF NewKey < Nodes[Parent].Key THEN
                Nodes[Parent].Left <- NextFree
            ELSE
                Nodes[Parent].Right <- NextFree
            ENDIF
        ENDIF
        NextFree <- NextFree + 1
        Inserted <- TRUE
    ENDIF
ENDPROCEDURE
```

2. Guards the null index **[1]**; recursive visit of left child before output **[1]**; output followed by recursive visit of right child **[1]**. **[3]**

```text
PROCEDURE InOrder(Position : INTEGER)
    IF Position <> -1 THEN
        CALL InOrder(Nodes[Position].Left)
        OUTPUT Nodes[Position].Key
        CALL InOrder(Nodes[Position].Right)
    ENDIF
ENDPROCEDURE
```

For keys `42, 18, 60, 27`, the traversal is `18, 27, 42, 60`. A call with −1 outputs nothing. A full tree must leave all stored nodes, `Root` and `NextFree` unchanged.

<span id="question-8-mark-scheme-9" class="legacy-anchor" aria-hidden="true"></span>

### Question 8 Indicative Marking Points [9]

1. `LDM #6` **[1]**; `ADD 25` **[1]**; `STO 40` **[1]**. **[3]**
2. `LDI 30` is indirect: address `30` contains the second address used to obtain the value **[1]**. `LDX 30` is indexed: the effective address is `30 + IX` **[1]**. **[2]**
3. `RULE priority(X) IF refrigerated(X)` contains a variable and applies the supplied relationship to any matching parcel **[2]**; `GOAL priority("P17")` **[1]**; the goal is satisfied because the fact matches the rule condition **[1]**. **[4]**

**Total: 75 marks**
