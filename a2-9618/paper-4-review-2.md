# A2 9618 Paper 4 Practical Review — Set B

> **Original practice paper:** an independent second practical set written in Java. All scenarios, data and reference solutions are newly written.

**Time:** 2 hours 30 minutes

**Total:** **75 marks**

**Language:** Java console mode

**Required evidence:** complete code, test input, expected result and actual result

Do not use a calculator. Work on a centre-provided offline computer without internet or email access. Complete every task in Java. Pseudocode may be used to plan before producing executable Java.

This set applies practical Sections 19–20 and contains no low-level or declarative programming tasks.

## Question 1 — Race Result Processing [25]

Class `RaceResult` stores unique integer `runnerId` and positive real `finishTime`.

1. Write `bubbleSortResults(RaceResult[] results)` for ascending finish time with early termination. Do not use a library sort. **[7]**
2. Write `linearSearchRunner(RaceResult[] results, int runnerId)` to return a record or `null`. **[4]**
3. Write recursive `countFaster(RaceResult[] results, double limit, int index)`. **[5]**
4. Write `loadResults(Path path)` for `runnerId,finishTime`. Report malformed/non-positive records, continue, and handle an unreadable file. **[5]**
5. Produce four tests: already sorted data, reverse order, missing runner and malformed row followed by a valid row. **[4]**

## Question 2 — Ticket Order Objects [26]

`Ticket` has private code, event name and non-negative base price. `GroupTicket` has group size 2–8 and charges `basePrice × groupSize × 0.90`. `TicketOrder` contains tickets.

1. Implement `Ticket` with constructor, getters, validated setter and `calculateFee()`. **[7]**
2. Implement `GroupTicket`, use `super`, validate size and override the fee. **[6]**
3. Implement `TicketOrder` with `addTicket()` and polymorphic `totalFee()`. **[5]**
4. Write `appendOrder(Path path, String customer, TicketOrder order)` and handle an `IOException`. **[4]**
5. Produce four tests covering a basic ticket, both valid size boundaries, a rejected size and a mixed order. **[4]**

## Question 3 — Search Tree Catalogue [24]

1. Implement `CatalogueNode` and `CatalogueTree`. Write iterative `insert(int id, String name)` and `find(int id)`. A duplicate ID updates its name. **[10]**
2. Write recursive `inOrder(CatalogueNode node, List<String> output)` to append records in ascending ID order. **[5]**
3. Write `loadCatalogue(Path path, CatalogueTree tree)`. Continue after malformed rows, handle an unreadable file and return the number loaded. **[5]**
4. Produce four tests: empty search, root/left/right insertion, duplicate update and malformed row followed by a valid row. **[4]**

## Mark Scheme

### Question 1 Mark Scheme [25]

- Bubble sort: upper boundary **[1]**; swapped flag **[1]**; passes/termination **[1]**; correct inner bounds **[1]**; compares times **[1]**; swaps records **[1]**; shrinks boundary **[1]**. **[7]**
- Linear search: iterates records **[1]**; compares ID **[1]**; returns match **[1]**; returns `null` after failure **[1]**. **[4]**
- Recursion: parameters **[1]**; base case **[1]**; comparison **[1]**; progresses index **[1]**; combines count **[1]**. **[5]**
- Loader: resource-safe read **[1]**; field conversion **[1]**; positive-time validation **[1]**; bad row reported/continued **[1]**; `IOException` handled/results returned **[1]**. **[5]**
- Testing: four required matching tests. **[4]**

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

class Paper4BQuestion1 {
    static class RaceResult {
        private final int runnerId;
        private final double finishTime;
        RaceResult(int runnerId, double finishTime) {
            if (finishTime <= 0) throw new IllegalArgumentException("time must be positive");
            this.runnerId = runnerId;
            this.finishTime = finishTime;
        }
        int getRunnerId() { return runnerId; }
        double getFinishTime() { return finishTime; }
    }

    static void bubbleSortResults(RaceResult[] results) {
        int upper = results.length - 1;
        boolean swapped = true;
        while (upper > 0 && swapped) {
            swapped = false;
            for (int index = 0; index < upper; index++) {
                if (results[index].getFinishTime() > results[index + 1].getFinishTime()) {
                    RaceResult temp = results[index];
                    results[index] = results[index + 1];
                    results[index + 1] = temp;
                    swapped = true;
                }
            }
            upper--;
        }
    }

    static RaceResult linearSearchRunner(RaceResult[] results, int runnerId) {
        for (RaceResult result : results) if (result.getRunnerId() == runnerId) return result;
        return null;
    }

    static int countFaster(RaceResult[] results, double limit, int index) {
        if (index >= results.length) return 0;
        int current = results[index].getFinishTime() < limit ? 1 : 0;
        return current + countFaster(results, limit, index + 1);
    }

    static List<RaceResult> loadResults(Path path) {
        List<RaceResult> results = new ArrayList<>();
        try {
            int lineNumber = 0;
            for (String line : Files.readAllLines(path)) {
                lineNumber++;
                try {
                    String[] f = line.split(",", -1);
                    if (f.length != 2) throw new IllegalArgumentException("two fields required");
                    results.add(new RaceResult(Integer.parseInt(f[0]), Double.parseDouble(f[1])));
                } catch (IllegalArgumentException error) {
                    System.out.println("Line " + lineNumber + " rejected: " + error.getMessage());
                }
            }
        } catch (IOException error) { System.out.println("Result file could not be read: " + error.getMessage()); }
        return results;
    }

    public static void main(String[] args) {
        RaceResult[] results = {new RaceResult(1, 42), new RaceResult(2, 35), new RaceResult(3, 28)};
        bubbleSortResults(results);
        if (results[0].getRunnerId() != 3 || linearSearchRunner(results, 2) == null) throw new AssertionError();
        if (countFaster(results, 40, 0) != 2 || linearSearchRunner(results, 99) != null) throw new AssertionError();
    }
}
```

### Question 2 Mark Scheme [26]

- `Ticket`: class/constructor **[1]**; private fields **[1]**; initialisation **[1]**; setter used **[1]**; getters **[1]**; negative rejected **[1]**; fee **[1]**. **[7]**
- `GroupTicket`: inheritance **[1]**; constructor **[1]**; super call **[1]**; private size **[1]**; inclusive validation **[1]**; overridden fee **[1]**. **[6]**
- `TicketOrder`: constructor/collection **[2]**; add **[1]**; loops all **[1]**; polymorphic call **[1]**. **[5]**
- Append: append mode **[1]**; complete record **[1]**; `IOException` **[1]**; success/failure result **[1]**. **[4]**
- Testing: four required matching tests. **[4]**

```java
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;

class Paper4BQuestion2 {
    static class Ticket {
        private final String code;
        private final String eventName;
        private double basePrice;
        Ticket(String code, String eventName, double basePrice) {
            this.code = code; this.eventName = eventName; setBasePrice(basePrice);
        }
        String getCode() { return code; }
        String getEventName() { return eventName; }
        double getBasePrice() { return basePrice; }
        void setBasePrice(double value) {
            if (value < 0) throw new IllegalArgumentException("negative price");
            basePrice = value;
        }
        double calculateFee() { return basePrice; }
    }

    static class GroupTicket extends Ticket {
        private final int groupSize;
        GroupTicket(String code, String event, double price, int groupSize) {
            super(code, event, price);
            if (groupSize < 2 || groupSize > 8) throw new IllegalArgumentException("group size 2 to 8");
            this.groupSize = groupSize;
        }
        int getGroupSize() { return groupSize; }
        @Override double calculateFee() { return getBasePrice() * groupSize * 0.90; }
    }

    static class TicketOrder {
        private final List<Ticket> tickets = new ArrayList<>();
        void addTicket(Ticket ticket) { tickets.add(ticket); }
        double totalFee() {
            double total = 0;
            for (Ticket ticket : tickets) total += ticket.calculateFee();
            return total;
        }
    }

    static boolean appendOrder(Path path, String customer, TicketOrder order) {
        try (BufferedWriter writer = Files.newBufferedWriter(path,
                StandardOpenOption.CREATE, StandardOpenOption.APPEND)) {
            writer.write(customer + "," + String.format("%.2f", order.totalFee()));
            writer.newLine(); return true;
        } catch (IOException error) {
            System.out.println("Order could not be saved: " + error.getMessage()); return false;
        }
    }

    public static void main(String[] args) {
        Ticket basic = new Ticket("T1", "Talk", 20);
        GroupTicket group = new GroupTicket("G1", "Lab", 10, 4);
        TicketOrder order = new TicketOrder(); order.addTicket(basic); order.addTicket(group);
        if (Math.abs(order.totalFee() - 56.0) > 0.000001) throw new AssertionError();
        new GroupTicket("L", "Low", 1, 2); new GroupTicket("H", "High", 1, 8);
        try { new GroupTicket("X", "Bad", 1, 9); throw new AssertionError(); }
        catch (IllegalArgumentException expected) { }
    }
}
```

### Question 3 Mark Scheme [24]

- Tree: node fields **[2]**; empty root **[1]**; empty insertion **[1]**; iterative comparison **[2]**; attaches child **[1]**; duplicate update **[1]**; ordered find **[1]**; returns name/null **[1]**. **[10]**
- In-order: parameters **[1]**; null base **[1]**; left **[1]**; current append **[1]**; right **[1]**. **[5]**
- Loader: reads/counts **[1]**; validates fields **[1]**; converts/inserts **[1]**; per-row error continues **[1]**; handles `IOException`/returns count **[1]**. **[5]**
- Testing: four required matching tests. **[4]**

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

class Paper4BQuestion3 {
    static class CatalogueNode {
        int id; String name; CatalogueNode left, right;
        CatalogueNode(int id, String name) { this.id = id; this.name = name; }
    }

    static class CatalogueTree {
        CatalogueNode root;
        void insert(int id, String name) {
            if (root == null) { root = new CatalogueNode(id, name); return; }
            CatalogueNode current = root;
            while (true) {
                if (id == current.id) { current.name = name; return; }
                if (id < current.id) {
                    if (current.left == null) { current.left = new CatalogueNode(id, name); return; }
                    current = current.left;
                } else {
                    if (current.right == null) { current.right = new CatalogueNode(id, name); return; }
                    current = current.right;
                }
            }
        }
        String find(int id) {
            CatalogueNode current = root;
            while (current != null) {
                if (id == current.id) return current.name;
                current = id < current.id ? current.left : current.right;
            }
            return null;
        }
    }

    static void inOrder(CatalogueNode node, List<String> output) {
        if (node == null) return;
        inOrder(node.left, output); output.add(node.id + "," + node.name); inOrder(node.right, output);
    }

    static int loadCatalogue(Path path, CatalogueTree tree) {
        int loaded = 0;
        try {
            for (String line : Files.readAllLines(path)) {
                try {
                    String[] f = line.split(",", 2);
                    if (f.length != 2 || f[1].isBlank()) throw new IllegalArgumentException();
                    tree.insert(Integer.parseInt(f[0]), f[1]); loaded++;
                } catch (IllegalArgumentException error) { System.out.println("Record skipped"); }
            }
        } catch (IOException error) { System.out.println("Catalogue could not be read: " + error.getMessage()); }
        return loaded;
    }

    public static void main(String[] args) {
        CatalogueTree tree = new CatalogueTree();
        if (tree.find(1) != null) throw new AssertionError();
        tree.insert(20, "Root"); tree.insert(10, "Left"); tree.insert(30, "Right"); tree.insert(10, "Updated");
        List<String> output = new ArrayList<>(); inOrder(tree.root, output);
        if (!"Updated".equals(tree.find(10)) || !output.equals(List.of("10,Updated", "20,Root", "30,Right"))) {
            throw new AssertionError();
        }
    }
}
```

## Final Check

- [ ] Every task was implemented and run in Java console mode.
- [ ] Pseudocode planning was translated into complete Java with explicit types.
- [ ] Algorithms were implemented without library replacements.
- [ ] Exception paths were tested rather than only described.
- [ ] Evidence states input, expected result and actual result.
- [ ] Question totals are 25 + 26 + 24 = 75 marks.
