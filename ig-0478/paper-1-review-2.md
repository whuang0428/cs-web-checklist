# IGCSE 0478 Paper 1 Mixed Review — Set B

> **Original practice paper:** an independent second set. Its scenarios, values and questions are newly written.

## Instructions

- Syllabus: **0478, examinations 2026–2028, Version 5**
- Recommended time: **1 hour 45 minutes**
- Total: **75 marks**
- Do not use a calculator.
- Answer all six questions.
- Show working for every calculation and apply each answer to the stated context.

### Coverage and assessment objectives

| Question | Topic | Marks | AO1 | AO2 | AO3 |
|---:|---|---:|---:|---:|---:|
| 1 | Data representation | 12 | 7 | 3 | 2 |
| 2 | Data transmission | 12 | 7 | 3 | 2 |
| 3 | Hardware | 14 | 8 | 3 | 3 |
| 4 | Software | 11 | 7 | 2 | 2 |
| 5 | The internet and its uses | 14 | 9 | 3 | 2 |
| 6 | Automated and emerging technologies | 12 | 7 | 1 | 4 |
| **Total** | **Topics 1–6** | **75** | **45** | **15** | **15** |

## Question 1 — Data Representation [12]

A sports club stores member numbers, badge images and short voice notes.

1. Convert binary `11010110` to denary. **[2]**
2. Convert denary `94` to hexadecimal. **[2]**
3. Perform the 8-bit binary addition `11001010 + 01011101` and state why overflow occurs. **[3]**
4. A colour badge is `320 × 200` pixels with a colour depth of 16 bits. Calculate its uncompressed size in KiB using `1 KiB = 1024 bytes`. **[3]**
5. Explain why lossless compression is appropriate for a text file containing membership records. **[2]**

## Question 2 — Data Transmission [12]

A theatre transmits ticket data between a front desk and a portable scanner.

1. Distinguish between simplex and full-duplex transmission. **[2]**
2. Explain why packet switching can use network links efficiently when many scanners are active. **[3]**
3. A byte is sent with odd parity. The received bits, including the parity bit, contain six `1` bits. State what the receiver concludes and give one limitation of parity. **[2]**
4. Describe how echo checking can detect an incorrectly transmitted ticket code. **[2]**
5. Explain the complete ARQ response when a packet or its acknowledgement is lost. **[3]**

## Question 3 — Hardware [14]

A design studio uses workstations, a 3D printer and online storage.

1. State what the MAR and MDR store during a memory read. **[2]**
2. Describe the fetch stage from the PC to the CIR. **[4]**
3. Explain how a 3D printer produces a physical model from a digital design. **[3]**
4. Give two reasons why a capacitive touchscreen is suitable for a multi-touch design interface. **[2]**
5. Evaluate storing the studio's only copy of project files in cloud storage. Give one benefit, one risk and one justified action. **[3]**

## Question 4 — Software [11]

A charity commissions a volunteer-management program.

1. Distinguish between system software and application software, giving one example of each. **[4]**
2. Explain how an interrupt allows a printer to request processor attention. **[2]**
3. State two differences between high-level and low-level languages. **[2]**
4. Explain how a compiler reports errors and produces a program that can be distributed. **[3]**

## Question 5 — The Internet and Its Uses [14]

A food bank publishes collection times on a website and accepts online donations.

1. State the purpose of a URL and the purpose of a web server. **[2]**
2. Describe how DNS helps the browser obtain the requested page. **[3]**
3. Explain how secure transmission and two-factor authentication protect different parts of a donation transaction. **[3]**
4. A caller persuades a volunteer to reveal an account reset code. Name the attack and explain why technical controls alone may not prevent it. **[3]**
5. Explain how a blockchain can provide a shared, difficult-to-alter transaction record. **[3]**

## Question 6 — Automated and Emerging Technologies [12]

A recycling centre uses a conveyor, cameras and robotic arms to separate materials.

1. Describe how the monitoring and control loop moves an identified item into the correct container. **[4]**
2. State two characteristics of the robotic arm. **[2]**
3. Explain how a machine-learning system can use labelled camera images to improve its classification decisions. **[3]**
4. Evaluate replacing all manual checking with the trained system. Give one benefit, one limitation and a justified conclusion. **[3]**

## Mark Scheme

### Question 1 Mark Scheme [12]

1. `128 + 64 + 16 + 4 + 2 = 214`; method/place values **[1]**, answer **[1]**. **[2]**
2. `94 = 5 × 16 + 14`, so `5E`; method **[1]**, answer **[1]**. **[2]**
3. The binary result is `1 00100111` **[2]**; the ninth carry bit cannot be represented in eight bits, so overflow occurs **[1]**. **[3]**
4. `320 × 200 × 16 = 1 024 000` bits **[1]**; `÷ 8 = 128 000` bytes **[1]**; `÷ 1024 = 125 KiB` **[1]**. **[3]**
5. Lossless compression preserves every original character/bit **[1]**, so decompression reconstructs the exact membership records without corrupting data **[1]**. **[2]**

### Question 2 Mark Scheme [12]

1. Simplex sends in one direction only **[1]**; full duplex permits simultaneous transmission in both directions **[1]**. **[2]**
2. Messages are divided into packets that share links with other traffic **[1]**; links are not reserved while a scanner is idle **[1]**; packets may take available routes and be reassembled at the destination **[1]**. **[3]**
3. Odd parity requires an odd total, so six `1` bits indicate an error **[1]**; an even number of changed bits may remain undetected **[1]**. **[2]**
4. Receiver sends the received code back **[1]**; sender compares it with the original and detects a mismatch **[1]**. **[2]**
5. Sender starts a timer after transmission **[1]**; no acknowledgement arrives before timeout when the packet or acknowledgement is lost **[1]**; sender retransmits the packet **[1]**. **[3]**

### Question 3 Mark Scheme [14]

1. MAR stores the address being accessed **[1]**; MDR stores the data/instruction transferred to or from memory **[1]**. **[2]**
2. PC address copies to MAR **[1]**; address is sent and memory read is signalled **[1]**; instruction returns to MDR on the data bus **[1]**; it copies to CIR and PC is incremented **[1]**. **[4]**
3. Software slices the model into layers **[1]**; the printer deposits, cures or fuses material for each layer **[1]**; successive layers bond to form the object **[1]**. **[3]**
4. It detects changes in capacitance rather than requiring pressure **[1]** and can detect more than one touch position for gestures **[1]**. **[2]**
5. Benefit such as access from multiple locations or provider-managed redundancy **[1]**; risk such as internet outage, account compromise or dependence on provider **[1]**; justified action such as keep tested independent backups and access controls rather than using cloud as the only copy **[1]**. **[3]**

### Question 4 Mark Scheme [11]

1. System software manages/controls the computer, for example an operating system **[2]**; application software performs a user task, for example the volunteer-management program **[2]**. **[4]**
2. Printer raises a request/flag **[1]**; processor saves state, runs the relevant ISR and resumes the interrupted process **[1]**. **[2]**
3. Any two paired differences: abstraction/readability, portability, hardware control, translation or typical instruction complexity. **[2]**
4. It translates the whole source program and reports detected errors together **[1]**; corrected source is translated to object/executable code **[1]**; the executable can run without the compiler/source being present **[1]**. **[3]**

### Question 5 Mark Scheme [14]

1. URL identifies the protocol/domain/resource location **[1]**; web server stores/delivers requested web resources **[1]**. **[2]**
2. Browser sends the domain to a DNS resolver **[1]**; DNS returns the matching IP address **[1]**; browser connects to that server and requests the resource **[1]**. **[3]**
3. Encryption in a secure connection makes intercepted transaction data unreadable without the key **[1]**; authentication/certificate helps verify the server **[1]**; 2FA means a stolen password alone is insufficient to enter the account **[1]**. **[3]**
4. Social engineering **[1]**; attacker manipulates a person into disclosing the code **[1]**; valid disclosed credentials may appear legitimate to technical controls, so training and verification procedures are also needed **[1]**. **[3]**
5. Transactions are stored in linked blocks/shared copies **[1]**; hashes link blocks so alteration changes later hash values **[1]**; network participants validate/agree updates, making unnoticed unilateral alteration difficult **[1]**. **[3]**

### Question 6 Mark Scheme [12]

1. Camera/sensor captures the item **[1]**; processor compares/classifies the input using stored rules/model **[1]**; control signal operates the appropriate arm/actuator **[1]**; repeated sensing confirms the result and supplies feedback **[1]**. **[4]**
2. Any two: programmable, senses its environment, moves/manipulates objects, performs more than one task, can act automatically. **[2]**
3. Labelled examples provide the expected material category **[1]**; the system identifies patterns/features associated with those examples **[1]**; using more suitable data or feedback allows later decisions to become more accurate **[1]**. **[3]**
4. One contextual benefit such as faster continuous sorting **[1]**; one limitation such as unusual/dirty items being misclassified **[1]**; conclusion linked to the evidence, such as retain sampled human checks until accuracy is demonstrated **[1]**. **[3]**
