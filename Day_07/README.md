# Day 07 | Python Dictionary

## Dictionary

A **dictionary** is a built-in Python data structure used to store data in the form of **key-value pairs**.

Unlike lists and tuples, dictionaries use **keys** to access values instead of indexes.

A dictionary is:
- Mutable (can be modified)
- Unordered (Python 3.7+ preserves insertion order)
- Stores data as **key : value** pairs
- Keys must be unique

---

# Creating Dictionaries

Python provides multiple ways to create a dictionary.

## 1. Using Curly Braces `{}`

```python
person = {
    "name": "Ram",
    "country": "USA",
    "telephone": 9898000000
}

print(person)
```

---

## 2. Using the `dict()` Constructor

```python
person = dict({
    "name": "Hari",
    "country": "Nepal",
    "telephone": 9898000000
})

print(person)
```

---

## 3. Using a Sequence of Key-Value Pairs

```python
person = dict([
    ("name", "Rita"),
    ("country", "Nepal"),
    ("telephone", 9898000000)
])

print(person)
```

---

# Dictionary Rules

### Keys

- Keys must be **unique**.
- Keys can be of any immutable data type.
- Keys do not have to be strings.

### Values

- Values can be of any data type.
- Multiple keys can have the same value.

---

# Example Dictionaries

## Dictionary with Mixed Keys

```python
sample_dict = {
    "name": "Gita",
    10: "Mobile"
}

print(sample_dict)
```

---

## Dictionary with List as Value

```python
person = {
    "name": "Sita",
    "telephones": [
        9898000001,
        9898000002,
        9898000000
    ]
}

print(person)
```

---

# Accessing Dictionary Elements

There are two common ways to access values from a dictionary.

## 1. Using Square Brackets `[]`

```python
person = {
    "name": "Sita",
    "country": "Nepal",
    "telephone": 9800000000
}

print(person["name"])
```

---

## 2. Using the `get()` Method

```python
print(person.get("telephone"))
```

### Difference between `[]` and `get()`

| Square Brackets `[]` | `get()` |
|----------------------|----------|
| Raises `KeyError` if the key doesn't exist | Returns `None` or a default value |
| Used when you're sure the key exists | Safer when the key may not exist |

---

# Modifying Dictionary Elements

Dictionary values can be updated using their corresponding keys.

```python
student = {
    "name": "Ram",
    "age": 18
}

student["age"] = 20

print(student)
```

---

# Dictionary Methods

## `pop()`

Removes the specified key and returns its value.

```python
person.pop("telephone")
```

Using a default value:

```python
person.pop("phone", "Not Found")
```

---

## `popitem()`

Removes and returns the **last inserted key-value pair**.

```python
person.popitem()
```

---

## `del`

Deletes a specific key-value pair.

```python
del person["weight"]
```

Delete the entire dictionary:

```python
del person
```

---

## `clear()`

Removes all key-value pairs from the dictionary.

```python
person.clear()
```

Output

```python
{}
```

---

# Dictionary Method Examples

```python
person = {
    "name": "Hari",
    "country": "USA",
    "telephone": 1178,
    "weight": 50,
    "height": 6
}

# Remove last inserted item
deleted_item = person.popitem()
print(deleted_item)

# Remove a specific key
deleted_item = person.pop("telephone")
print(deleted_item)

# Delete a key
del person["weight"]

# Remove all items
person.clear()

# Delete entire dictionary
del person
```

---

# Joining Dictionaries

Python provides multiple ways to merge dictionaries.

---

## Using `update()`

```python
dict1 = {
    "Jessa": 70,
    "Arul": 80,
    "Emma": 55
}

dict2 = {
    "Kelly": 68,
    "Harry": 50,
    "Olivia": 66
}

dict1.update(dict2)

print(dict1)
```

---

## Using Dictionary Unpacking (`**`)

```python
student_dict1 = {
    "Aadya": 1,
    "Arul": 2
}

student_dict2 = {
    "Harry": 5,
    "Olivia": 6
}

student_dict3 = {
    "Nancy": 7,
    "Perry": 9
}

student_dict = {
    **student_dict1,
    **student_dict2,
    **student_dict3
}

print(student_dict)
```

---

## Using Merge Operator `|` (Python 3.9+)

```python
dict1 = {
    "name": "Sam",
    "age": 65
}

dict2 = {
    "regno": 456,
    "subjects": ["Maths"]
}

merged_dict = dict1 | dict2

print(merged_dict)
```

---

# Sorting Dictionary Keys

The `sorted()` function returns the dictionary keys in ascending order.

```python
student = {
    "b": 2,
    "a": 1,
    "c": 3
}

result = sorted(student)

print(result)
```

Output

```python
['a', 'b', 'c']
```

---

# Common Dictionary Operations

- Create a dictionary
- Access values
- Add new key-value pairs
- Modify existing values
- Remove key-value pairs
- Merge dictionaries
- Sort dictionary keys
- Clear a dictionary
- Delete an entire dictionary

---

# Key Takeaways

- Dictionaries store data in **key-value pairs**.
- Keys must be unique, while values can be duplicated.
- Dictionary values are mutable and can be modified.
- Values are accessed using keys rather than indexes.
- `get()` is safer than `[]` when accessing keys that may not exist.
- Common methods include `pop()`, `popitem()`, `clear()`, `update()`, and `get()`.
- Dictionaries can be merged using `update()`, dictionary unpacking (`**`), or the merge operator (`|`).
- `sorted()` returns the keys in sorted order.

---

# Concepts Covered

- Dictionary Basics
- Creating Dictionaries
- Dictionary Rules
- Accessing Elements
- Modifying Values
- Dictionary Methods
- Joining Dictionaries
- Sorting Dictionary Keys
- Dictionary Operations