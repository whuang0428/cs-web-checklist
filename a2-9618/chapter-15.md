# A2 9618 Chapter 15: Hardware and Virtual Machines

<div class="chapter-meta"><strong>A2 9618 · Paper 3</strong><span>9618 · 2027–2029 · Version 2</span></div>

## Official Syllabus Checklist

Revise: processor architectures; parallel processing and virtual machines; Boolean algebra and sequential logic.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.


<span id="_3-one-page-mind-map" class="legacy-anchor" aria-hidden="true"></span>

## Chapter at a Glance

Use this overview to compare processors, explain virtual execution, simplify Boolean expressions and build circuits.

### Compare processors

<span lang="zh-CN">用指令复杂度、长度、周期和流水线建立成对比较。</span>

- RISC uses fewer simple fixed-format instructions and many registers.
- CISC uses a larger set of complex variable-length instructions that may take several cycles.
- Regular RISC instructions simplify pipelining, while CISC may reduce the number of instructions per task.

**Exam cue:** Compare the same processor feature on both sides.

### Explain parallel processing and VMs

<span lang="zh-CN">先区分指令流和数据流，再说明主机、客户机和虚拟机监控器。</span>

- SISD, SIMD, MISD and MIMD classify systems by instruction and data streams.
- Massively parallel systems divide suitable work across many processing elements.
- A hypervisor runs isolated guest systems on a host but introduces resource overhead.

**Exam cue:** Link the architecture or virtual-machine benefit to the workload.

### Simplify Boolean expressions

<span lang="zh-CN">每一步只应用一条代数定律，并保持补运算准确。</span>

- Apply identity, complement, absorption and distributive laws systematically.
- Use De Morgan's laws by changing the operator and complementing every term.
- Confirm a simplification with a truth table or Karnaugh map when appropriate.

**Exam cue:** Name or show each transformation so method marks remain visible.

### Build logic circuits

<span lang="zh-CN">把表达式、真值表和组合或时序电路逐步对应。</span>

- Half and full adders combine gates to produce sum and carry outputs.
- SR and JK flip-flops store state according to inputs and the current output.
- Karnaugh-map groups must contain powers of two and may wrap across edges.

**Exam cue:** Label intermediate signals and use the required gate or flip-flop notation.

---

## 15.1 Processors, Parallel Processing and Virtual Machines

### RISC processors

#### Core idea
RISC means **Reduced Instruction Set Computer**.

RISC processor <span lang="zh-CN">的设计思想是</span>：
<span lang="zh-CN">用较少</span>、<span lang="zh-CN">较简单</span>、<span lang="zh-CN">格式较固定的指令</span>，<span lang="zh-CN">让</span> CPU <span lang="zh-CN">更容易快速执行和流水线处理</span>。

#### Mark scheme answer
> A RISC processor uses a relatively small number of simple instructions, often fixed length and fixed format. Instructions usually use a single cycle, make use of general-purpose registers, and pipelining is easier to apply.
>

#### Required ideas / marking points
+ **Reduced Instruction Set Computer**
+ **few instructions**
+ **simple instructions**
+ **fixed length / fixed format**
+ **single-cycle instructions**
+ **general-purpose registers**
+ **pipelining**
+ **hard-wired control unit**

#### 2024–2025 style features
| Feature | Explanation |
| --- | --- |
| Few instructions | instruction set is reduced |
| Simple instructions | each instruction does a small operation |
| Fixed length / fixed format | easier to fetch and decode |
| Single-cycle execution | many instructions can complete in one clock cycle |
| Many registers | less need to access main memory |
| Easier pipelining | regular instructions fit pipeline stages better |
| Software emphasis | compiler may do more work |

#### Common weak answer
> RISC is faster and simpler.
>

This is too vague. You need features such as **fixed length instructions**, **few/simple instructions**, **single cycle**, **registers**, or **pipelining**.

---

### CISC processors

CISC means **Complex Instruction Set Computer**.

CISC processor <span lang="zh-CN">的设计思想是</span>：
<span lang="zh-CN">一条指令可以完成更复杂的操作</span>，<span lang="zh-CN">因此程序可能需要更少的指令</span>，<span lang="zh-CN">但</span> CPU <span lang="zh-CN">解码和执行会更复杂</span>。

#### Mark scheme answer
> A CISC processor has a larger instruction set with more complex instructions. Instructions may be variable length and may take several clock cycles to execute. The design emphasis is more on hardware.
>

#### RISC vs CISC comparison

| Area | RISC | CISC |
| --- | --- | --- |
| Full name | Reduced Instruction Set Computer | Complex Instruction Set Computer |
| Number of instructions | fewer | more |
| Instruction complexity | simple | complex |
| Instruction length | usually fixed | may be variable |
| Clock cycles | often single-cycle | may take several cycles |
| Registers | many general-purpose registers | may use fewer registers |
| Pipelining | easier to apply | more difficult because instructions vary |
| Design emphasis | software / compiler | hardware |
| Program length | may need more instructions | may need fewer instructions |

#### Exam sentence
> RISC uses simpler fixed-length instructions, so pipelining is easier. CISC uses more complex instructions that may take several cycles, so decoding and pipelining are more complex.
>

---

### Interrupt handling on RISC and CISC processors

#### Basic interrupt sequence
Interrupt handling <span lang="zh-CN">的核心不是</span>“CPU stop”，<span lang="zh-CN">而是</span>：

1. interrupt is detected
2. current process/program is temporarily stopped
3. registers / program counter / status are saved
4. Interrupt Service Routine (**ISR**) is executed
5. saved register values are restored
6. original program continues

#### Mark scheme answer
> When an interrupt is detected, the current program is temporarily stopped and the status of registers / program counter is stored on the stack. The Interrupt Service Routine is executed. After the interrupt has been serviced, the saved register values are restored and the original program continues.
>

#### Pipeline issue
Pipelining <span lang="zh-CN">会让</span> interrupt handling <span lang="zh-CN">更复杂</span>，<span lang="zh-CN">因为</span> pipeline <span lang="zh-CN">里可能已经有多条</span> instruction <span lang="zh-CN">正在不同</span> stage <span lang="zh-CN">中执行</span>。

#### 2024-style phrase
> There may be a number of instructions still in the pipeline when the interrupt is received, so some instructions may need to be discarded or the processor must restart from the correct next instruction after the ISR.
>

#### Common mistake
| Mistake | Correction |
| --- | --- |
| saying "CPU deletes the current program" | current state is saved, not deleted |
| forgetting ISR | must mention **Interrupt Service Routine** |
| saying registers are saved in RAM only | mark scheme often accepts stack / saved state |
| ignoring pipeline issue | for RISC/pipelining questions, mention instructions already in pipeline |

---

### Pipelining in RISC processors

#### Core idea
Pipelining means different instructions can be at different stages of execution at the same time.

Example stages:

```mermaid
flowchart LR
A[Fetch] --> B[Decode]
B --> C[Execute]
C --> D[Memory access]
D --> E[Write back]
```

#### Why RISC works well with pipelining
RISC instructions are usually:

+ simple
+ fixed length
+ fixed format
+ often single-cycle

This makes pipeline stages more regular.

#### Mark scheme answer
> Pipelining allows several instructions to be processed at the same time, with each instruction at a different stage. RISC processors are suitable for pipelining because instructions are simple and fixed length.
>

#### Benefits
+ improves instruction throughput
+ less idle time in CPU stages
+ multiple instructions are in progress at once

#### Limitation
+ branch / jump instructions may disrupt pipeline
+ interrupts can cause pipeline flushing
+ dependencies between instructions can create hazards

---

## Parallel Processing Architectures

### Flynn's four architectures

The four basic computer architectures are:

+ **SISD**
+ **SIMD**
+ **MISD**
+ **MIMD**

The key exam skill is:
**Instruction stream** <span lang="zh-CN">和</span> **data stream** <span lang="zh-CN">分别是</span> single <span lang="zh-CN">还是</span> multiple。

---

### SISD

#### Full name
**Single Instruction, Single Data**

#### Mark scheme answer
> SISD has one processor executing one instruction stream on one data stream. Instructions are executed sequentially.
>

#### Example
A traditional single-core computer running one instruction at a time.

#### Keywords
+ **single instruction**
+ **single data**
+ **one processor**
+ **sequential execution**

---

### SIMD

#### Full name
**Single Instruction, Multiple Data**

#### Mark scheme answer
> SIMD performs the same instruction on multiple data items at the same time.
>

#### Example
Applying the same image filter to many pixels at once.

#### Keywords
+ **same instruction**
+ **multiple data streams**
+ **simultaneously**
+ **parallel processing**

#### Common mistake
> SIMD means many instructions happen at once.
>

Wrong. SIMD = one instruction, many data items.

---

### MISD

#### Full name
**Multiple Instruction, Single Data**

#### Mark scheme answer
> MISD performs different instructions on the same data stream.
>

#### Example
A fault-tolerant system where the same data is processed by different processors using different operations.

#### Keywords
+ **multiple instructions**
+ **single data stream**
+ **same data**
+ **independent processors**

#### Exam warning
MISD is less common in real systems, but it is still syllabus content.

---

### MIMD

#### Full name
**Multiple Instruction, Multiple Data**

#### Mark scheme answer
> MIMD has multiple processors that can execute different instructions on different data streams independently or asynchronously.
>

#### Example
A multi-core computer running different tasks on different cores.

#### Keywords
+ **multiple instructions**
+ **multiple data streams**
+ **many processors**
+ **independent / asynchronous**

---

### Quick comparison table

| Architecture | Instructions | Data | Simple exam phrase |
| --- | --- | --- | --- |
| SISD | single | single | one processor runs one instruction on one data item |
| SIMD | single | multiple | same operation applied to many data items |
| MISD | multiple | single | different operations applied to same data |
| MIMD | multiple | multiple | different processors run different instructions on different data |

---

## Massively Parallel Computers

### Definition
A massively parallel computer uses a large number of processors or separate computers to perform coordinated computations at the same time.

#### Mark scheme answer
> A massively parallel computer contains a large number of processors / computers connected together, simultaneously performing coordinated computations and communicating using messages.
>

#### Required ideas / marking points
+ **large number of processors**
+ **separate computers connected together**
+ **simultaneously**
+ **coordinated computations**
+ **message interface**
+ **network infrastructure**

#### Uses
| Use | Why massively parallel is suitable |
| --- | --- |
| weather forecasting | huge number of repeated calculations |
| scientific simulation | can divide problem into smaller parts |
| AI training | many matrix/vector operations |
| image/video rendering | independent frames/pixels can be processed |
| cryptography research | many possible keys can be tested |

#### Common mistake
> It is just a very fast computer.
>

Too vague. You must mention **many processors** and **parallel coordinated processing**.

---

## Virtual Machines

### Concept of a virtual machine

A **virtual machine (VM)** is a software-based emulation of a computer system. It runs on a physical computer but behaves like a separate computer.

#### Key terms
| Term | Meaning |
| --- | --- |
| Host machine | physical computer that provides resources |
| Guest machine | virtual machine running on the host |
| Hypervisor | software that creates and manages VMs |
| Emulation / virtualisation | making software behave like hardware |

#### Mark scheme answer
> A virtual machine is a software implementation / emulation of a computer system that runs on a host computer and allows a guest operating system or program to run as if it had its own hardware.
>

---

### Roles / examples of virtual machines

| Role | Example |
| --- | --- |
| running different OS | running Linux on a Windows host |
| testing software safely | test malware or unstable programs in isolated VM |
| server consolidation | several virtual servers on one physical server |
| legacy software | run old software on a modern machine |
| cloud computing | cloud providers allocate virtual servers |
| education | students practise OS/network setup safely |

#### Scenario answer
> A VM allows the company to run several virtual servers on one physical server, reducing hardware cost and making better use of resources.
>

---

### Benefits of virtual machines

| Benefit | Explanation |
| --- | --- |
| Isolation | software inside one VM is separated from host/other VMs |
| Portability | VM can be moved or copied more easily than physical machine |
| Cost saving | fewer physical machines needed |
| Resource sharing | host resources can be divided among VMs |
| Testing safety | risky software can be tested without damaging host |
| Legacy support | old OS/software can still run |
| Easy backup | VM image can be snapshotted or restored |

#### Mark scheme answer
> Virtual machines allow several operating systems or servers to run on one physical machine. They provide isolation, make testing safer, reduce hardware costs, and allow VM images to be backed up or moved easily.
>

---

### Limitations of virtual machines

| Limitation | Explanation |
| --- | --- |
| Performance overhead | VM uses extra processing because hypervisor is needed |
| Resource competition | multiple VMs share CPU/RAM/storage |
| Single point of failure | if host fails, all VMs on it may fail |
| Security risk | misconfigured VM can still be attacked |
| Management complexity | many VMs can be hard to maintain |
| Licensing cost | some OS/software licences may still be needed |

#### Mark scheme answer
> Virtual machines can reduce performance because resources are shared and the hypervisor adds overhead. If the host machine fails, all virtual machines on that host may be affected.
>

---

## 15.2 Boolean Algebra and Logic Circuits

### Boolean algebra notation

| Symbol | Meaning | Logic gate |
| --- | --- | --- |
| `.` | AND | AND |
| `+` | OR | OR |
| overbar / `'` / NOT | NOT | NOT |

Example:

```text
A.B + C
```

means:

```text
(A AND B) OR C
```

#### Common mistake
`+` does not mean arithmetic addition in Boolean algebra.
It means **OR**.

---

### Core Boolean laws

| Law | AND form | OR form |
| --- | --- | --- |
| Identity | `A.1 = A` | `A + 0 = A` |
| Null | `A.0 = 0` | `A + 1 = 1` |
| Idempotent | `A.A = A` | `A + A = A` |
| Complement | `A.A' = 0` | `A + A' = 1` |
| Commutative | `A.B = B.A` | `A + B = B + A` |
| Distributive | `A.(B + C) = A.B + A.C` | `A + B.C = (A + B).(A + C)` |
| Absorption | `A.(A + B) = A` | `A + A.B = A` |
| Double complement | `(A')' = A` | — |

#### 2025 trend
2025 mark schemes reward not only the final answer but also correct application of laws such as:

+ **De Morgan's laws**
+ **Idempotent law**
+ **Distributive law**
+ **Absorption law**

So when showing working, write the law name if possible.

---

### De Morgan's laws

#### Law 1
```text
(A.B)' = A' + B'
```

Meaning:

> NOT(A AND B) = NOT A OR NOT B

#### Law 2
```text
(A + B)' = A'.B'
```

Meaning:

> NOT(A OR B) = NOT A AND NOT B

#### Exam method
When applying De Morgan:

1. change AND ↔ OR
2. complement each term
3. remove the outer NOT

#### Common mistake
| Wrong | Why wrong |
| --- | --- |
| `(A + B)' = A' + B'` | forgot to change OR to AND |
| `(A.B)' = A'.B` | forgot to complement every term |
| `(A + B.C)' = A'.B' + C'` | must treat grouped expression carefully |

#### Example
Simplify:

```text
(A + B)' . B
```

Step:

```text
(A + B)' . B
= A'.B'.B       De Morgan
= A'.0          Complement
= 0             Null
```

---

## Truth Tables

### Truth table method

For Paper 3, when a circuit or expression is given, do not jump straight to the answer. Make working columns.

Example expression:

```text
Z = (A + B).C'
```

Truth table:

| A | B | C | A + B | C' | Z |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

#### Mark scheme advice
2024–2025 mark schemes often award marks for:

+ intermediate working columns
+ first half of output rows
+ second half of output rows
+ correct final output

So always show working columns.

---

### Sum-of-products

A **sum-of-products** expression is made by OR-ing together product terms.

#### Method
1. Find rows where output = 1
2. For each row, write one AND term
3. If input is 1, write normal variable
4. If input is 0, write complemented variable
5. OR all terms together

#### Example
| A | B | C | Z |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

Rows with `Z = 1`:

```text
001, 011, 101, 111
```

Expression:

```text
Z = A'.B'.C + A'.B.C + A.B'.C + A.B.C
```

This simplifies to:

```text
Z = C
```

#### Common mistake
| Mistake | Correction |
| --- | --- |
| using rows where output = 0 | sum-of-products uses rows where output = 1 |
| forgetting complements | 0 means complemented variable |
| missing one minterm | check every row with output 1 |
| writing `A+B+C` for a row | each row gives an AND term, not OR |

---

## Half Adders and Full Adders

### Half adder

A half adder adds two one-bit inputs.

Inputs:

+ `A`
+ `B`

Outputs:

+ `S` = Sum
+ `C` = Carry

#### Truth table
| A | B | Sum S | Carry C |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

#### Expressions
```text
S = A XOR B
C = A.B
```

#### Exam phrase
> A half adder adds two binary bits and produces a sum bit and a carry bit.
>

---

### Full adder

A full adder adds three one-bit inputs:

+ `A`
+ `B`
+ `Cin`

Outputs:

+ `S`
+ `Cout`

#### Truth table
| A | B | Cin | Sum S | Carry Cout |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

#### Expressions
```text
S = A XOR B XOR Cin
Cout = A.B + A.Cin + B.Cin
```

#### Exam phrase
> A full adder adds two input bits and an incoming carry, producing a sum output and an outgoing carry.
>

---

## Flip-Flops

### What is a flip-flop?

A flip-flop is a logic circuit that can store one bit of data.

#### Mark scheme answer
> A flip-flop is a bistable circuit that can store one bit. Its output remains in the same state until the input causes it to change.
>

#### Required ideas / marking points
+ **bistable**
+ **stores one bit**
+ **data storage element**
+ **state**
+ **output retained**

---

### SR flip-flop

SR means:

+ `S` = Set
+ `R` = Reset

#### Basic SR truth table
| S | R | Q next | Meaning |
| --- | --- | --- | --- |
| 0 | 0 | Q | no change |
| 0 | 1 | 0 | reset |
| 1 | 0 | 1 | set |
| 1 | 1 | invalid / not allowed | undefined |

#### Key point
SR flip-flop can store a bit because when `S = 0` and `R = 0`, the output stays the same.

---

### JK flip-flop

JK flip-flop solves the invalid state problem of SR.

#### JK truth table
| J | K | Q next | Meaning |
| --- | --- | --- | --- |
| 0 | 0 | Q | no change |
| 0 | 1 | 0 | reset |
| 1 | 0 | 1 | set |
| 1 | 1 | Q' | toggle |

#### Exam phrase
> A JK flip-flop has no invalid state; when both inputs are 1, the output toggles.
>

---

## Karnaugh Maps

### What is a K-map?

A Karnaugh map is a visual method for simplifying Boolean expressions.

#### Mark scheme answer
> A Karnaugh map represents a truth table in a grid so adjacent 1s can be grouped to produce a simplified Boolean expression.
>

#### Benefit
+ reduces errors compared with long Boolean algebra
+ makes simplification easier
+ visually groups adjacent minterms
+ can produce a minimal sum-of-products expression

---

### K-map order

For two variables:

| A\B | 0 | 1 |
| --- | --- | --- |
| 0 |  |  |
| 1 |  |  |

For three variables:

| A\BC | 00 | 01 | 11 | 10 |
| --- | --- | --- | --- | --- |
| 0 |  |  |  |  |
| 1 |  |  |  |  |

For four variables:

| AB\CD | 00 | 01 | 11 | 10 |
| --- | --- | --- | --- | --- |
| 00 |  |  |  |  |
| 01 |  |  |  |  |
| 11 |  |  |  |  |
| 10 |  |  |  |  |

#### Important
K-map order is **Gray code**:

```text
00, 01, 11, 10
```

Not:

```text
00, 01, 10, 11
```

---

### Grouping rules

| Rule | Explanation |
| --- | --- |
| group only 1s | for sum-of-products simplification |
| group size must be powers of 2 | 1, 2, 4, 8, 16 |
| make groups as large as possible | larger group = simpler term |
| groups can overlap | allowed if it simplifies |
| wrap-around is allowed | left/right and top/bottom edges are adjacent |
| no groups of 3, 5, 6 | not powers of 2 |

#### Common mistake
| Mistake | Correction |
| --- | --- |
| grouping three 1s | group 2 or 4, not 3 |
| not using wrap-around | edge cells can be adjacent |
| using normal binary order | use Gray code |
| leaving an isolated 1 when it can join a group | make largest possible groups |
| including 0s in a group | only group 1s for SOP |

---

### Reading a group

When reading a group:

+ keep variables that stay the same
+ remove variables that change

Example:

| A\BC | 00 | 01 | 11 | 10 |
| --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 |

The four 1s are in columns `01` and `11`.

+ A changes → remove A
+ B changes from 0 to 1 → remove B
+ C stays 1 → keep C

So:

```text
Z = C
```

---

## Mark Scheme Keywords

### RISC / CISC
+ **Reduced Instruction Set Computer**
+ **Complex Instruction Set Computer**
+ **few instructions**
+ **simple instructions**
+ **fixed length / fixed format**
+ **single cycle**
+ **general-purpose registers**
+ **pipelining**
+ **hard-wired control unit**
+ **variable length instructions**
+ **several clock cycles**

### Interrupts
+ **interrupt detected**
+ **fetch-execute cycle**
+ **temporarily stopped**
+ **register status saved**
+ **program counter saved**
+ **stack**
+ **Interrupt Service Routine / ISR**
+ **registers restored**
+ **pipeline flushed / discarded instructions**

### Parallel processing
+ **SISD**
+ **SIMD**
+ **MISD**
+ **MIMD**
+ **single / multiple instruction stream**
+ **single / multiple data stream**
+ **many processors**
+ **asynchronously / independently**
+ **simultaneously**
+ **coordinated computations**
+ **message interface**

### Virtual machines
+ **software emulation**
+ **host**
+ **guest**
+ **hypervisor**
+ **isolation**
+ **portability**
+ **resource sharing**
+ **performance overhead**
+ **single point of failure**

### Boolean / K-map
+ **truth table**
+ **intermediate columns**
+ **sum-of-products**
+ **minterm**
+ **De Morgan's laws**
+ **Idempotent law**
+ **Distributive law**
+ **Absorption law**
+ **Karnaugh map / K-map**
+ **Gray code**
+ **group adjacent 1s**
+ **powers of two**
+ **wrap-around**
+ **simplified expression**

### Flip-flops and adders
+ **half adder**
+ **full adder**
+ **sum**
+ **carry**
+ **carry in / carry out**
+ **SR flip-flop**
+ **JK flip-flop**
+ **bistable**
+ **stores one bit**
+ **toggle**

---

## Topic-Specific Common Confusions

| Mistake | Why it loses marks | Correct version |
| --- | --- | --- |
| RISC = fast, CISC = slow | too vague and too absolute | compare instruction set, length, cycles, pipelining |
| forgetting fixed length for RISC | common mark scheme point missed | RISC often uses fixed-length instructions |
| saying SIMD has many instructions | wrong acronym | SIMD = one instruction, multiple data |
| confusing MIMD and SIMD | loses definition marks | MIMD = multiple instructions and multiple data |
| saying VM is another physical computer | concept wrong | VM is software emulation running on host |
| only saying VM saves money | insufficient | explain reduced hardware / multiple guests on one host |
| using binary order in K-map | wrong map placement | use Gray code: 00, 01, 11, 10 |
| grouping 3 cells in K-map | invalid group size | groups must be 1, 2, 4, 8... |
| forgetting complements in SOP | wrong expression | 0 = complemented variable, 1 = normal variable |
| applying De Morgan incompletely | common loss | change AND/OR and complement every term |
| saying flip-flop stores many bits | wrong | one flip-flop stores one bit |
| treating half adder as full adder | missing Cin | half adder has no carry-in |

---

## Scenario Answer Bank

### Scenario 1: A CPU designer chooses RISC for a new embedded processor.
#### Answer template
> RISC is suitable because it uses fewer and simpler instructions. These instructions are often fixed length and can be executed in a single cycle, making pipelining easier. This can improve instruction throughput and reduce hardware complexity.
>

### Scenario 2: A graphics program applies the same filter to many pixels.
#### Answer template
> SIMD is suitable because the same instruction can be applied to multiple data items at the same time. Each pixel is a separate data item, so the operation can be parallelised.
>

### Scenario 3: A cloud provider hosts many servers on one physical machine.
#### Answer template
> Virtual machines are suitable because several guest operating systems can run on one host machine. This reduces hardware cost, allows resources to be shared, and provides isolation between servers.
>

### Scenario 4: A student is asked why a VM may be slower than a physical machine.
#### Answer template
> A VM may be slower because the hypervisor adds overhead and the VM shares CPU, memory and storage with other VMs on the same host.
>

### Scenario 5: A truth table has many output 1s.
#### Answer template
> A K-map can be used to group adjacent 1s and produce a simplified Boolean expression. This is faster and less error-prone than simplifying a long sum-of-products expression manually.
>

### Scenario 6: A circuit must store one binary digit.
#### Answer template
> A flip-flop can be used because it is a bistable circuit that stores one bit. Its output remains in the same state until the inputs cause it to change.
>

### Scenario 7: An interrupt occurs during pipelining.
#### Answer template
> Interrupt handling is more complex because several instructions may already be in different pipeline stages. Some instructions may need to be discarded, the current state saved, the ISR executed, and the processor restarted from the correct instruction.
>

---

## Mermaid Process Diagrams

### Interrupt handling process

```mermaid
flowchart TD
A[Interrupt detected] --> B[Finish / pause current instruction]
B --> C[Save PC and register status]
C --> D[Run Interrupt Service Routine]
D --> E[Restore saved state]
E --> F[Continue original program]
```

### VM structure

```mermaid
flowchart TD
A[Physical Hardware<br/>CPU RAM Storage] --> B[Host Operating System]
B --> C[Hypervisor]
C --> D[Guest VM 1<br/>OS + Apps]
C --> E[Guest VM 2<br/>OS + Apps]
C --> F[Guest VM 3<br/>OS + Apps]
```

### K-map simplification process

```mermaid
flowchart LR
A[Truth table] --> B[Place output 1s in K-map]
B --> C[Group adjacent 1s]
C --> D[Use powers of 2 groups]
D --> E[Remove changing variables]
E --> F[Write simplified expression]
```

---

## Required Ideas and Exam Language

Use technical terms as part of a complete statement: identify the component or method, state what it does, then link its effect to the question context. A keyword without a correct relationship is not a complete marking point.

## Common Confusions

- Do not substitute a related term for the process named in the question.
- Do not list advantages or definitions without linking them to the stated context.

## Worked Examples

The worked calculations, process templates and scenario answers above model the chain of reasoning expected in examination responses. Rework each example before reading its answer.

## 10-Mark Quick Check

**Total: 10 marks**

### Questions

1. State two features of a RISC processor. `[2]`
2. Give one difference between RISC and CISC. `[1]`
3. What does SIMD stand for? `[1]`
4. Describe MIMD. `[2]`
5. State one benefit of a virtual machine. `[1]`
6. State one limitation of a virtual machine. `[1]`
7. Write De Morgan's law for `(A + B)'`. `[1]`
8. In a K-map, why is the order `00, 01, 11, 10` used? `[1]`

## Quick Check Answers

1. Any two: few/simple instructions; fixed length instructions; single-cycle instructions; many registers; easier pipelining.
2. RISC has fewer/simple instructions, while CISC has more/complex instructions.
3. Single Instruction, Multiple Data.
4. Multiple processors execute different instruction streams on different data streams independently/asynchronously.
5. Isolation / cost saving / portability / allows different OS / safer testing.
6. Performance overhead / resource sharing / host failure affects VMs / management complexity.
7. `(A + B)' = A'.B'`
8. It is Gray code, so only one bit changes between adjacent cells.

---

## 20-Mark Exam Practice

**Total: 20 marks**

### Question 1: RISC, interrupts and pipelining `[6]`

(a) Identify four features of a RISC processor. `[4]`
(b) Explain why interrupt handling can be more complex when pipelining is used. `[2]`

#### Mark scheme
(a) One mark each, max 4:

+ uses few instructions
+ uses simple instructions
+ fixed length / fixed format instructions
+ instructions often execute in a single cycle
+ uses general-purpose registers
+ pipelining is easier to apply
+ hard-wired control unit
+ design emphasis on software / compiler

(b)

+ several instructions may already be in the pipeline when the interrupt is detected `[1]`
+ instructions may need to be discarded / pipeline flushed / processor restarts at correct next instruction after ISR `[1]`

---

### Question 2: Parallel architectures `[4]`

Complete the table.

| Architecture | Full name | Description |
| --- | --- | --- |
| SISD |  |  |
| SIMD |  |  |
| MISD |  |  |
| MIMD |  |  |

#### Mark scheme
One mark per correct row, max 4:

+ SISD = Single Instruction, Single Data; one instruction stream on one data stream / sequential execution
+ SIMD = Single Instruction, Multiple Data; same instruction applied to multiple data items
+ MISD = Multiple Instruction, Single Data; different instructions applied to same data stream
+ MIMD = Multiple Instruction, Multiple Data; different processors execute different instructions on different data streams

---

### Question 3: Virtual machines `[4]`

A school wants students to test different operating systems without changing the computers in the classroom.

Explain two benefits and two limitations of using virtual machines. `[4]`

#### Mark scheme
Benefits, max 2:

+ different operating systems can run on one host machine
+ isolated from the host / other VMs
+ safer testing environment
+ VM can be restored from snapshot / backup
+ reduces need for extra physical machines

Limitations, max 2:

+ performance overhead due to hypervisor
+ VMs share CPU/RAM/storage resources
+ if host fails, VMs are affected
+ extra management complexity
+ security risk if poorly configured

---

### Question 4: Boolean algebra `[3]`

Simplify the expression:

```text
(A + B)'.B + A.B
```

Show working.

#### Mark scheme

```text
(A + B)'.B + A.B
= A'.B'.B + A.B      De Morgan
= A'.0 + A.B         Complement
= 0 + A.B            Null
= A.B                Identity
```

Marks:

+ correct De Morgan application `[1]`
+ correct use of complement/null law `[1]`
+ final answer `A.B` `[1]`

---

### Question 5: K-map and sum-of-products `[3]`

A logic function has output 1 for:

```text
A B C
0 0 1
0 1 1
1 0 1
1 1 1
```

(a) Write the full sum-of-products expression. `[2]`
(b) Simplify the expression. `[1]`

#### Mark scheme

(a)

```text
Z = A'.B'.C + A'.B.C + A.B'.C + A.B.C
```

Award:

+ any two correct minterms `[1]`
+ all four correct minterms and OR operators `[1]`

(b)

```text
Z = C
```

---

## Final Revision Checklist

- I can define the required terms precisely.
- I can explain each process in the correct order.
- I can apply the ideas to an unfamiliar scenario.
- I can complete the 10-mark check without notes.
- I can complete and self-mark the 20-mark practice.
