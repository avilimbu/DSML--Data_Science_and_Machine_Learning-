# Day 15 - Python Recursion, Decorators, Iterators, and Generators

---

# 1. Python Recursion

## Definition

Recursion is a programming technique where a function calls **itself** to solve a smaller version of the same problem until a stopping condition is reached. :contentReference[oaicite:0]{index=0}

---

## Two Rules of Recursion

### 1. Base Case

- Stops the recursion.
- Prevents infinite recursion.
- Returns the final value.

### 2. Recursive Case

- Function calls itself.
- The input becomes smaller in every call.
- Eventually reaches the base case.

---

## Example: Factorial

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

Output

```
120
```

---

## How factorial(3) Works

```
factorial(3)

3 × factorial(2)

3 × 2 × factorial(1)

3 × 2 × 1

= 6
```

---

## Fibonacci using Recursion

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Sequence

```
0
1
1
2
3
5
8
13
21
...
```

---

## Advantages

- Simple for tree-like problems
- Cleaner code
- Easier to understand mathematically

## Disadvantages

- Slower
- Uses more memory
- Can exceed recursion limit

---

# 2. Decorators

## Definition

A decorator is a function that **adds extra functionality to another function without modifying its original code.** :contentReference[oaicite:1]{index=1}

Think of it as wrapping an existing function with additional behaviour.

---

## Real-life Analogy

Imagine a gift.

Original function → Gift

Decorator → Gift Wrapper

The gift stays the same.

Only the wrapper adds something extra.

---

## General Syntax

```python
def decorator(func):

    def wrapper():
        # Extra work
        func()
        # Extra work

    return wrapper
```

---

## Using @ Syntax

```python
def my_decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@my_decorator
def greet():
    print("Hello!")

greet()
```

Output

```
Before
Hello!
After
```

---

## Decorator with Arguments

```python
def logger(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def greet(name, age):
    print(name, age)
```

Why use *args and **kwargs?

Because decorators should work for **any function**, regardless of how many parameters it has.

---

## Common Uses of Decorators

- Logging
- Authentication
- Authorization
- Timing execution
- Caching (Memoization)
- Validation
- Flask Routes
- Django Login Required

---

# 3. Nested Functions

## Definition

A function defined **inside another function**.

Example

```python
def outer(x):

    def inner(y):
        return x + y

    return inner

add_five = outer(5)

print(add_five(6))
```

Output

```
11
```

---

## Why Use Nested Functions?

- Hide helper functions
- Build decorators
- Create closures
- Improve code organization

---

# 4. Passing Functions as Arguments

Since functions are objects in Python, they can be passed like variables.

Example

```python
def add(a, b):
    return a + b

def calculate(func, x, y):
    return func(x, y)

print(calculate(add, 4, 6))
```

Output

```
10
```

---

# 5. Returning Functions

A function can also return another function.

Example

```python
def greeting(name):

    def hello():
        return "Hello " + name

    return hello

greet = greeting("Avik")

print(greet())
```

Output

```
Hello Avik
```

This concept is heavily used in decorators.

---

# 6. Iterators

## Definition

An iterator is an object that returns **one item at a time** from a collection. :contentReference[oaicite:2]{index=2}

---

## Iterator Protocol

Every iterator has two methods:

### __iter__()

Returns the iterator object.

### __next__()

Returns the next item.

Raises

```
StopIteration
```

when data finishes.

---

## Example

```python
numbers = [1,2,3]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

Output

```
1
2
3
```

---

# 7. Generators

## Definition

A generator is a simpler way to create an iterator using the **yield** keyword instead of return. :contentReference[oaicite:3]{index=3}

---

## yield vs return

return

- Ends the function completely.

yield

- Returns one value.
- Pauses execution.
- Remembers current state.
- Continues from where it stopped.

---

## Example

```python
def count_up(n):

    i = 1

    while i <= n:
        yield i
        i += 1

gen = count_up(3)

print(next(gen))
print(next(gen))
print(next(gen))
```

Output

```
1
2
3
```

---

## Why Generators?

- Faster
- Memory efficient
- Ideal for huge datasets
- Produce values only when needed

---

# 8. Iterator vs Generator

| Iterator | Generator |
|-----------|-----------|
| Created using class | Created using function |
| Uses __iter__() and __next__() | Uses yield |
| More code | Less code |
| Manual implementation | Automatic implementation |
| Slightly harder | Very easy |

---

# 9. Machine Learning Applications

Iterators and Generators are widely used because datasets are often too large to fit into memory. :contentReference[oaicite:4]{index=4}

Common uses

- Reading CSV files
- Batch processing
- Data preprocessing
- Streaming data
- Deep Learning training
- TensorFlow Dataset
- PyTorch DataLoader
- Pandas chunksize

---

## Reading Large CSV Efficiently

Instead of

```python
df = pd.read_csv("large.csv")
```

Use

```python
for chunk in pd.read_csv("large.csv", chunksize=10000):
    process(chunk)
```

Advantages

- Less RAM usage
- Faster processing
- Works for massive datasets

---

# 10. Memory Efficient Processing

Instead of loading the entire dataset,

Process one record at a time.

Example

```python
import csv

with open("big_data.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        process(row)
```

Benefits

- Low memory usage
- Suitable for millions of rows
- Efficient for Data Science projects

---

# Summary

- Recursion solves problems by calling itself.
- Decorators extend functions without changing their source code.
- Nested functions help build decorators and closures.
- Functions can be passed and returned like variables.
- Iterators provide sequential access to data.
- Generators simplify iterator creation using `yield`.
- Generators and iterators are essential for handling large datasets efficiently in Data Science and Machine Learning.