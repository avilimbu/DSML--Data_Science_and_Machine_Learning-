# Day 27 | NumPy Array Properties and Methods

## 1. Creating a NumPy Array

Created a 2D NumPy array:

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr)
```

### Output

```text
[[10 20 30]
 [40 50 60]]
```

---

## 2. Array Properties

### `shape`

Returns the dimensions of the array.

```python
print(arr.shape)
```

Output:

```text
(2, 3)
```

### `ndim`

Returns the number of dimensions of the array.

```python
print(arr.ndim)
```

Output:

```text
2
```

### `dtype`

Returns the data type of the elements.

```python
print(arr.dtype)
```

---

## 3. Reshaping an Array

Given array:

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
```

Convert it into a `2 × 4` matrix:

```python
reshaped = arr.reshape(2, 4)

print(reshaped)
```

Output:

```text
[[1 2 3 4]
 [5 6 7 8]]
```

---

## 4. Converting Back to 1D Using `ravel()`

The `ravel()` method converts the array into a 1D array.

```python
original = reshaped.ravel()

print(original)
```

Output:

```text
[1 2 3 4 5 6 7 8]
```

---

## 5. Sum, Cumulative Sum and Product

Given:

```python
arr = np.array([5, 10, 15, 20, 25])
```

### Sum

```python
print(arr.sum())
```

Output:

```text
75
```

### Cumulative Sum

```python
print(arr.cumsum())
```

Output:

```text
[ 5 15 30 50 75]
```

### Product

```python
print(arr.prod())
```

---

## 6. Maximum Value and Index

Given:

```python
arr = np.array([12, 45, 22, 78, 34])
```

### Maximum Value

```python
print(arr.max())
```

Output:

```text
78
```

### Index of Maximum Value

```python
print(arr.argmax())
```

Output:

```text
3
```

`argmax()` returns the index where the maximum value occurs.

---

## 7. Clipping Values

The `clip()` method limits values within a specified range.

For example, values can be clipped between `20` and `50`:

```python
arr = np.array([12, 45, 22, 78, 34])

clipped = np.clip(arr, 20, 50)

print(clipped)
```

Output:

```text
[20 45 22 50 34]
```

Values below `20` become `20`, while values above `50` become `50`.

---

## 8. Splitting an Array

Given:

```python
arr = np.array([1, 2, 3, 4, 5, 6])
```

Split the array into 3 equal parts using `np.split()`:

```python
parts = np.split(arr, 3)

print(parts)
```

Output:

```text
[array([1, 2]), array([3, 4]), array([5, 6])]
```

---

## 9. Concatenating Arrays

Given:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

Concatenate the arrays:

```python
result = np.concatenate((a, b))

print(result)
```

Output:

```text
[1 2 3 4 5 6]
```

---

## 10. Vertical Stacking

`vstack()` stacks arrays vertically.

```python
vertical = np.vstack((a, b))

print(vertical)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

---

## 11. Horizontal Stacking

`hstack()` stacks arrays horizontally.

```python
horizontal = np.hstack((a, b))

print(horizontal)
```

Output:

```text
[1 2 3 4 5 6]
```

