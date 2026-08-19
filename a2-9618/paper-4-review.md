# A2 9618 Paper 4 Practical Review — Set A

> **Original practice paper:** independently written Java practical work for Sections 19–20.

**Time:** 2 hours 30 minutes

**Total:** **75 marks**

**Language used in this practice:** Java console mode

**Required evidence:** complete program code and evidence of testing: test data, expected result and actual result

Do not use a calculator. Work on a centre-provided offline computer without internet or email access. Complete every task in Java. Pseudocode may be used to plan, but submitted solutions and test evidence must be executable Java.

This set contains no low-level or declarative programming tasks because Paper 4 excludes them.

## Question 1 — Delivery Algorithms [24]

Class `Delivery` stores an integer `id`, integer `zone` and real `weight`.

1. Write `insertionSortDeliveries(Delivery[] data)` to sort ascending by `id`. Implement insertion sort; do not use a library sort. **[7]**
2. Write `binarySearchDelivery(Delivery[] data, int target)` to return the target index or `-1`. **[5]**
3. Write recursive `totalWeight(Delivery[] data, int index)` to total weights from `index` onwards. **[4]**
4. Write `loadDeliveries(Path path)` for `id,zone,weight` records. Skip malformed records and handle an unreadable file. **[4]**
5. Produce four tests with expected and actual results: reverse order, duplicate-free search success, search failure and malformed row followed by a valid row. **[4]**

## Question 2 — Course Booking Objects [27]

`Course` has private ID, title and non-negative base fee. `Workshop` is a `Course` with positive practical hours and charges base fee plus `4.50` per practical hour. `Booking` contains courses and totals them polymorphically.

1. Implement `Course` with constructor, getters, validated setter and `calculateFee()`. **[8]**
2. Implement subclass `Workshop`, use the superclass constructor, validate hours and override `calculateFee()`. **[6]**
3. Implement `Booking` containment with `addCourse()` and polymorphic `totalFee()`. **[4]**
4. Write `saveCourses(Path, List<Course>)` and `loadCourses(Path)` using a type marker and specific exception handling. **[5]**
5. Produce four tests: normal course, workshop, rejected negative fee and mixed booking total. **[4]**

## Question 3 — Clinic Queue and Direct Lookup [24]

1. Implement fixed-capacity circular class `CircularQueue<T>` with `enqueue`, `dequeue` and `isFull`. Use front, rear and count; define empty/full behaviour. **[8]**
2. Write `loadPatients(Path, CircularQueue<String>)` for `patientID,name` records. Skip malformed records, stop when full and handle an unreadable file. **[6]**
3. Implement `PatientTable` with integer IDs and names using modulo hashing and bounded linear probing for `insert` and `find`. **[6]**
4. Produce four tests: queue overflow, empty dequeue, collision between IDs 10 and 17 in size 7, and missing-ID lookup. **[4]**

## Mark Scheme

### Question 1 Mark Scheme [24]

- Insertion sort: outer loop and saved record **[2]**; correct shifting condition **[2]**; shifts whole records **[1]**; inserts saved record **[1]**; all bounds correct **[1]**. **[7]**
- Binary search: low/high **[1]**; valid loop/middle **[1]**; equality return **[1]**; correct half selected **[1]**; failure returns `-1` **[1]**. **[5]**
- Recursion: parameters **[1]**; base case **[1]**; progressing call **[1]**; combines current weight **[1]**. **[4]**
- Loader: resource-safe reading **[1]**; validates/converts three fields **[1]**; reports and continues after bad row **[1]**; handles `IOException` and returns results **[1]**. **[4]**
- Testing: one mark for each required input with matching expected and actual result. **[4]**

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Paper4AQuestion1 {
    static class Delivery {
        private final int id;
        private final int zone;
        private final double weight;
        Delivery(int id, int zone, double weight) {
            this.id = id; this.zone = zone; this.weight = weight;
        }
        int getId() { return id; }
        int getZone() { return zone; }
        double getWeight() { return weight; }
    }

    static void insertionSortDeliveries(Delivery[] data) {
        for (int current = 1; current < data.length; current++) {
            Delivery item = data[current];
            int position = current - 1;
            while (position >= 0 && data[position].getId() > item.getId()) {
                data[position + 1] = data[position];
                position--;
            }
            data[position + 1] = item;
        }
    }

    static int binarySearchDelivery(Delivery[] data, int target) {
        int low = 0, high = data.length - 1;
        while (low <= high) {
            int middle = (low + high) / 2;
            if (data[middle].getId() == target) return middle;
            if (data[middle].getId() < target) low = middle + 1;
            else high = middle - 1;
        }
        return -1;
    }

    static double totalWeight(Delivery[] data, int index) {
        if (index >= data.length) return 0;
        return data[index].getWeight() + totalWeight(data, index + 1);
    }

    static List<Delivery> loadDeliveries(Path path) {
        List<Delivery> deliveries = new ArrayList<>();
        try {
            int lineNumber = 0;
            for (String line : Files.readAllLines(path)) {
                lineNumber++;
                try {
                    String[] fields = line.split(",", -1);
                    if (fields.length != 3) throw new IllegalArgumentException("three fields required");
                    deliveries.add(new Delivery(Integer.parseInt(fields[0]),
                            Integer.parseInt(fields[1]), Double.parseDouble(fields[2])));
                } catch (IllegalArgumentException error) {
                    System.out.println("Line " + lineNumber + " rejected: " + error.getMessage());
                }
            }
        } catch (IOException error) {
            System.out.println("Delivery file could not be read: " + error.getMessage());
        }
        return deliveries;
    }

    public static void main(String[] args) {
        Delivery[] data = {new Delivery(104, 2, 8.5), new Delivery(101, 1, 4.0),
                new Delivery(109, 3, 12.5), new Delivery(106, 2, 5.0)};
        insertionSortDeliveries(data);
        if (!Arrays.equals(Arrays.stream(data).mapToInt(Delivery::getId).toArray(),
                new int[]{101, 104, 106, 109})) throw new AssertionError();
        if (binarySearchDelivery(data, 106) != 2 || Math.abs(totalWeight(data, 0) - 30.0) > 0.000001) {
            throw new AssertionError();
        }
    }
}
```

### Question 2 Mark Scheme [27]

- `Course`: class/three private fields **[2]**; constructor uses validation **[2]**; getters **[1]**; setter rejects negative **[2]**; fee method **[1]**. **[8]**
- `Workshop`: inheritance/constructor/super call **[3]**; positive hours **[1]**; override **[1]**; correct fee **[1]**. **[6]**
- `Booking`: collection containment **[1]**; add **[1]**; loops all courses **[1]**; shared method call without type test **[1]**. **[4]**
- Files: writes marker and fields **[2]**; reads correct subtype **[2]**; handles file/record error **[1]**. **[5]**
- Testing: four required matching tests. **[4]**

```java
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

class Paper4AQuestion2 {
    static class Course {
        private final String id;
        private final String title;
        private double baseFee;
        Course(String id, String title, double baseFee) {
            this.id = id; this.title = title; setBaseFee(baseFee);
        }
        String getId() { return id; }
        String getTitle() { return title; }
        double getBaseFee() { return baseFee; }
        void setBaseFee(double value) {
            if (value < 0) throw new IllegalArgumentException("negative fee");
            baseFee = value;
        }
        double calculateFee() { return baseFee; }
    }

    static class Workshop extends Course {
        private final int practicalHours;
        Workshop(String id, String title, double fee, int hours) {
            super(id, title, fee);
            if (hours <= 0) throw new IllegalArgumentException("hours must be positive");
            practicalHours = hours;
        }
        int getPracticalHours() { return practicalHours; }
        @Override double calculateFee() { return getBaseFee() + practicalHours * 4.50; }
    }

    static class Booking {
        private final List<Course> courses = new ArrayList<>();
        void addCourse(Course course) { courses.add(course); }
        double totalFee() {
            double total = 0;
            for (Course course : courses) total += course.calculateFee();
            return total;
        }
    }

    static void saveCourses(Path path, List<Course> courses) {
        try (BufferedWriter writer = Files.newBufferedWriter(path)) {
            for (Course course : courses) {
                if (course instanceof Workshop) {
                    Workshop workshop = (Workshop) course;
                    writer.write("WORKSHOP," + course.getId() + "," + course.getTitle() + ","
                            + course.getBaseFee() + "," + workshop.getPracticalHours());
                } else {
                    writer.write("COURSE," + course.getId() + "," + course.getTitle() + ","
                            + course.getBaseFee());
                }
                writer.newLine();
            }
        } catch (IOException error) { System.out.println("Save failed: " + error.getMessage()); }
    }

    static List<Course> loadCourses(Path path) {
        List<Course> courses = new ArrayList<>();
        try {
            for (String line : Files.readAllLines(path)) {
                try {
                    String[] f = line.split(",", -1);
                    if (f[0].equals("COURSE") && f.length == 4)
                        courses.add(new Course(f[1], f[2], Double.parseDouble(f[3])));
                    else if (f[0].equals("WORKSHOP") && f.length == 5)
                        courses.add(new Workshop(f[1], f[2], Double.parseDouble(f[3]), Integer.parseInt(f[4])));
                    else throw new IllegalArgumentException("invalid record");
                } catch (IllegalArgumentException error) { System.out.println("Record skipped"); }
            }
        } catch (IOException error) { System.out.println("Load failed: " + error.getMessage()); }
        return courses;
    }

    public static void main(String[] args) {
        Course course = new Course("C1", "Writing", 20);
        Workshop workshop = new Workshop("W1", "Robotics", 30, 4);
        Booking booking = new Booking(); booking.addCourse(course); booking.addCourse(workshop);
        if (Math.abs(booking.totalFee() - 68.0) > 0.000001) throw new AssertionError();
        try { new Course("X", "Bad", -1); throw new AssertionError(); }
        catch (IllegalArgumentException expected) { }
    }
}
```

### Question 3 Mark Scheme [24]

- Queue: fixed array **[1]**; initial state **[1]**; full detection **[1]**; store/rear wrap/count **[2]**; empty detection **[1]**; retrieve/front wrap/count **[2]**. **[8]**
- Loader: reads records **[1]**; checks two fields **[1]**; validates numeric ID/name **[1]**; enqueues/counts **[1]**; stops/reports when full/bad row **[1]**; handles `IOException` **[1]**. **[6]**
- Hash table: fixed storage/hash **[2]**; bounded insertion/probing **[2]**; bounded lookup and failure **[2]**. **[6]**
- Testing: four required matching tests. **[4]**

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

class Paper4AQuestion3 {
    static class CircularQueue<T> {
        private final Object[] data;
        private int front, rear, count;
        CircularQueue(int capacity) {
            if (capacity <= 0) throw new IllegalArgumentException("capacity");
            data = new Object[capacity];
        }
        boolean enqueue(T item) {
            if (isFull()) return false;
            data[rear] = item; rear = (rear + 1) % data.length; count++; return true;
        }
        @SuppressWarnings("unchecked") T dequeue() {
            if (count == 0) return null;
            T item = (T) data[front]; data[front] = null;
            front = (front + 1) % data.length; count--; return item;
        }
        boolean isFull() { return count == data.length; }
    }

    static int loadPatients(Path path, CircularQueue<String> queue) {
        int added = 0;
        try {
            for (String line : Files.readAllLines(path)) {
                if (queue.isFull()) { System.out.println("Queue full"); break; }
                try {
                    String[] f = line.split(",", -1);
                    if (f.length != 2 || f[1].isBlank()) throw new IllegalArgumentException();
                    Integer.parseInt(f[0]);
                    if (queue.enqueue(line)) added++;
                } catch (IllegalArgumentException error) { System.out.println("Patient skipped"); }
            }
        } catch (IOException error) { System.out.println("Load failed: " + error.getMessage()); }
        return added;
    }

    static class PatientTable {
        private final Integer[] ids;
        private final String[] names;
        PatientTable(int size) { ids = new Integer[size]; names = new String[size]; }
        boolean insert(int id, String name) {
            int index = Math.floorMod(id, ids.length);
            for (int count = 0; count < ids.length; count++) {
                if (ids[index] == null || ids[index] == id) {
                    ids[index] = id; names[index] = name; return true;
                }
                index = (index + 1) % ids.length;
            }
            return false;
        }
        String find(int id) {
            int index = Math.floorMod(id, ids.length);
            for (int count = 0; count < ids.length; count++) {
                if (ids[index] == null) return null;
                if (ids[index] == id) return names[index];
                index = (index + 1) % ids.length;
            }
            return null;
        }
    }

    public static void main(String[] args) {
        CircularQueue<String> queue = new CircularQueue<>(2);
        if (!queue.enqueue("A") || !queue.enqueue("B") || queue.enqueue("C")) throw new AssertionError();
        if (!"A".equals(queue.dequeue())) throw new AssertionError();
        PatientTable table = new PatientTable(7); table.insert(10, "A"); table.insert(17, "B");
        if (!"A".equals(table.find(10)) || !"B".equals(table.find(17)) || table.find(99) != null) {
            throw new AssertionError();
        }
    }
}
```

## Final Check

- [ ] Every task was implemented and run in Java console mode.
- [ ] Pseudocode planning was translated into complete Java with explicit types.
- [ ] Required algorithms were not replaced by library shortcuts.
- [ ] Each test records input, expected result and actual result.
- [ ] Empty, full, invalid and exception paths were executed.
- [ ] Question totals are 24 + 27 + 24 = 75 marks.
