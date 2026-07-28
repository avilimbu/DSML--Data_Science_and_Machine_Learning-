# Day 18 – Python OOP: Method Overloading & Inheritance

# Method Overloading

## Definition

Method Overloading is the concept of creating multiple methods with the same name but different parameters.

Unlike languages such as Java or C++, **Python does not support true method overloading**. If multiple methods with the same name are defined, only the **last definition** is retained.

Python achieves similar behavior by using:

- Default arguments
- Variable-length arguments (`*args`)
- Keyword arguments (`**kwargs`)

---

## Example Using Default Arguments

```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))
```

### Output

```
5
15
30
```

---

## Example Using *args

```python
class Calculator:
    def add(self, *numbers):
        return sum(numbers)

calc = Calculator()

print(calc.add(2, 3))
print(calc.add(2, 3, 4))
print(calc.add(1, 2, 3, 4, 5))
```

### Output

```
5
9
15
```

---

# Inheritance

## Definition

Inheritance is an Object-Oriented Programming feature that allows one class to inherit the properties and methods of another class.

The existing class is called the **Parent (Base) Class**, while the new class is called the **Child (Derived) Class**.

### Benefits

- Code Reusability
- Better Code Organization
- Easy Maintenance
- Supports Polymorphism
- Reduces Code Duplication

---

# Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## 1. Single Inheritance

A child class inherits from one parent class.

### Example

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()

dog.speak()
dog.bark()
```

### Output

```
Animal makes a sound
Dog barks
```

---

## 2. Multiple Inheritance

A child class inherits from more than one parent class.

### Example

```python
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()

c.skill1()
c.skill2()
```

### Output

```
Driving
Cooking
```

---

## 3. Multilevel Inheritance

A class inherits from another child class, forming multiple inheritance levels.

### Example

```python
class GrandParent:
    def grand(self):
        print("Grandparent")

class Parent(GrandParent):
    def parent(self):
        print("Parent")

class Child(Parent):
    def child(self):
        print("Child")

obj = Child()

obj.grand()
obj.parent()
obj.child()
```

### Output

```
Grandparent
Parent
Child
```

---

## 4. Hierarchical Inheritance

Multiple child classes inherit from the same parent class.

### Example

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

Dog().sound()
Cat().sound()
```

### Output

```
Animal Sound
Animal Sound
```

---

## 5. Hybrid Inheritance

Hybrid inheritance is a combination of two or more inheritance types such as multiple and multilevel inheritance.

It is used in complex object-oriented systems.

---

# 6. Constructor Inheritance

Constructors of parent classes can also be inherited.

To initialize parent attributes, use **super()**.

### Example

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

s = Student("Avik", 101)

print(s.name)
print(s.roll)
```

### Output

```
Avik
101
```

---

# super() Function

## Definition

`super()` is used to call methods or constructors of the parent class.

### Benefits

- Reuses parent code
- Avoids duplicate code
- Makes inheritance cleaner
- Useful in multiple inheritance

---

## Example

```python
class Parent:
    def display(self):
        print("Parent Class")

class Child(Parent):
    def display(self):
        super().display()
        print("Child Class")

obj = Child()
obj.display()
```

### Output

```
Parent Class
Child Class
```

---

# Method Overriding

## Definition

Method Overriding occurs when the child class provides its own implementation of a method already defined in the parent class.

### Example

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

dog = Dog()
dog.sound()
```

### Output

```
Dog Barks
```

---

# Method Resolution Order (MRO)

## Definition

MRO determines the order in which Python searches for methods in multiple inheritance.

Python follows the **C3 Linearization Algorithm**.

---

## Example

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```

### Output

```
[<class '__main__.D'>,
 <class '__main__.B'>,
 <class '__main__.C'>,
 <class '__main__.A'>,
 <class 'object'>]
```

---

# Summary

- Python does **not** support true method overloading.
- Use **default parameters** or `*args` to mimic overloading.
- Inheritance promotes **code reuse**.
- Five common inheritance types:
  - Single
  - Multiple
  - Multilevel
  - Hierarchical
  - Hybrid
- `super()` helps access parent constructors and methods.
- Method overriding allows child classes to customize inherited behavior.
- MRO determines the order of method lookup in multiple inheritance.
