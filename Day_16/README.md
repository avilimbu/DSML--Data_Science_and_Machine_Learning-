# Day 16 – Python Exceptions and Exception Handling


#  What is an Exception?

An **Exception** is a runtime error that interrupts the normal execution of a program.

Instead of stopping the program immediately, Python allows us to catch and handle these exceptions.

Example:

```python
10 / 0
```

Output

```
ZeroDivisionError
```

---

# Exception Handling Structure

Python uses four main blocks for exception handling.

## 1. `try`

Contains the code that might produce an exception.

```python
try:
    result = 10 / 0
```

---

## 2. `except`

Handles the exception if one occurs.

```python
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 3. `else`

Runs only if **no exception** occurs.

```python
else:
    print("Operation successful.")
```

---

## 4. `finally`

Always executes whether an exception occurs or not.

Commonly used for:

- Closing files
- Closing database connections
- Cleaning resources

```python
finally:
    print("Execution completed.")
```

---

#  Complete Example

```python
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

else:
    print("Result:", result)

finally:
    print("Program Finished.")
```

---

#  Common Built-in Exceptions

## 1. ZeroDivisionError

Occurs when dividing by zero.

```python
10 / 0
```

---

## 2. TypeError

Occurs when incompatible data types are used together.

```python
10 + "5"
```

or

```python
len(100)
```

---

## 3. ValueError

Occurs when the correct data type contains an invalid value.

```python
int("abc")
```

or

```python
import math

math.sqrt(-5)
```

---

## 4. NameError

Occurs when using an undefined variable.

```python
print(age)
```

---

## 5. IndexError

Occurs when accessing an invalid list index.

```python
numbers = [10, 20, 30]

print(numbers[5])
```

---

## 6. KeyError

Occurs when a dictionary key does not exist.

```python
student = {
    "name": "Bibek",
    "age": 21
}

print(student["address"])
```

---

## 7. FileNotFoundError

Occurs when attempting to open a file that does not exist.

```python
open("data.txt")
```

---

#  Handling File Errors

```python
try:
    file = open("sample.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("File not found.")

else:
    print(content)

finally:
    print("File operation completed.")
```

---

#  Raising Exceptions

Sometimes Python does not automatically raise an exception.

In such cases, programmers can manually raise exceptions using the `raise` keyword.

Syntax

```python
raise ExceptionType("Message")
```

Example

```python
def set_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print(age)
```

---

#  Custom Exceptions

You can create your own exception classes by inheriting from Python's built-in `Exception` class.

Example

```python
class InvalidAgeError(Exception):
    pass
```

Using the custom exception

```python
class InvalidAgeError(Exception):
    pass


def set_age(age):

    if age > 120:
        raise InvalidAgeError("Age cannot be over 120.")


set_age(125)
```

---


# Summary

- Exceptions are runtime errors.
- Exception handling prevents unexpected program crashes.
- `try` contains risky code.
- `except` handles exceptions.
- `else` runs only if no exception occurs.
- `finally` always executes.
- `raise` is used to generate exceptions manually.
- Custom exceptions improve code readability and error management.
- Proper exception handling makes Python programs safer and more reliable.
