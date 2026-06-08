# A2 9618 Computer Science - Chapter 20 Updated Checklist
## Further Programming｜Syllabus-Aligned Paper 4 Revision Sheet

> **Version:** Syllabus-aligned revision for A2 Paper 4  
> **Target:** Cambridge International AS & A Level Computer Science 9618 A2  
> **Chapter:** 20 Further programming  
> **Main audience:** Students  
> **Teacher Appendix:** optional; kept at the end for teachers  
> **Style:** 中文解释 + English programming keywords

---

# 0. How to Use This Sheet

Chapter 20 prepares you for larger programming tasks. You need to write maintainable code using:

- modules and subroutines
- object-oriented programming
- recursion
- file processing
- exception handling
- ADT implementation
- testing and debugging

---

# 1. Modular Programming

Modular programming splits a solution into subroutines, classes or modules.

Benefits:

- easier to test
- easier to debug
- reusable code
- clearer responsibilities
- supports team development

Example module breakdown:

| Module | Responsibility |
| --- | --- |
| `InputModule` | get and validate data |
| `ProcessingModule` | calculate results |
| `StorageModule` | read/write files |
| `OutputModule` | display reports |

---

# 2. Parameters and Return Values

Good functions avoid unnecessary global variables.

```text
FUNCTION CalculateDiscount(price : REAL, rate : REAL) RETURNS REAL
    RETURN price * rate
ENDFUNCTION
```

Use parameters when:

- the subroutine needs input data
- the same logic should work for different values
- testing should be easier

Use return values when:

- the subroutine calculates a value
- the caller needs the result

---

# 3. Object-Oriented Programming

| Term | Meaning |
| --- | --- |
| class | template for objects |
| object | instance of a class |
| attribute | data stored in an object |
| method | operation belonging to an object |
| constructor | method used when creating an object |
| encapsulation | bundling data and methods, controlling access |
| inheritance | deriving a class from another class |
| polymorphism | same method name can behave differently in different classes |

Example:

```text
CLASS Vehicle
    PRIVATE Registration : STRING
    PRIVATE Speed : INTEGER

    PUBLIC PROCEDURE SetSpeed(newSpeed : INTEGER)
        IF newSpeed >= 0 THEN
            Speed <- newSpeed
        ENDIF
    ENDPROCEDURE

    PUBLIC FUNCTION GetSpeed() RETURNS INTEGER
        RETURN Speed
    ENDFUNCTION
ENDCLASS
```

---

# 4. Inheritance and Polymorphism

Inheritance example:

```text
CLASS ElectricCar INHERITS Vehicle
    PRIVATE BatteryLevel : INTEGER

    PUBLIC PROCEDURE Charge()
        BatteryLevel <- 100
    ENDPROCEDURE
ENDCLASS
```

Why use inheritance?

- avoids repeated attributes/methods
- models "is a" relationships
- allows shared behaviour in a superclass

Polymorphism example:

- `Draw()` behaves differently for `Circle`, `Rectangle` and `Triangle`.
- The same method call can run the correct version for the object.

---

# 5. Recursion in Programs

Recursive program checklist:

1. clear base case
2. recursive call uses a smaller/simpler input
3. result is returned or accumulated correctly
4. stack depth is reasonable

Example:

```text
FUNCTION BinarySearch(low : INTEGER, high : INTEGER, target : INTEGER) RETURNS INTEGER
    IF low > high THEN
        RETURN -1
    ENDIF

    mid <- (low + high) DIV 2
    IF Values[mid] = target THEN
        RETURN mid
    ELSE
        IF target < Values[mid] THEN
            RETURN BinarySearch(low, mid - 1, target)
        ELSE
            RETURN BinarySearch(mid + 1, high, target)
        ENDIF
    ENDIF
ENDFUNCTION
```

---

# 6. File Processing

Programming tasks may require reading, writing or updating files.

Core pattern:

```text
OPENFILE "Orders.txt" FOR READ
WHILE NOT EOF("Orders.txt")
    READFILE "Orders.txt", orderLine
    ProcessOrder(orderLine)
ENDWHILE
CLOSEFILE "Orders.txt"
```

Good file-handling habits:

- open before reading/writing
- close after use
- validate data read from file if needed
- handle missing or empty files where appropriate

---

# 7. Exception Handling

Exception handling deals with runtime errors without crashing the whole program.

Possible runtime problems:

- file not found
- invalid numeric conversion
- division by zero
- array index out of range
- network/database connection failure

General pattern:

```text
TRY
    result <- total / count
EXCEPT
    OUTPUT "Cannot divide by zero"
ENDTRY
```

Exam answer wording:

> Exception handling allows the program to respond to runtime errors in a controlled way instead of terminating unexpectedly.

---

# 8. Implementing ADTs

## 8.1 Stack with Array

```text
Top <- 0

PROCEDURE Push(newItem)
    IF Top = MaxSize THEN
        OUTPUT "Stack full"
    ELSE
        Top <- Top + 1
        Stack[Top] <- newItem
    ENDIF
ENDPROCEDURE
```

## 8.2 Queue with Pointers

Use:

- front pointer
- rear pointer
- array storage
- count or circular logic to detect full/empty

Common mistake: updating rear but forgetting front when the first item is added.

---

# 9. Debugging and Testing

Debugging techniques:

- trace table
- breakpoints
- watch variables
- step through code
- diagnostic output
- unit tests

Testing larger programs:

- test each module
- test integration between modules
- test boundary data
- test file and error cases
- retest after fixing bugs

---

# 10. Common Exam Mistakes

- Overusing global variables instead of parameters.
- Writing class attributes as public when encapsulation is expected.
- Confusing inheritance with object creation.
- No base case in recursive method.
- File opened but never closed.
- Exception handling described as preventing all errors. It handles errors when they occur.
- Stack/queue pointers updated in the wrong order.

---

# 11. Mini Practice

1. Write a class for a `Book` with private attributes and public get/set methods.
2. Explain why encapsulation improves maintainability.
3. Write a recursive function to find the sum of the first `n` positive integers.
4. Give two runtime errors that exception handling can catch.
5. Write pseudocode for pushing an item onto a stack stored in an array.

---

# 12. Teacher Appendix

> Optional teacher-facing planning notes. Students can skip this appendix during normal revision.

## 12.1 Suggested teaching order

1. Teach OOP using one running scenario across multiple lessons.
2. Require private attributes and public methods in class design practice.
3. Pair every ADT implementation with pointer trace tables.
4. Assess exception handling through scenario explanations and small code snippets.

