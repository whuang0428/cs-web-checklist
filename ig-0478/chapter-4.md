# IGCSE 0478 Chapter 4: Software

<div class="chapter-meta"><strong>IGCSE 0478 · Paper 1</strong><span>0478 · 2026–2028 · Version 5</span></div>

## Official Syllabus Checklist

Revise: system and application software; operating systems and interrupts; translators and IDEs.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.


## 4.1 Types of Software and Interrupts
### 4.1.1 Software Types｜System Software vs Application Software
**System Software**
Software that provides the services that the computer requires.

**Key idea:** manages / maintains hardware and software.

**Application Software**
Software that provides the services that the user requires.

**Key idea:** allows the user to perform tasks.

#### Core Exam Sentences
+ **System software** provides the services that the computer requires.
+ System software **manages / maintains hardware and software**.
+ Examples: **operating system**, **utility software**, **device driver**.
+ **Application software** provides the services that the user requires.
+ Application software allows the user to **perform specific tasks**.
+ Examples: word processor, spreadsheet, database, web browser, image editor, video editor.

> **Common trap**：<span lang="zh-CN">考试如果问</span> system software example，<span lang="zh-CN">最稳答案是</span> **operating system** <span lang="zh-CN">或</span> **utility software**。<span lang="zh-CN">不要写</span> brand name。
>

---

### 4.1.2 Utility Software｜Utility Programs
**Utility software** is software designed to **manage, maintain or protect** a computer system.

| Utility software | What it does |
| --- | --- |
| **Anti-virus / anti-malware** | scans, detects, quarantines or removes malware |
| **Backup software** | creates copies of files for recovery |
| **File compression software** | reduces file size |
| **Disk repair / analysis** | checks and repairs storage problems |
| **File management software** | helps organise, copy, move and delete files |
| **Defragmentation software** | reorganises fragmented files on magnetic storage |
| **Security software** | helps protect the system from unauthorised access |


#### Core Exam Sentences
+ Utility software helps to **manage, maintain and control computer resources**.
+ Utility software is a type of **system software**.
+ Anti-virus software is utility software because it helps protect the computer system.

> **<span lang="zh-CN">注意</span>**：defragmentation <span lang="zh-CN">主要适用于</span> **magnetic storage / HDD**，<span lang="zh-CN">不要把它当作</span> SSD <span lang="zh-CN">的主功能来写</span>。
>

---

### 4.1.3 Operating System｜Role and Basic Functions
An **operating system (OS)** is system software that manages the main functions of a computer.

#### OS Function Table
| Function | Mark scheme style role description |
| --- | --- |
| **Managing files** | allows users to create, store, delete, move, copy and organise files |
| **Handling interrupts** | assigns priority to interrupts and uses an ISR / interrupt handler to process them |
| **Providing an interface** | allows the user to interact with the computer, e.g. GUI / CLI |
| **Managing peripherals and drivers** | allows hardware devices to communicate with the OS and applications |
| **Managing memory** | allocates / deallocates memory to processes and checks enough memory is available |
| **Managing multitasking** | switches between processes and allocates processor time/resources |
| **Platform for applications** | allows application software to run and communicate with hardware |
| **System security** | manages usernames, passwords, access rights, updates and security software |
| **Managing user accounts** | allows multiple users to log in and have separate settings/access rights |


#### OS Memory Management Answer Structure
> **Describe the role of the OS in managing memory.**
>

Use these points:

+ It makes sure memory is used efficiently.
+ It **allocates memory** to processes.
+ It **deallocates memory** when a process is finished.
+ It checks that processes have enough memory available.
+ It makes sure two processes do not try to access the same memory location.
+ It keeps track of which memory locations are free or in use.
+ It protects the memory allocated to one process from access by another process.

Virtual memory itself belongs to Topic 3.3. Revise its purpose and operation in [Chapter 3](chapter-3.md#334-virtual-memory).

#### Core Exam Sentences
+ The OS provides a **platform for running application software**.
+ The OS manages **memory, files, peripherals, security, user accounts and multitasking**.
+ The OS handles interrupts by assigning priority and calling the **interrupt service routine**.

> **Common trap**：`loading the bootstrap` <span lang="zh-CN">不是</span> OS <span lang="zh-CN">的</span> function。Bootstrap / bootloader is firmware used to start the operating system.
>

---

### 4.1.4 Hardware, Firmware and OS｜How Applications Run
#### Golden Chain
```mermaid
flowchart TD
A[Hardware] --> B[Firmware / BIOS / Bootloader]
B --> C[Operating System]
C --> D[Application Software]
D --> E[User Task]
```

#### Explanation
| Layer | Role |
| --- | --- |
| **Hardware** | physical components of the computer |
| **Firmware** | permanent instructions stored in ROM / programmed into hardware |
| **BIOS / Bootloader** | starts the computer and loads the OS |
| **Operating system** | provides a platform for applications to run |
| **Application software** | allows the user to perform tasks |


#### Firmware Core Sentences
+ Firmware is **software / instructions programmed into a hardware device**.
+ Firmware is usually stored in **ROM**.
+ Firmware can allow hardware to be **controlled / managed**.
+ Firmware provides the operating system with a **platform to run on**.
+ Examples: **BIOS**, bootloader, firmware in printer / router / SSD / robot controller.

> **Common trap**：Firmware is not the same as normal application software. It is more permanent and is closely linked to hardware.
>

---

### 4.1.5 Interrupts｜Definition and Purpose
An **interrupt** is a signal sent from hardware or software to the processor to request attention.

#### Why Interrupts Are Needed
+ To show that the CPU’s attention is required.
+ To stop / pause the current process if something more urgent happens.
+ To allow **multitasking**.
+ To allow time-sensitive requests to be handled.
+ To improve efficiency because the CPU does not need to constantly poll devices.

#### Hardware vs Software Interrupts
| Type | Definition | Examples |
| --- | --- | --- |
| **Hardware interrupt** | generated by a hardware device | key press, mouse click, printer out of paper/ink, peripheral connected/disconnected |
| **Software interrupt** | generated by software or a software error | division by zero, two processes trying to access the same memory location, program error |


> **Exam-safe examples**：
Hardware interrupt = **key press on keyboard** / mouse click / printer out of ink.
Software interrupt = **division by zero** / two processes trying to access same memory location.
>

---

### 4.1.6 How Interrupts Are Handled｜High Mark Template
> **Describe how the OS / CPU handles an interrupt.**
>

```mermaid
flowchart TD
A[Interrupt generated] --> B[CPU / OS checks priority]
B --> C{Higher priority than current process?}
C -- No --> D[Continue current process]
C -- Yes --> E[Halt current process]
E --> F[Save current process status / store on stack]
F --> G[Check source of interrupt]
G --> H[Call ISR / interrupt handler]
H --> I[Service the interrupt]
I --> J[Restore saved status]
J --> K[Continue original process]
```

#### Full Mark Sentences
+ The CPU / OS checks the **priority** of the interrupt.
+ If the interrupt has higher priority, the current process is halted.
+ The status of the current process is saved, often on a **stack**.
+ The source of the interrupt is checked.
+ The **interrupt service routine (ISR)** / interrupt handler is called.
+ The interrupt is serviced.
+ The saved status is restored.
+ The original process continues from where it stopped.

#### One-Minute Version
> The OS checks the priority of the interrupt. If it has higher priority, the current process is halted and its status is saved. The OS then calls the interrupt service routine to service the interrupt. Once complete, the saved status is restored and the original process continues.
>

---

## 4.2 Programming Languages, Translators and IDEs
### 4.2.1 High-Level Language vs Low-Level Language
| Feature | High-Level Language | Low-Level Language |
| --- | --- | --- |
| Human readability | easier to read / write / understand | harder to read / write / understand |
| Debugging | easier to debug | more error-prone |
| Portability | machine independent / portable | machine dependent |
| Hardware control | less direct control of hardware | can directly manipulate memory / registers / hardware |
| Memory efficiency | may use more memory after translation | can be memory efficient |
| Examples | Python, Java, C# | machine code, assembly language |
| Translator | compiler or interpreter | assembler for assembly language |


#### Why Use a High-Level Language?
+ Easier for programmers to read, write and understand.
+ Easier to debug and maintain.
+ Less likely to make errors.
+ Machine independent / portable.
+ Does not require direct knowledge of memory locations or registers.
+ Can use an IDE.

#### Why Use a Low-Level Language?
+ Can directly access / manipulate memory locations and registers.
+ Can communicate directly with hardware.
+ Can be more memory efficient.
+ Can execute faster after translation.
+ Useful for embedded systems or hardware-specific programming.

> **Common trap**：<span lang="zh-CN">不要只写</span> “high-level is easier”。<span lang="zh-CN">要补出</span> **easier to debug / portable / machine independent / does not need hardware knowledge**。
>

---

### 4.2.2 Assembly Language and Assembler
**Assembly language** is a low-level language that uses **mnemonics**.

#### Core Exam Sentences
+ Assembly language is a **low-level language**.
+ It uses **mnemonics**.
+ It is used to communicate directly with the computer hardware.
+ It is machine dependent.
+ An **assembler** translates assembly language into machine code.

#### Example Concept
```latex
Assembly language  --assembler-->  Machine code
```

> **Common trap**：Assembler translates **assembly language**, not high-level language. Compiler / interpreter translate high-level language.
>

---

### 4.2.3 Translators｜Compiler, Interpreter and Assembler
| Translator | Source language | How it works | Output | Common use |
| --- | --- | --- | --- | --- |
| **Compiler** | high-level language | translates the whole code at once before execution | executable file / machine code file | final program / distribution |
| **Interpreter** | high-level language | translates and executes line by line | no separate executable file | development / debugging |
| **Assembler** | assembly language | translates assembly language into machine code | machine code | low-level programs |


---

### 4.2.4 Compiler vs Interpreter｜High Frequency
#### Compiler
+ Translates the **whole code** at once.
+ Translation happens **before execution**.
+ Produces an **executable file**.
+ Reports **all errors** in an error report if errors are found.
+ Once compiled, the compiler is not needed to run the program.
+ Useful for distributing the final program without source code.

#### Interpreter
+ Translates and executes code **line by line**.
+ Stops when an error is found.
+ The error can be corrected immediately.
+ Program can continue once the error is corrected.
+ Easier to debug during development.
+ No separate executable file is produced.
+ The interpreter is needed each time the program runs.

#### Compiler vs Interpreter Quick Table
| Question type | Best answer |
| --- | --- |
| During development | **Interpreter**, because it stops when an error is found and helps debug line by line |
| Final program distribution | **Compiler**, because it creates an executable file and source code is not needed |
| Error reporting | Compiler reports all errors; interpreter stops at the first error |
| Running after translation | Compiled program can run without compiler; interpreted program needs interpreter |


#### Core Exam Template
> A programmer may use an interpreter during development because it translates and executes code line by line, stops when an error is found, and helps debug the program. The programmer may use a compiler for the final program because it translates the whole program and creates an executable file, so the program can be distributed without the source code.
>

---

### 4.2.5 IDE｜Integrated Development Environment
An **IDE** is a suite of programs used to write, run, test and debug program code.

#### IDE Functions and Roles
| IDE function | Mark scheme style role description |
| --- | --- |
| **Code editor** | allows the programmer to write / change program code |
| **Run-time environment** | allows the programmer to run the code and see the output |
| **Translator** | converts source code into machine code / low-level code |
| **Error diagnostics** | helps find errors in the code |
| **Auto-completion** | suggests the rest of a command word while the programmer is typing |
| **Auto-correction** | corrects misspelled command words |
| **Prettyprint / syntax highlighting** | uses colours / formatting to make code easier to read |
| **Collapse / expand blocks** | hides or shows sections of code to improve readability |
| **Auto-documentation** | can generate documentation / comments for the code |


#### Core Exam Sentences
+ An IDE provides tools to help programmers write and test code.
+ A code editor allows the programmer to write or change program code.
+ A run-time environment allows the programmer to run the code and view output.
+ Error diagnostics help find errors in the code.
+ Auto-completion suggests possible command words.
+ Auto-correction corrects misspelled command words.
+ Prettyprint / syntax highlighting colours command words and identifiers to make code easier to read.

> **Common trap**：<span lang="zh-CN">如果题目要求</span> “function and description”，<span lang="zh-CN">只写</span> `auto-completion` <span lang="zh-CN">不够</span>，<span lang="zh-CN">要写它如何帮助</span> programmer。
>

---

<span id="_2-chapter-4-overall-mind-map" class="legacy-anchor" aria-hidden="true"></span>

## Chapter at a Glance

Use this overview to classify software, trace interrupts, translate code and select tools.

### Select software

<span lang="zh-CN">先判断软件服务的是计算机系统还是最终用户。</span>

- System software manages or maintains hardware and other software.
- Application software helps a user complete a specific task.
- Firmware is permanent control software normally stored in ROM.

**Exam cue:** Name a suitable example and explain the service it provides.

### Handle interrupts

<span lang="zh-CN">把中断写成保存、处理、恢复的完整过程。</span>

- A hardware or software event sends an interrupt signal to the processor.
- The processor saves its current state before running the interrupt service routine.
- The saved state is restored so the interrupted process can continue.

**Exam cue:** Include priority, the ISR and the saved processor state where relevant.

### Translate source code

<span lang="zh-CN">根据输入语言和输出方式区分三种翻译器。</span>

- A compiler translates a complete high-level program before execution.
- An interpreter translates and executes high-level code one statement at a time.
- An assembler translates assembly language into machine code.

**Exam cue:** Compare when translation happens, what output is produced and how errors are reported.

### Use IDE tools

<span lang="zh-CN">写出工具名称后，还要说明它怎样帮助程序员。</span>

- A code editor and runtime environment support writing and executing code.
- Diagnostics locate errors while auto-completion and auto-correction reduce typing mistakes.
- Prettyprint or syntax highlighting makes program structure easier to read.

**Exam cue:** Give the feature and its practical benefit, not the feature name alone.

---

## Mark Scheme Style Answer Templates
### Template A｜Difference between system software and application software
> System software provides the services that the computer requires and manages / maintains the hardware and software. An example is an operating system or utility software. Application software provides the services that the user requires and allows the user to perform tasks. An example is a word processor or spreadsheet.
>

---

### Template B｜Operating system memory management
> The operating system allocates memory to processes and deallocates it when processes finish. It keeps track of free and occupied locations, checks that enough memory is available and prevents one process from accessing memory allocated to another.
>

---

### Template C｜Firmware
> Firmware is permanent software / instructions programmed into a hardware device and usually stored in ROM. It can control hardware and provide a platform for the operating system to run on. An example is BIOS or a bootloader.
>

---

### Template D｜Interrupt handling
> The OS checks the priority of the interrupt. If it has a higher priority, the current process is halted and its status is saved, for example on a stack. The OS checks the source of the interrupt and calls the interrupt service routine / interrupt handler. Once the interrupt has been serviced, the saved status is restored and the original process continues.
>

---

### Template E｜Compiler vs interpreter
> A compiler translates the whole program before execution and produces an executable file. It reports all errors in the code. An interpreter translates and executes the code line by line and stops when an error is found. This makes an interpreter useful during development, while a compiler is useful for the final program.
>

---

### Template F｜Why use high-level language?
> A high-level language is easier for the programmer to read, write and understand. It is easier to debug and maintain. It is machine independent / portable, so the same program can be used on different types of computer after translation.
>

---

### Template G｜IDE functions
> A code editor allows the programmer to write and change code. A run-time environment allows the code to be run and the output to be seen. Error diagnostics help find errors in the code. Auto-completion suggests command words while the programmer is typing, and prettyprint colours / formats code to make it easier to read.
>

---

## Topic-Specific Common Confusions
| Topic | Weak answer | Why it loses marks | Better answer |
| --- | --- | --- | --- |
| System software | “It is software for computer.” | Too vague | “It provides services the computer requires and manages hardware/software.” |
| Application software | “Software on computer.” | Too vague | “It provides services the user requires and allows the user to perform tasks.” |
| Utility software | “It is an app.” | Utility is system software | “Utility software manages, maintains or protects the computer system.” |
| OS function | “OS controls computer.” | Too general | Give a named function + role, e.g. “manages memory by allocating memory to processes.” |
| Memory management | “Stores data.” | Not OS role enough | “Allocates/deallocates memory and prevents two processes accessing the same location.” |
| Firmware | “It is hardware.” | Firmware is software/instructions | “Firmware is software programmed into hardware and usually stored in ROM.” |
| Bootloader | “It is OS.” | Bootloader is firmware | “The bootloader loads/starts the operating system.” |
| Interrupt | “CPU stops.” | Missing process | “CPU checks priority, saves current status, calls ISR, restores status.” |
| Hardware interrupt | “Division by zero.” | That is software interrupt | “Key press / mouse click / printer out of ink.” |
| Software interrupt | “Keyboard press.” | That is hardware interrupt | “Division by zero / two processes accessing same memory location.” |
| ISR | “A program runs.” | Need name and role | “Interrupt service routine / interrupt handler services the interrupt.” |
| High-level language | “It is English.” | Too informal | “Easier to read/write/debug and machine independent.” |
| Low-level language | “It is hard.” | Too vague | “Machine dependent and can directly access memory/registers/hardware.” |
| Assembly language | “It is machine code.” | Assembly is not exactly machine code | “Assembly is low-level and uses mnemonics.” |
| Assembler | “Translates high-level language.” | Wrong translator | “Assembler translates assembly language into machine code.” |
| Compiler | “Runs code line by line.” | That is interpreter | “Compiler translates the whole code before execution.” |
| Interpreter | “Creates executable file.” | Compiler creates executable file | “Interpreter translates and executes line by line; no separate executable file.” |
| IDE | “It writes code.” | Need specific function | “Code editor allows programmer to write/change code.” |
| Auto-completion | “Fixes errors.” | Confused with diagnostics / auto-correction | “Suggests command words while typing.” |
| Prettyprint | “Prints code.” | Misread term | “Colours/formats code to make it easier to read.” |


---

## Fast Revision Tables
### Must-know Definitions
| Term | Definition |
| --- | --- |
| **System software** | software that provides services required by the computer |
| **Application software** | software that provides services required by the user |
| **Utility software** | system software used to manage, maintain or protect the computer |
| **Operating system** | system software that manages main functions of the computer |
| **Firmware** | software/instructions programmed into hardware, often stored in ROM |
| **Interrupt** | a signal sent to the processor to request attention |
| **ISR / interrupt handler** | program/routine that services an interrupt |
| **High-level language** | language closer to human language and easier to read/write/debug |
| **Low-level language** | language closer to machine code and hardware |
| **Assembly language** | low-level language that uses mnemonics |
| **Compiler** | translator that translates the whole high-level program before execution |
| **Interpreter** | translator that translates and executes high-level code line by line |
| **Assembler** | translator that translates assembly language into machine code |
| **IDE** | software suite used to write, run, test and debug programs |


---

### “Choose the best translator” Table
| Scenario | Best translator | Reason |
| --- | --- | --- |
| Debugging during development | Interpreter | stops at the line where an error is found |
| Testing sections of incomplete code | Interpreter | can test without complete program code |
| Final program distribution | Compiler | creates executable file |
| Protecting source code | Compiler | executable can be distributed without source code |
| Assembly language program | Assembler | translates assembly into machine code |
| High-level language program | Compiler / Interpreter | both translate high-level code |


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
Answer these in exam style.

1. State one example of system software. **[1]**
2. State one example of application software. **[1]**
3. Give one function of an operating system. **[1]**
4. State what is meant by firmware. **[1]**
5. Give one example of a hardware interrupt. **[1]**
6. Give one example of a software interrupt. **[1]**
7. Give the name of the translator used for assembly language. **[1]**
8. State one advantage of a high-level language and one advantage of a low-level language. **[2]**
9. State one IDE function and explain how it helps a programmer. **[1]**

## Quick Check Answers
1. Operating system / utility software / device driver.
2. Word processor / spreadsheet / database / web browser / image editor.
3. Managing files / handling interrupts / managing memory / managing multitasking / providing interface / etc.
4. Software/instructions programmed into hardware, usually stored in ROM.
5. Key press / mouse click / printer out of paper / printer out of ink.
6. Division by zero / two processes trying to access same memory location.
7. Assembler.
8. High level: easier to read/write/debug or portable; low level: direct hardware/register control, compact code or potentially efficient execution. Award one for each side.
9. One valid linked pair, for example error diagnostics identify/report an error and help locate it, or a run-time environment executes the program so its behaviour can be tested.

---

## 20-Mark Exam Practice

**Total: 20 marks**
### Question 1｜Software Types **[4]**
A student uses a computer to complete homework.
Describe the difference between system software and application software. Give one example of each.

#### Question 1 Mark Scheme
Any four from:

+ System software provides the services the computer requires.
+ System software manages / maintains hardware and software.
+ Example: operating system / utility software / device driver.
+ Application software provides the services the user requires.
+ Application software allows the user to perform tasks.
+ Example: word processor / spreadsheet / database / web browser / image editor.

---

### Question 2｜Operating System Memory Management **[3]**
Describe the role of the operating system in managing memory.

#### Question 2 Mark Scheme
Any three from:

+ Allocates memory to processes.
+ Deallocates memory when processes are finished.
+ Checks that processes have enough memory available.
+ Makes sure memory is used efficiently.
+ Makes sure two processes do not access the same memory location.
+ Keeps track of free and occupied memory locations.

---

### Question 3｜Interrupts **[5]**
A key is pressed on a keyboard while a computer is running another process.

(a) Give the type of interrupt generated. **[1]**
(b) Give the name of the program/routine used to service the interrupt. **[1]**
(c) Describe how the interrupt is handled. **[3]**

#### Question 3 Mark Scheme
(a) Hardware interrupt.
(b) Interrupt service routine / interrupt handler.
(c) Any three from:

+ CPU / OS checks priority of the interrupt.
+ Current process is halted if the interrupt has higher priority.
+ Status of current process is saved / stored on stack.
+ Source of interrupt is checked.
+ ISR / interrupt handler is called.
+ Interrupt is serviced.
+ Saved status is restored.
+ Original process continues.

---

### Question 4｜Compiler and Interpreter **[4]**
Explain why a programmer may use an interpreter during development but a compiler for the final program.

#### Question 4 Mark Scheme
Any four from:

+ Interpreter translates and executes code line by line.
+ Interpreter stops when an error is found.
+ This helps debug the program.
+ The program can continue once the error is corrected.
+ Compiler translates the whole program before execution.
+ Compiler creates an executable file.
+ The compiler is not needed to run the final program.
+ The source code does not need to be distributed.

---

### Question 5｜IDE Functions **[4]**
A programmer uses an IDE to create a program.
Describe two functions of an IDE and explain how each helps the programmer.

#### Question 5 Mark Scheme
One mark for function + one mark for matching role description, max four:

+ Code editor: allows the programmer to write/change code.
+ Run-time environment: allows the programmer to run code and see output.
+ Error diagnostics: helps find errors in the code.
+ Auto-completion: suggests command words while typing.
+ Auto-correction: corrects misspelled command words.
+ Prettyprint / syntax highlighting: colours / formats code to make it easier to read.
+ Translator: translates code into machine code / low-level language.

---

## Final Revision Checklist

- [ ] I can distinguish system/application software and explain OS functions.
- [ ] I can describe interrupt handling in the correct order.
- [ ] I can compare high-level/low-level languages and translators.
- [ ] I can explain how named IDE tools improve development.
- [ ] I can complete and self-mark both chapter practices.
