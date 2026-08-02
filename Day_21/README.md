# Day 21 | Duck Typing & Operator Overloading in Python

## Overview

This section covers two important concepts of **Polymorphism** in Python:

- Duck Typing
- Operator Overloading

Duck Typing focuses on an object's **behavior** rather than its type, while Operator Overloading allows built-in operators to perform different operations on user-defined objects.

---

# 1. Duck Typing

## What is Duck Typing?

Duck Typing is a concept in Python where the **type of an object is less important than the methods or behaviors it provides**.

Instead of checking whether an object belongs to a particular class, Python checks whether the object has the required method or attribute.

The name comes from the famous saying:

> **"If it walks like a duck and quacks like a duck, then it is probably a duck."**

This means that if an object behaves like another object, Python allows it to be used in the same way.

---

## Why Use Duck Typing?

- Makes code more flexible.
- Reduces dependency on specific classes.
- Encourages reusable code.
- Works naturally with Python's dynamic typing.

---

## Example

```python
class Duck:

    def swim(self):
        return "Duck swimming"

    def fly(self):
        return "Duck flying"


class Airplane:

    def fly(self):
        return "Airplane flying"


def fly_test(entity):
    print(entity.fly())


# Create objects
duck = Duck()
airplane = Airplane()

# Same function works with different objects
fly_test(duck)
fly_test(airplane)
```

### Output

```
Duck flying
Airplane flying
```

---

## Explanation

The `fly_test()` function does not check whether the object is a `Duck` or an `Airplane`.

It simply calls the `fly()` method.

As long as the object has a `fly()` method, the function works correctly.

This is known as **Duck Typing**.

---

## Key Points

- Focuses on an object's behavior instead of its class.
- No explicit inheritance is required.
- Objects with the required methods can be used interchangeably.
- Commonly used in Python because of its dynamic nature.

---

# 2. Operator Overloading

## What is Operator Overloading?

Operator Overloading is a feature in Python that allows built-in operators to have different meanings depending on the object they are used with.

Python provides special methods (also called **magic methods** or **dunder methods**) that allow developers to redefine operator behavior for user-defined classes.

---

## Why Use Operator Overloading?

- Makes user-defined objects behave like built-in data types.
- Improves code readability.
- Enables intuitive operations on custom objects.
- Supports object-oriented programming.

---

## Example

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Create Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Using + operator
p3 = p1 + p2

print(p3)
```

### Output

```
Point(4, 6)
```

---

## Explanation

The `+` operator is overloaded using the special method:

```python
__add__()
```

When Python executes:

```python
p1 + p2
```

it internally calls:

```python
p1.__add__(p2)
```

which returns a new `Point` object whose coordinates are the sum of the two points.

The `__str__()` method is used to define how the object is displayed when printed.

---

## Common Magic Methods

| Method | Operator | Description |
|---------|----------|-------------|
| `__add__()` | `+` | Addition |
| `__sub__()` | `-` | Subtraction |
| `__mul__()` | `*` | Multiplication |
| `__truediv__()` | `/` | Division |
| `__eq__()` | `==` | Equality comparison |
| `__lt__()` | `<` | Less than comparison |
| `__gt__()` | `>` | Greater than comparison |
| `__str__()` | `print()` | String representation |

---

# Duck Typing vs Operator Overloading

| Duck Typing | Operator Overloading |
|-------------|----------------------|
| Focuses on object behavior. | Focuses on redefining operators. |
| Objects are accepted if they provide the required methods. | Operators perform custom operations on user-defined objects. |
| Does not require inheritance. | Uses special (magic) methods. |
| Supports flexible programming. | Makes custom objects behave like built-in types. |

---

# Summary

- Duck Typing allows objects with the required methods to be used regardless of their class.
- Python determines suitability based on behavior, not object type.
- Operator Overloading enables built-in operators to work with user-defined classes.
- Special methods like `__add__()` and `__str__()` define custom operator behavior.
- Both Duck Typing and Operator Overloading are examples of **Polymorphism** in Python.

