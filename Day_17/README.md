# Day 17 – Python Classes and Objects (Introduction)

# Overview

Object-Oriented Programming (OOP) is one of the most important programming paradigms in Python. It helps organize code into reusable, maintainable, and scalable structures using **classes** and **objects**.

---

# What is a Class?

A **Class** is a blueprint or template used to create objects.

Think of a class as the design of a house.

- The blueprint describes the house.
- The actual houses built from it are objects.

One class can create multiple objects.

### Syntax

```python
class ClassName:
    pass
```

---

# What is an Object?

An **Object** is an instance of a class.

Objects contain the actual data and can access the methods defined inside the class.

### Syntax

```python
object_name = ClassName()
```

### Example

```python
class Bike:
    name = ""
    gear = 0

bike1 = Bike()
```

Here,

- `Bike` is the class.
- `bike1` is the object.

---

# Constructor (`__init__()`)

The constructor automatically runs whenever an object is created.

It is mainly used to initialize object attributes.

### Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# Types of Attributes

Python mainly provides two types of attributes.

---

## 1. Instance Attributes

Instance attributes belong to individual objects.

They are created inside the constructor using `self`.

### Example

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Each object has its own copy of the attribute.

---

## 2. Class Attributes

Class attributes belong to the class itself.

They are shared among all objects.

### Example

```python
class Student:

    school = "ABC School"
```

All objects use the same value unless changed.

---

# Types of Methods

Python classes mainly contain three types of methods.

---

## 1. Instance Method

Instance methods operate on object data.

They receive `self` as the first parameter.

### Example

```python
class Student:

    def display(self):
        print(self.name)
```

Used when working with object-specific information.

---

## 2. Class Method

Class methods operate on the class itself.

They use the `@classmethod` decorator and receive `cls` as the first parameter.

### Example

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)
```

Used for working with class attributes.

---

## 3. Static Method

Static methods are utility methods.

They do not use `self` or `cls`.

They are created using the `@staticmethod` decorator.

### Example

```python
class Student:

    @staticmethod
    def welcome():
        print("Welcome to Python OOP")
```

Used for helper functions related to the class.

---

# Difference Between Attributes

| Feature | Instance Attribute | Class Attribute |
|----------|-------------------|-----------------|
| Belongs To | Object | Class |
| Defined In | `__init__()` | Inside class |
| Shared | No | Yes |
| Access | `self.attribute` | `ClassName.attribute` |

---

# Difference Between Methods

| Method | First Parameter | Decorator | Used For |
|---------|----------------|-----------|-----------|
| Instance Method | `self` | None | Access object data |
| Class Method | `cls` | `@classmethod` | Access class data |
| Static Method | None | `@staticmethod` | Utility functions |

---

# Example Program

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student:", self.name)

    @classmethod
    def show_school(cls):
        print(cls.school)

    @staticmethod
    def welcome():
        print("Welcome to Python OOP")

student = Student("Rodri")

student.display()
Student.show_school()
Student.welcome()
```

### Output

```
Student: Rodri
ABC School
Welcome to Python OOP
```
