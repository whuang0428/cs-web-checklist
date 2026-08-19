# A2 9618 Chapter 20: Further Programming

<div class="chapter-meta"><strong>A2 9618 · Papers 3–4</strong><span>9618 · 2027–2029 · Version 2</span></div>

## Official Syllabus Checklist

Revise: programming paradigms; low-level programming and five addressing modes; declarative facts, rules, variables and goals; OOP, containment, inheritance and polymorphism; file organisation/processing; exception handling; practical implementation and testing.

> **Paper 3 focus:** Section 20 theory, including low-level and declarative programming.
>
> **Paper 4 focus:** practical Sections 19–20, but **Paper 4 excludes low-level and declarative programming**. This project uses **Java console mode**. Pseudocode is still required for planning, tracing and language-neutral algorithm answers.

## Core Knowledge

## Chapter at a Glance

### Separate the four paradigms

<span lang="zh-CN">先判断程序由什么规则驱动。</span>

- Imperative code changes state through ordered statements.
- Object-Oriented code organises state and behaviour into objects.
- Declarative code states facts, rules and goals.
- Low-level code uses processor instructions and explicit addressing modes.

**Exam cue:** identify the defining feature, not merely a language name.

### Reason about low-level code

<span lang="zh-CN">操作数可能是值、地址或偏移量。</span>

- Trace ACC, IX, memory and comparison result after every instruction.
- Distinguish immediate, direct, indirect, indexed and relative addressing.

**Exam cue:** calculate the effective address before changing a register.

### Design Java objects

<span lang="zh-CN">封装数据，通过公共方法维护有效状态。</span>

- Constructors establish valid objects.
- Containment models has-a; inheritance models is-a.
- Overridden methods enable polymorphism through a common superclass type.

**Exam cue:** show where validation occurs and why dynamic dispatch is used.

### Process files safely

<span lang="zh-CN">文件组织方式、访问方式和异常处理必须匹配。</span>

- Serial, sequential and random files support different access patterns.
- Handle expected exceptions specifically and preserve valid records.
- Tests must state input, expected result and actual result.

**Exam cue:** do not use an empty catch block.

---

## Syllabus Map

| Requirement | Evidence |
|---|---|
| Four paradigms | Programming Paradigms |
| Five addressing modes and example instructions | Low-Level Programming for Paper 3 |
| Facts, rules, variables and goals | Declarative Programming for Paper 3 |
| OOP, containment, inheritance and polymorphism | Java OOP for Paper 4 |
| Serial, sequential and random files | File Organisation and Processing |
| Hashing and exceptions | Worked Examples 3 and 4 |

## Programming Paradigms

| Paradigm | Main idea | Typical evidence |
|---|---|---|
| imperative/procedural | statements update state in a defined order | assignment, selection, iteration, procedures |
| Object-Oriented | objects combine private state and public behaviour | classes, objects, methods, inheritance |
| declarative | facts/rules describe relationships and a goal asks what follows | knowledge base and inference |
| low-level | instructions map closely to processor operations | accumulator, memory addresses, jumps |

## Low-Level Programming for Paper 3

### Five addressing modes

| Mode | Operand means | Example | Effect |
|---|---|---|---|
| immediate | literal value | `LDM #8` | `ACC ← 8` |
| direct | memory address | `LDD 20` | `ACC ← Memory[20]` |
| indirect | address holding another address | `LDI 20` | `ACC ← Memory[Memory[20]]` |
| indexed | base address plus IX | `LDX 20` | `ACC ← Memory[20 + IX]` |
| relative | offset from current PC | `JMP +4` | branch relative to current instruction position |

### Current example instruction set

| Instruction | Meaning |
|---|---|
| `LDM #n` | load immediate value into ACC |
| `LDD address` | load direct from memory |
| `LDI address` | load indirect from memory |
| `LDX address` | load from address plus IX |
| `LDR #n` | load immediate value into IX |
| `MOV IX` | copy ACC into IX |
| `STO address` | store ACC in memory |
| `ADD address` / `ADD #n` | add memory value or immediate value |
| `SUB address` / `SUB #n` | subtract memory value or immediate value |
| `CMP address` / `CMP #n` | compare ACC with operand |
| `CMI address` | compare ACC indirectly |
| `JMP address` | unconditional jump |
| `JPE address` | jump when previous comparison is true/equal |
| `JPN address` | jump when previous comparison is false/not equal |

### Worked low-level writing example

Load immediate `6`, add the value stored at address `30`, and store the result at address `31`:

```text
LDM #6
ADD 30
STO 31
```

For conditional flow, `CMP #10` records whether ACC equals 10. `JPE MATCH` follows the true/equal path; `JPN OTHER` follows the false/not-equal path. Both depend on the preceding compare.

## Worked Example 1 — Addressing and Memory Trace

Given `Memory[12] = 20`, `Memory[20] = 7`, `Memory[14] = 9` and `IX = 2`:

| Instruction | Mode | Result |
|---|---|---|
| `LDM #12` | immediate | `ACC = 12` |
| `LDD 12` | direct | `ACC = 20` |
| `LDI 12` | indirect | `ACC = Memory[20] = 7` |
| `LDX 12` | indexed | `ACC = Memory[14] = 9` |

The same numeric operand can lead to four different values because its interpretation changes.

## Declarative Programming for Paper 3

This chapter uses the following self-contained notation:

- `FACT relation(item)` states a known relationship.
- `RULE result(X) IF condition(X)` states an implication.
- A capital letter such as `X` is a **variable**.
- `GOAL relation(item)` asks whether the knowledge base can satisfy a relationship.

Example:

```text
FACT refrigerated(vaccine)
FACT urgent(vaccine)
FACT refrigerated(juice)

RULE priority(X) IF refrigerated(X) AND urgent(X)

GOAL priority(vaccine)
```

The goal succeeds because both conditions can be matched with `X = vaccine`. `GOAL priority(juice)` fails because no `urgent(juice)` fact is supplied.

## Worked Example 2 — Natural Language to Rule and Goal

Statement: “Every member with an overdue loan is blocked. Mina has an overdue loan.”

```text
FACT overdue(mina)
RULE blocked(X) IF overdue(X)
GOAL blocked(mina)
```

The goal succeeds by applying the rule to the matching fact. The variable makes the rule general; `mina` is a specific value.

## Java OOP for Paper 4

### Encapsulation, containment and polymorphism

- Private fields prevent uncontrolled direct changes.
- A constructor establishes a valid initial state.
- A `Booking` containing activities is a has-a relationship.
- `TimedActivity extends Activity` is an is-a relationship.
- Calling an overridden `fee()` through an `Activity` reference is polymorphism.

```java
import java.util.ArrayList;
import java.util.List;

class Ch20OopDemo {
    static class Activity {
        private final String name;
        private double baseFee;
        Activity(String name, double baseFee) {
            this.name = name;
            setBaseFee(baseFee);
        }
        String getName() { return name; }
        double getBaseFee() { return baseFee; }
        void setBaseFee(double value) {
            if (value < 0) throw new IllegalArgumentException("negative fee");
            baseFee = value;
        }
        double fee() { return baseFee; }
    }

    static class TimedActivity extends Activity {
        private final int minutes;
        TimedActivity(String name, double baseFee, int minutes) {
            super(name, baseFee);
            if (minutes <= 0) throw new IllegalArgumentException("invalid minutes");
            this.minutes = minutes;
        }
        @Override double fee() { return getBaseFee() + minutes * 0.20; }
    }

    static class Booking {
        private final String customer;
        private final List<Activity> activities = new ArrayList<>();
        Booking(String customer) { this.customer = customer; }
        void addActivity(Activity activity) { activities.add(activity); }
        double totalFee() {
            double total = 0;
            for (Activity activity : activities) total += activity.fee();
            return total;
        }
    }

    public static void main(String[] args) {
        Booking booking = new Booking("Learner");
        booking.addActivity(new Activity("Basic", 10));
        booking.addActivity(new TimedActivity("Timed", 10, 5));
        if (Math.abs(booking.totalFee() - 21.0) > 0.000001) throw new AssertionError();
    }
}
```

The total loop contains no type test. Dynamic dispatch selects the correct `fee()` implementation.

## File Organisation and Processing

| Organisation | Arrangement | Access | Suitable use |
|---|---|---|---|
| serial | records in arrival order, no key order | read through until found | append-only logs |
| sequential | records in key order | efficient ordered batch processing | payroll/report runs |
| random/direct | calculated address or key lookup | jump to likely record location | frequent individual lookup/update |

Java text processing normally uses `BufferedReader`/`BufferedWriter`. For true random access, `RandomAccessFile` supports `seek()` to a byte position. File formats must define field order, delimiter and validation rules.

## Worked Example 3 — HashTable with Linear Probing

For size 7, keys 10 and 17 both hash to index 3. Key 10 occupies index 3; key 17 probes index 4. Searches must repeat the identical probe sequence and stop after at most seven attempts.

```java
class Ch20HashTableDemo {
    static class HashTable {
        private final Integer[] keys;
        private final String[] values;
        HashTable(int size) { keys = new Integer[size]; values = new String[size]; }
        boolean insert(int key, String value) {
            int index = Math.floorMod(key, keys.length);
            for (int count = 0; count < keys.length; count++) {
                if (keys[index] == null || keys[index] == key) {
                    keys[index] = key; values[index] = value; return true;
                }
                index = (index + 1) % keys.length;
            }
            return false;
        }
        String find(int key) {
            int index = Math.floorMod(key, keys.length);
            for (int count = 0; count < keys.length; count++) {
                if (keys[index] == null) return null;
                if (keys[index] == key) return values[index];
                index = (index + 1) % keys.length;
            }
            return null;
        }
    }
    public static void main(String[] args) {
        HashTable table = new HashTable(7);
        if (!table.insert(10, "A") || !table.insert(17, "B")) throw new AssertionError();
        if (!"A".equals(table.find(10)) || !"B".equals(table.find(17))) throw new AssertionError();
    }
}
```

## Exception Handling

Catch exceptions you can handle. Examples include `FileNotFoundException`, `IOException` and `NumberFormatException`. A `finally` block is useful for cleanup, although try-with-resources closes files automatically.

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

class Ch20FileDemo {
    static double average(Path path) {
        double total = 0;
        int count = 0;
        try (BufferedReader reader = Files.newBufferedReader(path)) {
            String line;
            while ((line = reader.readLine()) != null) {
                try {
                    total += Double.parseDouble(line.trim());
                    count++;
                } catch (NumberFormatException error) {
                    System.out.println("Invalid number skipped: " + line);
                }
            }
        } catch (IOException error) {
            System.out.println("File could not be read: " + error.getMessage());
        }
        return count == 0 ? 0 : total / count;
    }
    public static void main(String[] args) {
        if (average(Path.of("file-that-does-not-exist.txt")) != 0) throw new AssertionError();
    }
}
```

## Worked Example 4 — Select the Exception Boundary

Place the outer `IOException` handler around opening and reading the file. Place the inner `NumberFormatException` handler around one record conversion. A malformed row is then reported and skipped without discarding later valid rows. Catching every exception around the entire method would hide programming faults and stop useful recovery.

## Required Ideas and Exam Language

- Identify the paradigm from its defining control model.
- For low-level code, state the addressing mode and effective address.
- For declarative code, distinguish a known fact from a general rule and a tested goal.
- Explain containment as has-a and inheritance as is-a.
- Explain polymorphism as the same method call selecting an overridden implementation.
- Match file organisation to the access pattern and catch specific Java exceptions.

## Common Confusions

- [ ] I do not include low-level or declarative tasks in Paper 4 practice.
- [ ] I distinguish direct from indirect addressing.
- [ ] I base `JPE`/`JPN` on the preceding comparison.
- [ ] I do not treat a failed declarative goal as a false fact unless the question defines that meaning.
- [ ] I keep fields private and validate through constructors/setters.
- [ ] I distinguish serial arrival order from sequential key order.
- [ ] I never leave a Java catch block empty.
- [ ] I plan in pseudocode and implement executable Paper 4 solutions in Java.

## Worked Examples

The four examples cover Paper 3 low-level/declarative reasoning and Paper 4 Java data structures, files and exceptions.

## 10-Mark Quick Check

1. Identify the addressing mode in each instruction: `LDM #5`, `LDD 20`, `LDI 20`, `LDX 20`, `JMP +3`. **[5]**
2. Write three instructions to load immediate 4, add the value at address 12 and store the result at address 13. **[3]**
3. Given `FACT cold(sample)` and the notation above, write a rule stating that every cold item needs checking, then write a goal asking whether `sample` needs checking. **[2]**

**Total: 10 marks**

## Quick Check Answers

1. Immediate, direct, indirect, indexed, relative. **[5]**
2. `LDM #4` **[1]**, `ADD 12` **[1]**, `STO 13` **[1]**. **[3]**
3. `RULE needs_check(X) IF cold(X)` **[1]**; `GOAL needs_check(sample)` **[1]**. **[2]**

## 20-Mark Exam Practice

Write a Java class `SensorReading` and a loader.

1. Create private sensor ID and reading fields, a constructor, getters and a setter accepting readings from `-50.0` to `150.0` inclusive. Invalid readings must throw `IllegalArgumentException`. **[8]**
2. Write `loadReadings(Path path)` to read `sensorID,reading` records into an `ArrayList<SensorReading>`. Report and skip malformed records; handle an unreadable file without crashing. **[8]**
3. Give four tests with input, expected result and actual result: both reading boundaries, one rejected value and one malformed file row followed by a valid row. **[4]**

**Total: 20 marks**

### 20 Marks Practice Mark Scheme

1. Class and private fields **[2]**; constructor assigns ID and uses validation **[2]**; getters **[1]**; inclusive boundary test **[1]**; valid update **[1]**; throws `IllegalArgumentException` for invalid input **[1]**. **[8]**
2. Correct return collection and resource handling **[2]**; reads every line **[1]**; splits/checks two fields **[1]**; converts numeric value **[1]**; constructs/adds valid object **[1]**; catches per-record format/range error and continues **[1]**; handles `IOException` **[1]**. **[8]**
3. One mark for each named test with matching expected and actual evidence. **[4]**

## Final Revision Checklist

- [ ] I can distinguish imperative, Object-Oriented, declarative and low-level paradigms.
- [ ] I can trace all five addressing modes and conditional jumps.
- [ ] I can write and evaluate facts, rules, variables and goals.
- [ ] I can explain encapsulation, containment, inheritance and polymorphism.
- [ ] I can select serial, sequential or random file organisation.
- [ ] I can implement Java file handling and specific exception recovery.
- [ ] I can plan with pseudocode and produce tested Java console programs.
