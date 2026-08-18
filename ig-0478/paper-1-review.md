# IGCSE 0478 Paper 1 Mixed Review — Set A

> **Original practice paper:** independently written for revision. It is not an official Cambridge paper and does not reproduce a past-paper question.

## Instructions

- Syllabus: **0478, examinations 2026–2028, Version 5**
- Recommended time: **1 hour 45 minutes**
- Total: **75 marks**
- Answer all six questions.
- Show working for every calculation.
- Attempt the complete paper before opening the mark scheme.

### Coverage and assessment objectives

| Question | Topic | Marks | AO1 | AO2 | AO3 |
|---:|---|---:|---:|---:|---:|
| 1 | Data representation | 12 | 7 | 3 | 2 |
| 2 | Data transmission | 12 | 7 | 3 | 2 |
| 3 | Hardware | 13 | 8 | 3 | 2 |
| 4 | Software | 11 | 7 | 2 | 2 |
| 5 | The internet and its uses | 15 | 9 | 3 | 3 |
| 6 | Automated and emerging technologies | 12 | 7 | 1 | 4 |
| **Total** | **Topics 1–6** | **75** | **45** | **15** | **15** |

## Question 1 — Data Representation [12]

A wildlife centre stores identification numbers, photographs and audio recordings.

1. Convert denary `173` to 8-bit binary. **[2]**
2. Convert hexadecimal `B6` to denary. **[2]**
3. Add the two 8-bit binary values `01101101` and `00110111`. State whether overflow occurs. **[3]**
4. A monochrome image is 640 pixels wide and 400 pixels high. Calculate its uncompressed file size in KiB. Show your working and use 1 KiB = 1024 bytes. **[3]**
5. Explain why lossy compression is unsuitable for archiving the centre's only master copy of a research photograph. **[2]**

## Question 2 — Data Transmission [12]

A remote weather station sends readings to a control centre.

1. Distinguish between serial and parallel transmission. **[2]**
2. Give two reasons why serial transmission is suitable for the long cable between the station and the control centre. **[2]**
3. The station sends the seven data bits `1011010` using even parity. State the parity bit and explain your answer. **[2]**
4. Describe how a checksum can be used to detect an error in a transmitted block. **[3]**
5. Explain why automatic repeat request needs both an acknowledgement and a timeout. **[3]**

## Question 3 — Hardware [13]

A museum installs interactive display terminals.

1. State the purpose of the control unit and the arithmetic logic unit. **[2]**
2. Name two registers used in the fetch–decode–execute cycle and state what each holds. **[4]**
3. Explain how increasing cache size can improve processor performance. **[2]**
4. The terminal uses a touch screen instead of a keyboard and mouse. Give two benefits in this context. **[2]**
5. The display stores its operating system on solid-state storage. Explain two advantages of solid-state storage over a magnetic hard disk for this terminal and one disadvantage. **[3]**

## Question 4 — Software [11]

A community theatre uses an application to manage seat bookings.

1. State two functions of an operating system. **[2]**
2. Explain the purpose of an interrupt when a customer clicks a button. **[2]**
3. Distinguish between a compiler and an interpreter. **[3]**
4. Give two integrated development environment features and explain how each supports a programmer. **[4]**

## Question 5 — The Internet and Its Uses [15]

An online ticket service lets customers create accounts and pay for events.

1. Distinguish between the internet and the World Wide Web. **[2]**
2. Explain how a web browser uses a URL and DNS to request a web page from a server. **[3]**
3. Describe two features of a strong password policy. **[2]**
4. A customer receives a message containing a link to a fake login page. Name this threat and explain how it may compromise the account. **[3]**
5. Explain how a firewall and two-factor authentication provide different layers of protection for the service. **[3]**
6. State two characteristics of a digital currency. **[2]**

## Question 6 — Automated and Emerging Technologies [12]

A greenhouse uses sensors, a microprocessor and actuators to control plant conditions.

1. Identify one suitable sensor and one suitable actuator for controlling temperature. **[2]**
2. Describe the feedback process used to maintain the target temperature. **[4]**
3. Give two characteristics that distinguish a robot from a simple automated system. **[2]**
4. The owner proposes an artificial-intelligence system that predicts watering needs. Evaluate this proposal, giving two benefits, two limitations and a justified conclusion. **[4]**

## Mark Scheme

### Question 1 Mark Scheme [12]

1. `10101101`. Award one mark for a correct method or place values and one for the answer. **[2]**
2. `11 × 16 + 6 = 182`. **[2]**
3. `01101101 + 00110111 = 10100100` **[2]**; no overflow because the result fits in eight bits / there is no ninth carry bit **[1]**. **[3]**
4. `640 × 400 × 1 = 256000` bits **[1]**; `256000 ÷ 8 = 32000` bytes **[1]**; `32000 ÷ 1024 = 31.25 KiB` **[1]**. **[3]**
5. Lossy compression permanently removes data **[1]**; the original detail cannot be reconstructed, so future research or editing may use an inaccurate source **[1]**. **[2]**

### Question 2 Mark Scheme [12]

1. Serial sends one bit at a time over one channel; parallel sends several bits simultaneously over multiple channels. **[2]**
2. Any two: fewer wires, lower cost, less interference/crosstalk, less timing skew, more reliable over distance. **[2]**
3. Parity bit `0` **[1]** because the data already contains four `1` bits, an even count **[1]**. **[2]**
4. Sender calculates a value from the block and transmits it **[1]**; receiver independently recalculates the checksum **[1]**; unequal values indicate corruption, although a matching checksum cannot prove that no error occurred **[1]**. **[3]**
5. Acknowledgement confirms successful receipt **[1]**; timeout prevents the sender waiting indefinitely if data or acknowledgement is lost **[1]**; after the timeout, the block is retransmitted **[1]**. **[3]**

### Question 3 Mark Scheme [13]

1. Control unit coordinates processor operations / issues control signals **[1]**; ALU performs arithmetic and logical operations **[1]**. **[2]**
2. Any two valid register-and-content pairs, one mark for the register and one for its content: PC holds the address of the next instruction; MAR holds the address currently being accessed; MDR holds data or an instruction moving to/from memory; CIR holds the current instruction; accumulator stores an intermediate result. **[4]**
3. Cache stores frequently/recently used instructions and data close to the CPU **[1]**, reducing slower main-memory accesses and increasing throughput **[1]**. **[2]**
4. Any two contextual benefits: direct selection, intuitive for visitors, no separate input devices, less desk space, easier sealed/kiosk installation, supports on-screen accessibility controls. **[2]**
5. Any two advantages: faster access, no moving parts, quieter, lower power, more resistant to shock **[2]**; one disadvantage: higher cost per unit of storage or limited write endurance **[1]**. **[3]**

### Question 4 Mark Scheme [11]

1. Any two: user interface, memory management, processor scheduling, peripheral management, file management, security/user management. **[2]**
2. The click causes a signal requesting processor attention **[1]**; the current task state is saved and an interrupt service routine handles the event before execution resumes **[1]**. **[2]**
3. A compiler translates the whole source program and produces executable/object code **[1]**; an interpreter translates and executes one statement at a time **[1]**; compiled code can run without the compiler whereas interpreted execution needs the interpreter / errors are reported differently **[1]**. **[3]**
4. Two explained features, one mark for each feature and one for its support: editor with syntax highlighting, auto-completion, error diagnostics, debugger/breakpoints, translator, run-time environment. **[4]**

### Question 5 Mark Scheme [15]

1. The internet is the global network infrastructure connecting networks/devices **[1]**; the Web is a service of linked pages/resources accessed over the internet **[1]**. **[2]**
2. Browser interprets the URL to identify protocol/domain/resource **[1]**; DNS maps the domain to an IP address **[1]**; browser sends an HTTP/HTTPS request to that server and receives the resource **[1]**. **[3]**
3. Any two: minimum length, mixture of character types where appropriate, block common/compromised passwords, rate limiting/lockout, do not reuse recent passwords. **[2]**
4. Phishing **[1]**; user is deceived into entering credentials on the attacker's page **[1]**; attacker captures and uses the credentials **[1]**. **[3]**
5. Firewall filters network traffic using rules and blocks suspicious/unauthorised connections **[1]**; two-factor authentication requires a second, independent factor **[1]**; stolen password alone is therefore insufficient, so the controls address different attack stages **[1]**. **[3]**
6. Any two: exists electronically, transactions are recorded electronically, may be decentralised, may use a distributed ledger/cryptography, value can change, can transfer without physical cash. **[2]**

### Question 6 Mark Scheme [12]

1. Temperature sensor/thermistor **[1]**; heater, fan, motorised vent or cooling unit **[1]**. **[2]**
2. Sensor repeatedly measures temperature **[1]**; analogue value is converted if required and sent to the microprocessor **[1]**; reading is compared with stored target/range **[1]**; control signal operates or stops the actuator, then new readings provide feedback **[1]**. **[4]**
3. Any two: programmable, can sense its environment, can move/manipulate objects, performs a range of tasks, may make rule-based/autonomous decisions. **[2]**
4. Award one mark each for two valid benefits, such as adapting water to conditions and reducing waste **[2]**; one mark for valid limitations, such as biased/insufficient training data, sensor failure, cost or opaque decisions **[1]**; one mark for a conclusion justified using the scenario, such as trial it with human override and measured validation before full control **[1]**. **[4]**
