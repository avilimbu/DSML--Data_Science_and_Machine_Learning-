# Day 34 — Data Manipulation & Outlier Handling

# 1. Data Manipulation

## What is Data Manipulation?

**Data manipulation** is the process of organizing, transforming, modifying, and preparing data so that it can be properly analyzed.

Using Pandas, we can perform many data manipulation operations efficiently.

For example:

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
```

After loading a dataset, we can manipulate its rows, columns, indexes, data types, and values.

---

# 2. `groupby()`

The `groupby()` method is used to divide data into groups based on one or more columns.

It is commonly used with aggregation functions such as:

* `mean()`
* `sum()`
* `count()`
* `min()`
* `max()`
* `median()`

## Example

```python
import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 45000, 55000]
})

result = df.groupby("Department")["Salary"].mean()

print(result)
```

### Output

```text
Department
HR    50000.0
IT    55000.0
Name: Salary, dtype: float64
```

Here, the data is grouped according to the `Department` column and the average salary of each department is calculated.

---

## Multiple Aggregations

We can also perform multiple calculations at once.

```python
result = df.groupby("Department")["Salary"].agg(
    ["mean", "max", "min"]
)

print(result)
```

This allows us to understand the data from multiple perspectives.

---

# 3. Creating a New Column

Pandas allows us to create a new column using existing columns.

For example, in the Titanic dataset, the passenger's title can be extracted from the `Name` column.

```python
titanic_df["Title"] = titanic_df["Name"].str.extract(
    r",\s*([^.]*)\."
)
```

This creates a new column called `Title`.

### Example

Suppose the `Name` column contains:

```text
Braund, Mr. Owen Harris
Cumings, Mrs. John Bradley
Heikkinen, Miss. Laina
```

The extracted titles would be:

```text
Mr
Mrs
Miss
```

---

## Understanding the Code

### Selecting the column

```python
titanic_df["Name"]
```

Selects the `Name` column.

### `.str`

```python
titanic_df["Name"].str
```

Allows us to perform string operations on Pandas string data.

### `.str.extract()`

```python
titanic_df["Name"].str.extract(...)
```

Extracts a pattern from each string.

### Regular Expression

```python
r",\s*([^.]*)\."
```

The regular expression searches for the text between:

```text
,
```

and

```text
.
```

For example:

```text
Braund, Mr. Owen Harris
        ↑
       Mr
```

---

# 4. Pandas Method Chaining

## What is Method Chaining?

**Method chaining** means applying multiple Pandas operations one after another in a single expression.

Instead of creating separate variables for every operation, we can chain multiple methods together.

---

## Without Method Chaining

```python
df = df.drop_duplicates()

df["Age"] = df["Age"].fillna(df["Age"].median())

df = df.reset_index(drop=True)
```

---

## With Method Chaining

```python
df = (
    df
    .drop_duplicates()
    .assign(
        Age=lambda x: x["Age"].fillna(x["Age"].median())
    )
    .reset_index(drop=True)
)
```

Method chaining can make a data-cleaning workflow more organized and easier to follow.

---

# 5. Duplicate Data

## What is Duplicate Data?

Duplicate data means that the same record appears more than once in a dataset.

For example:

```text
Name    Age
Ram     20
Shyam   21
Ram     20
```

The first and third rows are duplicates.

Duplicates can cause incorrect results during data analysis.

---

# 6. Detecting Duplicate Rows

The `duplicated()` method is used to identify duplicate rows.

```python
df.duplicated()
```

It returns a Boolean value:

```text
False
False
True
```

`True` indicates that the row is a duplicate.

---

## Counting Duplicates

```python
df.duplicated().sum()
```

This returns the total number of duplicate rows.

---

# 7. Removing Duplicate Rows

The `drop_duplicates()` method removes duplicate rows.

```python
df = df.drop_duplicates()
```

We can also modify the original DataFrame directly:

```python
df.drop_duplicates(inplace=True)
```

### Important

Before removing duplicates, we should understand whether the repeated rows are actually incorrect.

Not every repeated value is necessarily an unwanted duplicate.

---

# 8. Data Type Conversion

A dataset can contain columns with incorrect data types.

For example, numbers may sometimes be stored as strings:

```text
"20"
"25"
"30"
```

instead of numeric values:

```text
20
25
30
```

Correct data types are important because different operations require different types of data.

---

## Using `astype()`

```python
df["Age"] = df["Age"].astype(int)
```

This converts the `Age` column into integer values.

### Float

```python
df["Age"] = df["Age"].astype(float)
```

### String

```python
df["Name"] = df["Name"].astype(str)
```

---

# 9. Using `pd.to_numeric()`

`pd.to_numeric()` is useful when converting values into numeric data.

```python
df["Age"] = pd.to_numeric(df["Age"])
```

It can also handle invalid values.

```python
df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)
```

With `errors="coerce"`, invalid values are converted into `NaN`.

---

# 10. Converting to DateTime

Pandas provides `pd.to_datetime()` for converting values into datetime format.

```python
df["Date"] = pd.to_datetime(df["Date"])
```

This is useful when working with:

* Dates
* Time
* Year
* Month
* Day
* Time-series data

---

# 11. DataFrame Index

An **index** identifies the rows of a DataFrame.

By default, Pandas creates a numerical index:

```text
0
1
2
3
4
```

Example:

```python
df = pd.DataFrame({
    "Name": ["Ram", "Shyam", "Hari"],
    "Age": [20, 21, 22]
})

print(df)
```

Output:

```text
    Name  Age
0    Ram   20
1  Shyam   21
2   Hari   22
```

Here:

```text
0, 1, 2
```

are the indexes.

---

# 12. `set_index()`

The `set_index()` method is used to make an existing column the DataFrame index.

```python
df = df.set_index("Name")
```

Now the DataFrame becomes:

```text
       Age
Name
Ram     20
Shyam   21
Hari    22
```

The `Name` column is now being used as the index.

---

## Why Use `set_index()`?

Setting a meaningful index can make data easier to:

* Identify
* Access
* Organize
* Analyze

---

# 13. `reset_index()`

The `reset_index()` method restores the default numerical index.

```python
df = df.reset_index()
```

The previous index becomes a normal column again.

---

## Using `drop=True`

```python
df = df.reset_index(drop=True)
```

When `drop=True` is used, the old index is discarded instead of being added as a new column.

This is particularly useful after filtering or removing rows.

---

# 14. Outliers

## What is an Outlier?

An **outlier** is a data point that is significantly different from the majority of the observations.

For example:

```text
10, 12, 11, 13, 12, 100
```

Here, `100` may be considered an outlier because it is much larger than the other values.

---

## Why Are Outliers Important?

Outliers can affect:

* Mean
* Standard deviation
* Correlation
* Statistical analysis
* Data visualization
* Machine Learning models

However, an outlier is not automatically an error.

For example, if a person's salary is much higher than everyone else's, that value may be legitimate.

Therefore, outliers should be investigated before removing them.

---

# 15. Visualizing Outliers

One common method for identifying potential outliers is a **boxplot**.

Using Pandas:

```python
df["Age"].plot.box()
```

Or:

```python
df.boxplot(column="Age")
```

---

## Boxplot Components

A boxplot generally represents:

```text
Minimum
   |
Q1
   |
Median
   |
Q3
   |
Maximum
```

Potential outliers are usually displayed separately from the main distribution.

---

# 16. IQR — Interquartile Range

**IQR** stands for **Interquartile Range**.

It represents the range of the middle 50% of the data.

The formula is:

```text
IQR = Q3 - Q1
```

Where:

* **Q1** = First Quartile / 25th percentile
* **Q3** = Third Quartile / 75th percentile

---

# 17. Calculating Q1 and Q3

Using Pandas:

```python
Q1 = df["Age"].quantile(0.25)

Q3 = df["Age"].quantile(0.75)
```

Here:

```python
0.25
```

represents the 25th percentile.

And:

```python
0.75
```

represents the 75th percentile.

---

# 18. Calculating IQR

```python
IQR = Q3 - Q1
```

The IQR represents the spread between Q1 and Q3.

---

# 19. Finding Outlier Boundaries

The standard IQR method uses:

```text
Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

In Python:

```python
lower_bound = Q1 - 1.5 * IQR

upper_bound = Q3 + 1.5 * IQR
```

Values below the lower bound or above the upper bound are considered potential outliers using this rule.

---

# 20. Detecting Outliers

```python
outliers = df[
    (df["Age"] < lower_bound) |
    (df["Age"] > upper_bound)
]
```

This returns the rows containing potential outliers.

---

## Counting Outliers

```python
outliers.shape[0]
```

Or:

```python
len(outliers)
```

---

# 21. Removing Outliers

If investigation shows that the outliers should be removed, we can filter the DataFrame.

```python
df_cleaned = df[
    (df["Age"] >= lower_bound) &
    (df["Age"] <= upper_bound)
]
```

This keeps values inside the calculated boundaries.

---

# 22. Complete IQR Example

```python
Q1 = df["Age"].quantile(0.25)

Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR

upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Age"] < lower_bound) |
    (df["Age"] > upper_bound)
]

df_cleaned = df[
    (df["Age"] >= lower_bound) &
    (df["Age"] <= upper_bound)
]
```

---

# 23. Complete Data Cleaning Workflow

The concepts learned today can be combined into a basic data-cleaning workflow.

```python
import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Explore data
print(df.head())
print(df.info())

# Check duplicate rows
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert data type
df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)

# Create a new column
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 35, 60, 100],
    labels=["Child", "Young Adult", "Adult", "Senior"]
)

# Find outliers
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers if appropriate
df = df[
    (df["Age"] >= lower_bound) &
    (df["Age"] <= upper_bound)
]

# Reset index
df = df.reset_index(drop=True)

print(df.head())
```

---

# 24. Important Pandas Methods

| Method              | Purpose                                    |
| ------------------- | ------------------------------------------ |
| `groupby()`         | Groups data based on one or more columns   |
| `agg()`             | Performs multiple aggregation operations   |
| `duplicated()`      | Detects duplicate rows                     |
| `drop_duplicates()` | Removes duplicate rows                     |
| `astype()`          | Converts a column to a specified data type |
| `pd.to_numeric()`   | Converts values to numeric data            |
| `pd.to_datetime()`  | Converts values to datetime                |
| `set_index()`       | Sets a column as the DataFrame index       |
| `reset_index()`     | Resets the DataFrame index                 |
| `assign()`          | Creates or modifies columns                |
| `quantile()`        | Calculates a percentile                    |
| `plot.box()`        | Creates a boxplot                          |
| `boxplot()`         | Creates a boxplot                          |

---

# 25. Key Concepts

## Data Manipulation

```text
Raw Data
   ↓
Select
   ↓
Transform
   ↓
Group
   ↓
Create Columns
   ↓
Analyze
```

## Data Cleaning

```text
Dataset
   ↓
Check Duplicates
   ↓
Remove/Handle Duplicates
   ↓
Check Data Types
   ↓
Convert Data Types
   ↓
Manage Index
   ↓
Check Outliers
   ↓
Clean Dataset
```

## Outlier Detection

```text
Dataset
   ↓
Calculate Q1
   ↓
Calculate Q3
   ↓
IQR = Q3 - Q1
   ↓
Calculate Lower Bound
   ↓
Calculate Upper Bound
   ↓
Identify Potential Outliers
   ↓
Investigate
   ↓
Handle if Necessary
```

---

# 26. Summary

Outliers should **not always be deleted automatically**.

Before removing an outlier, ask:

1. Is the value actually incorrect?
2. Could it represent a legitimate observation?
3. Was there an error while collecting the data?
4. Does the domain explain why the value is unusual?
5. Will removing it improve the analysis or introduce bias?

Possible ways to handle outliers include:

* Keeping them
* Removing them
* Capping/extreme-value treatment
* Transforming the data
* Using models that are less sensitive to outliers

The correct approach depends on the dataset and the problem.

---

# 28. Final Takeaway

Data cleaning is one of the most important steps in a Data Science and Machine Learning workflow.

A model is only as useful as the quality of the data provided to it.

Today's concepts helped me understand how to move from:

```text
Raw Dataset
     ↓
Data Manipulation
     ↓
Data Cleaning
     ↓
Duplicate Handling
     ↓
Data Type Conversion
     ↓
Index Management
     ↓
Outlier Detection
     ↓
Outlier Handling
     ↓
Clean Dataset
     ↓
Data Analysis / Machine Learning
```

Understanding these preprocessing techniques will help work with real-world datasets more effectively.

