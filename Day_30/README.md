# Day 30 — Data Exploration with Pandas

## What is Data Exploration?

**Data Exploration in Pandas** is the process of examining, understanding, and summarizing a dataset before performing analysis or modeling.

During exploration, we investigate:

* Dataset structure
* Number of rows and columns
* Data types
* Missing values
* Duplicate values
* Data distributions
* Outliers
* Patterns within the data

The purpose is to understand the dataset before deciding what preprocessing or analysis should be performed.

---

## Data Exploration with Pandas

Pandas provides several functions that make it easier to inspect and understand datasets.

### Common Exploration Operations

Some of the commonly used exploration operations include:

```python
df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()
df.dtypes
df.isnull().sum()
df.duplicated().sum()
```

These functions allow us to quickly understand different aspects of a dataset.

---

## Exploring Dataset Structure

### 1. `head()`

Displays the first few rows of the dataset.

```python
df.head()
```

### 2. `tail()`

Displays the last few rows.

```python
df.tail()
```

### 3. `shape`

Returns the number of rows and columns.

```python
df.shape
```

Example:

```text
(891, 12)
```

This means the dataset contains:

* 891 rows
* 12 columns

### 4. `columns`

Displays the column names.

```python
df.columns
```

### 5. `info()`

Provides information about:

* Number of entries
* Column names
* Data types
* Non-null values

```python
df.info()
```

### 6. `describe()`

Generates statistical information for numerical columns.

```python
df.describe()
```

---

## Checking Missing Values

Missing values are an important part of data exploration.

We can check the number of missing values in each column using:

```python
df.isnull().sum()
```

This helps us determine which columns may require further data-cleaning operations.

---

## Detecting Duplicate Data

Duplicate records can affect analysis and machine learning results.

To count duplicate rows:

```python
df.duplicated().sum()
```

If duplicate records exist, they can be investigated before deciding whether they should be removed.

---

## Understanding Data Distribution

Data exploration also involves understanding how values are distributed.

For example:

```python
df["Age"].describe()
```

This can help identify:

* Minimum value
* Maximum value
* Mean
* Standard deviation
* Quartiles

Understanding distributions can also help identify unusual values and possible outliers.

