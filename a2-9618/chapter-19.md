# A2 9618 Chapter 19: Computational Thinking and Problem-Solving

<div class="chapter-meta"><strong>A2 9618 · Papers 3–4</strong><span>9618 · 2027–2029 · Version 2</span></div>

## Official Syllabus Checklist

Revise: algorithm tracing and comparison; linear and binary search; bubble and insertion sort; stacks, queues, linked lists, trees and graphs; Big O time and space complexity; recursion and call-stack unwinding.

> **Paper 3 focus:** explain, trace and compare algorithms, abstract data types, complexity and recursion.
>
> **Paper 4 focus:** implement, run and test algorithms and data structures. This project uses **Java console mode**. Pseudocode remains essential for planning and tracing before implementation.

## Core Knowledge

## Chapter at a Glance

### Choose and trace algorithms

<span lang="zh-CN">先确认前置条件，再逐步跟踪状态。</span>

- Linear search works on unsorted data; binary search requires sorted data.
- Bubble sort swaps adjacent out-of-order items; insertion sort inserts each item into a sorted prefix.
- A trace must show index, comparison and changed data, not only the final answer.

**Exam cue:** state why an algorithm suits this data set.

### Implement abstract data types

<span lang="zh-CN">操作规则和底层表示要分开解释。</span>

- A stack is LIFO; a queue is FIFO.
- A linked list uses data and pointer arrays with start and free-list pointers.
- Trees and graphs require explicit traversal rules and visited-state control.

**Exam cue:** explain both the operation and the pointer/index change.

### Compare efficiency

<span lang="zh-CN">复杂度描述输入规模增长时的趋势。</span>

- State time and auxiliary space separately.
- Link `O(1)`, `O(log n)`, `O(n)` or `O(n²)` to the actual access, split or loop.

**Exam cue:** do not call an algorithm “fast” without a growth-rate reason.

### Control recursion

<span lang="zh-CN">递归必须有可达的终止条件。</span>

- Every call reduces the problem towards a base case.
- Parameters and return addresses are stored on the call stack.
- Results combine while calls unwind.

**Exam cue:** show the calls going down and the returned values coming back.

---

## Syllabus Map

| Requirement | Evidence in this chapter |
|---|---|
| Trace and compare searching/sorting | Worked Examples 1 and 2 |
| Use pseudocode and Java implementations | Search and Sort Patterns |
| Explain stack, queue and linked-list operations | Abstract Data Types and Worked Example 3 |
| Explain tree and graph traversal | Trees and Graphs |
| Use Big O time and space | Complexity and Worked Example 4 |
| Write and trace recursion | Recursion and practice |

## Search and Sort Patterns

Linear search compares each item in order. It has worst-case time `O(n)` and works without sorting. Binary search compares the middle item, discards half of a **sorted** range and repeats; its worst-case time is `O(log n)`.

Pseudocode for linear search:

```text
FUNCTION LinearSearch(Values, Target, High) RETURNS INTEGER
    FOR Index <- 0 TO High
        IF Values[Index] = Target THEN
            RETURN Index
        ENDIF
    NEXT Index
    RETURN -1
ENDFUNCTION
```

Pseudocode for binary search, with `High` supplied as the final valid array index:

```text
FUNCTION BinarySearch(Values, Target, High) RETURNS INTEGER
    Low <- 0
    WHILE Low <= High
        Middle <- (Low + High) DIV 2
        IF Values[Middle] = Target THEN
            RETURN Middle
        ELSE
            IF Values[Middle] < Target THEN
                Low <- Middle + 1
            ELSE
                High <- Middle - 1
            ENDIF
        ENDIF
    ENDWHILE
    RETURN -1
ENDFUNCTION
```

Bubble sort repeatedly compares neighbours and swaps them. Insertion sort maintains a sorted prefix and shifts larger values before inserting the current value. Both are `O(n²)` in the worst case; insertion sort can be efficient for small or nearly sorted data.

Pseudocode for bubble sort, using a flag to stop after a pass with no swap:

```text
PROCEDURE BubbleSort(Values, High)
    REPEAT
        Swapped <- FALSE
        FOR Index <- 0 TO High - 1
            IF Values[Index] > Values[Index + 1] THEN
                Temp <- Values[Index]
                Values[Index] <- Values[Index + 1]
                Values[Index + 1] <- Temp
                Swapped <- TRUE
            ENDIF
        NEXT Index
        High <- High - 1
    UNTIL Swapped = FALSE OR High = 0
ENDPROCEDURE
```

Pseudocode for insertion sort:

```text
PROCEDURE InsertionSort(Values, High)
    FOR Current <- 1 TO High
        Item <- Values[Current]
        Position <- Current - 1
        WHILE Position >= 0 AND Values[Position] > Item
            Values[Position + 1] <- Values[Position]
            Position <- Position - 1
        ENDWHILE
        Values[Position + 1] <- Item
    NEXT Current
ENDPROCEDURE
```

```java
import java.util.Arrays;

class Ch19SearchSortDemo {
    static int binarySearch(int[] values, int target) {
        int low = 0;
        int high = values.length - 1;
        while (low <= high) {
            int middle = (low + high) / 2;
            if (values[middle] == target) return middle;
            if (values[middle] < target) low = middle + 1;
            else high = middle - 1;
        }
        return -1;
    }

    static void insertionSort(int[] values) {
        for (int current = 1; current < values.length; current++) {
            int item = values[current];
            int position = current - 1;
            while (position >= 0 && values[position] > item) {
                values[position + 1] = values[position];
                position--;
            }
            values[position + 1] = item;
        }
    }

    public static void main(String[] args) {
        int[] values = {7, 3, 5, 2};
        insertionSort(values);
        if (!Arrays.equals(values, new int[]{2, 3, 5, 7})) throw new AssertionError();
        if (binarySearch(values, 5) != 2) throw new AssertionError();
    }
}
```

## Worked Example 1 — Trace Binary Search

Search `[4, 9, 15, 21, 28, 33, 40]` for `28`.

| Step | Low | High | Middle | Value | Action |
|---:|---:|---:|---:|---:|---|
| 1 | 0 | 6 | 3 | 21 | target larger, so `Low = 4` |
| 2 | 4 | 6 | 5 | 33 | target smaller, so `High = 4` |
| 3 | 4 | 4 | 4 | 28 | return index 4 |

The sorted-data precondition permits half of the remaining range to be discarded.

## Worked Example 2 — Trace One Insertion

The sorted prefix is `[3, 6, 10, 14]` and the next item is `8`: save `8`; shift `14` and `10` right; stop at `6`; insert `8` to obtain `[3, 6, 8, 10, 14]`. Saving the item first prevents it being overwritten.

## Abstract Data Types

An ADT defines permitted operations independently of its representation.

| ADT | Rule | Core operations | Typical representation |
|---|---|---|---|
| Stack | LIFO | push, pop, peek | array plus top pointer |
| Queue | FIFO | enqueue, dequeue | circular array plus front/rear/count |
| Linked list | pointer order | insert, delete, find | data and next arrays, start/free pointers |
| Binary search tree | smaller left, larger right | insert, find, traverse | linked nodes or array records |
| Graph | vertices and edges | add edge, breadth/depth traversal | adjacency matrix/list |

### Required operations in pseudocode

These templates expose the boundary checks and pointer/index changes that an ADT trace must show.

```text
PROCEDURE Push(Item)
    IF Top = MaxIndex THEN
        OUTPUT "Stack full"
    ELSE
        Top <- Top + 1
        Stack[Top] <- Item
    ENDIF
ENDPROCEDURE

FUNCTION Pop() RETURNS ItemType
    IF Top = -1 THEN
        OUTPUT "Stack empty"
    ELSE
        Item <- Stack[Top]
        Top <- Top - 1
        RETURN Item
    ENDIF
ENDFUNCTION

PROCEDURE Enqueue(Item)
    IF Count = Capacity THEN
        OUTPUT "Queue full"
    ELSE
        Rear <- (Rear + 1) MOD Capacity
        Queue[Rear] <- Item
        Count <- Count + 1
    ENDIF
ENDPROCEDURE

FUNCTION Dequeue() RETURNS ItemType
    IF Count = 0 THEN
        OUTPUT "Queue empty"
    ELSE
        Item <- Queue[Front]
        Front <- (Front + 1) MOD Capacity
        Count <- Count - 1
        RETURN Item
    ENDIF
ENDFUNCTION
```

For an array linked list, insertion removes the first node from the free list and connects it into the live chain. Search follows `Next` until the item or null pointer is reached. Deletion reconnects the previous node around the target and returns the removed node to the free list; the `ArrayLinkedList` example below implements all three operations.

For a binary search tree:

```text
FUNCTION TreeFind(Node, Target) RETURNS BOOLEAN
    WHILE Node <> NULL
        IF Target = Node.Key THEN RETURN TRUE
        IF Target < Node.Key THEN Node <- Node.Left ELSE Node <- Node.Right
    ENDWHILE
    RETURN FALSE
ENDFUNCTION

FUNCTION TreeInsert(Node, Item) RETURNS NodeType
    IF Node = NULL THEN RETURN NEW NodeType(Item)
    IF Item < Node.Key THEN Node.Left <- TreeInsert(Node.Left, Item)
    IF Item > Node.Key THEN Node.Right <- TreeInsert(Node.Right, Item)
    RETURN Node
ENDFUNCTION

FUNCTION TreeDelete(Node, Target) RETURNS NodeType
    IF Node = NULL THEN RETURN NULL
    IF Target < Node.Key THEN
        Node.Left <- TreeDelete(Node.Left, Target)
    ELSE IF Target > Node.Key THEN
        Node.Right <- TreeDelete(Node.Right, Target)
    ELSE
        IF Node.Left = NULL THEN RETURN Node.Right
        IF Node.Right = NULL THEN RETURN Node.Left
        Successor <- SmallestNode(Node.Right)
        Node.Key <- Successor.Key
        Node.Right <- TreeDelete(Node.Right, Successor.Key)
    ENDIF
    RETURN Node
ENDFUNCTION
```

The delete cases are: leaf (replace by null), one child (replace by that child), and two children (copy the in-order successor/predecessor, then delete that copied node).

### Dictionary ADT

A dictionary stores **key–value pairs** and supports `insert(key, value)`, `find(key)` and `delete(key)`. Keys are unique even when values repeat. It may be represented by parallel key/value arrays, a binary search tree, or a hash table. With open-address hashing, insertion and search must use the same probe sequence; deletion uses a tombstone rather than an empty slot so later colliding keys remain reachable.

```text
FUNCTION DictionaryFind(TargetKey) RETURNS ValueType
    Index <- Hash(TargetKey)
    FOR Count <- 1 TO Capacity
        IF State[Index] = EMPTY THEN RETURN NOT_FOUND
        IF State[Index] = OCCUPIED AND Keys[Index] = TargetKey THEN
            RETURN Values[Index]
        ENDIF
        Index <- (Index + 1) MOD Capacity
    NEXT Count
    RETURN NOT_FOUND
ENDFUNCTION
```

### ArrayLinkedList

`StartPointer` identifies the first live node. `FreeListPointer` identifies the first unused node. Deleting a node must return it to the free list.

```java
class Ch19ArrayLinkedListDemo {
    static class ArrayLinkedList {
        private final String[] data;
        private final int[] next;
        private int startPointer = -1;
        private int freeListPointer;

        ArrayLinkedList(int capacity) {
            data = new String[capacity];
            next = new int[capacity];
            for (int i = 0; i < capacity - 1; i++) next[i] = i + 1;
            if (capacity > 0) next[capacity - 1] = -1;
            freeListPointer = capacity == 0 ? -1 : 0;
        }

        boolean insertFront(String value) {
            if (freeListPointer == -1) return false;
            int node = freeListPointer;
            freeListPointer = next[node];
            data[node] = value;
            next[node] = startPointer;
            startPointer = node;
            return true;
        }

        int find(String target) {
            int current = startPointer;
            while (current != -1) {
                if (data[current].equals(target)) return current;
                current = next[current];
            }
            return -1;
        }

        boolean delete(String target) {
            int current = startPointer;
            int previous = -1;
            while (current != -1 && !data[current].equals(target)) {
                previous = current;
                current = next[current];
            }
            if (current == -1) return false;
            if (previous == -1) startPointer = next[current];
            else next[previous] = next[current];
            next[current] = freeListPointer;
            freeListPointer = current;
            return true;
        }
    }

    public static void main(String[] args) {
        ArrayLinkedList list = new ArrayLinkedList(2);
        if (!list.insertFront("A") || !list.insertFront("B")) throw new AssertionError();
        if (list.insertFront("C") || !list.delete("A")) throw new AssertionError();
        if (!list.insertFront("C") || list.find("C") == -1) throw new AssertionError();
    }
}
```

### TwoStackQueue

The input stack receives new items. When the output stack is empty, all input items move to it; this reversal makes the oldest item appear on top.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Ch19TwoStackQueueDemo {
    static class TwoStackQueue<T> {
        private final Deque<T> input = new ArrayDeque<>();
        private final Deque<T> output = new ArrayDeque<>();
        void enqueue(T item) { input.push(item); }
        T dequeue() {
            if (output.isEmpty()) while (!input.isEmpty()) output.push(input.pop());
            if (output.isEmpty()) throw new IllegalStateException("queue empty");
            return output.pop();
        }
    }
    public static void main(String[] args) {
        TwoStackQueue<String> queue = new TwoStackQueue<>();
        queue.enqueue("first"); queue.enqueue("second");
        if (!queue.dequeue().equals("first") || !queue.dequeue().equals("second")) throw new AssertionError();
    }
}
```

## Worked Example 3 — Delete from an Array Linked List

If `StartPointer = 2` and the live chain is `2 → 5 → 1 → -1`, deleting node `5` sets `Next[2] = Next[5]`, then `Next[5] = FreeListPointer`, then `FreeListPointer = 5`. The first change repairs the live chain; the last two recycle the node.

## Trees and Graphs

A **BinarySearchTree** follows an ordering rule. In-order traversal visits left subtree, node, right subtree and produces ascending keys. A graph may use an adjacency matrix or adjacency list. Breadth-first traversal uses a queue; depth-first traversal uses recursion or a stack. Both need a visited set.

```java
import java.util.ArrayList;
import java.util.List;

class Ch19TreeDemo {
    static class Node { int key; Node left, right; Node(int key) { this.key = key; } }
    static class BinarySearchTree {
        Node root;
        void insert(int key) { root = insert(root, key); }
        private Node insert(Node node, int key) {
            if (node == null) return new Node(key);
            if (key < node.key) node.left = insert(node.left, key);
            else if (key > node.key) node.right = insert(node.right, key);
            return node;
        }
        boolean find(int key) {
            Node current = root;
            while (current != null) {
                if (key == current.key) return true;
                current = key < current.key ? current.left : current.right;
            }
            return false;
        }
        void inOrder(Node node, List<Integer> output) {
            if (node == null) return;
            inOrder(node.left, output); output.add(node.key); inOrder(node.right, output);
        }
    }
    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();
        tree.insert(20); tree.insert(10); tree.insert(30);
        List<Integer> values = new ArrayList<>(); tree.inOrder(tree.root, values);
        if (!tree.find(10) || !values.equals(List.of(10, 20, 30))) throw new AssertionError();
    }
}
```

## Complexity

| Pattern | Time | Reason |
|---|---|---|
| array access by index | `O(1)` | one direct access |
| binary search | `O(log n)` | range halves each step |
| linear search/traversal | `O(n)` | up to every item visited |
| two nested full loops | `O(n²)` | about `n × n` operations |

Space complexity counts additional storage. Recursion may use `O(n)` call-stack space even without an explicit array.

## Recursion

Recursion is suitable when a problem is naturally defined in smaller versions of itself, such as tree traversal, divide-and-conquer search, directory traversal or processing a recursively defined grammar. Prefer iteration when a simple loop expresses the task clearly and deep recursion could exhaust stack memory.

At each recursive call, the compiler/runtime creates a **stack frame** containing the return address, parameters and local variables. Frames are pushed while calls descend. When the base case returns, frames are popped in reverse order and each suspended calculation continues; this is **unwinding**. Missing progress causes infinite recursion, while excessive depth can cause stack overflow.

```java
class Ch19RecursionDemo {
    static long factorial(int value) {
        if (value < 0) throw new IllegalArgumentException("negative value");
        if (value <= 1) return 1;
        return value * factorial(value - 1);
    }
    public static void main(String[] args) {
        if (factorial(5) != 120) throw new AssertionError();
    }
}
```

## Worked Example 4 — Calls and Unwinding

For `factorial(4)` the calls descend as `4 → 3 → 2 → 1`. The base case returns `1`. Unwinding gives `2`, then `6`, then `24`. The base case prevents infinite recursion; the reducing parameter makes that case reachable.

## Required Ideas and Exam Language

- State the algorithm's precondition, such as sorted data for binary search.
- For an ADT operation, name the affected pointer/index and the empty/full condition.
- Give a Big O class and link it to halving, one pass or nested passes.
- When tracing recursion, show calls and returned values during unwinding.
- In Java answers, use explicit types, bounds and defined error behaviour.

## Common Confusions

- [ ] I do not use binary search on unsorted data.
- [ ] I distinguish the ADT interface from its representation.
- [ ] I return deleted nodes to the free list.
- [ ] I mark graph vertices as visited.
- [ ] I state time and auxiliary space separately.
- [ ] I include a reachable base case and progress towards it.
- [ ] I use pseudocode for language-neutral design and Java for executable implementation.

## Worked Examples

The four worked examples model trace evidence, pointer reasoning, complexity language and recursion unwinding. Rework each before reading its conclusion.

## 10-Mark Quick Check

1. State the precondition and worst-case time complexity of binary search. **[2]**
2. State the removal order of a stack and a queue. **[2]**
3. State what a dictionary stores and name one operation other than insertion. **[2]**
4. State the time complexity of two full nested loops and explain it. **[2]**
5. State the two requirements that make recursion terminate. **[2]**

**Total: 10 marks**

## Quick Check Answers

1. Data must be sorted **[1]**; worst case `O(log n)` **[1]**. **[2]**
2. Stack LIFO **[1]**; queue FIFO **[1]**. **[2]**
3. Key–value pairs with unique keys **[1]**; `find`/lookup or `delete` **[1]**. **[2]**
4. `O(n²)` **[1]** because the inner loop runs about `n` times for each outer iteration **[1]**. **[2]**
5. Reachable base case **[1]** and progress towards it **[1]**. **[2]**

## 20-Mark Exam Practice

A Java program stores unique integer catalogue keys in a binary search tree.

1. Write Java method `boolean find(int target)` using iteration. **[5]**
2. Write Java method `void insert(int key)` that preserves tree ordering and ignores a duplicate. **[7]**
3. Write recursive Java method `int count(Node node)` that returns the number of nodes. **[4]**
4. State the average search time for a balanced tree and worst-case search time for a fully skewed tree, with reasons. **[4]**

**Total: 20 marks**

### 20 Marks Practice Mark Scheme

1. Starts at root **[1]**; continues while non-null **[1]**; equality returns true **[1]**; selects correct child **[1]**; returns false after failure **[1]**. **[5]**
2. Handles empty root **[1]**; creates node **[1]**; traverses from root **[1]**; compares key **[1]**; follows correct child **[1]**; attaches at null child **[1]**; ignores duplicate **[1]**. **[7]**
3. Null base case **[1]**; counts left **[1]**; counts right **[1]**; returns `1 + left + right` **[1]**. **[4]**
4. Balanced average `O(log n)` because a comparison discards about half a subtree **[2]**; skewed worst case `O(n)` because nodes form one chain **[2]**. **[4]**

## Final Revision Checklist

- [ ] I can express an algorithm in pseudocode before implementing it in Java.
- [ ] I can trace and compare required searches and sorts.
- [ ] I can implement stack, queue, linked-list and tree operations safely.
- [ ] I can choose a graph representation and control repeated visits.
- [ ] I can justify time and auxiliary-space complexity.
- [ ] I can trace recursive calls and unwinding.
- [ ] I can test empty, boundary, duplicate and full-structure cases.
