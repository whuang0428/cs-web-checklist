# A2 9618 Paper 3 Advanced Theory Review — Set B

> **Original practice paper:** an independent second set for Sections 13–20. It uses new contexts and does not reproduce official questions, mark schemes or Set A scenarios.

## Instructions

- Syllabus: **9618, examinations 2027–2029, Version 2**
- Recommended time: **1 hour 30 minutes**
- Total: **75 marks**
- Answer all eight questions.
- Show every Boolean and floating-point step that is required.
- Attempt the complete paper before opening the mark scheme.

### Coverage and assessment objectives

| Question | Section | Marks | AO1 | AO2 |
|---:|---|---:|---:|---:|
| 1 | 13 Data representation | 9 | 5 | 4 |
| 2 | 14 Communication and internet technologies | 10 | 6 | 4 |
| 3 | 15 Hardware and virtual machines | 9 | 5 | 4 |
| 4 | 16 System software | 10 | 6 | 4 |
| 5 | 17 Security | 9 | 5 | 4 |
| 6 | 18 Artificial intelligence | 10 | 6 | 4 |
| 7 | 19 Computational thinking and problem-solving | 9 | 6 | 3 |
| 8 | 20 Further programming | 9 | 6 | 3 |
| **Total** | **Sections 13–20** | **75** | **45** | **30** |

## Question 1 — Scientific Data [9]

A satellite stores signed sensor readings using normalised floating-point values.

1. State the purpose of the mantissa and exponent. **[2]**
2. Explain why normalisation gives the greatest precision available for a fixed number of bits. **[2]**
3. A calculation produces a value too small for the available exponent. Name this condition and explain one consequence. **[2]**
4. Compare random and sequential file organisation for retrieving one named satellite record and processing every record in key order. **[3]**

## Question 2 — Resilient Communication [10]

A live translation service streams audio between users in different countries.

1. Explain the different responsibilities of TCP and IP. **[3]**
2. Describe how a router uses a routing table when forwarding a packet. **[2]**
3. Explain two reasons why buffering may be needed at the receiver and one effect of making the buffer too large. **[3]**
4. State one advantage and one disadvantage of packet switching for this service. **[2]**

## Question 3 — Parallel Rendering [9]

A studio uses virtual machines on a multicore server to render animation frames.

1. Explain why rendering separate frames can benefit from parallel processing. **[2]**
2. State two factors that limit the speed-up obtained by adding processor cores. **[2]**
3. Give three benefits of running each rendering job in a separate virtual machine. **[3]**
4. Simplify `X AND (X OR Y)` and name the Boolean law used. **[2]**

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
4. Give one limitation of relying only on encryption and one limitation of relying only on a password. **[2]**

## Question 6 — Intelligent Crop System [10]

A system classifies leaf images and recommends treatment.

1. Distinguish training data, validation data and test data. **[3]**
2. Explain the roles of weights, an activation function and backpropagation in an artificial neural network. **[3]**
3. Explain how biased training images could affect recommendations. **[2]**
4. State one reason to retain human review and one measure that could improve future performance. **[2]**

## Question 7 — Choosing Algorithms [9]

A warehouse maintains a changing list of product codes and a tree-shaped map of storage locations.

1. Give the precondition for binary search and explain why frequent insertions may make maintaining it costly. **[3]**
2. Compare the worst-case time complexity of linear search and binary search. **[2]**
3. Explain how depth-first traversal can be implemented using recursion or a stack. **[2]**
4. State two properties of a well-defined algorithm. **[2]**

## Question 8 — Program Design [9]

A booking system contains several ticket classes and imports booking records from files.

1. Explain how inheritance and method overriding can support different ticket-price rules. **[3]**
2. Explain why composition may be preferable to inheritance for representing the tickets contained in an order. **[2]**
3. Distinguish syntax, logic and runtime errors, giving a relevant example of each. **[3]**
4. State why file resources should be closed even when an exception occurs. **[1]**

## Mark Scheme

### Question 1 Mark Scheme [9]

1. Mantissa stores significant digits/fraction **[1]**; exponent gives the scale/position of the binary point **[1]**. **[2]**
2. A normalised non-zero mantissa uses the available significant-bit positions rather than wasting leading bits **[1]**, so the representation retains as many significant bits as the format permits **[1]**. **[2]**
3. Underflow **[1]**; value may be represented as zero/the smallest available value or lose significant accuracy **[1]**. **[2]**
4. Random organisation calculates/directly locates a record from its key and is suitable for one named item **[1]**; sequential organisation stores records in key order and supports ordered batch processing **[1]**; finding one item sequentially may require reading preceding records **[1]**. **[3]**

### Question 2 Mark Scheme [10]

1. TCP provides end-to-end connection, segmentation/reassembly, ordering, error recovery and flow control **[2]**; IP provides logical addressing and routes datagrams between networks without guaranteeing delivery **[1]**. **[3]**
2. Router reads destination IP address and matches it to the most specific route **[1]**; forwards packet through the indicated next hop/interface, or uses a default route **[1]**. **[2]**
3. Buffer absorbs jitter/variable arrival times **[1]** and stores enough audio when delivery momentarily slows **[1]**; an excessively large buffer increases end-to-end delay, harming conversation **[1]**. **[3]**
4. Advantage: shared routes can adapt to failure/congestion or use capacity efficiently **[1]**; disadvantage: variable delay, loss or reordering can interrupt real-time audio **[1]**. **[2]**

### Question 3 Mark Scheme [9]

1. Frames can be computed largely independently **[1]**, so different cores process different frames simultaneously and reduce elapsed time/increase throughput **[1]**. **[2]**
2. Any two: serial portions, communication/synchronisation overhead, shared-memory/bandwidth contention, uneven tasks, limited number of independent frames. **[2]**
3. Any three: isolation between jobs, different operating systems/dependencies, snapshots/rollback, resource limits, server consolidation, repeatable environments, safer testing. **[3]**
4. Absorption law: `X AND (X OR Y) = X` **[1]**; law correctly named **[1]**. **[2]**

### Question 4 Mark Scheme [10]

1. Each ready request receives a time slice **[1]**; short requests need not wait for the whole report **[1]**; users receive earlier responses/fairer access, although the report is repeatedly pre-empted **[1]**. **[3]**
2. More frequent context switches consume processor time saving/restoring state **[1]**, reducing useful throughput **[1]**. **[2]**
3. Virtual address is split into page number and offset **[1]**; page number indexes the page table to find a frame or not-present flag **[1]**; frame address plus offset gives the physical address **[1]**. **[3]**
4. Page fault occurs when one referenced page is not in RAM and must be loaded **[1]**; thrashing is sustained excessive page swapping, leaving little time for useful execution **[1]**. **[2]**

### Question 5 Mark Scheme [9]

1. Sender publishes a digest produced from the update **[1]**; device hashes the received update and unequal digests reveal alteration/corruption **[1]**. **[2]**
2. Manufacturer signs the update digest with its private key **[1]**; device uses the manufacturer's public key to verify the signature **[1]**; a valid result links the signer to an unchanged digest/update **[1]**. **[3]**
3. Any two: certificate-authority signature/chain, correct subject/domain/identity, validity dates, revocation status, permitted key use. **[2]**
4. Encryption alone does not prove authorised origin or protect an already decrypted device **[1]**; password alone may be guessed, phished, reused or leaked **[1]**. **[2]**

### Question 6 Mark Scheme [10]

1. Training data adjusts model parameters **[1]**; validation data tunes/selects the model during development **[1]**; unseen test data estimates final generalisation without further tuning **[1]**. **[3]**
2. Weights scale connections/signals **[1]**; activation function transforms a neuron's combined input/output and can add non-linearity **[1]**; backpropagation propagates error gradients backwards to update weights/biases **[1]**. **[3]**
3. Underrepresented crops/conditions may be misclassified **[1]**, producing systematically less accurate or harmful recommendations for those cases **[1]**. **[2]**
4. Human review can reject unsafe/low-confidence advice or consider missing context **[1]**; collect representative labelled outcomes, monitor errors and retrain/validate the model **[1]**. **[2]**

### Question 7 Mark Scheme [9]

1. List must be sorted on the search key **[1]**; insertion may require finding a position and shifting/rebuilding/rebalancing data **[1]**, so repeated updates can offset faster searches **[1]**. **[3]**
2. Linear search worst case `O(n)` **[1]**; binary search worst case `O(log n)` **[1]**. **[2]**
3. Visit a node, mark it and continue down an unvisited child **[1]**; recursive calls use the call stack, while an iterative solution explicitly pushes/pops nodes on a stack **[1]**. **[2]**
4. Any two: finite/terminates, unambiguous steps, defined inputs, defined outputs, effective/executable operations. **[2]**

### Question 8 Mark Scheme [9]

1. Common ticket state/behaviour is defined in a superclass **[1]**; subclasses inherit it and override a price method **[1]**; polymorphic calls select the correct rule for the actual ticket object **[1]**. **[3]**
2. An order **has** a collection of tickets rather than being a kind of ticket **[1]**; composition allows different ticket objects to be added/removed without forcing an invalid class hierarchy **[1]**. **[2]**
3. Syntax: violates language grammar, for example a missing colon **[1]**; logic: runs but gives a wrong result, for example applying the discount twice **[1]**; runtime: fails during execution, for example opening a missing file or invalid conversion **[1]**. **[3]**
4. Closing releases the file handle/lock and ensures buffered data is flushed; use a `finally` block or context manager. **[1]**
