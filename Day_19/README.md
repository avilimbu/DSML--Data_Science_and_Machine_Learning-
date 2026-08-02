# Day 19 – Method Overriding, Encapsulation & Abstraction in Python

# 1. Method Overriding

## Definition

Method Overriding is an Object-Oriented Programming (OOP) concept where a child class provides its own implementation of a method that already exists in its parent class.

When an object of the child class calls that method, Python automatically executes the child class version instead of the parent class version.

### Why use Method Overriding?

- Modify inherited behavior.
- Provide specialized implementation.
- Achieve Runtime Polymorphism.
- Improve code flexibility and reusability.

---

## Syntax

```python
class Parent:
    def show(self):
        print("Parent Method")

class Child(Parent):
    def show(self):
        print("Child Method")

obj = Child()
obj.show()
```

### Output

```
Child Method
```

---

## Example: Employee and Sales Officer

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary


class SalesOfficer(Employee):

    def __init__(self, name, salary, incentive):
        super().__init__(name, salary)
        self.incentive = incentive

    def getSalary(self):
        return self.salary + self.incentive


emp = Employee("Rajesh", 9000)
print(emp.getSalary())

sales = SalesOfficer("Kiran", 10000, 1000)
print(sales.getSalary())
```

### Output

```
9000
11000
```

---

## `super()` Function

`super()` is used to call methods or constructors from the parent class.

Example:

```python
super().__init__(name, salary)
```

### Benefits

- Avoids duplicate code.
- Reuses parent class initialization.
- Makes inheritance cleaner and easier to maintain.

---

# 2. Encapsulation

## Definition

Encapsulation is the process of combining data (variables) and methods (functions) into a single unit (class) while controlling access to the internal data.

It helps protect object data from accidental modification.

---

## Advantages

- Data hiding
- Better security
- Easier maintenance
- Better organization
- Improves code reliability

---

# Access Modifiers in Python

Python provides three types of access modifiers.

---

## 1. Public Members

Accessible from anywhere.

```python
class Student:

    def __init__(self):
        self.name = "Ram"
```

Can be accessed directly:

```python
obj = Student()
print(obj.name)
```

---

## 2. Protected Members

Protected members begin with a single underscore `_`.

```python
class Student:

    def __init__(self):
        self._age = 20
```

- Intended for use inside the class and subclasses.
- Can still be accessed outside the class, but it is not recommended.

---

## 3. Private Members

Private members begin with double underscores `__`.

```python
class Student:

    def __init__(self):
        self.__marks = 90
```

They cannot be accessed directly outside the class.

Python internally performs **Name Mangling**.

Example:

```python
obj._Student__marks
```

---

# Complete Encapsulation Example

```python
class Example:

    def __init__(self):
        self.public_var = 1
        self._protected_var = 2
        self.__private_var = 3

    def public_method(self):
        print(self.__private_var)

obj = Example()

print(obj.public_var)
print(obj._protected_var)

print(obj._Example__private_var)
```

---

## Summary

| Access Modifier | Symbol | Accessible |
|-----------------|--------|------------|
| Public | `variable` | Everywhere |
| Protected | `_variable` | Class & Child Class (recommended) |
| Private | `__variable` | Only inside the class |

---

# 3. Abstraction

## Definition

Abstraction is the process of hiding implementation details and exposing only the essential functionality to the user.

It focuses on **what an object does**, not **how it does it**.

---

## Why use Abstraction?

- Hides unnecessary details.
- Makes programs easier to use.
- Improves maintainability.
- Enforces a common interface for subclasses.

---

# Abstract Class

An Abstract Class:

- Cannot be instantiated.
- Can contain abstract methods.
- Must be inherited.
- Forces child classes to implement required methods.

Python provides the `abc` module for abstraction.

---

## Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print("Bark")


class Cat(Animal):

    def make_sound(self):
        print("Meow")


dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()
```

### Output

```
Bark
Meow
```

---

# Difference Between Encapsulation and Abstraction

| Encapsulation | Abstraction |
|--------------|-------------|
| Wraps data and methods together | Hides implementation details |
| Protects object data | Simplifies program usage |
| Uses access modifiers | Uses abstract classes and abstract methods |
| Focuses on data security | Focuses on essential functionality |

---

# Summaray

- Method Overriding allows child classes to redefine inherited methods.
- `super()` helps reuse parent class constructors and methods.
- Encapsulation protects data using public, protected, and private members.
- Private members use name mangling in Python.
- Abstraction hides implementation details and exposes only essential functionality.
- Abstract classes cannot be instantiated directly and require subclasses to implement abstract methods.
- These OOP concepts make programs more secure, reusable, maintainable, and easier to understand.

