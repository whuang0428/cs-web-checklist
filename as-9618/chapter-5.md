# AS 9618 Chapter 5: System Software

<div class="chapter-meta"><strong>AS 9618 · Paper 1</strong><span>9618 · 2027–2029 · Version 2</span></div>

## Official Syllabus Checklist

Revise: operating systems and utilities; program libraries; translators and integrated development environments.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.


<span id="_3-one-page-mind-map" class="legacy-anchor" aria-hidden="true"></span>

## Chapter at a Glance

Use this overview to explain management, choose support software, trace translation and use development tools.

### Explain OS management

<span lang="zh-CN">不要只写“操作系统管理电脑”，要指出资源和动作。</span>

- The OS provides an interface and an environment in which applications run.
- It allocates memory, schedules processes and manages files, hardware and security.
- It detects errors and coordinates access to shared system resources.

**Exam cue:** Name the resource, describe the OS action and state why it is needed.

### Choose utilities and libraries

<span lang="zh-CN">根据任务区分维护工具与可复用程序代码。</span>

- Utility software performs maintenance such as backup, malware checking and disk repair.
- Compression, formatting and defragmentation utilities change storage organisation or use.
- Program libraries provide tested reusable routines, including dynamically linked libraries.

**Exam cue:** Match the named utility or library benefit to the scenario.

### Trace translation

<span lang="zh-CN">说明翻译单位、输出结果和错误出现的时间。</span>

- An assembler translates assembly language instructions into machine code.
- A compiler translates a whole high-level program, while an interpreter works statement by statement.
- Java source can be compiled to bytecode and executed by a virtual machine.

**Exam cue:** Compare complete translation, execution method and error reporting.

### Use IDE tools

<span lang="zh-CN">把每个开发工具与调试或编写代码的具体帮助联系起来。</span>

- Coding prompts, syntax checks and prettyprint help create readable valid code.
- Breakpoints and single stepping pause execution at controlled points.
- A watch window displays changing variable values while the program runs.

**Exam cue:** Explain what the tool reveals or prevents during development.

---

## 5.1 Operating Systems

### Why a computer system requires an OS

#### Student-friendly explanation

Operating System <span lang="zh-CN">就像电脑的</span>“<span lang="zh-CN">总管</span>”。<span lang="zh-CN">没有</span> OS，<span lang="zh-CN">普通用户和</span> application software <span lang="zh-CN">很难直接控制硬件</span>。OS <span lang="zh-CN">提供一个环境</span>，<span lang="zh-CN">让程序可以运行</span>，<span lang="zh-CN">也帮用户和硬件之间进行沟通</span>。

#### Mark scheme answer

> An operating system is needed to provide an interface between the user/application software and the hardware, to manage hardware and system resources, and to provide an environment in which applications can run.

#### Required ideas / marking points

+ **interface**
+ **user**
+ **application software**
+ **hardware**
+ **resources**
+ **manage**
+ **environment**
+ **run applications**

#### Common weak answer

> The OS controls the computer.

This is too vague. You need to say **what it controls / manages** and **why it is needed**.

---

### Key OS management tasks

#### Exam structure

If the question asks “Describe management tasks carried out by the OS”, use this structure:

```mermaid
flowchart TD
A[OS management task] --> B[Name the task]
B --> C[Say what the OS does]
C --> D[Apply to device / user / program]
```

---

### Memory management

#### Meaning

Memory management <span lang="zh-CN">是</span> OS <span lang="zh-CN">管理</span> main memory / RAM <span lang="zh-CN">的过程</span>。<span lang="zh-CN">它决定哪些</span> programs <span lang="zh-CN">和</span> data <span lang="zh-CN">放进</span> RAM，<span lang="zh-CN">分配多少</span> memory，<span lang="zh-CN">并防止程序互相破坏数据</span>。

#### Mark scheme phrases

> The OS allocates memory to programs and data.  
> It keeps track of which memory locations are in use.  
> It prevents one process from accessing memory allocated to another process.  
> It may use virtual memory when RAM is insufficient.

#### What to remember

| Point | Student explanation |
| --- | --- |
| Allocate memory | <span lang="zh-CN">给正在运行的程序分配</span> RAM |
| Deallocate memory | <span lang="zh-CN">程序结束后释放</span> RAM |
| Track memory | <span lang="zh-CN">记录哪些</span> memory locations <span lang="zh-CN">正在被用</span> |
| Memory protection | <span lang="zh-CN">防止一个</span> program <span lang="zh-CN">改到另一个</span> program <span lang="zh-CN">的</span> memory |
| Virtual memory | RAM <span lang="zh-CN">不够时</span>，<span lang="zh-CN">用</span> secondary storage <span lang="zh-CN">的一部分临时代替</span> |

#### Common mistake

| Mistake | Correction |
| --- | --- |
| “Memory management stores files permanently.” | Permanent files are stored on secondary storage; memory management mainly controls RAM. |
| “RAM is unlimited.” | RAM is limited; OS must allocate it carefully. |
| “Virtual memory makes computer faster.” | Not always. It allows more programs to run but is slower than RAM. |

---

### File management

#### Meaning

File management <span lang="zh-CN">是</span> OS <span lang="zh-CN">管理</span> files <span lang="zh-CN">和</span> folders/directories <span lang="zh-CN">的功能</span>。2024 Paper 1 <span lang="zh-CN">特别喜欢问这个</span>。

#### Mark scheme answer

> The OS manages files and directories by allowing files to be created, named, opened, saved, copied, moved, deleted and organised. It keeps track of file locations and controls access permissions.

#### Keywords

+ **create**
+ **open**
+ **save**
+ **copy**
+ **move**
+ **rename**
+ **delete**
+ **directories / folders**
+ **file location**
+ **permissions / access rights**

#### 2024-style answer bank

| Question wording | Strong answer |
| --- | --- |
| Describe file management tasks | Creates, deletes, moves and renames files/folders; stores file metadata and file locations |
| How does OS help user organise files? | Allows directories/folders and paths to group related files |
| How can OS protect files? | Uses permissions/access rights so only authorised users can read/write/delete files |

#### Common mistake

> “File management backs up files.”

Backup is usually **utility software**, not the core meaning of file management.

---

### Security management

#### Meaning

Security management <span lang="zh-CN">是</span> OS <span lang="zh-CN">防止</span> unauthorised access，<span lang="zh-CN">保护</span> data <span lang="zh-CN">和</span> resources。

#### Mark scheme phrases

> The OS manages user accounts and passwords.  
> It controls access rights / permissions.  
> It prevents unauthorised access to files and resources.  
> It may support security updates and system protection.

#### Examples

| Method | How it protects |
| --- | --- |
| User account | Identifies each user |
| Password / authentication | Checks the user is allowed to access the system |
| Access rights | Controls what files/resources a user can read/write/delete |
| Automatic updates | Fixes security vulnerabilities |
| Lock screen / timeout | Stops unauthorised access when user leaves device |

#### Weak vs strong answer

| Weak | Strong |
| --- | --- |
| “The OS keeps it safe.” | “The OS uses user accounts, passwords and access rights to prevent unauthorised access.” |

---

### Hardware / peripheral management

#### Meaning

The OS manages input/output devices and peripherals. It allows communication between hardware and software.

#### Mark scheme phrases

> The OS uses device drivers to allow communication with peripheral devices.  
> It sends data to output devices and receives data from input devices.  
> It uses buffers to manage different data transfer speeds.  
> It handles interrupts from devices.

#### Important terms

| Term | Meaning |
| --- | --- |
| Device driver | Software that allows OS to communicate with a hardware device |
| Buffer | Temporary storage used when two devices work at different speeds |
| Interrupt | Signal sent to CPU/OS when a device needs attention |
| Spooling | Storing print jobs in a queue before sending them to printer |

#### Scenario example

A printer is much slower than the CPU.

> The OS sends print data to a buffer/spool. The printer takes data from the buffer at its own speed. This allows the CPU/program to continue with other tasks.

---

### Process management

#### Meaning

Process management <span lang="zh-CN">是</span> OS <span lang="zh-CN">管理正在运行的</span> programs/processes。<span lang="zh-CN">它决定哪个</span> process <span lang="zh-CN">使用</span> CPU，<span lang="zh-CN">什么时候运行</span>，<span lang="zh-CN">以及如何切换</span>。

#### Mark scheme answer

> The OS schedules processes, allocates processor time, manages multitasking, changes process states and ensures that processes do not interfere with each other.

#### Key ideas

| Concept | Explanation |
| --- | --- |
| Process | A program currently running |
| Scheduling | Deciding which process uses CPU next |
| Processor time | CPU time allocated to each process |
| Multitasking | More than one process appears to run at the same time |
| Process state | ready / running / blocked / waiting |
| Context switching | Saving one process state and loading another |

#### Common mistake

> “Process management means writing programs.”

No. It means managing **running programs**.

---

## Utility Software

### What is utility software?

Utility software <span lang="zh-CN">是</span> system software <span lang="zh-CN">的一种</span>，<span lang="zh-CN">用来维护</span>、<span lang="zh-CN">保护</span>、<span lang="zh-CN">优化或管理</span> computer system。

#### Mark scheme answer

> Utility software is system software used to maintain, protect, analyse or improve the operation of a computer system.

#### Syllabus examples

+ **disk formatter**
+ **virus checker**
+ **defragmentation software**
+ **disk contents analysis / disk repair software**
+ **file compression**
+ **back-up software**

---

### Back-up software

#### Meaning

Back-up software creates copies of files/data so they can be restored if the original is lost or damaged.

#### Mark scheme phrases

> It creates a copy of data/files.  
> The copy can be used to restore data after accidental deletion, corruption, hardware failure or malware attack.

#### 2024-style answer

> Back-up software is needed because the file may be accidentally deleted, corrupted or lost due to hardware failure. A backup copy can be restored so the user does not need to recreate the file.

#### Common mistake

| Mistake | Correction |
| --- | --- |
| “Backup stops data being deleted.” | Backup does not stop deletion; it allows recovery. |
| “Backup is the same as archive.” | Backup is for recovery; archive is long-term storage. |
| “Backup always stores everything.” | It may be full, incremental or differential, but AS usually only needs general recovery idea. |

---

### File compression utility

#### Meaning

File compression software reduces file size.

#### Benefits

| Benefit | Explanation |
| --- | --- |
| Less storage | File takes up less space |
| Faster upload/download | Less data needs to be transferred |
| Less bandwidth | Useful when emailing/transmitting files |
| Easier to send as attachment | May fit within file size limit |

#### Mark scheme answer

> Compression reduces the file size, so the file needs less storage space and can be transmitted/downloaded faster using less bandwidth.

#### Exam warning

Do not say “compression makes the file better quality”. It usually reduces size, not improve quality.

---

### Virus checker / anti-virus utility

#### Meaning

A virus checker scans files/programs for malware.

#### Mark scheme phrases

> It scans files for known malware signatures.  
> It can quarantine/delete infected files.  
> It can prevent malware from running.  
> It needs regular updates to detect new threats.

#### Common mistake

> “A virus checker guarantees no virus.”

No. It reduces risk but cannot guarantee perfect protection.

---

### Defragmentation software

#### Meaning

Defragmentation reorganises file fragments on a magnetic hard disk so parts of a file are stored contiguously.

#### Mark scheme phrases

> It rearranges file fragments so each file is stored in contiguous blocks.  
> This reduces disk head movement and can improve access speed on an HDD.

#### Important limitation

Defragmentation is mainly relevant to **magnetic hard disks**, not SSDs.

---

### Disk formatter

#### Meaning

Disk formatter prepares a storage device for use.

#### Mark scheme phrases

> It prepares the disk for storing files.  
> It creates a file system / directory structure.  
> It may erase existing data.

---

### Disk contents analysis / disk repair

#### Meaning

Disk analysis checks storage usage and errors. Disk repair attempts to fix file system errors or mark bad sectors.

#### Mark scheme phrases

> It analyses how storage space is used.  
> It checks the disk for errors.  
> It attempts to repair file system errors or prevent use of damaged areas.

---

## Program Libraries and DLL Files

### What is a program library?

A program library is a collection of pre-written routines/modules that programmers can use in their own software.

#### Mark scheme answer

> A program library contains existing code/routines that can be reused by programmers when developing software.

#### Benefits to developer

| Benefit | Explanation |
| --- | --- |
| Saves time | Developer does not need to write common code again |
| Reduces errors | Library routines may already be tested |
| Allows reuse | Same routine can be used in many programs |
| Modular design | Program can be built from smaller parts |
| Specialist functions | Developer can use complex functions written by experts |
| Easier maintenance | Library routine can be updated instead of rewriting every program |

#### 2024-style answer

> Using library files saves development time because the student can reuse existing routines. The routines may already have been tested, so there are fewer errors. It also allows the program to be developed in modules.

---

### Dynamic Link Library (DLL)

#### Meaning

A DLL is a library file that is linked/loaded when the program runs, not permanently copied into every executable.

#### Mark scheme phrases

> A DLL can be shared by several programs.  
> It is loaded at run time when required.  
> It reduces memory/storage use because the same library code is not copied into every program.  
> Updating the DLL can update the shared routine for programs that use it.

#### Common mistake

| Mistake | Correction |
| --- | --- |
| “DLL means the code is rewritten each time.” | DLL means shared code can be reused/loaded when needed. |
| “DLL is part of source code only.” | It is a linked library file used by executable programs. |
| “DLL always makes program faster.” | It mainly saves memory/storage and supports shared updates. |

---

## 5.2 Language Translators

### Why translators are needed

Computers execute machine code. Programmers usually write high-level language or assembly language. Translators convert code into a form the processor can execute.

#### Mark scheme answer

> A translator converts a program written in assembly language or a high-level language into machine code/object code so it can be executed by the processor.

---

### Assembler

#### Meaning

Assembler translates assembly language into machine code.

#### Mark scheme answer

> An assembler translates assembly language instructions into machine code.

#### Exam warning

Do not say an assembler translates Java or other high-level source code. It translates **assembly language**.

---

### Compiler

#### Meaning

Compiler translates the whole high-level language program into object code / executable code before it is run.

#### Mark scheme phrases

> Translates the whole program before execution.  
> Produces object code / executable code.  
> The executable can be run without translating the source code again.  
> Lists errors after compilation.

#### Benefits

| Benefit | Explanation |
| --- | --- |
| Faster execution after translation | Object code runs directly |
| Source code not needed by user | Helps protect source code |
| Errors can be listed together | Developer can fix many errors |
| Program can be distributed as executable | End user does not need compiler/source |

#### Drawbacks

| Drawback | Explanation |
| --- | --- |
| Compilation can take time | Whole program translated first |
| Harder to debug line-by-line | Errors are not found interactively during execution |
| Object code may be platform dependent | May need recompilation for different processor/OS |

---

### Interpreter

#### Meaning

Interpreter translates and executes high-level language instructions one statement at a time.

#### Mark scheme phrases

> Translates and executes one line/statement at a time.  
> Stops when it finds an error.  
> No separate executable/object code is produced.  
> Useful during development and debugging.

#### Benefits

| Benefit | Explanation |
| --- | --- |
| Easier debugging | Stops at the line with an error |
| Good for testing | Program can be run quickly during development |
| More portable if interpreter exists | Source can run on any system with suitable interpreter |

#### Drawbacks

| Drawback | Explanation |
| --- | --- |
| Slower execution | Each statement is translated during execution |
| Source code needed | User may need access to source code |
| Error later in program not found until reached | It stops when execution reaches the error |

---

### Compiler vs interpreter exam comparison

| Feature | Compiler | Interpreter |
| --- | --- | --- |
| Translation | Whole program before execution | One statement at a time |
| Output | Object/executable code | Usually no separate executable |
| Execution speed after translation | Faster | Slower |
| Error reporting | Many errors after compilation | Stops at first error encountered |
| Source code needed to run | Not usually | Usually yes |
| Good for | Final distributed program | Development/testing/debugging |

#### Mark scheme style answer

> A compiler is suitable for a finished program because it produces executable code that runs faster and can be distributed without source code. An interpreter is suitable during development because it executes code statement by statement and stops at the line where an error occurs, making debugging easier.

---

### Java partial compilation and interpretation

#### What AS students need

Java-style execution is often described as partly compiled and partly interpreted.

```mermaid
flowchart LR
A[Java source code] --> B[Compiler]
B --> C[Bytecode]
C --> D[Virtual Machine]
D --> E[Interpreted / executed on target computer]
```

#### Mark scheme answer

> A Java program may be compiled into bytecode. The bytecode is then interpreted/executed by a virtual machine on the target computer.

#### Benefits

| Benefit | Explanation |
| --- | --- |
| Portable | Same bytecode can run on different systems with a suitable virtual machine |
| Some speed benefit | Bytecode is partly translated before execution |
| Easier distribution | Bytecode can be distributed instead of source code |

#### Common mistake

> “Java is only compiled” or “Java is only interpreted.”

For AS 9618, remember: **partially compiled and partially interpreted**.

---

## Integrated Development Environment (IDE)

### What is an IDE?

An IDE is software that provides tools to help programmers write, test, debug and maintain programs.

#### Mark scheme answer

> An IDE provides tools for coding, error detection, presentation and debugging when developing programs.

---

### Coding feature: context-sensitive prompts

#### Meaning

Context-sensitive prompts suggest possible commands, variables, functions or parameters depending on where the programmer is typing.

#### Mark scheme phrases

> Suggests valid keywords/functions/variables while code is being typed.  
> Reduces typing errors and speeds up coding.

#### Example

If a programmer types `print`, the IDE may suggest the correct function syntax or available variables.

---

### Initial error detection: dynamic syntax checks

#### Meaning

Dynamic syntax checking checks code while it is being typed or before full execution.

#### Mark scheme phrases

> Highlights syntax errors as code is typed.  
> Identifies missing brackets, incorrect keywords or invalid punctuation.  
> Allows programmer to correct errors earlier.

#### Common mistake

> “Dynamic syntax check finds all logic errors.”

No. It mainly finds **syntax errors**, not all logical errors.

---

### Presentation features

2024 Paper 1 asked students to identify and describe presentation features. You need **feature + description**.

| Feature | Description |
| --- | --- |
| Prettyprint | Automatically formats code using indentation, spacing and layout |
| Expand / collapse code blocks | Hides or shows sections of code such as procedures or loops |
| Line numbering | Displays line numbers to help locate code/errors |
| Colour coding / syntax highlighting | Shows keywords, strings, comments in different colours/styles |

#### Mark scheme style

> Prettyprint formats code with indentation and spacing so the program is easier to read.  
> Collapse code blocks hides sections of code so the programmer can focus on one part of the program.

---

### Debugging features

2024 Paper 1 also asked students to identify and describe debugging features.

| Feature | Description |
| --- | --- |
| Single stepping | Executes one line/instruction at a time |
| Breakpoint | Stops execution at a selected line |
| Watch window / variable report | Shows current values of variables/expressions |
| Error report window | Displays error messages and sometimes line numbers |
| Trace | Shows sequence of statements executed |

#### Mark scheme style

> A breakpoint stops the program at a chosen line so the programmer can inspect variable values at that point.  
> A watch window displays the value of selected variables or expressions while the program is running.

#### Common mistake

| Mistake | Correction |
| --- | --- |
| Only naming “breakpoint” | Add what it does |
| Saying “prettyprint finds errors” | Prettyprint is presentation, not debugging |
| Saying “single stepping runs the whole program” | It executes one line at a time |
| Saying “watch window changes variable automatically” | It displays values; it does not necessarily change them |

---

## Mark Scheme Keywords

### Operating System

+ **interface between user/application and hardware**
+ **manages resources**
+ **allows applications to run**
+ **memory management**
+ **file management**
+ **security management**
+ **hardware/peripheral management**
+ **process management**
+ **device drivers**
+ **buffers**
+ **interrupts**
+ **allocates processor time**
+ **schedules processes**

### Utility Software

+ **maintain / protect / optimise**
+ **backup copy**
+ **restore data**
+ **accidental deletion**
+ **corruption**
+ **hardware failure**
+ **reduces file size**
+ **less storage**
+ **less bandwidth**
+ **faster transmission**
+ **scan / quarantine / delete malware**
+ **defragment / contiguous blocks**
+ **disk formatter / file system**

### Program Libraries

+ **existing code**
+ **pre-written routines**
+ **reusable**
+ **tested**
+ **save development time**
+ **reduce errors**
+ **modular**
+ **Dynamic Link Library**
+ **loaded at runtime**
+ **shared by multiple programs**

### Language Translators

+ **source code**
+ **object code**
+ **machine code**
+ **assembler**
+ **compiler**
+ **interpreter**
+ **whole program**
+ **one statement at a time**
+ **executable**
+ **error reporting**
+ **bytecode**
+ **virtual machine**

### IDE

+ **context-sensitive prompts**
+ **dynamic syntax checks**
+ **prettyprint**
+ **expand / collapse code blocks**
+ **single stepping**
+ **breakpoints**
+ **watch window**
+ **variables / expressions report window**

---

## Topic-Specific Common Confusions

| Mistake | Why it loses marks | Correct version |
| --- | --- | --- |
| OS is “software that controls computer” only | Too vague | Say interface + manages resources + lets applications run |
| Confusing file management with backup | Different syllabus areas | File management organises files; backup copies/restores data |
| Saying defragmentation is for all storage | Not precise | Mainly for magnetic hard disks |
| Saying backup prevents data loss | Too absolute | Backup allows recovery after loss/corruption |
| Saying library means “internet library” | Wrong context | Program library = reusable code/routines |
| Saying compiler runs one line at a time | Wrong | Interpreter translates/executes one statement at a time |
| Saying interpreter produces executable file | Usually wrong | Compiler produces object/executable code |
| Naming IDE feature without description | Often only half answer | Give feature + what it does |
| Saying syntax check finds logic errors | Wrong | Syntax check finds grammar/structure errors |
| Mixing presentation and debugging features | Common Paper 1 error | Prettyprint = presentation; breakpoint = debugging |

---

## Scenario Answer Bank

### Scenario 1: Student writes a program in an IDE

**Question:** Explain how IDE debugging features help the student.

**Answer template:**

> The student can use **single stepping** to execute the program one line at a time, so they can see where the error occurs. They can set a **breakpoint** to pause the program at a chosen line. They can use a **watch window** to view the current values of variables and expressions while the program is running.

---

### Scenario 2: Program code is emailed as an attachment

**Question:** Explain benefits of compressing the file.

**Answer template:**

> Compression reduces the file size, so the attachment uses less storage and less bandwidth. It can be uploaded and downloaded faster, and it is more likely to fit within an email attachment size limit.

---

### Scenario 3: Laptop stores important coursework

**Question:** Explain need for backup software.

**Answer template:**

> Backup software creates a copy of the coursework files. If the original file is accidentally deleted, corrupted, lost due to hardware failure, or affected by malware, the student can restore the file from the backup.

---

### Scenario 4: Team creates a program library

**Question:** Explain benefits to programmers.

**Answer template:**

> A program library allows programmers to reuse existing routines, so they do not need to write the same code again. The routines may already be tested, reducing errors. It also supports modular development because different parts of the program can use the same shared routines.

---

### Scenario 5: Finished commercial program

**Question:** Justify compiler rather than interpreter.

**Answer template:**

> A compiler is suitable because it translates the whole program into executable/object code. The finished program runs faster because it does not need to be translated line-by-line during execution. The source code does not need to be distributed to users, which helps protect the developer's code.

---

### Scenario 6: Program is still being developed

**Question:** Justify interpreter rather than compiler.

**Answer template:**

> An interpreter is suitable during development because it translates and executes one statement at a time. It stops when it finds an error, making it easier for the programmer to locate and fix errors during testing.

---

## Process Diagram: OS + Application + Hardware

```mermaid
flowchart TD
U[User] --> A[Application Software]
A --> OS[Operating System]
OS --> M[Memory Management]
OS --> F[File Management]
OS --> S[Security Management]
OS --> H[Hardware / Peripheral Management]
OS --> P[Process Management]
H --> D[Device Drivers]
H --> B[Buffers]
H --> I[Interrupts]
OS --> HW[Hardware]
```

---

## Process Diagram: Translator Choice

```mermaid
flowchart TD
A[Program code] --> B{Language type?}
B -->|Assembly language| C[Assembler]
C --> D[Machine code]
B -->|High-level finished program| E[Compiler]
E --> F[Object / executable code]
B -->|High-level development / testing| G[Interpreter]
G --> H[Translate and execute statement by statement]
B -->|Java-style| I[Compile to bytecode]
I --> J[Virtual machine interprets / executes bytecode]
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

1. State two reasons why a computer system requires an OS. **[2]**
2. Give two file management tasks carried out by an OS. **[2]**
3. Explain why backup software is needed. **[2]**
4. State one benefit of using a program library. **[1]**
5. Identify one presentation feature of an IDE and describe it. **[2]**
6. State the purpose of an assembler. **[1]**

## Quick Check Answers

1. Any two:
   + provides interface between user/application and hardware
   + manages system resources
   + allows applications to run
   + manages hardware/peripherals/files/memory/processes/security  
2. Any two:
   + create / open / save / copy / move / rename / delete files
   + organise files into directories/folders
   + keep track of file locations
   + manage file permissions  
3. Creates copies of files/data; can restore data after accidental deletion / corruption / hardware failure / malware attack.  
4. Reuses existing tested code / saves development time / reduces errors / supports modular development.  
5. Example:
   + Prettyprint: automatically formats code with indentation and spacing.
   + Expand/collapse: hides or shows code blocks to make code easier to navigate.
   + Line numbering: shows line numbers to help find errors.  
6. Translates assembly language into machine code.

---

## 20-Mark Exam Practice

**Total: 20 marks**

### Question 1: Operating System and Utility Software **[8]**

A student uses a laptop to write a program. The laptop has an Operating System and several utility programs.

#### (a) Explain why the laptop requires an Operating System. **[3]**

#### (b) Describe two file management tasks carried out by the Operating System. **[2]**

#### (c) The student uses backup software. Explain why backup software is needed. **[3]**

---

### Question 2: Program Libraries and IDE **[7]**

A team of programmers is developing a large program using an IDE. They decide to create and use program libraries.

#### (a) Explain three benefits of using program libraries. **[3]**

#### (b) Identify and describe one coding feature of an IDE. **[2]**

#### (c) Identify and describe one debugging feature of an IDE. **[2]**

---

### Question 3: Language Translators **[5]**

A programmer writes a high-level language program.

#### (a) Explain one benefit of using a compiler instead of an interpreter for the finished program. **[2]**

#### (b) Explain one benefit of using an interpreter during development. **[2]**

#### (c) State what is meant by Java being partially compiled and partially interpreted. **[1]**

---

## Practice Mark Scheme

### Question 1 Mark Scheme **[8]**

#### (a) OS purpose **[3]**

Award 1 mark each:

+ provides an interface between user/application software and hardware
+ manages system resources / hardware / memory / files / processes
+ provides an environment for applications to run
+ hides hardware complexity from user/programs
+ handles input/output/peripherals

#### (b) File management **[2]**

Award 1 mark each:

+ create / open / save / copy / move / rename / delete files
+ organise files into directories/folders
+ keep track of file locations / paths
+ manage file permissions/access rights

#### (c) Backup software **[3]**

Award 1 mark each:

+ creates copies of files/data
+ backup copy can be restored
+ after accidental deletion / corruption / hardware failure / malware attack / loss of original

---

### Question 2 Mark Scheme **[7]**

#### (a) Program libraries **[3]**

Award 1 mark each:

+ reuse existing code/routines
+ saves development time
+ routines may already be tested, reducing errors
+ supports modular development
+ allows specialist routines to be used
+ easier maintenance/update of shared code

#### (b) IDE coding feature **[2]**

1 mark for feature, 1 mark for description:

+ context-sensitive prompts suggest valid commands/variables/functions depending on code context
+ auto-completion completes keywords/identifiers to reduce typing errors

#### (c) IDE debugging feature **[2]**

1 mark for feature, 1 mark for description:

+ breakpoint stops program at a chosen line
+ single stepping executes one line at a time
+ watch window/report window displays variable/expression values
+ trace shows statements executed

---

### Question 3 Mark Scheme **[5]**

#### (a) Compiler benefit **[2]**

Award 1 mark each:

+ produces object/executable code
+ executable runs faster because it does not need statement-by-statement translation
+ source code does not need to be distributed
+ suitable for final distribution

#### (b) Interpreter benefit **[2]**

Award 1 mark each:

+ translates/executes one statement at a time
+ stops at line with error
+ easier to debug/test during development
+ no need to compile whole program before testing

#### (c) Java partial compilation/interpreting **[1]**

+ Source code is compiled into bytecode, then bytecode is interpreted/executed by a virtual machine.

---

## Final Revision Checklist

- [ ] I can explain OS management, utilities and libraries/DLLs.
- [ ] I can compare compiler, interpreter and assembler operation.
- [ ] I can explain Java bytecode and virtual-machine execution.
- [ ] I can select IDE tools for syntax, runtime and logic faults.
- [ ] I can complete and self-mark both chapter practices.
