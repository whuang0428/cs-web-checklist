# A2 9618 Chapter 19: Computational Thinking and Problem-Solving

<div class="chapter-meta"><strong>A2 9618 · Papers 3–4</strong><span>9618 · 2027–2029 · Version 2</span></div>

## Official Syllabus Checklist

Revise: searching and sorting; abstract data types; algorithm complexity and recursion.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.

> **Paper 3 focus:** explain, trace and compare searching, sorting, abstract data types, complexity and recursion.
>
> **Paper 4 focus:** implement, run, test and justify those algorithms in a permitted console-mode language.

This chapter uses **Python 3 console-mode code** because Python is one of the languages permitted for Paper 4. The algorithms and design principles also apply to Java and Visual Basic .NET.

---

## Syllabus Map

| Syllabus objective | Where it is covered |
|---|---|
| Implement linear and binary searching | Searching and Worked Example 1 |
| State the conditions for binary search and explain its performance | Searching; Comparing Algorithms with Big O |
| Implement insertion sort and bubble sort | Sorting and Worked Example 2 |
| Relate sorting performance to input order and size | Sorting; Comparing Algorithms with Big O |
| Find, insert and delete items in required ADTs | Abstract Data Types; Array-Based Linked List and ADT Composition and Worked Example 3 |
| Describe stacks, queues, linked lists, dictionaries and binary trees | Abstract Data Types |
| Explain graphs and justify their use without implementing graph code | Abstract Data Types |
| Implement one ADT using another | Array-Based Linked List and ADT Composition |
| Compare time and space complexity using Big O notation | Comparing Algorithms with Big O |
| Explain, write and trace recursion | Recursion and Worked Example 4 |
| Explain the call stack and unwinding | Recursion |

---

## Paper 4 Algorithm Workflow

Paper 4 rewards working program code and visible evidence, not an untested algorithm description.

Use this workflow:

1. identify inputs, required outputs and constraints
2. select the data structure and algorithm
3. write a small interface before the internal logic
4. implement one complete operation at a time
5. test normal, boundary and failure cases
6. record meaningful output as evidence
7. re-run earlier tests after every correction

A solution is not complete because it works for one supplied example. It must also handle empty structures, full structures, missing items, duplicate keys and invalid input where these states are possible.

---

## Searching

### Linear search

Linear search checks items in sequence and does not require sorted data.

```python
def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1
```

Properties:

- works with sorted or unsorted data
- worst-case time complexity is `O(n)`
- needs at most one pass
- is often appropriate for a short list or a structure that cannot be indexed efficiently

### Binary search

Binary search repeatedly removes half of the remaining search interval.

```python
def binary_search(values, target):
    low = 0
    high = len(values) - 1

    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if target < values[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return -1
```

Required conditions:

- the data must already be sorted using the same key used by the search
- the algorithm must be able to access the middle item efficiently

For `n` indexed items, binary search has `O(log n)` worst-case time. Doubling the number of items usually adds only one further comparison level. It is unsuitable for an unsorted list and usually a poor choice for a linked list because locating the middle node is not constant time.

---

## Sorting

### Bubble sort

```python
def bubble_sort(values):
    upper = len(values) - 1
    swapped = True

    while upper > 0 and swapped:
        swapped = False
        for index in range(upper):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True
        upper -= 1
```

After each complete pass, the largest remaining item is in its final position. The `swapped` flag allows an already sorted list to stop early.

### Insertion sort

```python
def insertion_sort(values):
    for current in range(1, len(values)):
        item = values[current]
        position = current - 1

        while position >= 0 and values[position] > item:
            values[position + 1] = values[position]
            position -= 1

        values[position + 1] = item
```

The left-hand part of the list is kept sorted. Each new item is shifted into its correct position.

### Performance comparison

| Input condition | Bubble sort | Insertion sort |
|---|---|---|
| already sorted | `O(n)` with early-stop flag | `O(n)` |
| reverse order | `O(n²)` | `O(n²)` |
| random order | normally `O(n²)` | normally `O(n²)` |
| extra space | `O(1)` | `O(1)` |

Do not claim insertion sort is always faster. Its advantage is strongest for small or nearly sorted data because it performs few shifts in that case.

---

## Abstract Data Types

An **abstract data type (ADT)** defines permitted data and operations independently of its implementation.

| ADT | Defining behaviour | Typical operations |
|---|---|---|
| stack | LIFO | push, pop, peek, is-empty |
| queue | FIFO | enqueue, dequeue, is-empty |
| linked list | nodes connected by links | find, insert, delete, traverse |
| dictionary | key maps to value | insert/update, find, delete |
| binary tree | each node has at most two children | find, insert, traverse |
| graph | vertices connected by edges | add/connect/find/traverse conceptually |

### Stack and queue using built-in types

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0
```

```python
class Queue:
    def __init__(self):
        self._items = []
        self._front = 0

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        item = self._items[self._front]
        self._front += 1
        return item

    def is_empty(self):
        return self._front == len(self._items)
```

The queue avoids deleting index `0` on every operation. In a fixed-size array implementation, a circular queue reuses released positions.

### Dictionary

A dictionary associates each unique key with a value. A hash table is one possible implementation; a search tree is another.

```python
def count_codes(codes):
    frequencies = {}
    for code in codes:
        frequencies[code] = frequencies.get(code, 0) + 1
    return frequencies
```

Average dictionary lookup is commonly treated as `O(1)` for a well-designed hash table, but collision handling can increase the work.

### Binary search tree

```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def contains(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return False
```

A balanced binary search tree supports search and insertion in `O(log n)`. A badly skewed tree can degrade to `O(n)`.

### Graph boundary

A graph contains:

- **vertices/nodes** representing entities
- **edges/arcs** representing connections
- optionally weights, directions or labels

Suitable uses include road networks, social connections and dependency networks. The syllabus requires candidates to describe and justify graphs, but not write graph-structure code.

---

## Array-Based Linked List and ADT Composition

### Linked list with a free list

The following fixed-size implementation uses parallel arrays. `start` points to the first active node and `free` points to the first unused node.

```python
class ArrayLinkedList:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.next_index = [index + 1 for index in range(capacity)]
        if capacity > 0:
            self.next_index[-1] = -1
            self.free = 0
        else:
            self.free = -1
        self.start = -1

    def find(self, target):
        current = self.start
        while current != -1:
            if self.data[current] == target:
                return current
            current = self.next_index[current]
        return -1

    def insert_front(self, item):
        if self.free == -1:
            return False
        new_index = self.free
        self.free = self.next_index[new_index]
        self.data[new_index] = item
        self.next_index[new_index] = self.start
        self.start = new_index
        return True

    def delete(self, target):
        previous = -1
        current = self.start

        while current != -1 and self.data[current] != target:
            previous = current
            current = self.next_index[current]

        if current == -1:
            return False

        if previous == -1:
            self.start = self.next_index[current]
        else:
            self.next_index[previous] = self.next_index[current]

        self.data[current] = None
        self.next_index[current] = self.free
        self.free = current
        return True
```

Deletion has two separate cases: deleting the head and deleting after a previous node. The removed node must be returned to the free list.

### Queue implemented using two stacks

This demonstrates that one ADT can be implemented from another ADT.

```python
class TwoStackQueue:
    def __init__(self):
        self._input = []
        self._output = []

    def enqueue(self, item):
        self._input.append(item)

    def dequeue(self):
        if not self._output:
            while self._input:
                self._output.append(self._input.pop())
        if not self._output:
            raise IndexError("queue is empty")
        return self._output.pop()
```

An item may be moved once from `_input` to `_output`, so a sequence of operations has efficient amortised behaviour even though one dequeue may move several items.

---

## Comparing Algorithms with Big O

Big O describes how resource use grows as input size `n` grows. It ignores constant multipliers and small lower-order terms.

| Complexity | Growth | Example |
|---|---|---|
| `O(1)` | constant | index an array item |
| `O(log n)` | logarithmic | binary search |
| `O(n)` | linear | linear search |
| `O(n log n)` | linearithmic | efficient comparison sorts |
| `O(n²)` | quadratic | insertion/bubble sort worst case |

Compare both:

- **time complexity:** number of significant operations
- **space complexity:** additional memory required as input grows

Example: an iterative factorial calculation uses `O(n)` time and `O(1)` auxiliary space. A direct recursive factorial also uses `O(n)` time but `O(n)` call-stack space.

Use Big O honestly. A hash-table lookup is average `O(1)`, not guaranteed constant time under every collision pattern. A binary search tree is average `O(log n)` only when its shape remains reasonably balanced.

---

## Recursion

A recursive algorithm must contain:

1. a **base case** that returns without another recursive call
2. a **recursive case**
3. progress toward the base case
4. correct combination or propagation of returned results

```python
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)
```

Trace for `factorial(4)`:

```text
factorial(4)
= 4 * factorial(3)
= 4 * 3 * factorial(2)
= 4 * 3 * 2 * factorial(1)
= 4 * 3 * 2 * 1 * factorial(0)
= 4 * 3 * 2 * 1 * 1
= 24
```

### Call stack and unwinding

For every active call, the runtime must preserve information such as:

- parameter and local-variable values
- the return address
- where the returned value will be used

Calls are pushed onto the call stack. Once the base case returns, stack frames are popped in reverse order; this is **unwinding**.

### When recursion is beneficial

Recursion is suitable when the structure is naturally recursive:

- binary-tree traversal
- divide-and-conquer search
- nested folder processing
- backtracking problems

Prefer iteration when it is simpler and deep recursion could exhaust the call stack.

---

## Worked Example 1 — Binary Search Trace

Search for `42` in:

```text
Index:  0   1   2   3   4   5   6   7
Value:  4  11  19  27  35  42  56  80
```

| Step | low | high | middle | value | action |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 7 | 3 | 27 | target is larger; `low = 4` |
| 2 | 4 | 7 | 5 | 42 | found at index 5 |

Only two comparisons are needed. A linear search from index 0 would require six comparisons.

Failure case: when `low` becomes greater than `high`, return `-1`. Do not access another middle item after the interval becomes empty.

---

## Worked Example 2 — Insertion Sort Trace

Sort `[7, 3, 5, 2]`.

| current item | sorted part before insertion | shifts | array after insertion |
|---:|---|---|---|
| 3 | `[7]` | move 7 right | `[3, 7, 5, 2]` |
| 5 | `[3, 7]` | move 7 right | `[3, 5, 7, 2]` |
| 2 | `[3, 5, 7]` | move 7, 5, 3 right | `[2, 3, 5, 7]` |

The last insertion performs the most work because `2` is smaller than every item in the sorted part. This demonstrates why reverse or badly ordered input produces quadratic behaviour.

---

## Worked Example 3 — Linked-List Allocation and Deletion

For capacity 4, the initial free chain is:

```text
free -> 0 -> 1 -> 2 -> 3 -> -1
start -> -1
```

After inserting `C`, then `B`, then `A` at the front:

```text
active: start -> 2(A) -> 1(B) -> 0(C) -> -1
free:   3 -> -1
```

Delete `B`:

1. `previous = 2`, `current = 1`
2. bypass node 1 by setting `next_index[2] = next_index[1]`
3. return node 1 to the free list

```text
active: start -> 2(A) -> 0(C) -> -1
free:   1 -> 3 -> -1
```

Required test cases:

- delete the head
- delete a middle/tail node
- delete a missing value
- insert when full
- delete from an empty list

---

## Worked Example 4 — Recursive Tree Traversal

Calculate the number of nodes in a binary tree.

```python
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```

For a root with two leaf children:

```text
count(root)
= 1 + count(left) + count(right)
= 1 + (1 + 0 + 0) + (1 + 0 + 0)
= 3
```

The empty-subtree base case is essential. Each call moves to a child, so the algorithm progresses toward `None`. Time complexity is `O(n)` because every node is visited once; auxiliary stack space is `O(h)`, where `h` is the tree height.

---

## Required Ideas and Exam Language

Use technical terms as part of a complete statement: identify the component or method, state what it does, then link its effect to the question context. A keyword without a correct relationship is not a complete marking point.

## Common Confusions

- [ ] I do not use binary search before proving the data is sorted.
- [ ] My search failure condition terminates and returns an explicit value.
- [ ] My insertion and bubble sorts use correct index boundaries.
- [ ] I handle empty and full ADT states.
- [ ] Linked-list deletion reconnects the active list and repairs the free list.
- [ ] I distinguish average and worst-case complexity.
- [ ] Every recursive function has a reachable base case.
- [ ] My recursive input becomes smaller or structurally closer to the base case.
- [ ] I test output, state changes and failure behaviour.

---

## Worked Examples

The worked calculations, process templates and scenario answers above model the chain of reasoning expected in examination responses. Rework each example before reading its answer.

## 10-Mark Quick Check

1. State the condition that must be true before binary search is used. **[1]**
2. Give the worst-case time complexity of binary search. **[1]**
3. Explain why insertion sort is efficient for nearly sorted data. **[2]**
4. State the removal order used by a stack and a queue. **[2]**
5. State the two essential branches of a recursive function. **[2]**
6. Explain what happens during recursive unwinding. **[2]**

**Total: 10 marks**

## Quick Check Answers

1. The data is sorted using the search key. **[1]**
2. `O(log n)`. **[1]**
3. The sorted portion needs few shifts **[1]**, so the number of comparisons/moves approaches linear behaviour **[1]**.
4. Stack: LIFO **[1]**; queue: FIFO **[1]**.
5. A base case **[1]** and a recursive case **[1]**.
6. Completed calls are popped from the call stack in reverse order **[1]**, and their return values/state are passed back to the waiting callers **[1]**.

---

## 20-Mark Exam Practice

A program stores unique integer keys in a binary search tree.

1. Write a Python function `tree_search(root, target)` that returns `True` when the target exists and `False` otherwise. Use iteration or recursion. **[5]**
2. Write a Python function `tree_insert(root, key)` that inserts the key and returns the root. Duplicate keys must not be inserted. **[7]**
3. State the average and worst-case time complexity of search and explain the cause of the difference. **[4]**
4. Give four distinct test cases for the two functions, including the expected result or tree state. **[4]**

**Total: 20 marks**

### 20 Marks Practice Mark Scheme

`tree_search`: correct termination for `None` **[1]**; comparison for equality **[1]**; selects left/right using the ordering rule **[2]**; correct Boolean result **[1]**. **[5]**

```python
def tree_search(root, target):
    current = root
    while current is not None:
        if target == current.key:
            return True
        if target < current.key:
            current = current.left
        else:
            current = current.right
    return False
```

`tree_insert`: creates a node **[1]**; handles empty tree **[1]**; traverses according to key order **[2]**; connects to the correct empty child **[1]**; rejects duplicate **[1]**; returns root **[1]**. **[7]**

```python
def tree_insert(root, key):
    if root is None:
        return TreeNode(key)

    current = root
    while True:
        if key == current.key:
            return root
        if key < current.key:
            if current.left is None:
                current.left = TreeNode(key)
                return root
            current = current.left
        else:
            if current.right is None:
                current.right = TreeNode(key)
                return root
            current = current.right
```

Complexity: average `O(log n)` for a reasonably balanced tree **[1]**; worst `O(n)` **[1]**; balanced search removes a subtree at each comparison **[1]**; ordered insertion can produce a skewed chain **[1]**. **[4]**

Tests, one mark each for a distinct case with expected result/state, for example: empty-tree search returns `False`; empty-tree insertion creates the root; insert smaller/larger keys attaches left/right; duplicate insertion leaves the tree unchanged; search for root/leaf/missing key returns the expected Boolean. Maximum **[4]**.

---

## Final Revision Checklist

- [ ] I can implement and test linear and binary searches.
- [ ] I can implement insertion and bubble sorts without index errors.
- [ ] I can find, insert and delete items in the required ADTs.
- [ ] I can explain how one ADT is implemented using another.
- [ ] I can justify a graph without writing graph code.
- [ ] I can compare time and space using Big O notation.
- [ ] I can write and trace recursive algorithms and explain unwinding.
- [ ] I completed both marked practice sets before reading the answers.
