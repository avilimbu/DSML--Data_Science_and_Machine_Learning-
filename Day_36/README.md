# Day 36 | Data Integration & Encoding

# 1. Data Integration

## What is Data Integration?

**Data Integration** is the process of collecting data from multiple sources and combining it into one unified dataset so that it can be analyzed more easily.

### Common Data Integration Approaches

The learning material introduced several approaches:

- **Manual Integration** – manually combining data from different sources.
- **API Integration** – extracting data from systems through APIs.
- **ETL Integration** – Extract, Transform, and Load data into a target system.
- **Virtual Integration** – creating a virtual view that makes multiple data sources appear as one.

For DataFrame-based work in Pandas, the main operations practiced were:

- `concat()`
- `merge()`
- `join()`
- `stack()`

---

# 2. Concatenation

## What is Concatenation?

**Concatenation** is the process of combining DataFrames by adding their rows or columns together.

In Pandas, concatenation is performed using:

```python
pd.concat()
```

### Row-wise Concatenation

When `axis=0` is used, DataFrames are combined **vertically**.

```python
row_concat = pd.concat([df1, df2], axis=0)
```

### Column-wise Concatenation

When `axis=1` is used, DataFrames are combined **horizontally**.

```python
column_concat = pd.concat([df1, df2], axis=1)
```

```text
axis=0  →  Row-wise / Vertical
axis=1  →  Column-wise / Horizontal
```

---

# 3. Merging

## What is Merging?

**Merging** is the process of combining two or more DataFrames based on one or more **common columns or keys**.

In Pandas:

```python
pd.merge()
```

### Example

```python
inner_merge = pd.merge(
    marks,
    students,
    on="student_id",
    how="inner"
)
```

Here:

- `marks` → first DataFrame
- `students` → second DataFrame
- `student_id` → common column/key
- `how="inner"` → keeps matching records

### Quick Revision

```text
merge()
   ↓
Common column / key
   ↓
Combine related records
```

### Real-World Example

Suppose we have:

```text
Students
student_id | name
-----------|------
1          | Ravi
2          | Hari
3          | Javi

Marks
student_id | marks
-----------|------
1          | 44
2          | 55
3          | 66
```

We can merge both datasets using:

```python
pd.merge(students, marks, on="student_id")
```

Result:

```text
student_id | name | marks
-----------|------|------
1          | Ravi | 44
2          | Hari | 55
3          | Javi | 66
```

---

# 4. Join

## What is Join?

**Join** is similar to merging, but in the practiced Pandas example it is specifically used to combine DataFrames based on their **indexes**.

The method used is:

```python
DataFrame.join()
```

### Example

First, set the key as the index:

```python
df1 = df1.set_index("key")
df2 = df2.set_index("key")
```

Then join the DataFrames:

```python
df1.join(df2, how="inner")
```

### Outer Join

```python
df1.join(df2, how="outer")
```

An outer join keeps the indexes from both DataFrames.

### Quick Revision

```text
merge()  → commonly combines using columns/keys
join()   → commonly combines using indexes
```

---

# 5. Stacking

## What is Stacking?

In the practical notebook, `stack()` was used as a **data reshaping operation**.

It moves column values into rows and creates a hierarchical index.

```python
stacked = df1.stack()
```

### Important Note

Although stacking was studied alongside Data Integration, it is more accurately considered a **data reshaping operation** rather than a direct data-combination operation.

### Quick Revision

```text
stack()
   ↓
Columns → Rows
   ↓
Reshape the DataFrame
```

---

# 6. Data Integration — Quick Comparison

| Operation | Main Purpose | Common Use |
|-----------|--------------|------------|
| `concat()` | Combine DataFrames | Add rows or columns |
| `merge()` | Combine using common keys | Relational-style data combination |
| `join()` | Combine using indexes | Index-based combination |
| `stack()` | Reshape data | Convert columns into rows |

### Easy Way to Remember

```text
CONCAT → Put DataFrames together
MERGE  → Match using a common key
JOIN   → Combine using indexes
STACK  → Reshape columns into rows
```

---

# 7. Encoding

## What is Encoding?

**Encoding** is the process of converting categorical data into a numerical representation so that it can be used effectively in machine learning workflows.

Categorical values are often represented as text, for example:

```text
Sex
----
Male
Female
```

Machine learning algorithms generally require numerical representations, so categorical values need to be encoded.

---

# 8. One-Hot Encoding

## What is One-Hot Encoding?

**One-Hot Encoding** converts categorical values into separate binary columns.

Each category receives its own column, and the value is represented using:

```text
0 → Category is not present
1 → Category is present
```

---

## Example: Encoding `Sex`

Suppose the dataset contains:

```text
Sex
----
Male
Female
Female
Male
```

Using Pandas:

```python
pd.get_dummies(
    titanic_df,
    columns=["Sex"],
    dtype=int
)
```

The categorical column is transformed into separate columns such as:

```text
Sex_Female | Sex_Male
-----------|---------
1          | 0
0          | 1
0          | 1
1          | 0
```

---

## Example: Encoding `Embarked`

The same approach can be used for another categorical column:

```python
pd.get_dummies(
    titanic_df,
    columns=["Embarked"],
    dtype=int
)
```

---

# 9. One-Hot Encoding — Quick Revision

### Before Encoding

```text
Color
-----
Red
Blue
Green
Red
```

### After One-Hot Encoding

```text
Color_Blue | Color_Green | Color_Red
-----------|-------------|-----------
0          | 0           | 1
1          | 0           | 0
0          | 1           | 0
0          | 0           | 1
```

### Remember

```text
Categorical Data
       ↓
One-Hot Encoding
       ↓
Multiple Binary Columns
       ↓
0 / 1 Representation
```

---

# 10. Real-World Examples

The concepts learned today can be applied to real-world datasets.

### E-Commerce

```text
January Sales + February Sales
            ↓
         concat()
```

### Customer & Order Data

```text
Customer Information
        +
Order Information
        ↓
     merge()
        ↓
Customer_ID
```

### Sales & Customer Information

```text
Sales Data
    +
Customer Data
    ↓
  join()
    ↓
Index-based combination
```

### Reshaping Monthly Data

```text
Monthly Columns
      ↓
    stack()
      ↓
Individual Rows
```

### Categorical Data

```text
Sex / Embarked
      ↓
One-Hot Encoding
      ↓
Numerical 0 / 1 Columns
```

---

# 11. Practical Code Summary

## Import Pandas

```python
import pandas as pd
```

## Concatenation

```python
pd.concat([df1, df2], axis=0)
pd.concat([df1, df2], axis=1)
```

## Merging

```python
pd.merge(
    df1,
    df2,
    on="common_column",
    how="inner"
)
```

## Join

```python
df1.join(
    df2,
    how="inner"
)
```

## Stacking

```python
df1.stack()
```

## One-Hot Encoding

```python
pd.get_dummies(
    df,
    columns=["column_name"],
    dtype=int
)
```

---

# 12. Important Points to Remember

- **Data Integration** combines data from multiple sources into a unified form.
- `pd.concat()` can combine DataFrames **row-wise or column-wise**.
- `pd.merge()` combines DataFrames using **common columns/keys**.
- `DataFrame.join()` is commonly used for **index-based combination**.
- `stack()` is mainly a **data reshaping operation**.
- **Encoding** converts categorical information into a numerical representation.
- **One-Hot Encoding** creates separate binary columns for categories.
- `pd.get_dummies()` is a convenient Pandas method for One-Hot Encoding.
- `dtype=int` makes the generated dummy values appear as `0` and `1`.

---

# 13. Data Integration & Encoding Workflow

```text
             RAW DATA
                 │
                 ▼
        ┌─────────────────┐
        │ Multiple Sources│
        └────────┬────────┘
                 │
                 ▼
        DATA INTEGRATION
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
    concat()   merge()   join()
       │         │         │
       └─────────┼─────────┘
                 │
                 ▼
             Combined
              Dataset
                 │
                 ▼
          Data Reshaping
             stack()
                 │
                 ▼
        Categorical Data
                 │
                 ▼
             Encoding
                 │
                 ▼
       One-Hot Encoding
                 │
                 ▼
          Numerical Data
                 │
                 ▼
       Ready for ML Workflow
```




