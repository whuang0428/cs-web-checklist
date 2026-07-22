# A2 9618 Chapter 20: Further Programming

> **Paper 4 focus:** build procedural and object-oriented Python console programs that process files, handle exceptions and produce test evidence.

Paper 4 excludes **low-level** and **declarative** programming, but these paradigms remain part of Section 20 theory for Paper 3. This chapter labels that boundary explicitly.

---

## 1. Syllabus Coverage

| Syllabus objective | Where it is covered |
|---|---|
| Define a programming paradigm | Section 3 |
| Describe low-level, imperative, object-oriented and declarative paradigms | Section 3 |
| Write procedural code using variables, constructs and subroutines | Section 4 |
| Use all required OOP terminology accurately | Section 5 |
| Design classes and write OOP code | Sections 5–6 and Worked Example 1 |
| Open, read, write, append and close files | Section 7 |
| Process serial, sequential and random files | Sections 7–8 and Worked Examples 2–3 |
| Explain exceptions and select when to handle them | Section 9 |
| Write exception-handling code | Section 9 and Worked Example 4 |
| Produce complete code and testing evidence | Sections 2 and 10–13 |

---

## 2. Paper 4 Scope and Evidence

Paper 4 is a practical examination. Candidates use Python, Java or Visual Basic in console mode and submit:

- complete program code
- evidence that the program was executed and tested

The practical paper applies Sections 19–20 but excludes low-level and declarative programming.

A strong evidence sequence shows:

1. the code or relevant program section
2. the exact input or test file used
3. the output produced
4. a short statement of what the test proves

Do not submit only the successful normal case. Include boundary and failure behaviour where the task allows it.

---

## 3. Programming Paradigms

A **programming paradigm** is a general approach to organising computation and expressing solutions.

| Paradigm | Main idea | Typical features | Paper 4? |
|---|---|---|---|
| low-level | closely represents processor operations | registers, memory addresses, addressing modes | excluded |
| imperative/procedural | program state changes through ordered instructions | variables, selection, iteration, procedures, functions | included |
| object-oriented | interacting objects combine state and behaviour | classes, methods, inheritance, encapsulation | included |
| declarative | states facts, rules or desired results rather than control steps | facts, rules, goals | excluded |

### Low-level programming

Low-level code uses operations and addressing modes such as immediate, direct, indirect, indexed and relative. It offers hardware control but is machine-dependent and harder to maintain.

### Imperative programming

An imperative program states **how** to perform a task through an ordered sequence. Procedural programming groups those instructions into reusable procedures and functions.

### Object-oriented programming

OOP models a problem using classes and objects. Each object owns state and exposes controlled behaviour through methods.

### Declarative programming

Declarative code describes facts/rules and asks whether a goal can be satisfied. The engine decides the control sequence. For example, a family-relationship system can store a `parent` fact and define an `ancestor` rule.

Low-level and declarative programming can be assessed in Paper 3 theory but must not be made part of a Paper 4 practice task.

---

## 4. Imperative and Procedural Design

Use functions and procedures to give each part one responsibility.

```python
def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a value greater than zero")
        except ValueError:
            print("Enter a whole number")


def calculate_total(price, quantity):
    return price * quantity
```

Good procedural design:

- passes required data as parameters
- returns a result instead of changing unrelated global state
- separates input, processing, storage and output
- keeps validation close to the input boundary
- gives subroutines names that describe one action

Global constants can be appropriate. Mutable global variables usually make testing and reasoning harder.

---

## 5. Object-Oriented Terminology

| Term | Precise meaning |
|---|---|
| class | definition/template describing attributes and methods |
| object/instance | one runtime occurrence created from a class |
| attribute/property | data belonging to an object |
| method | operation belonging to a class/object |
| constructor | initialises a new object |
| encapsulation | keeps state with its methods and controls direct access |
| getter | returns a controlled view of an attribute |
| setter | validates or controls a change to an attribute |
| inheritance | creates a subclass from a superclass |
| polymorphism | the same method call can execute different subclass behaviour |
| containment/aggregation | one object stores or uses other objects: a “has-a” relationship |

Distinguish the relationships:

- `ElectricCar` **is a** `Vehicle`: inheritance
- `Fleet` **has** `Vehicle` objects: containment/aggregation

---

## 6. Designing and Implementing Classes

```python
class Activity:
    def __init__(self, title, base_fee):
        self.__title = title
        self.__base_fee = 0.0
        self.set_base_fee(base_fee)

    def get_title(self):
        return self.__title

    def get_base_fee(self):
        return self.__base_fee

    def set_base_fee(self, new_fee):
        if new_fee < 0:
            raise ValueError("fee cannot be negative")
        self.__base_fee = float(new_fee)

    def calculate_fee(self):
        return self.__base_fee


class TimedActivity(Activity):
    def __init__(self, title, base_fee, minutes):
        super().__init__(title, base_fee)
        if minutes <= 0:
            raise ValueError("minutes must be positive")
        self.__minutes = minutes

    def calculate_fee(self):
        return self.get_base_fee() + self.__minutes * 0.20


class Booking:
    def __init__(self, customer):
        self.__customer = customer
        self.__activities = []

    def add_activity(self, activity):
        self.__activities.append(activity)

    def total_fee(self):
        total = 0.0
        for activity in self.__activities:
            total += activity.calculate_fee()
        return total
```

This design demonstrates:

- private attributes and controlled access
- a subclass inheriting common behaviour
- an overridden `calculate_fee()` method
- polymorphism in `Booking.total_fee()`
- containment because a booking stores activity objects

Python does not enforce private access in the same way as every other language. Double-underscore name mangling signals and supports encapsulation, but good design still depends on using the public interface.

---

## 7. File Processing

### Modes and safe closure

| Mode | Meaning | Important effect |
|---|---|---|
| `"r"` | read | fails if the file does not exist |
| `"w"` | write | creates or truncates the file |
| `"a"` | append | adds to the end, creating the file if needed |

Use `with` so the file closes even if an exception occurs.

```python
def write_names(filename, names):
    with open(filename, "w", encoding="utf-8") as output_file:
        for name in names:
            output_file.write(name + "\n")


def append_name(filename, name):
    with open(filename, "a", encoding="utf-8") as output_file:
        output_file.write(name + "\n")


def read_names(filename):
    names = []
    with open(filename, "r", encoding="utf-8") as input_file:
        for line in input_file:
            names.append(line.strip())
    return names
```

### Records in a text file

```python
def load_scores(filename):
    scores = []
    with open(filename, "r", encoding="utf-8") as input_file:
        for line_number, line in enumerate(input_file, start=1):
            fields = line.strip().split(",")
            if len(fields) != 2:
                raise ValueError(f"invalid record on line {line_number}")
            name = fields[0]
            score = int(fields[1])
            scores.append((name, score))
    return scores
```

Validate:

- field count
- data type conversion
- required range
- unique key if required
- empty/malformed records

---

## 8. Serial, Sequential and Random Files

| Organisation | Record arrangement | Access pattern |
|---|---|---|
| serial | records stored in the order received | normally scan from the start |
| sequential | records stored in key order | scan in order; merging/range processing is efficient |
| random/direct | record location derived from its key | calculate location and access without scanning all earlier records |

### Serial file

An append-only event log is normally serial. New records are added at the end, without rearranging earlier data.

### Sequential file

A customer file sorted by customer ID is sequential. Processing every customer in ID order is efficient, but inserting a new record may require rewriting the file.

### Random access simulation

Paper 4 source files are text files. Random organisation can be simulated by loading records into a hash table and using a hash function to calculate a slot.

```python
class HashTable:
    def __init__(self, size):
        self.__keys = [None] * size
        self.__values = [None] * size

    def _start_index(self, key):
        return key % len(self.__keys)

    def insert(self, key, value):
        index = self._start_index(key)
        for _ in range(len(self.__keys)):
            if self.__keys[index] in (None, key):
                self.__keys[index] = key
                self.__values[index] = value
                return True
            index = (index + 1) % len(self.__keys)
        return False

    def find(self, key):
        index = self._start_index(key)
        for _ in range(len(self.__keys)):
            if self.__keys[index] is None:
                return None
            if self.__keys[index] == key:
                return self.__values[index]
            index = (index + 1) % len(self.__keys)
        return None
```

This uses **linear probing** to resolve collisions. The loop is bounded by the table size, preventing an infinite search when the table is full.

---

## 9. Exception Handling

An **exception** is an event raised during execution that interrupts the normal control flow.

Handle an exception when the program can respond meaningfully, for example:

- ask again after an invalid conversion
- display a clear message for a missing file
- skip and report a damaged input record
- release a resource and stop safely

Do not use a broad `except:` to hide programming errors.

```python
def read_integer_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            return [int(line.strip()) for line in input_file if line.strip()]
    except FileNotFoundError:
        print("The input file was not found")
    except ValueError:
        print("The file contains a non-integer value")
    except OSError as error:
        print(f"The file could not be read: {error}")
    return None
```

Use specific exception types because each represents a different failure and may require a different response. Exception handling does not prevent the fault; it controls what happens after the exception is raised.

---

## 10. Worked Example 1 — OOP Design from Requirements

Requirements:

- every account has an ID and balance
- balance cannot be changed directly
- `SavingsAccount` adds an interest rate
- a portfolio contains several accounts and calculates a total balance

```python
class Account:
    def __init__(self, account_id, opening_balance):
        if opening_balance < 0:
            raise ValueError("opening balance cannot be negative")
        self.__account_id = account_id
        self.__balance = float(opening_balance)

    def get_account_id(self):
        return self.__account_id

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.__balance += amount


class SavingsAccount(Account):
    def __init__(self, account_id, opening_balance, interest_rate):
        super().__init__(account_id, opening_balance)
        self.__interest_rate = interest_rate

    def projected_balance(self):
        return self.get_balance() * (1 + self.__interest_rate)


class Portfolio:
    def __init__(self):
        self.__accounts = []

    def add_account(self, account):
        self.__accounts.append(account)

    def total_balance(self):
        return sum(account.get_balance() for account in self.__accounts)
```

Design justification:

- `SavingsAccount` **is an** `Account`, so inheritance is appropriate
- `Portfolio` **has accounts**, so containment is appropriate
- private balance plus validated `deposit()` protects the object invariant

---

## 11. Worked Example 2 — Sequential File Merge

Two files contain records sorted by integer ID. Merge them without sorting the combined result again.

```python
def parse_record(line):
    identifier, name = line.rstrip("\n").split(",", 1)
    return int(identifier), name


def merge_sorted_files(first_name, second_name, output_name):
    with open(first_name, "r", encoding="utf-8") as first_file:
        first_records = [parse_record(line) for line in first_file if line.strip()]
    with open(second_name, "r", encoding="utf-8") as second_file:
        second_records = [parse_record(line) for line in second_file if line.strip()]

    first_index = 0
    second_index = 0
    merged = []

    while first_index < len(first_records) and second_index < len(second_records):
        if first_records[first_index][0] <= second_records[second_index][0]:
            merged.append(first_records[first_index])
            first_index += 1
        else:
            merged.append(second_records[second_index])
            second_index += 1

    merged.extend(first_records[first_index:])
    merged.extend(second_records[second_index:])

    with open(output_name, "w", encoding="utf-8") as output_file:
        for identifier, name in merged:
            output_file.write(f"{identifier},{name}\n")
```

Because both inputs are already ordered, the merge is `O(n + m)`. A common error is stopping when either file ends and forgetting to copy the remaining records from the other file.

---

## 12. Worked Example 3 — Hash Collision Trace

For table size 7, use `key MOD 7` and linear probing.

Insert keys `10`, `17`, `24`:

| key | calculated slot | collision path | final slot |
|---:|---:|---|---:|
| 10 | 3 | none | 3 |
| 17 | 3 | slot 3 occupied | 4 |
| 24 | 3 | slots 3 and 4 occupied | 5 |

Searching for `24` must repeat the same probing sequence: `3 → 4 → 5`. Stopping after the first collision would incorrectly report that the key is absent.

Tests should include:

- key found at its home slot
- key found after one or more collisions
- missing key that reaches an unused slot
- insertion when every slot is occupied
- update of an existing key

---

## 13. Worked Example 4 — Controlled File Failure

```python
def average_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            values = [float(line.strip()) for line in input_file if line.strip()]
        if not values:
            raise ValueError("the file contains no values")
        return sum(values) / len(values)
    except FileNotFoundError:
        print("No file was found")
    except ValueError as error:
        print(f"Invalid data: {error}")
    return None
```

Evidence should show at least:

| Test | Expected result |
|---|---|
| valid numeric lines | correct average returned |
| missing file | clear missing-file message; program continues safely |
| non-numeric line | invalid-data message |
| empty file | explicit empty-data message |

---

## 14. Common Mistakes Checklist

- [ ] I do not include low-level or declarative tasks in Paper 4 practice.
- [ ] I distinguish an object from its class.
- [ ] I use inheritance only for an “is-a” relationship.
- [ ] I use containment for a “has-a” relationship.
- [ ] Setters preserve object invariants instead of assigning blindly.
- [ ] Overridden methods demonstrate real polymorphic behaviour.
- [ ] I understand that write mode truncates an existing file.
- [ ] I distinguish serial, sequential and random organisation.
- [ ] Hash probing is bounded and uses the same path for insert and find.
- [ ] I catch specific exceptions and do not hide unrelated faults.
- [ ] My test evidence states the expected and actual result.

---

## 15. 10 Marks Quick Check

1. Define a programming paradigm. **[1]**
2. State the two Section 20 paradigms excluded from Paper 4. **[2]**
3. Distinguish inheritance from containment. **[2]**
4. Explain how polymorphism is shown by an overridden method. **[2]**
5. State the effect of opening an existing file in write mode. **[1]**
6. Explain why specific exception types should be caught. **[2]**

**Total: 10 marks**

### Quick Check Answers

1. A general approach/style for organising computation and expressing solutions. **[1]**
2. Low-level **[1]** and declarative **[1]**.
3. Inheritance models an “is-a” relationship between subclass and superclass **[1]**; containment stores/uses another object in a “has-a” relationship **[1]**.
4. A subclass supplies a different implementation under the same method name/interface **[1]**; calling the method on different object types selects the appropriate behaviour **[1]**.
5. The existing contents are truncated/replaced. **[1]**
6. Different failures can receive appropriate responses **[1]**, while unrelated programming errors are not silently hidden **[1]**.

---

## 16. 20 Marks Practice

A text file contains sensor records in the format `sensor_id,reading`. Design a robust object-oriented loader.

1. Write a Python class `SensorReading` with private sensor ID and reading attributes, a constructor, getters and a validated setter that accepts readings from `-50.0` to `150.0` inclusive. **[8]**
2. Write `load_readings(filename)` to read valid records into a list of `SensorReading` objects. It must handle a missing file and report malformed/out-of-range records without stopping the remaining load. **[8]**
3. Give four tests with expected outcomes, including a boundary and a failure case. **[4]**

**Total: 20 marks**

### 20 Marks Practice Mark Scheme

Class header and two private attributes **[2]**; constructor uses the setter **[1]**; two getters **[2]**; inclusive range validation **[2]**; controlled assignment or appropriate exception **[1]**. **[8]**

```python
class SensorReading:
    def __init__(self, sensor_id, reading):
        self.__sensor_id = sensor_id
        self.__reading = 0.0
        self.set_reading(reading)

    def get_sensor_id(self):
        return self.__sensor_id

    def get_reading(self):
        return self.__reading

    def set_reading(self, new_reading):
        value = float(new_reading)
        if value < -50.0 or value > 150.0:
            raise ValueError("reading outside permitted range")
        self.__reading = value
```

Opens and iterates through the file safely **[2]**; splits/validates each record **[1]**; creates and stores objects **[1]**; handles missing file **[1]**; catches malformed conversion/range errors per record **[2]**; returns the completed list **[1]**. **[8]**

```python
def load_readings(filename):
    readings = []
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            for line_number, line in enumerate(input_file, start=1):
                try:
                    fields = line.strip().split(",")
                    if len(fields) != 2 or fields[0] == "":
                        raise ValueError("record must contain ID and reading")
                    readings.append(SensorReading(fields[0], fields[1]))
                except ValueError as error:
                    print(f"Line {line_number} rejected: {error}")
    except FileNotFoundError:
        print("The sensor file was not found")
    return readings
```

Tests, one mark each for data plus expected outcome, for example: `-50.0` accepted; `150.0` accepted; `150.1` rejected and later valid lines still load; malformed field count rejected; non-numeric reading rejected; missing file returns an empty list and displays the message. Maximum **[4]**.

---

## 17. Final Self-Assessment

- [ ] I can distinguish all four paradigms and the Paper 4 exclusion boundary.
- [ ] I can design procedural subroutines with clear parameters and returns.
- [ ] I can use every required OOP term accurately.
- [ ] I can implement inheritance, polymorphism, containment and encapsulation.
- [ ] I can read, write and append text-file records safely.
- [ ] I can distinguish serial, sequential and random organisation.
- [ ] I can implement and test hash-based direct access with collisions.
- [ ] I can catch appropriate exceptions without hiding programming errors.
- [ ] I completed both marked practice sets before reading the answers.
