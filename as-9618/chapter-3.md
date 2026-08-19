# AS 9618 Chapter 3: Hardware

<div class="chapter-meta"><strong>AS 9618 · Paper 1</strong><span>9618 · 2027–2029 · Version 2</span></div>

## Official Syllabus Checklist

Revise: computer components; memory and storage; logic gates and logic circuits.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.


<span id="_3-one-page-mind-map" class="legacy-anchor" aria-hidden="true"></span>

## Chapter at a Glance

Use this overview to classify hardware, compare storage, trace control and solve logic tasks.

### Classify hardware

<span lang="zh-CN">先判断设备是输入、输出、存储还是嵌入式系统的一部分。</span>

- An embedded system is built into a larger device for a specific task.
- Input devices capture data, while output devices present information or perform an action.
- Choose magnetic, optical or solid-state storage from capacity, speed, durability and cost.

**Exam cue:** Name the hardware and link its feature to the stated use.

### Compare memory and storage

<span lang="zh-CN">用易失性、速度、成本和用途建立比较。</span>

- RAM is volatile working memory, while ROM stores non-volatile instructions such as firmware.
- SRAM is faster and more expensive, while DRAM is denser and requires refreshing.
- PROM, EPROM and EEPROM differ in how stored instructions can be written or erased.

**Exam cue:** Give one paired difference and its consequence for use.

### Trace monitoring and control

<span lang="zh-CN">按传感器、处理器、输出和反馈描述完整控制循环。</span>

- A sensor measures a physical property and sends data to a processor.
- The processor compares the data with stored values and sends an output signal.
- An actuator changes the system, allowing later sensor readings to provide feedback.

**Exam cue:** Apply each stage to the named system and measurement.

### Build logic answers

<span lang="zh-CN">在逻辑表达式、真值表和电路之间逐步转换。</span>

- Recognise NOT, AND, OR, NAND, NOR and XOR gates from symbols or behaviour.
- Evaluate each input combination systematically to complete a truth table.
- Translate between a logic expression, gate circuit and required output condition.

**Exam cue:** Show intermediate outputs so a single error does not corrupt the whole answer.

---

## Syllabus Map

| Syllabus area | What to know | Revision priority |
| --- | --- | --- |
| 3.1 Computers and their components | Input/output/storage devices, embedded systems, main memory, secondary storage, ports, buffers, monitoring/control | Very high |
| 3.2 Logic Gates and Logic Circuits | Logic gate symbols, truth tables, logic expressions, logic circuits | Very high |

---

## 3.1 Computers and Their Components

### Embedded systems

#### Definition

> An embedded system is a computer system built into a larger device, designed to perform a specific / dedicated task.

<span lang="zh-CN">中文理解</span>：
<span lang="zh-CN">嵌入式系统不是一台</span>“<span lang="zh-CN">通用电脑</span>”，<span lang="zh-CN">而是放在某个设备里面</span>，<span lang="zh-CN">只负责几个固定任务</span>。<span lang="zh-CN">比如</span> smart doorbell、washing machine、car braking system、microwave controller。

#### Mark scheme keywords

+ **built into a larger device**
+ **specific task**
+ **dedicated hardware**
+ **dedicated software / firmware**
+ **limited processing requirements**
+ **limited functionality**

#### Good answer structure

> The device is an embedded system because the processor, memory and software are built into the device and are dedicated to a specific task, such as detecting motion / recording video / controlling the device.

#### Drawbacks of embedded systems

| Drawback | Mark scheme style explanation |
| --- | --- |
| difficult to update | firmware cannot be easily changed by the user |
| difficult to repair | troubleshooting may need a specialist |
| limited functionality | designed for one task, not easily adapted |
| may become e-waste | faulty/outdated devices are often thrown away |
| security issue | if not updated, vulnerabilities may remain |

#### Common weak answer

> It is small and cheap.

This may be true in some cases, but it does not prove “embedded”. Use **specific task / built-in / dedicated**.

---

### Input, output and storage devices

#### Input devices

| Device | Data captured |
| --- | --- |
| Keyboard | key presses / text |
| Mouse / touchpad | pointer movement / selection |
| Camera | image / video |
| Microphone | sound |
| Scanner | image of a document |
| Sensor | physical measurement from environment |

#### Output devices

| Device | Output |
| --- | --- |
| Monitor / screen | visual output |
| Speaker | sound |
| Printer | hard copy |
| Actuator | physical movement / action |
| Light / LED | visual signal |

#### Principal operations of required input and output devices

##### Laser printer

1. A drum is given an electrostatic charge.
2. A laser changes the charge to form an image on the drum.
3. Oppositely charged toner is attracted to the image.
4. The toner is transferred to paper.
5. Heated pressure rollers fuse the toner permanently to the paper.

##### 3D printer

1. A digital model is divided into thin layers.
2. The printer deposits, melts or fuses material for one layer.
3. The platform or print head moves and the process repeats until the physical object is complete.

##### Microphone

1. Sound waves make a diaphragm vibrate.
2. A transducer converts the vibration into a changing analogue electrical signal.
3. An ADC samples the signal when digital sound data is required.

##### Speaker

1. A DAC converts digital sound data into an analogue electrical signal when necessary.
2. The changing current in a coil creates a changing magnetic force.
3. The attached cone moves the air and produces sound waves.

##### Touchscreen

1. The display presents visual output and a sensing layer detects a touch.
2. The controller calculates the touch coordinates from a pressure, capacitance or interrupted-beam change.
3. The coordinates are sent to the processor as input and matched to the displayed control.

##### Virtual reality headset

1. Two slightly different images are displayed through lenses to create a stereoscopic view.
2. Orientation and motion sensors detect movement of the user's head or controllers.
3. The processor updates the displayed viewpoint with low delay so the virtual scene follows that movement.

#### Principal-operation drill

- A printer leaves loose toner on a page: the missing final operation is **heating and pressure in the fuser**.
- A recorded waveform contains only analogue voltages: the microphone signal still needs **analogue-to-digital conversion**.
- A VR image does not follow a head turn: the system must read its **orientation sensors** and render a new viewpoint.

#### Storage devices

| Device type | Examples | Main idea |
| --- | --- | --- |
| Magnetic | HDD | uses magnetised areas on platters |
| Optical | CD / DVD / Blu-ray | uses laser and reflective surface |
| Solid-state | SSD / flash drive | uses electronic circuits, no moving parts |

---

### Sensors

#### Common sensors and uses

| Scenario | Suitable sensor | Why |
| --- | --- | --- |
| Door is open / closed | contact / magnetic sensor | detects whether contact is broken |
| Light level is low | light sensor | measures brightness / light intensity |
| Person detected nearby | infrared / motion / proximity sensor | detects movement or distance |
| Item removed from shelf | pressure sensor | detects change in weight / pressure |
| Beam broken by object | infrared sensor | detects interruption of beam |
| Temperature changes | temperature sensor | measures heat / temperature |
| Sound level too high | sound sensor / microphone | detects sound amplitude |

#### Exam answer pattern

> A **pressure sensor** can be used because when the item is removed, the pressure / weight on the shelf decreases. The system can use this change to identify that an item has been taken.

---

### Monitoring systems vs control systems

#### Monitoring system

> A monitoring system collects data from sensors and may store, display or transmit the data, but it does not automatically change the environment being measured.

#### Control system

> A control system collects data from sensors, processes it, and sends a signal to an actuator / output device to change the environment or system.

#### Key difference

| Type | What happens |
| --- | --- |
| Monitoring | sensor data is observed / stored / transmitted |
| Control | sensor data causes an action that changes something |

#### Mark scheme style

> This is a control system because the sensor data is processed and used to send a signal to an output device / actuator, such as turning on a light or sounding an alarm.

#### Common mistake

| Student writes | Why weak |
| --- | --- |
| “It has sensors, so it is monitoring.” | Control systems also use sensors. |
| “It has output, so it is control.” | Need to say the output changes the system/environment. |
| “It analyses data.” | Both monitoring and control may process data. |

---

### Actuators

#### Definition

> An actuator is an output device that converts a control signal into physical movement or action.

#### Examples

| Actuator / output | Action |
| --- | --- |
| motor | opens door / turns fan |
| heater | increases temperature |
| valve | controls water/gas flow |
| speaker / alarm | sounds warning |
| light | turns on/off |

---

### Buffers

#### Definition

> A buffer is an area of memory used to temporarily store data while it is being transferred between devices or processes.

#### Why buffers are used

Buffers are used when:

+ devices work at different speeds
+ data arrives faster than it can be processed
+ data must be written in blocks
+ streaming needs temporary data before playback

#### Mark scheme answer

> The buffer temporarily stores data because the sending device and receiving device work at different speeds. Data can be stored in the buffer until the receiving device is ready to process / write / display it.

#### Examples

| Scenario | Buffer use |
| --- | --- |
| Writing to optical disc | stores data until the disc writer is ready |
| Video streaming | stores received video data before it is displayed |
| Sensor system | stores readings until processor can process them |
| Printer | stores print data while printer prints slowly |

#### Common mistake

> A buffer stores data permanently.

Wrong. A buffer is **temporary storage**.

---

## Memory

### RAM and ROM

| Feature | RAM | ROM |
| --- | --- | --- |
| Full name | Random Access Memory | Read Only Memory |
| Volatile? | volatile | non-volatile |
| Stores | current data, instructions, running programs | firmware, bootstrap/start-up instructions |
| Can be changed? | read/write | normally read-only / difficult to change |
| Used for | active processing | start-up and fixed instructions |

#### RAM mark scheme phrases

+ **currently running data and instructions**
+ **programs in use**
+ **volatile**
+ **faster access than secondary storage**
+ **more RAM reduces need for virtual memory**

#### ROM mark scheme phrases

+ **firmware**
+ **bootstrap program**
+ **start-up instructions**
+ **non-volatile**
+ **retains contents without power**

---

### Effect of RAM on performance

#### Good answer

> More RAM allows more currently running data and instructions to be stored in main memory. This reduces the need to use virtual memory or fetch data from slower secondary storage, so there is less delay / latency.

#### Weak answer

> More RAM makes the computer faster.

This is too vague. Say **why**.

---

### SRAM vs DRAM

| Feature | SRAM | DRAM |
| --- | --- | --- |
| Full name | Static RAM | Dynamic RAM |
| Refresh needed? | no refresh needed | needs refreshing |
| Speed | faster | slower |
| Cost | more expensive | cheaper |
| Density | lower density | higher density |
| Common use | cache memory | main memory |

#### DRAM advantages

+ cheaper to manufacture
+ higher density per chip
+ can store more data per chip

#### DRAM disadvantages

+ needs refreshing
+ slower than SRAM
+ more power may be used due to refreshing

#### SRAM advantages

+ faster access
+ no refresh needed
+ suitable for cache

#### SRAM disadvantages

+ expensive
+ lower storage density

---

### PROM, EPROM and EEPROM

| Memory type | Meaning | Key point |
| --- | --- | --- |
| PROM | Programmable ROM | programmed once only |
| EPROM | Erasable Programmable ROM | erased using ultraviolet light |
| EEPROM | Electrically Erasable Programmable ROM | erased/written using electrical signals |

#### EPROM vs EEPROM

| EPROM | EEPROM |
| --- | --- |
| erased using ultraviolet light | erased using electrical signal |
| often must be removed from circuit | can usually remain in circuit |
| usually erases all data | can erase selected parts |
| less convenient | more convenient |

---

## Secondary Storage

### Magnetic hard disk

#### Principal operation

A magnetic hard disk:

1. has one or more **platters**
2. platters are mounted on a **spindle**
3. platters rotate at high speed
4. a **read/write head** moves across the surface
5. data is stored using changes in **magnetic field / magnetised areas**
6. when reading, changes in magnetic field produce a change in electric current

#### Mark scheme keywords

+ **platters**
+ **spindle**
+ **read/write head**
+ **magnetic field**
+ **magnetised surface**
+ **rotates at high speed**

#### Advantages

+ large capacity
+ low cost per GB
+ suitable for long-term storage of large files

#### Disadvantages

+ moving parts
+ slower than SSD
+ can be damaged by shock
+ more power/noise/heat

---

### Optical storage

#### Principal operation

An optical disc reader/writer:

1. uses a **laser**
2. the laser is directed onto the disc surface
3. the disc has areas with different reflectivity / pits and lands
4. reflected light is detected by a sensor
5. differences in reflection are interpreted as binary data

#### Mark scheme keywords

+ **laser**
+ **reflected light**
+ **pits and lands**
+ **sensor detects reflection**
+ **binary data**

#### Buffer with optical disc

> A buffer stores data temporarily before it is written to the optical disc because the computer may send data faster than the disc can write it.

---

### Solid-state storage / flash memory

#### Principal operation

1. Each memory cell contains a control gate and an electrically isolated floating gate.
2. An applied voltage adds or removes electrons from the floating gate.
3. The stored charge changes whether current can pass through the transistor.
4. The controller interprets the resulting electrical state as stored binary data.
5. The trapped charge remains when power is removed, so the storage is non-volatile.

#### Key features

+ no moving parts
+ faster access than magnetic storage
+ more durable
+ silent
+ lower power use
+ more expensive per GB

#### Flash memory gate terms

| Term | Meaning |
| --- | --- |
| NAND / NOR gates | used to create solid-state memory devices |
| floating gate | retains electrons without power |
| control gate | allows or stops current from passing |
| cell | stores a bit / value |

#### Mark scheme style

> Flash memory is non-volatile because the floating gate can retain electrons even when power is removed.

---

## Ports and Peripheral Connection

### USB

#### Why USB is useful

+ widely used for peripherals
+ supports plug-and-play
+ can provide power
+ can transfer data
+ device can be automatically recognised

#### Mark scheme answer

> USB supports plug-and-play. When the device is connected, the OS detects it and loads / installs the appropriate driver so it can be used automatically.

---

### HDMI

#### Why HDMI may be better than VGA

| HDMI | VGA |
| --- | --- |
| digital | analogue |
| carries video and audio | video only |
| supports higher resolution | lower quality for modern high-res displays |
| less interference | more prone to signal degradation |
| no need for separate audio cable | needs separate audio cable |

#### Mark scheme style

> HDMI can transmit both video and audio, so a separate sound cable is not needed. It is a digital interface, so there is no analogue conversion loss and it can support high-resolution displays.

---

## Processor-related Hardware Performance

Although detailed CPU architecture is mainly Chapter 4, exam questions can mix hardware performance into Chapter 3-style device comparison questions.

### Number of cores

| More cores can help when... | Why |
| --- | --- |
| software supports parallel processing | different cores can process different tasks |
| multitasking | several processes can run at the same time |
| suitable workload | tasks can be divided between cores |

#### Warning

More cores do not always mean faster performance if the software cannot use them.

---

### Clock speed

> Clock speed is the number of cycles per second. Higher clock speed may allow more instructions to be processed per second.

#### Weak answer

> Higher GHz is better.

Better:

> A higher clock speed means more clock cycles per second, so the processor may fetch/decode/execute instructions more quickly.

---

### Bus width

| Bus | Effect |
| --- | --- |
| Data bus | wider data bus transfers more data at one time |
| Address bus | wider address bus allows more memory locations to be directly addressed |
| Control bus | carries control signals |

#### Exam-style answer

> A wider data bus means more data can be transferred between components at one time, reducing delay. A wider address bus means more memory locations can be addressed directly.

---

## 3.2 Logic Gates and Logic Circuits

### Basic gates

| Gate | Meaning | Output is 1 when... |
| --- | --- | --- |
| NOT | inversion | input is 0 |
| AND | both conditions | both inputs are 1 |
| OR | at least one | one or both inputs are 1 |
| NAND | NOT AND | not both inputs are 1 |
| NOR | NOT OR | both inputs are 0 |
| XOR | exclusive OR | inputs are different |

---

### Truth tables

#### NOT

| A | X |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

#### AND

| A | B | X |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

#### OR

| A | B | X |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

#### NAND

| A | B | X |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

#### NOR

| A | B | X |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

#### XOR

| A | B | X |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

---

### Writing logic expressions from a circuit

#### Method

1. Label each gate output.
2. Work from left to right.
3. Write the expression for each intermediate output.
4. Combine carefully using brackets.
5. Do not ignore NOT bubbles.

#### Example

If:

```text
X = A AND (NOT B OR C)
```

Then write:

```text
X = A AND (NOT B OR C)
```

or in symbolic form:

```text
X = A . (B̅ + C)
```

#### Mark scheme style

Cambridge accepts word-form expressions such as:

+ `A AND B`
+ `A OR NOT B`
+ `(A XOR B) NAND C`

---

### Completing truth tables for complex expressions

Example:

```text
X = (A OR B) XOR (B OR C)
```

Recommended working columns:

| A | B | C | A OR B | B OR C | X |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 | 0 |

#### Common method error

Students often calculate `XOR` as normal `OR`.
Remember:

```text
XOR = 1 only when inputs are different
```

---

### Drawing logic circuits from expressions

#### Method

For:

```text
X = (A AND B) OR (NOT C)
```

Draw:

1. A and B into AND gate.
2. C into NOT gate.
3. Outputs of AND and NOT into OR gate.
4. Output is X.

#### Exam warning

+ Use the correct gate symbol.
+ Connect all inputs.
+ Put NOT before the correct variable.
+ Use brackets to decide gate order.

---

## Mark Scheme Keywords

### Embedded systems

+ built into a larger device
+ dedicated task
+ specific task
+ dedicated processor / memory / software
+ limited functionality
+ firmware difficult to update
+ specialist repair

### Sensors and control

+ sensor detects / measures
+ data is input to processor
+ processor compares with stored value
+ signal sent to output device / actuator
+ changes the environment / system
+ monitoring does not affect input/environment

### Memory

+ RAM stores current data and instructions
+ volatile
+ ROM stores firmware / bootstrap / start-up instructions
+ non-volatile
+ SRAM faster / more expensive / no refresh
+ DRAM cheaper / higher density / needs refresh

### Storage

+ magnetic platters
+ spindle
+ read/write head
+ magnetic field
+ laser
+ reflected light
+ pits and lands
+ floating gate
+ control gate
+ NAND / NOR

### Buffers

+ temporary storage
+ different speeds
+ stores data until device/process is ready
+ prevents data loss / reduces waiting

### Logic

+ AND / OR / NOT / NAND / NOR / XOR
+ NOT means invert
+ XOR means inputs are different
+ truth table
+ intermediate working columns
+ brackets show order

---

## Topic-Specific Common Confusions

| Mistake | Why it loses marks | Correct version |
| --- | --- | --- |
| “Embedded system is a small computer.” | Too vague | built into a larger device and performs a specific task |
| “RAM stores files permanently.” | RAM is volatile | RAM stores current data/instructions while in use |
| “ROM is same as RAM but cannot be changed.” | Not enough | ROM is non-volatile and stores firmware/start-up instructions |
| “DRAM is better because it has dynamic.” | Meaningless | DRAM is cheaper/higher density but needs refresh and is slower |
| “Buffer speeds up the computer.” | Too vague | buffer stores data temporarily when devices work at different speeds |
| “Monitoring system controls sensors.” | Wrong | monitoring collects/stores/displays data; control changes environment |
| “XOR is same as OR.” | Wrong truth table | XOR outputs 1 only when inputs are different |
| Missing brackets in logic expression | Can change meaning | write brackets around each sub-expression |
| “SSD stores data magnetically.” | Wrong storage principle | SSD uses flash memory/electronic circuits |
| “Optical disc uses magnetism.” | Wrong | optical disc uses laser/reflected light |

---

## Scenario Answer Bank

### Embedded smart doorbell

> This is an embedded system because the processor, memory and software are built into the doorbell and are dedicated to specific tasks such as motion detection, video recording and sending notifications. It is not a general-purpose computer.

### Security light system

> This is a control system because sensor readings are processed and used to send a signal to turn on the floodlight. The output changes the environment by increasing the light level.

### Temperature monitoring system

> This is a monitoring system if it only records or displays the temperature readings. It becomes a control system if the processor uses the readings to switch on a fan/heater through an actuator.

### Buffer for optical writing

> The buffer temporarily stores data before it is written to the optical disc because the computer may send data faster than the disc writer can write it. The data remains in the buffer until the writer is ready.

### More RAM

> More RAM allows more currently running programs, data and instructions to be stored in main memory. This reduces the need to use virtual memory or access slower secondary storage, reducing delay.

### Wider data bus

> A wider data bus allows more data to be transferred between components at one time, so there may be less delay when data is fetched or transferred.

### USB automatic connection

> USB supports plug-and-play. When the device is connected, the OS detects it and loads the required driver, allowing the device to be used automatically.

### HDMI instead of VGA

> HDMI is digital and can carry both video and audio. It supports high-resolution displays and does not need a separate audio cable, unlike VGA.

### Sensor on shop shelf

> A pressure sensor can detect that the pressure/weight on the shelf has decreased when an item is removed. This data is sent to the system so it can identify the item taken.

### Logic expression answer

> Work from left to right. Give each gate an intermediate expression, then combine them with brackets. For example: `X = (A AND NOT B) OR C`.

---

## Process Diagram

```mermaid
flowchart TD
A[Physical change in environment] --> B[Sensor detects measurement]
B --> C[Analogue/digital data sent to processor]
C --> D{Condition met?}
D -- No --> E[Store/display data only<br/>monitoring behaviour]
D -- Yes --> F[Send signal to output device / actuator]
F --> G[Actuator changes environment<br/>control behaviour]
```

---

## Logic Circuit Working Process

```mermaid
flowchart LR
A[Read circuit / expression] --> B[Add intermediate labels]
B --> C[Apply NOT first]
C --> D[Apply AND / OR / NAND / NOR / XOR]
D --> E[Use brackets]
E --> F[Complete truth table rows]
F --> G[Check XOR and NOT carefully]
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

1. Define an embedded system. [2]
2. Give one drawback of an embedded system. [1]
3. State what RAM stores while a program is running. [1]
4. Give one difference between SRAM and DRAM. [1]
5. State how a microphone first converts sound into an electrical signal. [1]
6. Identify a suitable sensor to detect whether a door is open. [1]
7. State the output of `1 XOR 1`. [1]
8. State the output of `1 NAND 1`. [1]
9. State why a VR headset must track the user's head movement. [1]

## Quick Check Answers

1. Built into a larger device [1], performs a specific/dedicated task [1].
2. Difficult to update / limited functionality / specialist repair / e-waste [1].
3. Current data and instructions / currently running programs [1].
4. SRAM is faster / more expensive / no refresh; DRAM is cheaper / higher density / needs refresh [1].
5. Sound waves vibrate a diaphragm / transducer, producing a changing analogue electrical signal [1].
6. Contact sensor / magnetic sensor [1].
7. `0` [1].
8. `0` [1].
9. The processor must update the displayed viewpoint so it follows the user's orientation/movement [1].

---

## 20-Mark Exam Practice

**Total: 20 marks**

### Question 1: Embedded system and sensors [6]

A smart security doorbell has a camera, motion sensor, speaker and network connection. It detects movement and sends a video notification to a user’s phone.

(a) Explain why the smart doorbell is an embedded system. [2]
(b) Identify a suitable sensor for detecting movement near the door. [1]
(c) Explain whether the doorbell is a monitoring system or a control system. [3]

#### Mark scheme

(a) Built into a larger device / doorbell [1], performs specific tasks such as motion detection / video recording / notification [1].
(b) Infrared / motion / proximity sensor [1].
(c) Award up to [3]:
+ monitoring if it records/transmits video without affecting the sensor input [1]
+ control if it processes data and sends a signal to an output device such as speaker/light [1]
+ must justify using the given scenario: data from sensor causes output/action or only records/transmits [1]

---

### Question 2: Memory and storage [6]

A computer has 2 GB RAM, ROM, a magnetic hard disk and a USB flash drive.

(a) Explain how more RAM can improve performance. [3]
(b) Describe the principal operation of a magnetic hard disk. [3]

#### Mark scheme

(a) Award up to [3]:
+ more current data/instructions/programs can be stored in main memory [1]
+ less need for virtual memory / secondary storage access [1]
+ secondary storage has slower access time, so there is less delay/latency [1]

(b) Award up to [3]:
+ platters are magnetised and rotate on a spindle [1]
+ read/write head moves across the surface [1]
+ changes in magnetic field are detected / used to read binary data [1]

---

### Question 3: Buffers and ports [4]

A computer writes sensor readings to an optical disc. The computer also connects to a monitor with built-in speakers.

(a) Explain why a buffer may be used when writing to the optical disc. [2]
(b) Explain one benefit of using HDMI to connect the monitor instead of VGA. [2]

#### Mark scheme

(a) Temporary storage [1] because the computer and optical disc writer work at different speeds / data is stored until writer is ready [1].
(b) HDMI carries audio and video so no separate audio cable is needed [1] OR HDMI is digital / supports higher resolution [1], with a clear comparison to VGA [1].

---

### Question 4: Logic gates [4]

Complete the truth table for:

```text
X = (A AND NOT B) OR (B XOR C)
```

| A | B | C | X |
| --- | --- | --- | --- |
| 0 | 0 | 0 |   |
| 0 | 0 | 1 |   |
| 0 | 1 | 0 |   |
| 0 | 1 | 1 |   |
| 1 | 0 | 0 |   |
| 1 | 0 | 1 |   |
| 1 | 1 | 0 |   |
| 1 | 1 | 1 |   |

#### Mark scheme

| A | B | C | X |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Award [2] for first four rows correct and [2] for second four rows correct.

---

## Final Revision Checklist

- [ ] I can explain required device and storage principal operations.
- [ ] I can distinguish monitoring from control and trace feedback.
- [ ] I can compare memory, storage and buffer roles.
- [ ] I can derive logic expressions, truth tables and circuits.
- [ ] I can complete and self-mark both chapter practices.
