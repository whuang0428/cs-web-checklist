# A2 9618 Paper 4 Practical Review — Set A

> **Original practice paper:** three independent programming scenarios covering Sections 19–20. All tasks and data are original and are not copied from Cambridge examination material.

**Time:** 2 hours 30 minutes  
**Total:** **75 marks**  
**Language used in this practice:** Python 3 console mode  
**Required output:** complete program code and evidence of testing

Paper 4 does not assess low-level or declarative programming. Do not use a calculator. Complete every question on a centre-provided computer without internet or email access while timing yourself.

---

## Candidate Instructions

For each question:

1. save the source code using a clear filename
2. run every requested test
3. record the input, expected result and actual result
4. preserve evidence of both code and output
5. correct faults, then repeat the failed test and related earlier tests

Marks reward the specified programming features. Code that produces one correct sample output but does not implement the required algorithm or structure may not earn the algorithm marks.

---

## Question 1 — Delivery Algorithms [24]

A relief centre stores each planned delivery as a list:

```text
[delivery_id, priority, weight]
```

Example:

```text
[[104, 2, 8.5], [101, 1, 4.0], [109, 3, 12.5], [106, 2, 5.0]]
```

Delivery IDs are unique integers. Weight is measured in kilograms.

1. Write `insertion_sort_deliveries(deliveries)` to sort the list into ascending delivery-ID order. You must implement insertion sort and must not call `sort()` or `sorted()`. **[7]**
2. Write `binary_search_delivery(deliveries, target_id)` to return the index of a matching delivery or `-1`. The input list will already be sorted by delivery ID. **[5]**
3. Write a recursive function `total_weight(deliveries, index)` that returns the total weight from `index` to the final record. The base case must handle an index beyond the final record. **[4]**
4. Write main-program code that displays the records before and after sorting, searches for IDs `106` and `999`, and displays the recursive total weight. **[4]**
5. Produce four tests with expected and actual results. Include an empty list, one item, a missing search key and the supplied four-record list. **[4]**

---

## Question 2 — Course Booking Objects [27]

A community centre sells places on courses.

Every course has:

- a private course ID
- a private title
- a private base fee that cannot be negative

A workshop is a specialised course. It also stores a positive number of practical hours and adds `4.50` per practical hour to the base fee.

A booking stores a customer name and a collection of course objects.

1. Write a class `Course` with a constructor, getters, a validated base-fee setter and `calculate_fee()`. **[7]**
2. Write a subclass `Workshop`. Its constructor must call the superclass constructor. Override `calculate_fee()` to include the practical-hour charge. **[6]**
3. Write a class `Booking` that contains course objects. Include `add_course()` and `total_fee()`. `total_fee()` must use polymorphism rather than checking object types. **[5]**
4. Write `save_courses(filename, courses)` and `load_courses(filename)`. Use comma-separated text records beginning with `COURSE` or `WORKSHOP`, preserve all fields and handle a missing input file. **[5]**
5. Produce four tests with expected and actual results: valid basic course, valid workshop, rejected negative fee and a booking containing both course types. **[4]**

---

## Question 3 — Clinic Queue and Direct Lookup [24]

A clinic stores waiting patients as `[patient_id, name]` records.

1. Write a class `CircularQueue` using a fixed-size list, front pointer, rear pointer and item count. Implement `enqueue()` and `dequeue()`. Enqueue must return `False` when full; dequeue must return `None` when empty. **[8]**
2. Write `load_patients(filename, queue)` to read records in the format `patient_id,name`. Add valid records until the file ends or the queue is full. Report malformed records and handle a missing file without crashing. Return the number added. **[6]**
3. Write a fixed-size `PatientTable` that uses `patient_id MOD table_size` with linear probing. Implement `insert(patient_id, name)` and `find(patient_id)`. Both operations must terminate when the table is full. **[6]**
4. Produce four tests with expected and actual results, covering queue overflow, queue underflow, a hash collision and a missing patient ID. **[4]**

---

## Mark Scheme

### Question 1 Mark Scheme

#### 1.1 Insertion sort — 7 marks

- function accepts the delivery list **[1]**
- outer loop begins with the second record **[1]**
- current record is saved before shifting **[1]**
- previous records are compared using delivery ID **[1]**
- larger records shift one place right **[1]**
- insertion position is updated safely **[1]**
- saved record is placed in the gap **[1]**

```python
def insertion_sort_deliveries(deliveries):
    for current in range(1, len(deliveries)):
        record_to_insert = deliveries[current]
        position = current - 1

        while position >= 0 and deliveries[position][0] > record_to_insert[0]:
            deliveries[position + 1] = deliveries[position]
            position -= 1

        deliveries[position + 1] = record_to_insert
```

#### 1.2 Binary search — 5 marks

- correct low/high initialisation **[1]**
- loop continues while the interval is non-empty **[1]**
- middle index calculated correctly **[1]**
- correct equality and left/right updates **[1]**
- returns matching index or `-1` **[1]**

```python
def binary_search_delivery(deliveries, target_id):
    low = 0
    high = len(deliveries) - 1

    while low <= high:
        middle = (low + high) // 2
        middle_id = deliveries[middle][0]
        if middle_id == target_id:
            return middle
        if target_id < middle_id:
            high = middle - 1
        else:
            low = middle + 1

    return -1
```

#### 1.3 Recursive total — 4 marks

- function accepts list and index **[1]**
- reachable base case returns zero **[1]**
- recursive call progresses to `index + 1` **[1]**
- current weight and recursive result are combined **[1]**

```python
def total_weight(deliveries, index):
    if index >= len(deliveries):
        return 0.0
    return deliveries[index][2] + total_weight(deliveries, index + 1)
```

#### 1.4 Main program — 4 marks

- output before and after sorting **[1]**
- sort function called **[1]**
- both required searches called and displayed **[1]**
- recursive total called and displayed **[1]**

```python
def run_delivery_program():
    deliveries = [
        [104, 2, 8.5],
        [101, 1, 4.0],
        [109, 3, 12.5],
        [106, 2, 5.0],
    ]
    print("Before:", deliveries)
    insertion_sort_deliveries(deliveries)
    print("After:", deliveries)
    print("Search 106:", binary_search_delivery(deliveries, 106))
    print("Search 999:", binary_search_delivery(deliveries, 999))
    print("Total weight:", total_weight(deliveries, 0))
```

Expected sorted IDs: `101, 104, 106, 109`; search `106` returns index `2`; search `999` returns `-1`; total weight is `30.0`.

#### 1.5 Testing — 4 marks

One mark for each required test with explicit input, expected result and matching actual result:

- empty list remains empty and total weight is `0.0`
- one-item list remains valid; its ID is found at index `0`
- missing key returns `-1`
- supplied list sorts to IDs `101, 104, 106, 109` and total weight is `30.0`

**Question 1 total: 24 marks**

---

### Question 2 Mark Scheme

#### 2.1 Course class — 7 marks

- class and constructor **[1]**
- three private attributes **[1]**
- constructor initialises ID and title **[1]**
- constructor uses validated fee setter **[1]**
- ID and title getters **[1]**
- fee getter **[1]**
- rejects negative fee and `calculate_fee()` returns the stored fee **[1]**

```python
class Course:
    def __init__(self, course_id, title, base_fee):
        self.__course_id = course_id
        self.__title = title
        self.__base_fee = 0.0
        self.set_base_fee(base_fee)

    def get_course_id(self):
        return self.__course_id

    def get_title(self):
        return self.__title

    def get_base_fee(self):
        return self.__base_fee

    def set_base_fee(self, new_fee):
        value = float(new_fee)
        if value < 0:
            raise ValueError("base fee cannot be negative")
        self.__base_fee = value

    def calculate_fee(self):
        return self.__base_fee
```

#### 2.2 Workshop subclass — 6 marks

- correct inheritance **[1]**
- constructor receives superclass and additional data **[1]**
- calls `super().__init__()` correctly **[1]**
- stores practical hours privately **[1]**
- rejects non-positive hours **[1]**
- overridden calculation adds `hours * 4.50` **[1]**

```python
class Workshop(Course):
    def __init__(self, course_id, title, base_fee, practical_hours):
        super().__init__(course_id, title, base_fee)
        if practical_hours <= 0:
            raise ValueError("practical hours must be positive")
        self.__practical_hours = int(practical_hours)

    def get_practical_hours(self):
        return self.__practical_hours

    def calculate_fee(self):
        return super().calculate_fee() + self.__practical_hours * 4.50
```

#### 2.3 Booking containment and polymorphism — 5 marks

- class stores customer and private collection **[1]**
- constructor initialises empty collection **[1]**
- `add_course()` stores an object **[1]**
- total loops through all contained objects **[1]**
- calls the common `calculate_fee()` interface without type tests **[1]**

```python
class Booking:
    def __init__(self, customer):
        self.__customer = customer
        self.__courses = []

    def add_course(self, course):
        self.__courses.append(course)

    def total_fee(self):
        total = 0.0
        for course in self.__courses:
            total += course.calculate_fee()
        return total
```

#### 2.4 File save and load — 5 marks

- write mode and one record per object **[1]**
- type marker and all required fields preserved **[1]**
- read mode parses records and constructs the correct class **[1]**
- missing file handled **[1]**
- returns loaded object list **[1]**

```python
def save_courses(filename, courses):
    with open(filename, "w", encoding="utf-8") as output_file:
        for course in courses:
            if isinstance(course, Workshop):
                fields = [
                    "WORKSHOP",
                    course.get_course_id(),
                    course.get_title(),
                    str(course.get_base_fee()),
                    str(course.get_practical_hours()),
                ]
            else:
                fields = [
                    "COURSE",
                    course.get_course_id(),
                    course.get_title(),
                    str(course.get_base_fee()),
                ]
            output_file.write(",".join(fields) + "\n")


def load_courses(filename):
    courses = []
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            for line in input_file:
                fields = line.strip().split(",")
                if fields[0] == "COURSE" and len(fields) == 4:
                    courses.append(Course(fields[1], fields[2], float(fields[3])))
                elif fields[0] == "WORKSHOP" and len(fields) == 5:
                    courses.append(
                        Workshop(fields[1], fields[2], float(fields[3]), int(fields[4]))
                    )
                else:
                    print("Invalid course record skipped")
    except FileNotFoundError:
        print("Course file not found")
    return courses
```

#### 2.5 Testing — 4 marks

One mark for each required test with expected and matching actual result:

- `Course("C1", "Writing", 20)` returns fee `20.0`
- `Workshop("W1", "Robotics", 30, 4)` returns fee `48.0`
- negative base fee raises `ValueError`
- booking containing those two valid objects returns total `68.0`

**Question 2 total: 27 marks**

---

### Question 3 Mark Scheme

#### 3.1 Circular queue — 8 marks

- constructor allocates fixed-size storage **[1]**
- front, rear and count initialised **[1]**
- enqueue detects full state and returns `False` **[1]**
- enqueue stores at rear **[1]**
- rear wraps with modulo and count increases **[1]**
- dequeue detects empty state and returns `None` **[1]**
- dequeue reads at front **[1]**
- front wraps and count decreases **[1]**

```python
class CircularQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.__data = [None] * capacity
        self.__front = 0
        self.__rear = 0
        self.__count = 0

    def enqueue(self, item):
        if self.__count == len(self.__data):
            return False
        self.__data[self.__rear] = item
        self.__rear = (self.__rear + 1) % len(self.__data)
        self.__count += 1
        return True

    def dequeue(self):
        if self.__count == 0:
            return None
        item = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % len(self.__data)
        self.__count -= 1
        return item

    def is_full(self):
        return self.__count == len(self.__data)
```

#### 3.2 Patient-file loader — 6 marks

- opens file safely and loops through records **[1]**
- validates exactly two non-empty fields **[1]**
- converts patient ID to integer **[1]**
- enqueues valid record and counts success **[1]**
- stops when full and reports malformed records **[1]**
- handles missing file and returns count **[1]**

```python
def load_patients(filename, queue):
    added = 0
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            for line_number, line in enumerate(input_file, start=1):
                if queue.is_full():
                    print("Queue full; remaining records not loaded")
                    break
                try:
                    fields = line.strip().split(",")
                    if len(fields) != 2 or fields[0] == "" or fields[1] == "":
                        raise ValueError("expected patient ID and name")
                    patient = [int(fields[0]), fields[1]]
                    if queue.enqueue(patient):
                        added += 1
                except ValueError as error:
                    print(f"Line {line_number} rejected: {error}")
    except FileNotFoundError:
        print("Patient file not found")
    return added
```

#### 3.3 Patient hash table — 6 marks

- fixed-size key and value storage **[1]**
- initial slot uses modulo **[1]**
- insert handles empty or matching slot **[1]**
- collision advances with wraparound **[1]**
- find repeats probing and returns matching name **[1]**
- both operations are bounded and return failure values **[1]**

```python
class PatientTable:
    def __init__(self, table_size):
        self.__ids = [None] * table_size
        self.__names = [None] * table_size

    def insert(self, patient_id, name):
        index = patient_id % len(self.__ids)
        for _ in range(len(self.__ids)):
            if self.__ids[index] in (None, patient_id):
                self.__ids[index] = patient_id
                self.__names[index] = name
                return True
            index = (index + 1) % len(self.__ids)
        return False

    def find(self, patient_id):
        index = patient_id % len(self.__ids)
        for _ in range(len(self.__ids)):
            if self.__ids[index] is None:
                return None
            if self.__ids[index] == patient_id:
                return self.__names[index]
            index = (index + 1) % len(self.__ids)
        return None
```

#### 3.4 Testing — 4 marks

One mark for each required test with expected and matching actual result:

- enqueue beyond capacity returns `False`
- dequeue on an empty queue returns `None`
- IDs `10` and `17` in a size-7 table collide and both remain findable
- an uninserted ID returns `None`

**Question 3 total: 24 marks**

---

## Final Check

- [ ] All three questions were attempted in 2 hours 30 minutes.
- [ ] Every program was saved and executed.
- [ ] Required algorithms were implemented instead of replaced by library shortcuts.
- [ ] OOP relationships are visible in the code.
- [ ] File and exception paths were tested.
- [ ] Evidence includes the code, input, expected result and actual output.
- [ ] Question totals are 24 + 27 + 24 = 75 marks.
