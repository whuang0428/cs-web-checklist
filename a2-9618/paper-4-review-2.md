# A2 9618 Paper 4 Practical Review — Set B

> **Original practice paper:** an independent second practical set. All scenarios, data and reference solutions are newly written.

**Time:** 2 hours 30 minutes  
**Total:** **75 marks**  
**Language:** Python 3 console mode  
**Required evidence:** complete code, test input, expected result and actual output

This set applies Sections 19–20 and contains no low-level or declarative programming tasks.

---

## Question 1 — Race Result Processing [25]

Each race result is stored as `[runner_id, finish_time]`, where IDs are unique integers and time is a positive real number.

1. Write `bubble_sort_results(results)` to sort results into ascending finish-time order. Implement bubble sort with early termination; do not call `sort()` or `sorted()`. **[7]**
2. Write `linear_search_runner(results, runner_id)` to return the matching record or `None`. **[4]**
3. Write a recursive function `count_faster(results, limit, index)` that returns how many results from `index` onwards have a finish time below `limit`. **[5]**
4. Write `load_results(filename)` to read `runner_id,finish_time` records. Report malformed records, reject non-positive times and handle a missing file without crashing. **[5]**
5. Produce four tests with expected and actual results, including already sorted data, reverse-ordered data, a missing runner and a malformed file record. **[4]**

---

## Question 2 — Ticket Order Objects [26]

Every event ticket has a private code, private event name and non-negative base price. A `GroupTicket` also stores a group size from 2 to 8 and applies a 10% discount to the total `base price * group size`.

An order contains ticket objects and uses their common fee method.

1. Write class `Ticket` with constructor, getters, validated price setter and `calculate_fee()`. **[7]**
2. Write subclass `GroupTicket`, call the superclass constructor, validate group size and override `calculate_fee()`. **[6]**
3. Write class `TicketOrder` that contains tickets and implements `add_ticket()` and polymorphic `total_fee()`. **[5]**
4. Write `append_order(filename, customer, order)` to append the customer and total fee as one comma-separated line. Handle a file-writing error. **[4]**
5. Produce four tests with expected and actual results: basic ticket, both group-size boundaries, rejected group size and a mixed order. **[4]**

---

## Question 3 — Search Tree Catalogue [24]

A catalogue stores unique integer item IDs in a binary search tree. Each node also stores an item name.

1. Write classes `CatalogueNode` and `CatalogueTree`. Implement iterative `insert(item_id, name)` and `find(item_id)`. Duplicate IDs must update the existing name rather than insert a new node. **[10]**
2. Write recursive `in_order(node, output)` to append `[item_id, name]` records to `output` in ascending ID order. **[5]**
3. Write `load_catalogue(filename, tree)` for `item_id,name` text records. Continue after malformed records and handle a missing file. Return the number loaded. **[5]**
4. Produce four tests with expected and actual results: empty search, root/left/right insertion, duplicate update and malformed input. **[4]**

---

## Mark Scheme

### Question 1 Mark Scheme

#### 1.1 Bubble sort — 7 marks

- function accepts list and sets upper boundary **[1]**
- swapped flag initialised for first pass **[1]**
- repeated passes while work remains **[1]**
- correct adjacent loop bounds **[1]**
- compares finish-time field **[1]**
- swaps complete records **[1]**
- early termination and shrinking boundary **[1]**

```python
def bubble_sort_results(results):
    upper = len(results) - 1
    swapped = True
    while upper > 0 and swapped:
        swapped = False
        for index in range(upper):
            if results[index][1] > results[index + 1][1]:
                results[index], results[index + 1] = results[index + 1], results[index]
                swapped = True
        upper -= 1
```

#### 1.2 Linear search — 4 marks

- loop through records **[1]**
- compare ID field **[1]**
- return matching record immediately **[1]**
- return `None` after complete failure **[1]**

```python
def linear_search_runner(results, runner_id):
    for result in results:
        if result[0] == runner_id:
            return result
    return None
```

#### 1.3 Recursive count — 5 marks

- correct parameters **[1]**
- reachable end-of-list base case **[1]**
- current record compared with limit **[1]**
- recursive call progresses to next index **[1]**
- current contribution combined with returned count **[1]**

```python
def count_faster(results, limit, index):
    if index >= len(results):
        return 0
    current = 1 if results[index][1] < limit else 0
    return current + count_faster(results, limit, index + 1)
```

#### 1.4 File loader — 5 marks

- opens/iterates safely **[1]**
- checks field count and converts values **[1]**
- rejects non-positive time **[1]**
- reports a bad record and continues **[1]**
- handles missing file and returns list **[1]**

```python
def load_results(filename):
    results = []
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            for line_number, line in enumerate(input_file, start=1):
                try:
                    fields = line.strip().split(",")
                    if len(fields) != 2:
                        raise ValueError("expected two fields")
                    runner_id = int(fields[0])
                    finish_time = float(fields[1])
                    if finish_time <= 0:
                        raise ValueError("time must be positive")
                    results.append([runner_id, finish_time])
                except ValueError as error:
                    print(f"Line {line_number} rejected: {error}")
    except FileNotFoundError:
        print("Result file not found")
    return results
```

#### 1.5 Testing — 4 marks

One mark for each required test with input, expected and matching actual result: sorted data stops without changing order; reverse data becomes ascending; missing ID returns `None`; malformed file row is reported while later valid rows still load. **[4]**

**Question 1 total: 25 marks**

---

### Question 2 Mark Scheme

#### 2.1 Ticket — 7 marks

- class/constructor **[1]**
- three private attributes **[1]**
- code and name initialised **[1]**
- constructor uses setter **[1]**
- code/name getters **[1]**
- price getter/setter rejects negative **[1]**
- fee returns base price **[1]**

```python
class Ticket:
    def __init__(self, code, event_name, base_price):
        self.__code = code
        self.__event_name = event_name
        self.__base_price = 0.0
        self.set_base_price(base_price)

    def get_code(self):
        return self.__code

    def get_event_name(self):
        return self.__event_name

    def get_base_price(self):
        return self.__base_price

    def set_base_price(self, new_price):
        value = float(new_price)
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__base_price = value

    def calculate_fee(self):
        return self.__base_price
```

#### 2.2 GroupTicket — 6 marks

- inherits from `Ticket` **[1]**
- constructor receives all fields **[1]**
- superclass constructor called **[1]**
- group size stored privately **[1]**
- inclusive 2–8 validation **[1]**
- overridden calculation applies size and 10% discount **[1]**

```python
class GroupTicket(Ticket):
    def __init__(self, code, event_name, base_price, group_size):
        super().__init__(code, event_name, base_price)
        if group_size < 2 or group_size > 8:
            raise ValueError("group size must be from 2 to 8")
        self.__group_size = int(group_size)

    def get_group_size(self):
        return self.__group_size

    def calculate_fee(self):
        return self.get_base_price() * self.__group_size * 0.90
```

#### 2.3 TicketOrder — 5 marks

- class/constructor stores customer and empty collection **[2]**
- add method stores object **[1]**
- loops over all objects **[1]**
- calls shared fee method without type tests **[1]**

```python
class TicketOrder:
    def __init__(self, customer):
        self.__customer = customer
        self.__tickets = []

    def add_ticket(self, ticket):
        self.__tickets.append(ticket)

    def total_fee(self):
        return sum(ticket.calculate_fee() for ticket in self.__tickets)
```

#### 2.4 Append order — 4 marks

- append mode/encoding **[1]**
- customer and total written as one record **[1]**
- specific file error handled **[1]**
- returns success/failure **[1]**

```python
def append_order(filename, customer, order):
    try:
        with open(filename, "a", encoding="utf-8") as output_file:
            output_file.write(f"{customer},{order.total_fee():.2f}\n")
        return True
    except OSError as error:
        print(f"Order could not be saved: {error}")
        return False
```

#### 2.5 Testing — 4 marks

One mark each: basic ticket returns its base fee; group sizes 2 and 8 are accepted with correct discounted totals; size 1 or 9 is rejected; mixed order calls both implementations and returns their sum. Maximum **[4]**.

**Question 2 total: 26 marks**

---

### Question 3 Mark Scheme

#### 3.1 Tree classes, insert and find — 10 marks

- node stores ID, name, left and right **[2]**
- tree initialises empty root **[1]**
- insert handles empty tree **[1]**
- iterative comparison selects left/right **[2]**
- attaches at the correct empty child **[1]**
- duplicate updates name **[1]**
- find follows ordering **[1]**
- find returns name or `None` **[1]**

```python
class CatalogueNode:
    def __init__(self, item_id, name):
        self.item_id = item_id
        self.name = name
        self.left = None
        self.right = None


class CatalogueTree:
    def __init__(self):
        self.root = None

    def insert(self, item_id, name):
        if self.root is None:
            self.root = CatalogueNode(item_id, name)
            return

        current = self.root
        while True:
            if item_id == current.item_id:
                current.name = name
                return
            if item_id < current.item_id:
                if current.left is None:
                    current.left = CatalogueNode(item_id, name)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = CatalogueNode(item_id, name)
                    return
                current = current.right

    def find(self, item_id):
        current = self.root
        while current is not None:
            if item_id == current.item_id:
                return current.name
            if item_id < current.item_id:
                current = current.left
            else:
                current = current.right
        return None
```

#### 3.2 Recursive traversal — 5 marks

- correct parameters **[1]**
- base case for `None` **[1]**
- recursively visits left **[1]**
- appends current record **[1]**
- recursively visits right **[1]**

```python
def in_order(node, output):
    if node is None:
        return
    in_order(node.left, output)
    output.append([node.item_id, node.name])
    in_order(node.right, output)
```

#### 3.3 File loader — 5 marks

- opens/loops and counts **[1]**
- validates two fields **[1]**
- converts ID and inserts **[1]**
- malformed-record exception handled per line **[1]**
- missing-file handling and return **[1]**

```python
def load_catalogue(filename, tree):
    loaded = 0
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            for line_number, line in enumerate(input_file, start=1):
                try:
                    fields = line.strip().split(",", 1)
                    if len(fields) != 2 or fields[1] == "":
                        raise ValueError("expected ID and name")
                    tree.insert(int(fields[0]), fields[1])
                    loaded += 1
                except ValueError as error:
                    print(f"Line {line_number} rejected: {error}")
    except FileNotFoundError:
        print("Catalogue file not found")
    return loaded
```

#### 3.4 Testing — 4 marks

One mark each: empty find returns `None`; root plus smaller/larger IDs appear in sorted traversal; duplicate changes name without another node; malformed row is reported and later valid row loads. **[4]**

**Question 3 total: 24 marks**

---

## Final Check

- [ ] All three questions were attempted in 2 hours 30 minutes.
- [ ] Required algorithms were implemented without library replacements.
- [ ] Every exception path was executed at least once.
- [ ] Evidence states input, expected result and actual output.
- [ ] Question totals are 25 + 26 + 24 = 75 marks.
