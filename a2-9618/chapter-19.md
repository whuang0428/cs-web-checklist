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
- A binary search tree follows an ordering rule; a graph models items as vertices and connections as edges.

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
| Explain tree operations and graph features/use | Trees and Graphs |
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
| Graph | vertices and edges | describe connections; justify use | graph ADT |

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

PROCEDURE Pop(BYREF Item : ItemType, BYREF Success : BOOLEAN)
    IF Top = -1 THEN
        Success <- FALSE
    ELSE
        Item <- Stack[Top]
        Top <- Top - 1
        Success <- TRUE
    ENDIF
ENDPROCEDURE

PROCEDURE Enqueue(Item)
    IF Count = Capacity THEN
        OUTPUT "Queue full"
    ELSE
        Rear <- (Rear + 1) MOD Capacity
        Queue[Rear] <- Item
        Count <- Count + 1
    ENDIF
ENDPROCEDURE

PROCEDURE Dequeue(BYREF Item : ItemType, BYREF Success : BOOLEAN)
    IF Count = 0 THEN
        Success <- FALSE
    ELSE
        Item <- Queue[Front]
        Front <- (Front + 1) MOD Capacity
        Count <- Count - 1
        Success <- TRUE
    ENDIF
ENDPROCEDURE
```

`Success` makes the empty-structure contract explicit: the caller uses `Item` only when `Success = TRUE`. This avoids a function path that has no return value.

For an array linked list, insertion removes the first node from the free list and connects it into the live chain. Search follows `Next` until the item or null pointer is reached. Deletion reconnects the previous node around the target and returns the removed node to the free list; the `ArrayLinkedList` example below implements all three operations.

For a binary search tree:

```text
FUNCTION TreeFind(Node : NodeType, Target : KeyType) RETURNS BOOLEAN
    WHILE Node <> NULL
        IF Target = Node.Key THEN
            RETURN TRUE
        ELSE
            IF Target < Node.Key THEN
                Node <- Node.Left
            ELSE
                Node <- Node.Right
            ENDIF
        ENDIF
    ENDWHILE
    RETURN FALSE
ENDFUNCTION

FUNCTION TreeInsert(Node : NodeType, Item : KeyType) RETURNS NodeType
    DECLARE NewNode : NodeType
    IF Node = NULL THEN
        NewNode <- NEW NodeType(Item)
        RETURN NewNode
    ENDIF
    IF Item < Node.Key THEN
        Node.Left <- TreeInsert(Node.Left, Item)
    ELSE
        IF Item > Node.Key THEN
            Node.Right <- TreeInsert(Node.Right, Item)
        ENDIF
    ENDIF
    RETURN Node
ENDFUNCTION

FUNCTION TreeDelete(Node : NodeType, Target : KeyType) RETURNS NodeType
    DECLARE Successor : NodeType
    IF Node = NULL THEN
        RETURN NULL
    ENDIF
    IF Target < Node.Key THEN
        Node.Left <- TreeDelete(Node.Left, Target)
    ELSE
        IF Target > Node.Key THEN
            Node.Right <- TreeDelete(Node.Right, Target)
        ELSE
            IF Node.Left = NULL THEN
                RETURN Node.Right
            ENDIF
            IF Node.Right = NULL THEN
                RETURN Node.Left
            ENDIF
            Successor <- SmallestNode(Node.Right)
            Node.Key <- Successor.Key
            Node.Right <- TreeDelete(Node.Right, Successor.Key)
        ENDIF
    ENDIF
    RETURN Node
ENDFUNCTION
```

The delete cases are: leaf (replace by null), one child (replace by that child), and two children (copy the in-order successor/predecessor, then delete that copied node).

### Dictionary ADT

A dictionary stores **key–value pairs** and supports `insert(key, value)`, `find(key)` and `delete(key)`. Keys are unique even when values repeat. It may be represented by parallel key/value arrays, a binary search tree, or a hash table. With open-address hashing, insertion and search must use the same probe sequence; deletion uses a tombstone rather than an empty slot so later colliding keys remain reachable.

```text
FUNCTION DictionaryFind(TargetKey : KeyType) RETURNS ValueType
    DECLARE Index : INTEGER
    DECLARE Count : INTEGER
    Index <- Hash(TargetKey)
    FOR Count <- 1 TO Capacity
        IF State[Index] = EMPTY THEN
            RETURN NOT_FOUND
        ENDIF
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

A **BinarySearchTree** follows an ordering rule. In-order traversal visits the left subtree, then the node, then the right subtree and produces ascending keys.

A **graph** is an ADT that represents items or places as **vertices** and their relationships as **edges**. An edge may be directed or undirected and may store a weight such as distance, time or cost. A graph is suitable when a problem involves many-to-many connections, such as a route network, social network or dependency map. Candidates need to describe these key features and justify graph use for a situation; they are not required to write code for a graph structure in Section 19.

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
- [ ] I describe graph vertices, edges, direction/weights where relevant, and justify using a graph for the scenario.
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

An inventory program needs searching, sorting and several ADTs. Answer in pseudocode or precise algorithm steps unless Java is requested.

1. Write the essential comparison/update steps for:
   - **(a)** a linear search and a binary search, including the binary-search precondition **[2]**
   - **(b)** bubble sort and insertion sort **[2]**
2. For array or linked implementations, write the essential state changes for:
   - **(a)** push and pop on a stack **[2]**
   - **(b)** enqueue and dequeue on a circular queue **[2]**
   - **(c)** find, insert and delete on a linked list **[3]**
   - **(d)** find and insert in a binary search tree **[2]**
   - **(e)** dictionary lookup by key **[1]**
3. State two defining features of a graph and justify using one for a route network. **[2]**
4. Give the time complexity of linear search and binary search, and state one auxiliary-space cost that could differ between two algorithms. **[2]**
5. State the base case and progressing recursive call for a recursive tree-node count, then state what happens while the calls unwind. **[2]**

**Total: 20 marks**

### 20 Marks Practice Mark Scheme

1. **(a)** Linear search compares items in sequence until found/end **[1]**; binary search requires sorted data and compares the middle item before moving a bound **[1]**. **[2]**

   **(b)** Bubble sort compares and swaps adjacent out-of-order items over repeated passes **[1]**; insertion sort saves the next item, shifts larger prefix items and inserts into the gap **[1]**. **[2]**
2. **(a)** Push checks full, increments `Top` and stores; pop checks empty, returns the top item and decrements `Top` **[2]**.

   **(b)** Enqueue advances `Rear` modulo capacity and increments `Count`; dequeue reads at `Front`, advances it modulo capacity and decrements `Count`, with full/empty checks **[2]**.

   **(c)** Find follows `Next` until match/null **[1]**; insertion takes a free node and reconnects it into the live chain **[1]**; deletion bypasses the target and returns its node to the free list **[1]**. **[3]**

   **(d)** Both operations compare keys and follow left for smaller/right for larger **[1]**; find ends at match/null, while insert attaches a new node at the null link **[1]**. **[2]**

   **(e)** Hash/find the key and return its associated value, using the representation's defined collision/search rule **[1]**.
3. Vertices represent items/places and edges represent connections **[1]**; a route network is naturally modelled because edges can store direct connections/weights and graph search can find a route **[1]**. **[2]**
4. Linear search `O(n)` and binary search `O(log n)` **[1]**; a valid separate space comparison, such as recursive traversal using `O(n)` call-stack space while an iterative version uses `O(1)` auxiliary space **[1]**. **[2]**
5. Null node returns `0`, otherwise call on smaller left/right subtrees **[1]**; stack frames pop in reverse order and combine `1 + left + right` **[1]**. **[2]**

## Final Revision Checklist

- [ ] I can express an algorithm in pseudocode before implementing it in Java.
- [ ] I can trace and compare required searches and sorts.
- [ ] I can implement stack, queue, linked-list and tree operations safely.
- [ ] I can describe the key features of a graph and justify its use for a given situation.
- [ ] I can justify time and auxiliary-space complexity.
- [ ] I can trace recursive calls and unwinding.
- [ ] I can test empty, boundary, duplicate and full-structure cases.
