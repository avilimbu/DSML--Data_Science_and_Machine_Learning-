
# Day 29 | Eigenvalues and Eigenvecotrs, Singular Value Decomposition (SVD), and Pandas Basics


# Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors are fundamental concepts for understanding **linear transformations**.

NumPy provides:

```python
np.linalg.eig()
```

### Example

```python
A = np.array([
    [2, 0],
    [0, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)
```

The function returns:

* Eigenvalues
* Corresponding eigenvectors

---

# Singular Value Decomposition (SVD)

**Singular Value Decomposition (SVD)** factorizes a matrix into three components:

```text
A = U × S × VT
```

Where:

* `U` → Left singular vectors
* `S` → Singular values
* `VT` → Right singular vectors

NumPy provides:

```python
np.linalg.svd()
```

### Example

```python
A = np.array([
    [1, 2],
    [3, 4]
])

U, S, VT = np.linalg.svd(A)

print("U:")
print(U)

print("S:")
print(S)

print("VT:")
print(VT)
```

SVD has applications in areas such as:

* Signal processing
* Statistics
* Data analysis
* Dimensionality reduction

---

## What is Pandas?

**Pandas** is an open-source Python library used for:

* Data manipulation
* Data analysis
* Data cleaning
* Data preparation

Pandas provides powerful data structures that make working with structured data easier and faster.

### Pandas is widely used in:

* Data Analysis
* Data Science
* Machine Learning
* Financial Analysis
* Business Intelligence
* Data Cleaning and Preparation

---

# 1. Series

A **Series** is a one-dimensional, array-like object that can store different types of data, such as:

* Integers
* Strings
* Floats
* Python objects

A Series also contains **labels called an index**.

### Syntax

```python
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False)
```

### Creating a Series from a List

```python
import pandas as pd

a = ['g', 'e', 'e', 'k', 's']

res = pd.Series(a)

print(res)
```

### Series with Integer Data

```python
import pandas as pd

a = [1, 2, 3, 4, 5]

res = pd.Series(a)

print(res)
```

### Series from a Dictionary

A Series can also be created from a dictionary.

```python
import pandas as pd

a = {
    'Id': 1013,
    'Name': 'Mohan',
    'State': 'ktm',
    'Age': 24
}

res = pd.Series(a)

print(res)
```

---

# 2. DataFrame

A **DataFrame** is a **two-dimensional data structure** that can store different types of data in columns.

It is similar to:

* A spreadsheet
* A SQL table
* A `data.frame`

A DataFrame contains:

* Rows
* Columns
* Column labels
* Index labels

By default, the index starts from **0** and increases sequentially.

### Example

```text
Name     Age     Sex
---------------------
Ram      20      M
Sita     21      F
Hari     22      M
```

Here:

* `Name`, `Age`, and `Sex` are columns.
* Each row has an index.
* Different columns can contain different types of data.

---

# 3. DataFrame Syntax

```python
pandas.DataFrame(
    data=None,
    index=None,
    columns=None,
    dtype=None,
    copy=False
)
```

### Parameters

| Parameter | Description                                                                        |
| --------- | ---------------------------------------------------------------------------------- |
| `data`    | Input data such as lists, dictionaries, NumPy arrays, Series, or another DataFrame |
| `index`   | Optional labels for rows                                                           |
| `columns` | Optional labels for columns                                                        |
| `dtype`   | Optional data type for columns                                                     |
| `copy`    | Boolean value specifying whether to copy the data                                  |

---

# 4. Creating a DataFrame from a List

A DataFrame can be created from a list.

```python
import pandas as pd

a = [
    'Python',
    'Pandas',
    'Numpy'
]

df = pd.DataFrame(a, columns=['Tech'])

print(df)
```

Output:

```text
     Tech
0  Python
1  Pandas
2   Numpy
```

---

# 5. Creating a DataFrame from a Dictionary

A dictionary can also be used to create a DataFrame.

```python
import pandas as pd

a = {
    'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
    'Age': [20, 21, 19, 18]
}

res = pd.DataFrame(a)

print(res)
```

The dictionary keys become the **column names**, while the values become the data in those columns.

---

# 6. Selecting Columns from a DataFrame

We can select one or multiple columns from a DataFrame.

### Example DataFrame

```python
import pandas as pd

a = {
    'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age': [27, 24, 22, 32],
    'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd']
}

df = pd.DataFrame(a)
```

### Selecting Multiple Columns

```python
print(df[['Name', 'Qualification']])
```

This returns a new DataFrame containing only the selected columns.

---

# 7. Accessing Columns

### Accessing a Single Column

```python
print(df['Name'])
```

`df['Name']` returns a **Series** containing the values from the `Name` column.

### Accessing Multiple Columns

```python
print(df[['Name', 'City']])
```

When multiple columns are selected, the result is a **DataFrame**.

### Important Difference

```python
df['Name']
```

Returns:

```text
Series
```

While:

```python
df[['Name', 'City']]
```

Returns:

```text
DataFrame
```

---

# 8. Filtering Rows Using `loc`

Pandas provides `.loc[]` to access and filter rows.

### Example

```python
import pandas as pd

a = {
    'Name': ['Mohe', 'Shyni', 'Parul', 'Sam'],
    'ID': [12, 43, 54, 32],
    'City': ['Delhi', 'Kochi', 'Pune', 'Patna']
}

df = pd.DataFrame(a)

res = df.loc[df['Name'] == 'Mohe']

print(res)
```

### How it works

```python
df['Name'] == 'Mohe'
```

checks which rows have `Mohe` in the `Name` column.

Then:

```python
df.loc[...]
```

returns the row or rows that satisfy the condition.

---


# Quick Reference

| Operation               | Syntax                       |
| ----------------------- | ---------------------------- |
| Import Pandas           | `import pandas as pd`        |
| Create Series           | `pd.Series(data)`            |
| Create DataFrame        | `pd.DataFrame(data)`         |
| Select one column       | `df['column']`               |
| Select multiple columns | `df[['column1', 'column2']]` |
| Filter rows             | `df.loc[condition]`          |


