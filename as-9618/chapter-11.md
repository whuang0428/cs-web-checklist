# AS 9618 Chapter 11: Programming
## Programming｜Syllabus-Aligned Paper 2 Revision Sheet

> **Version:** Syllabus-aligned revision for AS Paper 2  
> **Target:** Cambridge International AS & A Level Computer Science 9618  
> **Chapter:** 11 Programming  
> **Main audience:** Students  
> **Style:** Chinese explanation + English programming keywords

---

# 0. How to Use This Sheet

Chapter 11 is the practical programming chapter. You should be able to read and write code using:

- variables and constants
- selection and iteration
- arrays and records
- procedures and functions
- parameters
- recursion
- object-oriented programming basics

---

# 1. Programming Constructs

## 1.1 Sequence

Statements run in order.

```text
INPUT width
INPUT height
area <- width * height
OUTPUT area
```

## 1.2 Selection

```text
IF stockLevel < reorderLevel THEN
    OUTPUT "Reorder"
ELSE
    OUTPUT "Enough stock"
ENDIF
```

## 1.3 Iteration

```text
FOR i <- 1 TO 10
    OUTPUT i
NEXT i
```

---

# 2. Procedures, Functions and Parameters

| Feature | Procedure | Function |
| --- | --- | --- |
| returns value | no | yes |
| used for | action/task | calculation/decision |
| example | display menu | calculate average |

```text
FUNCTION CalculateAverage(total : REAL, count : INTEGER) RETURNS REAL
    RETURN total / count
ENDFUNCTION
```

Parameter benefits:

- same subroutine works with different values
- reduces global variables
- improves testing

---

# 3. Local and Global Variables

| Type | Scope |
| --- | --- |
| local variable | only available inside a subroutine |
| global variable | available throughout the program |

Prefer local variables where possible because they reduce accidental changes and make testing easier.

Common mistake: assuming a local variable from one procedure exists in another procedure.

---

# 4. Recursion

Recursion is when a subroutine calls itself.

Every recursive solution needs:

1. base case: stops the recursion
2. recursive case: calls itself with a smaller or simpler problem

Example:

```text
FUNCTION Factorial(n : INTEGER) RETURNS INTEGER
    IF n = 0 THEN
        RETURN 1
    ELSE
        RETURN n * Factorial(n - 1)
    ENDIF
ENDFUNCTION
```

Common mistake: no base case, causing infinite recursion.

---

# 5. Object-Oriented Programming Basics

| Term | Meaning |
| --- | --- |
| class | template/blueprint for objects |
| object | instance of a class |
| attribute | data stored in an object |
| method | action/subroutine belonging to a class |
| constructor | special method used to create an object |
| encapsulation | keeping data and methods together, controlling access |
| inheritance | one class receives attributes/methods from another |

Example:

```text
CLASS Student
    PRIVATE Name : STRING
    PRIVATE Mark : INTEGER

    PUBLIC PROCEDURE SetMark(newMark : INTEGER)
        Mark <- newMark
    ENDPROCEDURE
ENDCLASS
```

---

# 6. Reading Code

When asked to explain code:

1. identify variables and data structures
2. follow loops carefully
3. trace conditions
4. record output
5. describe the purpose, not only each line

Weak: "It loops."

Strong: "It loops through every mark, counts marks greater than or equal to 50, then outputs the number of passes."

---

# 7. Common Programming Errors

| Error | Example | Fix |
| --- | --- | --- |
| syntax | missing `ENDIF` | follow language rules |
| logic | average uses wrong count | trace with test data |
| runtime | division by zero | validate before division |
| off-by-one | loop misses last item | check loop bounds |
| scope error | uses local variable outside procedure | pass as parameter or return value |

---

# 8. Mini Practice

1. Write a function that returns the largest of two integers.
2. Explain the difference between a procedure and a function.
3. Trace a recursive factorial call for `Factorial(3)`.
4. Define class, object, attribute and method.
5. Explain one benefit of encapsulation.

---
