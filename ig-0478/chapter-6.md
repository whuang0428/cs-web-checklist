# IGCSE 0478 Chapter 6: Automated and Emerging Technologies

<div class="chapter-meta"><strong>IGCSE 0478 · Paper 1</strong><span>0478 · 2026–2028 · Version 5</span></div>

## Official Syllabus Checklist

Revise: automated systems; robotics; artificial intelligence, expert systems and machine learning.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.


## 6.1 Automated Systems
### 6.1.1 Core Definition
An **automated system** is a system that can perform actions **without human intervention**, usually by using:

**1. Sensor**
Collects data from the environment.

**2. Microprocessor**
Processes sensor data and makes decisions.

**3. Actuator / Output**
Carries out the action or gives an alert.

---

### 6.1.2 The Golden Answer Template
> **Describe how sensors, microprocessors and actuators are used in an automated system.**
>

Use this structure almost every time:

1. The **sensor** detects / measures data from the environment.
2. The sensor data is sent to the **microprocessor**.
3. The microprocessor compares the data with a **stored value / preset value / acceptable range**.
4. If the condition is met, the microprocessor sends a **signal**.
5. The signal triggers an **actuator** or output device.
6. The process repeats continuously.

```mermaid
flowchart LR
A[Sensor collects data] --> B[Data sent to microprocessor]
B --> C[Compare with stored/preset value]
C --> D{Condition met?}
D -- Yes --> E[Send signal]
E --> F[Actuator/output performs action]
D -- No --> G[No action / continue monitoring]
F --> A
G --> A
```

---

### 6.1.3 Mark Scheme Style Sentences
#### Example A: Automatic weather alert system
> **Describe how the system uses a sensor and microprocessor to trigger an alert.**
>

High-scoring answer:

+ A sensor, such as a **temperature / humidity / light / level sensor**, collects environmental data.
+ The data is sent to the **microprocessor**.
+ The microprocessor compares the data with a **preset value**, for example 40.
+ If the value is greater than 40, the microprocessor sends a signal to **trigger the alert**.

#### Example B: Automatic welcome message on an ATM
+ An **infra-red / proximity sensor** detects that a person is nearby.
+ The sensor sends data continuously to the microprocessor.
+ The microprocessor calculates / checks the distance.
+ If the person is within the preset distance, the microprocessor sends a signal to display a welcome message.

---

### 6.1.4 Advantages and Disadvantages of Automated Systems
#### General Advantages
| Advantage | Mark scheme expansion |
| --- | --- |
| Faster response | The system can react more quickly than a human. |
| Works continuously | It can work 24/7 without breaks. |
| Safer for humans | Humans do not need to enter dangerous environments. |
| More consistent | It performs repetitive tasks in the same way each time. |
| More accurate | It reduces human error in measurement or control. |
| Long-term cost saving | Fewer workers may be needed after setup. |


#### General Disadvantages
| Disadvantage | Mark scheme expansion |
| --- | --- |
| Expensive setup | Sensors, microprocessors, actuators and software cost money. |
| Maintenance cost | The system needs checking, repairs and updates. |
| Job loss / deskilling | Human workers may be replaced or lose practical skills. |
| Cybersecurity risk | The system could be hacked or controlled maliciously. |
| Malfunction risk | Hardware or software errors may cause wrong actions. |
| Unexpected cases | The system may fail when a situation was not considered during design. |


---

### 6.1.5 Scenario Transfer Table
| Scenario | Possible sensor | Action / actuator | Strong answer idea |
| --- | --- | --- | --- |
| **Agriculture irrigation** | moisture sensor | valve / water pump | If soil moisture is below preset value, pump turns on. |
| **Weather alert** | temperature / humidity / light / level sensor | alarm / screen alert | If reading passes threshold, alert is triggered. |
| **Lighting system** | light sensor / infra-red sensor | lamp switched on/off | If light level is low or movement detected, lights switch on. |
| **Factory production** | pressure / temperature / proximity sensor | robotic arm / motor | If object is detected, actuator moves the part. |
| **Transport** | proximity / speed sensor | brake / steering actuator | If obstacle detected, system sends signal to slow or stop. |
| **Gaming** | controller / motion sensor | in-game output | Sensor input changes game actions automatically. |
| **Science lab** | pH / temperature sensor | heater / warning output | If value outside safe range, system adjusts equipment or warns user. |


---

## 6.2 Robotics
### 6.2.1 Definition
**Robotics** is a branch of computer science that includes the **design, construction and operation of robots**.

---

### 6.2.2 What Makes Something a Robot?
A robot should usually have several of these features:

| Robot characteristic | How to write it in exam |
| --- | --- |
| Mechanical structure / framework | It has a physical body or structure. |
| Electrical components | It contains sensors, microprocessors and/or actuators. |
| Programmable | It can be programmed to perform tasks. |
| Ability to move | It can move itself or move part of itself. |
| Can sense surroundings | It uses sensors to detect data from the environment. |


> **Important exam trap**
A device can be “smart” but still **not** be a robot if it has no mechanical structure, no actuator and cannot move itself.
Example: a smart speaker can use AI, but it is normally not a robot.
>

---

### 6.2.3 Common Robot Roles
| Area | Example | What the robot does |
| --- | --- | --- |
| Industry | factory robot arm | lifts, welds, assembles or moves parts |
| Transport | autonomous vehicle / delivery robot | navigates routes and avoids obstacles |
| Agriculture | self-driving tractor | ploughs, plants seeds, avoids obstacles |
| Medicine | remote surgery robot | allows precise surgery using robotic tools |
| Domestic settings | robot vacuum cleaner | cleans floors automatically |
| Entertainment | game / toy robot | moves or interacts with users |


---

### 6.2.4 Robot Advantages by Scenario
#### Industry / Factory
| Benefit | Expansion |
| --- | --- |
| Safer for workers | Workers do not need to lift heavy machinery or work in dangerous areas. |
| More consistent | Robots can repeat the same action accurately. |
| Works continuously | Robots can work overnight or 24/7. |
| Maintenance jobs created | Some workers may be trained to repair and maintain the robots. |


#### Remote Surgery Robot
| Benefit | Expansion |
| --- | --- |
| Specialist can operate remotely | A doctor does not need to travel to the hospital. |
| Shorter waiting time | Surgery can happen sooner without waiting for travel. |
| Higher precision | Robotic tools can make smaller and more accurate movements. |
| Smaller incision | Smaller tools can enter the body, which may reduce recovery time. |
| Safer / more hygienic | The doctor may not need to be near an infectious patient. |


#### Delivery Robot for Elderly Customers
| Benefit | Expansion |
| --- | --- |
| Supermarket gains more customers | Elderly people who cannot visit the store can still shop. |
| More efficient delivery | Multiple orders can be delivered without one worker for each customer. |
| Supports independence | Customers can receive goods without travelling. |


---

### 6.2.5 Robot Disadvantages by Scenario
| Drawback | Expansion |
| --- | --- |
| Expensive to buy and maintain | The cost may be too high for smaller organisations. |
| Hardware may malfunction | The robot may stop working or perform a wrong action. |
| Internet connection may fail | Remote robots may stop receiving commands. |
| Hacking risk | A malicious user could control or disrupt the robot. |
| Data corruption | Transmitted instructions could be changed or lost. |
| Job replacement | Human workers may lose jobs or become deskilled. |
| Difficult non-standard tasks | Robots may struggle with unusual situations. |


---

### 6.2.6 Exam Templates for Robotics
#### Q1. Give one reason why a self-driving tractor is a robot.
Good answers:

+ It has **electrical components**, such as sensors and actuators.
+ It is **programmable**.
+ It can **move**.
+ It can sense its surroundings.

#### Q2. Explain why a smart speaker may not be a robot.
Good answer:

+ It does not have a **mechanical structure**.
+ It does not have **actuators**.
+ It cannot **move itself**.

#### Q3. Explain one benefit of using robots in a factory.
Good answer:

+ Workers do not need to lift heavy machinery, so they are less likely to injure themselves.
+ Robots can perform repetitive tasks, so workers can focus on higher-skilled jobs.

---

## 6.3 Artificial Intelligence
### 6.3.1 Definition
**Artificial intelligence (AI)** is the simulation of intelligent behaviour by computers.

In IGCSE 0478, AI is mainly limited to:

**Expert systems**
Use expert knowledge, rules and inference to suggest decisions.

**Machine learning**
Allows a program to automatically adapt its own processes and/or data.

---

### 6.3.2 Main Characteristics of AI
A strong answer should include any of these:

| Characteristic | Exam wording |
| --- | --- |
| Collection of data | AI uses stored data. |
| Rules for using data | AI uses rules to process and apply the data. |
| Ability to reason | AI can make decisions based on data and rules. |
| Ability to learn | AI can improve from feedback or previous examples. |
| Ability to adapt | AI can change its own processes or data. |
| Analyse patterns | AI can identify patterns and make predictions. |


#### 3-mark AI definition template
> AI is the simulation of intelligent behaviour by computers.
It uses a collection of data and rules for using that data.
It can reason or make decisions, and may learn/adapt from previous results.
>

---

## 6.3.3 Expert Systems
### Core idea
An **expert system** is a form of AI that mimics the knowledge and decision-making of a human expert in a specific area.

Common scenarios:

+ medical diagnosis
+ car fault diagnosis
+ plant disease diagnosis
+ financial advice
+ technical support

---

### Expert System Components
| Component | Role |
| --- | --- |
| **User interface / interface** | Allows the user to enter data and receive output. |
| **Knowledge base** | Stores expert facts and knowledge about the topic. |
| **Rule base** | Stores rules / logic that link facts to conclusions. |
| **Inference engine** | Applies the rule base to the knowledge base and user input to reach a conclusion. |


> **Do not overfocus on “explanation system”**
It may appear in textbooks, but the core IGCSE syllabus components are:
**interface, knowledge base, rule base, inference engine**.
>

---

### Expert System Operation Flow
```mermaid
flowchart TD
A[User enters symptoms / data] --> B[Interface]
B --> C[Inference engine decides next question]
C --> D[Uses previous user input]
D --> E[Compares facts with knowledge base]
E --> F[Applies rules from rule base]
F --> G[Diagnosis / recommendation]
G --> H[Output shown on interface]
```

#### Mark Scheme Style Answer: Doctor diagnosis
> The doctor enters data about the patient’s symptoms into the **interface**.
The **inference engine** decides which questions to ask based on the previous answers.
It compares the symptoms with facts in the **knowledge base**.
It applies the **rule base** to decide a diagnosis.
The diagnosis is output through the **interface**.
>

---

## 6.3.4 Machine Learning
### Definition
**Machine learning** is when a program can automatically adapt its own processes and/or data.

A simple exam-friendly explanation:

> The system learns from previous data or feedback, identifies patterns, and changes its rules, data or processes to improve future decisions.
>

---

### Machine Learning Universal Flow
```mermaid
flowchart LR
A[Collect data] --> B[Store data]
B --> C[Analyse patterns / trends]
C --> D[Compare success and failure]
D --> E[Receive feedback / results]
E --> F[Adapt rules, data or processes]
F --> G[Make better prediction / decision]
```

---

### Machine Learning Answer Bank
#### 1. Weather prediction AI
Use these points:

+ It collects weather data over time.
+ It analyses the data for **patterns / trends**.
+ It predicts future weather based on these patterns.
+ Feedback is given on whether the prediction was correct.
+ It changes future predictions based on this feedback.
+ It can learn what weather occurs at certain times of year.

#### 2. Game enemy / gaming AI
Use these points:

+ It collects data about the player’s actions.
+ It analyses patterns in the player’s movements.
+ It learns how the player moves.
+ It predicts the player’s next movement.
+ It adapts its own movements / processes to match the player.
+ It stores successful and unsuccessful moves.
+ It learns the most efficient / optimal movement against the player.

#### 3. Smart speaker voice recognition
Use these points:

+ It gathers data from many different voices.
+ It analyses patterns in a user’s voice.
+ It learns different pronunciations or accents.
+ It stores successful and unsuccessful voice commands.
+ It learns different ways of making the same request.
+ It learns to ignore background noise.

#### 4. Delivery robot / farming robot
Use these points:

+ It collects route / field / obstacle data.
+ It identifies patterns in the route or field.
+ It remembers successful routes.
+ It remembers obstacles to avoid.
+ It adapts its route to become more efficient.
+ It makes fewer mistakes in future.

---

### 6.3.5 Expert System vs Machine Learning
| Feature | Expert system | Machine learning |
| --- | --- | --- |
| Main basis | Human expert knowledge | Data and training examples |
| Uses rules? | Yes, rule base is central | May create/adapt rules from data |
| Learns automatically? | Usually no, unless ML is added | Yes |
| Best for | Clear decision problems with expert rules | Pattern recognition and prediction |
| Example | Medical diagnosis expert system | Weather prediction AI / smart speaker voice recognition |


---

## 7. High-Frequency Exam Command Words
| Command word | What students should do | Example |
| --- | --- | --- |
| **State / Give / Identify** | One short point only | “Microprocessor.” |
| **Describe** | Give features or steps | “The sensor sends data to the microprocessor.” |
| **Explain** | Point + reason / effect | “The robot can work 24/7, so production can continue overnight.” |
| **Suggest** | Apply knowledge to the given scenario | “A humidity sensor could be used because it measures water vapour in the air.” |
| **Compare** | Similarity/difference on both sides | “Expert systems use fixed rules, whereas machine learning can adapt its own processes.” |


---

## Worked Scenario Question Bank
### Q1. Automated weather alert system [3]
A weather station sends an alert when a sensor value is greater than 40.
Describe how the sensor and microprocessor are used.

Answer

 - A sensor collects environmental data. - The sensor sends the data to the microprocessor. - The microprocessor compares the data with the preset value of 40. - If the data is greater than 40, the microprocessor sends a signal to trigger the alert.

---

### Q2. Robot judgement [3]
Explain why a smart speaker is not normally considered a robot.

Answer

 - It does not have a mechanical structure. - It does not have actuators. - It cannot move itself.

---

### Q3. Medical expert system [4]
Describe how an expert system can help a doctor diagnose an illness.

Answer

 - The doctor enters symptoms into the interface. - The inference engine decides which questions to ask based on previous answers. - The inference engine compares symptoms with facts in the knowledge base. - It applies rules from the rule base. - A diagnosis is output through the interface.

---

### Q4. Machine learning in gaming [3]
Explain how machine learning can improve the movement of a game enemy.

Answer

 - It collects data about the player’s actions. - It analyses patterns in the player’s movements. - It predicts the player’s next movement. - It adapts its own movements to match the player. - It stores successful and unsuccessful moves.

---

### Q5. Remote surgery robot [4]
Explain two benefits of using a robot for remote surgery.

Answer

 - A specialist doctor does not need to travel, so surgery can happen sooner. - The robot can improve precision, so smaller incisions can be made. - Smaller incisions may reduce recovery time. - The doctor may not need to be near an infectious patient, so the surgery can be safer or more hygienic.

---

<span id="_9-final-one-page-revision-map" class="legacy-anchor" aria-hidden="true"></span>

## 9. Chapter at a Glance

Use this overview to trace automated control, classify robots, explain AI and evaluate impacts.

### Trace an automated system

<span lang="zh-CN">按输入、处理、输出和反馈的顺序描述系统。</span>

- A sensor measures a physical property and sends data to a microprocessor.
- The microprocessor compares the input with stored rules or a preset value.
- An output device or actuator changes the system and new sensor data provides feedback.

**Exam cue:** Apply every stage to the named scenario rather than giving a generic list.

### Classify robots

<span lang="zh-CN">机器人必须同时体现结构、控制和运动能力。</span>

- A robot has a mechanical structure, electrical components and programmable control.
- Robots perform dangerous, repetitive or precise tasks in industry, medicine and other fields.
- A device is not a robot merely because it contains sensors or artificial intelligence.

**Exam cue:** Link each claimed benefit to the task the robot performs.

### Explain AI

<span lang="zh-CN">说明系统怎样使用数据和规则进行推理或学习。</span>

- AI systems use data and rules to reason, learn, adapt or make predictions.
- An expert system combines a user interface, knowledge base, rule base and inference engine.
- Machine learning analyses training data and feedback to improve future outputs.

**Exam cue:** Describe the mechanism, not just the phrase “the computer learns”.

### Evaluate impacts

<span lang="zh-CN">优点和缺点都要与具体使用场景产生联系。</span>

- Automation can improve speed, consistency, availability and safety.
- Costs, maintenance, malfunction and hacking can reduce reliability or increase risk.
- Robotics and AI can change employment while also enabling work humans cannot do safely.

**Exam cue:** Develop each point with a consequence for the organisation, worker or user.

---

## Revision Readiness Checklist
Before the exam, students should be able to answer:

- [ ] Can I describe the sensor → microprocessor → actuator cycle?
- [ ] Can I explain why a system is automated?
- [ ] Can I give scenario-specific advantages and disadvantages?
- [ ] Can I list robot characteristics without calling every smart device a robot?
- [ ] Can I explain why a smart speaker is not usually a robot?
- [ ] Can I explain remote surgery robot benefits and risks?
- [ ] Can I define AI using data, rules, reason, learn and adapt?
- [ ] Can I explain expert system components?
- [ ] Can I describe how an expert system diagnoses a problem?
- [ ] Can I explain machine learning using collect data → analyse patterns → adapt?
- [ ] Can I apply machine learning to weather, gaming, voice recognition and robot navigation?

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

1. State the three main stages of an automated control system. **[2]**
2. Describe how an automated greenhouse responds when its temperature rises above a stored maximum. **[3]**
3. Give two characteristics that distinguish a robot from a simple smart device. **[2]**
4. Describe how a medical expert system uses a knowledge base, rule base and inference engine. **[3]**

## Quick Check Answers

1. Sensor/input, microprocessor/controller and actuator/output. Award any two correctly ordered stages. **[2]**
2. A sensor measures temperature and sends the reading to the microprocessor **[1]**; the reading is compared with the stored maximum **[1]**; the processor signals an actuator such as a fan or vent to reduce the temperature **[1]**. **[3]**
3. Any two: mechanical structure, electrical components, programmable control, movement or manipulation, sensing its environment. **[2]**
4. The knowledge base stores facts **[1]**; the rule base stores conditional expert rules **[1]**; the inference engine matches the entered symptoms to facts/rules to produce questions and a possible diagnosis **[1]**. **[3]**

## 20-Mark Exam Practice

**Total: 20 marks**

### Question 1 — Automated Warehouse [6]

A warehouse uses a light sensor and motorised lamps to maintain a minimum light level. Describe the complete feedback process. **[6]**

### Question 2 — Agricultural Robot [6]

Evaluate the use of a robot to inspect crops and remove weeds. Give two benefits, two limitations and a justified conclusion. **[6]**

### Question 3 — Machine-Learning Prediction [8]

A water company wants a machine-learning system to predict pipe failures. Explain how data would be used to train and improve the system, and identify one risk that must be controlled. **[8]**

## Practice Mark Scheme

### Question 1 Mark Scheme [6]

Sensor repeatedly measures light level **[1]**; analogue reading is converted to digital if required **[1]**; data is sent to the microprocessor **[1]**; reading is compared with the stored minimum **[1]**; if below the minimum, a signal switches/brightens the lamps **[1]**; new readings provide feedback and lamps are reduced/switched off when the target is reached **[1]**. **[6]**

### Question 2 Mark Scheme [6]

Benefits: any two contextual points, such as continuous operation, consistent detection, reduced chemical use, less repetitive labour or access to large fields **[2]**. Limitations: any two contextual points, such as purchase/maintenance cost, crop-recognition errors, damage from malfunction, weather/terrain limits or cyber attack **[2]**. Conclusion compares the evidence and proposes a justified condition, such as supervised trials and a manual stop before full deployment **[2]**. **[6]**

### Question 3 Mark Scheme [8]

Collect historical labelled examples containing pipe condition, sensor readings and whether/when failure occurred **[2]**; clean and divide representative data into training and test/validation sets **[1]**; train the model to find patterns linking inputs to failures **[1]**; compare predictions with known outcomes and calculate error **[1]**; adjust the model and repeat with further outcomes/feedback **[1]**; test on unseen data before operational use **[1]**; control a relevant risk such as biased/incomplete data, false alarms, missed failures or insecure sensor data **[1]**. **[8]**

## Final Revision Checklist

- I can describe a sensor–processor–actuator feedback loop in order.
- I can distinguish an automated system, a robot, an expert system and machine learning.
- I can apply benefits and limitations to a named scenario.
- I can explain how training data and feedback change a machine-learning model.
- I can complete and self-mark both assessment sections.
