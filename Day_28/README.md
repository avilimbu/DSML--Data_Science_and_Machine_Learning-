# Day 28 — NumPy Matrix Operations & Linear Algebra

# 1. Element-wise Matrix Operations

Element-wise operations perform calculations between corresponding elements of arrays or matrices.

They are widely used in:

* Data manipulation
* Machine learning
* Mathematical computations
* Large dataset transformations

### Common Element-wise Operations

### Addition

Corresponding elements are added together.

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

result = A + B

print(result)
```

Output:

```text
[[ 6  8]
 [10 12]]
```

---

### Subtraction

Corresponding elements are subtracted.

```python
result = A - B
print(result)
```

Output:

```text
[[-4 -4]
 [-4 -4]]
```

---

### Multiplication

Corresponding elements are multiplied.

```python
result = A * B
print(result)
```

Output:

```text
[[ 5 12]
 [21 32]]
```

> **Important:** `A * B` performs element-wise multiplication. It is different from matrix multiplication.

---

### Division

Corresponding elements are divided.

```python
result = B / A

print(result)
```

---

# 2. Scalar Operations

A scalar operation performs an arithmetic operation between a matrix and a single value.

```python
A = np.array([
    [1, 2],
    [3, 4]
])

print(A + 10)
print(A - 10)
print(A * 10)
print(A / 10)
```

The scalar value is applied to every element of the matrix.

---

# 3. Broadcasting in NumPy

**Broadcasting** allows NumPy to perform operations between arrays with different shapes when their shapes are compatible.

NumPy automatically expands the smaller array across the larger array during the operation.

### Example

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([10, 20, 30])

result = A + B

print(result)
```

Output:

```text
[[11 22 33]
 [14 25 36]]
```

Here, NumPy effectively applies:

```text
[10, 20, 30]
```

to each row of `A`.

### Why Broadcasting Is Useful

Broadcasting allows us to perform operations without manually creating repeated copies of an array.

---

# 4. Linear Algebra in NumPy

NumPy provides the `numpy.linalg` module for many linear algebra operations.

```python
import numpy as np
```

Some useful functions include:

```python
np.linalg.det()
np.linalg.inv()
np.linalg.eig()
np.linalg.svd()
np.linalg.solve()
np.linalg.matrix_rank()
```

---

# 5. Determinant of a Matrix

The determinant is a scalar value calculated from a square matrix.

NumPy provides:

```python
np.linalg.det()
```

### Example

```python
A = np.array([
    [1, 2],
    [3, 4]
])

det_A = np.linalg.det(A)

print(det_A)
```

---

# 6. Inverse of a Matrix

The inverse of a square matrix `A` is commonly represented as:

```text
A⁻¹
```

NumPy provides:

```python
np.linalg.inv()
```

### Example

```python
A = np.array([
    [1, 2],
    [3, 4]
])

A_inv = np.linalg.inv(A)

print(A_inv)
```

### Verifying the Inverse

A matrix multiplied by its inverse should produce the identity matrix:

```python
result = A @ np.linalg.inv(A)

print(result)
```

Due to floating-point calculations, you may see values extremely close to `0` and `1`.

---

# 7. Transpose of a Matrix

The transpose changes rows into columns and columns into rows.

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.T)
```

Output:

```text
[[1 4]
 [2 5]
 [3 6]]
```

---

# 8. Identity Matrix

An identity matrix has `1`s on the main diagonal and `0`s elsewhere.

### Create a 4 × 4 Identity Matrix

```python
identity = np.eye(4)

print(identity)
```

Output:

```text
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

---

# 9. Matrix Rank

The rank of a matrix represents the number of linearly independent rows or columns.

NumPy provides:

```python
np.linalg.matrix_rank()
```

Example:

```python
A = np.array([
    [1, 2],
    [2, 4]
])

rank = np.linalg.matrix_rank(A)

print(rank)
```

---

# 10. Trace of a Matrix

The trace is the sum of the elements on the main diagonal of a square matrix.

```python
A = np.array([
    [1, 2],
    [3, 4]
])

trace = np.trace(A)

print(trace)
```

Output:

```text
5
```

Because:

```text
1 + 4 = 5
```
---

# Summary

* How element-wise matrix operations work.
* How to perform addition, subtraction, multiplication, and division with NumPy arrays.
* How scalar operations work.
* What broadcasting means in NumPy.
* How to calculate determinants and matrix inverses.
* How to find eigenvalues and eigenvectors using `np.linalg.eig()`.
* What SVD is and its three components: `U`, `S`, and `VT`.
* How to solve linear equations using `np.linalg.solve()`.
* How to calculate matrix rank and trace.
* The difference between `*` and `@` for matrix operations.
* How to calculate vector norms, dot products, and cross products.

