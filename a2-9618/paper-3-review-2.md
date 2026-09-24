# A2 9618 Paper 3 Advanced Theory Review — Set B

> **Original practice paper:** an independent second set for Sections 13–20. It uses new contexts and does not reproduce official questions, mark schemes or Set A scenarios.

## Instructions

- Syllabus: **9618, examinations 2027–2029, Version 2**
- Recommended time: **1 hour 30 minutes**
- Total: **75 marks**
- Do not use a calculator.
- Answer all eight questions.
- Show every Boolean and floating-point step that is required.
- Attempt the complete paper before opening the indicative marking points.

### Coverage and assessment objectives

| Question | Section | Marks | AO1 | AO2 |
|---:|---|---:|---:|---:|
| 1 | 13 Data representation | 9 | 4 | 5 |
| 2 | 14 Communication and internet technologies | 10 | 8 | 2 |
| 3 | 15 Hardware and virtual machines | 9 | 3 | 6 |
| 4 | 16 System software | 10 | 8 | 2 |
| 5 | 17 Security | 9 | 7 | 2 |
| 6 | 18 Artificial intelligence | 10 | 8 | 2 |
| 7 | 19 Computational thinking and problem-solving | 9 | 0 | 9 |
| 8 | 20 Further programming | 9 | 7 | 2 |
| **Total** | **Sections 13–20** | **75** | **45** | **30** |

## Question 1 — Scientific Data [9]

A satellite uses an 8-bit two's-complement mantissa (binary point after the sign bit) and a 5-bit two's-complement exponent. A stored value has mantissa `11101000` and exponent `00101`.

1. Calculate the denary value and then normalise the representation without changing that value. Show the new mantissa and exponent. **[4]**
2. The 13-bit format is redesigned with a 10-bit mantissa and a 3-bit exponent. Explain the effects on precision and range. **[2]**
3. Compare random and sequential file organisation for retrieving one named satellite record and processing every record in key order. **[3]**

## Question 2 — Resilient Communication [10]

A live translation service streams audio between users in different countries.

1. Explain the different responsibilities of TCP and IP. **[3]**
2. Describe how a router uses a routing table when forwarding a packet. **[2]**
3. Compare POP3 and IMAP for a user who reads the same mailbox on several devices. **[3]**
4. State one advantage and one disadvantage of packet switching for this service. **[2]**

## Question 3 — Parallel Rendering [9]

A studio uses virtual machines on a multicore server to render animation frames.

1. Explain why separate frames can benefit from parallel processing and give one factor limiting the speed-up. **[3]**
2. A four-input control circuit has the following Karnaugh map. Derive a minimal sum-of-products expression, identifying each group and the variables removed. Explain the wrap-around adjacency used. **[6]**

   | AB \ CD | 00 | 01 | 11 | 10 |
   |---|---:|---:|---:|---:|
   | 00 | 1 | 0 | 0 | 1 |
   | 01 | 0 | 0 | 0 | 0 |
   | 11 | 0 | 1 | 1 | 0 |
   | 10 | 1 | 0 | 0 | 1 |

## Question 4 — Memory and Scheduling [10]

A server runs many short interactive requests and one long report task.

1. Explain why round-robin scheduling may be more responsive than first-come-first-served in this situation. **[3]**
2. Explain the effect of choosing a time slice that is extremely short. **[2]**
3. Describe how a page table supports virtual memory address translation. **[3]**
4. Distinguish a page fault from disk thrashing. **[2]**

## Question 5 — Trusted Update [9]

A manufacturer distributes a software update over a public network.

1. Explain how a cryptographic hash supports an integrity check. **[2]**
2. Describe how a digital signature lets a device verify the update's origin and integrity. **[3]**
3. Explain two checks the device should perform on the signer's digital certificate. **[2]**
4. Describe how the manufacturer obtains its digital certificate from a Certificate Authority before the certificate is used. **[2]**

## Question 6 — Intelligent Crop System [10]

A system classifies leaf images and recommends treatment.

1. Explain how reinforcement learning uses rewards and penalties, and state what a regression method predicts. **[3]**
2. Explain the roles of weights, an activation function and backpropagation in an artificial neural network. **[3]**
3. Compare supervised and unsupervised learning for the crop data. **[2]**
4. Explain why deep learning is suitable for identifying complex features in leaf images. **[2]**

## Question 7 — Choosing Algorithms [9]

A warehouse stores unique integer product codes in an array-based linked list. Global arrays `Data[0:5]` and `Link[0:5]` hold values and next indexes. `Head` identifies the active list, `Free` identifies the free list, and −1 terminates either list. The active and free lists together contain every array position exactly once.

1. Write complete pseudocode for `RemoveKey(BYVAL Target : INTEGER, BYREF Removed : BOOLEAN)`. Search the active list; return false without changing either list if absent. Otherwise unlink the matching node, return it to the front of the free list and return true. Handle deletion of the head and of the only active node. **[7]**
2. Initially `Head=2`, `Free=0`, `Data=[0, 50, 20, 0, 35, 0]` and `Link=[3, -1, 4, 5, 1, -1]`. Trace removal of 20, then removal of 50. Give `Head`, `Free` and the active chain after each call. **[2]**

## Question 8 — Program Design [9]

A booking system contains several ticket classes and imports booking records from files.

1. Explain how inheritance and method overriding can support different ticket-price rules. **[3]**
2. Explain why composition may be preferable to inheritance for representing the tickets contained in an order. **[2]**
3. Using `LDM`, `STO` and `JPE`, write the three low-level instructions needed to load the immediate value `12`, store it at address `40`, and jump to label `MATCH` when the preceding comparison was true. **[3]**
4. State why file resources should be closed even when an exception occurs. **[1]**

<span id="mark-scheme" class="legacy-anchor" aria-hidden="true"></span>

## Indicative Marking Points

<span id="question-1-mark-scheme-9" class="legacy-anchor" aria-hidden="true"></span>

### Question 1 Indicative Marking Points [9]

1. Mantissa = −24/128 = −0.1875 **[1]**; exponent = 5, so the value is −6 **[1]**. Normalised mantissa `10100000` = −0.75 **[1]**; exponent `00011` = 3 **[1]**. Two left shifts remove redundant sign bits, so decrease the exponent by two. **[4]**
2. More mantissa bits allow finer distinctions/more significant bits **[1]**; fewer exponent bits reduce the range of magnitudes, making overflow/underflow more likely **[1]**. **[2]**
3. Random organisation calculates a location from the key, supporting direct retrieval **[1]**; sequential organisation stores records in key order for ordered batch processing **[1]**; a sequential search may read preceding records before finding one target **[1]**. **[3]**

<span id="question-2-mark-scheme-10" class="legacy-anchor" aria-hidden="true"></span>

### Question 2 Indicative Marking Points [10]

1. TCP provides end-to-end connection, segmentation/reassembly, ordering, error recovery and flow control **[2]**; IP provides logical addressing and routes datagrams between networks without guaranteeing delivery **[1]**. **[3]**
2. Router reads destination IP address and matches it to the most specific route **[1]**; forwards packet through the indicated next hop/interface, or uses a default route **[1]**. **[2]**
3. POP3 downloads messages to a client and may remove the server copy **[1]**; IMAP keeps messages and folders on the server and synchronises their state **[1]**; IMAP is therefore more suitable when read/unread state and folders must remain consistent across devices **[1]**. **[3]**
4. Advantage: shared routes can adapt to failure/congestion or use capacity efficiently **[1]**; disadvantage: variable delay, loss or reordering can interrupt real-time audio **[1]**. **[2]**

<span id="question-3-mark-scheme-9" class="legacy-anchor" aria-hidden="true"></span>

### Question 3 Indicative Marking Points [9]

1. Different frames are largely independent **[1]**, so cores can compute them simultaneously **[1]**. One limit: serial work, communication/synchronisation overhead, shared-resource contention or uneven task sizes **[1]**. **[3]**
2. Group the four corner cells **[1]**; A and C vary, leaving `NOT B AND NOT D` **[1]**. Group row `AB=11`, columns `01` and `11` **[1]**; C varies, leaving `A AND B AND D` **[1]**. The complete expression is `(NOT B AND NOT D) OR (A AND B AND D)` **[1]**. In Gray-code order, first/last rows and first/last columns differ in only one variable and are adjacent across the edges **[1]**. **[6]**

<span id="question-4-mark-scheme-10" class="legacy-anchor" aria-hidden="true"></span>

### Question 4 Indicative Marking Points [10]

1. Each ready request receives a time slice **[1]**; short requests need not wait for the whole report **[1]**; users receive earlier responses/fairer access, although the report is repeatedly pre-empted **[1]**. **[3]**
2. More frequent context switches consume processor time saving/restoring state **[1]**, reducing useful throughput **[1]**. **[2]**
3. Virtual address is split into page number and offset **[1]**; page number indexes the page table to find a frame or not-present flag **[1]**; frame address plus offset gives the physical address **[1]**. **[3]**
4. Page fault occurs when one referenced page is not in RAM and must be loaded **[1]**; thrashing is sustained excessive page swapping, leaving little time for useful execution **[1]**. **[2]**

<span id="question-5-mark-scheme-9" class="legacy-anchor" aria-hidden="true"></span>

### Question 5 Indicative Marking Points [9]

1. Sender publishes a digest produced from the update **[1]**; device hashes the received update and unequal digests reveal alteration/corruption **[1]**. **[2]**
2. Manufacturer signs the update digest with its private key **[1]**; device uses the manufacturer's public key to verify the signature **[1]**; a valid result links the signer to an unchanged digest/update **[1]**. **[3]**
3. Any two: certificate-authority signature/chain, correct subject/domain/identity, validity dates, revocation status, permitted key use. **[2]**
4. The manufacturer sends identity details and its public key in a certificate request **[1]**; the CA verifies the identity and issues/signs a certificate binding that identity to the public key **[1]**. **[2]**

<span id="question-6-mark-scheme-10" class="legacy-anchor" aria-hidden="true"></span>

### Question 6 Indicative Marking Points [10]

1. An agent receives a reward for a desirable action **[1]** and a penalty / lower reward for an undesirable action, then adjusts its policy to maximise future reward **[1]**; regression predicts a continuous numerical value from input variables **[1]**. **[3]**
2. Weights scale connections/signals **[1]**; activation function transforms a neuron's combined input/output and can add non-linearity **[1]**; backpropagation propagates error gradients backwards to update weights/biases **[1]**. **[3]**
3. Supervised learning uses labelled examples with known target outputs **[1]**; unsupervised learning uses unlabelled data to discover groups or patterns **[1]**. **[2]**
4. Multiple hidden layers can learn successive/hierarchical features **[1]**, allowing complex image patterns to be represented and classified **[1]**. **[2]**

### Question 7 Indicative Marking Points [9]

1. Initialises current/previous and false result **[1]**; follows links and stops at a match/end without indexing −1 **[2]**; handles absent key without mutation **[1]**; unlinks head or predecessor link correctly **[1]**; returns node to free list in the correct order **[1]**; sets true result **[1]**. **[7]**

```text
PROCEDURE RemoveKey(BYVAL Target : INTEGER, BYREF Removed : BOOLEAN)
    DECLARE Current, Previous : INTEGER
    DECLARE Found : BOOLEAN
    Current <- Head
    Previous <- -1
    Found <- FALSE
    Removed <- FALSE
    WHILE Current <> -1 AND Found = FALSE
        IF Data[Current] = Target THEN
            Found <- TRUE
        ELSE
            Previous <- Current
            Current <- Link[Current]
        ENDIF
    ENDWHILE
    IF Found = TRUE THEN
        IF Previous = -1 THEN
            Head <- Link[Current]
        ELSE
            Link[Previous] <- Link[Current]
        ENDIF
        Link[Current] <- Free
        Free <- Current
        Removed <- TRUE
    ENDIF
ENDPROCEDURE
```

2. Remove 20: `Head=4`, `Free=2`, active chain `4→1→−1` (35, 50) **[1]**. Remove 50: `Head=4`, `Free=1`, active chain `4→−1` (35) **[1]**. Final free chain: `1→2→0→3→5→−1`. **[2]**

<span id="question-8-mark-scheme-9" class="legacy-anchor" aria-hidden="true"></span>

### Question 8 Indicative Marking Points [9]

1. Common ticket state/behaviour is defined in a superclass **[1]**; subclasses inherit it and override a price method **[1]**; polymorphic calls select the correct rule for the actual ticket object **[1]**. **[3]**
2. An order **has** a collection of tickets rather than being a kind of ticket **[1]**; composition allows different ticket objects to be added/removed without forcing an invalid class hierarchy **[1]**. **[2]**
3. `LDM #12` **[1]**; `STO 40` **[1]**; `JPE MATCH` **[1]**. **[3]**
4. Closing releases the file handle/lock and ensures buffered data is flushed; use a `finally` block or context manager. **[1]**
