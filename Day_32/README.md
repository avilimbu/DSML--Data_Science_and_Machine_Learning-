# Day 32 — Visualization in Pandas & Data Manipulation

# 1. Visualization in Pandas

**Pandas** is a powerful open-source Python library used for data analysis and manipulation.

It is particularly useful for working with **labeled data**, such as tables containing rows and columns.

Pandas also provides built-in functions that allow us to create different types of graphs directly from DataFrame data.

---

# 2. Pandas Visualization

Pandas can be used to visualize data directly from a DataFrame.

A basic visualization can be created using:

```python
df.plot()
```

The `plot()` function provides a convenient way to create graphs from DataFrame or Series data.

### Example

```python
import pandas as pd

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [100, 150, 120, 200]
})

df.plot()
```

---

# 3. Line Plot

A **line plot** is useful for showing changes or trends in data.

```python
df.plot(
    x="Month",
    y="Sales",
    kind="line"
)
```

A line plot connects data points with lines, making it useful for observing how a value changes across another variable.

---

# 4. Bar Plot

A **bar plot** represents data using rectangular bars.

It is useful for comparing values between different categories.

```python
df.plot(
    x="Month",
    y="Sales",
    kind="bar"
)
```

For example, a bar plot can be used to compare sales across different months.

---

# 5. Horizontal Bar Plot

A horizontal bar plot can be created using:

```python
df.plot(
    x="Month",
    y="Sales",
    kind="barh"
)
```

The bars are displayed horizontally instead of vertically.

---

# 6. Histogram

A **histogram** is used to understand the distribution of numerical data.

```python
df["Sales"].plot(
    kind="hist"
)
```

A histogram divides numerical values into intervals and shows how frequently values occur within those intervals.

---

# 7. Box Plot

A **box plot** provides a visual representation of the distribution of numerical data.

```python
df["Sales"].plot(
    kind="box"
)
```

Box plots are useful for understanding the spread of data and can also help identify potential extreme values.

---

# 8. Area Plot

An **area plot** is similar to a line plot, but the area below the line is filled.

```python
df.plot(
    x="Month",
    y="Sales",
    kind="area"
)
```

Area plots can be useful for showing changes in values across an ordered sequence.

---

# 9. Scatter Plot

A **scatter plot** displays individual data points using two numerical variables.

```python
df.plot(
    x="Month",
    y="Sales",
    kind="scatter"
)
```

Scatter plots are commonly used to observe relationships between variables.

---

# 10. Data Manipulation

**Data Manipulation** is the process of modifying, organizing, cleaning, and transforming data into a format that is easier to analyze or use.

It can involve:

* Creating data points
* Arranging data
* Deleting data points
* Cleaning data
* Transforming data

The purpose of data manipulation is to make it easier to work with data and obtain useful insights.

---

# 11. Data Manipulation in Pandas

Pandas provides many functions for working with and manipulating datasets.

Important operations include:

* Loading datasets
* Cleaning missing values
* Removing duplicates
* Filtering data
* Sorting data
* Grouping and aggregating data
* Merging and joining datasets
* Creating and modifying columns
* Reshaping data

These operations are part of the Data Manipulation topics covered in Day 32.

---

# 12. Loading Datasets

Pandas can load datasets from different file formats.

### CSV File

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

The `read_csv()` function is used to load a CSV dataset.

---

### Excel File

```python
df = pd.read_excel("data.xlsx")
```

The `read_excel()` function is used to load an Excel dataset.

---

# 13. Handling Missing Values

Missing values are common in real-world datasets.

Pandas provides:

```python
fillna()
dropna()
```

for handling missing values.

### `fillna()`

Used to replace missing values.

```python
df["Age"] = df["Age"].fillna(0)
```

### `dropna()`

Used to remove rows or columns containing missing values.

```python
df = df.dropna()
```

---

# 14. Removing Duplicates

Duplicate records can be removed using:

```python
drop_duplicates()
```

### Example

```python
df = df.drop_duplicates()
```

This removes duplicate rows from the DataFrame.

---

# 15. Filtering Data

Filtering allows us to select specific rows based on a condition.

### Example

```python
filtered_df = df[df["Age"] > 18]

print(filtered_df)
```

Only rows where `Age` is greater than `18` are selected.

---

# 16. Sorting Data

The `sort_values()` function is used to arrange data according to a column.

### Ascending Order

```python
df = df.sort_values("Age")
```

### Descending Order

```python
df = df.sort_values(
    "Age",
    ascending=False
)
```

Sorting is useful when we want to arrange data from smallest to largest or largest to smallest.

---

# 17. Grouping and Aggregating Data

The `groupby()` function allows us to divide data into groups.

### Example

```python
result = df.groupby("Sex")["Survived"].mean()

print(result)
```

Common aggregation functions include:

```python
mean()
sum()
count()
min()
max()
```

Grouping and aggregation can be used to summarize data and identify patterns.

---

# 18. Merging and Joining Data

Pandas can combine information from multiple datasets.

### Merge

```python
merged_df = pd.merge(
    df1,
    df2,
    on="ID"
)
```

### Join

```python
joined_df = df1.join(df2)
```

Merging and joining are useful when related information is stored in separate DataFrames.

---

# 19. Creating and Modifying Columns

New columns can be created using existing data.

### Example

```python
df["Total"] = df["Price"] * df["Quantity"]
```

A new `Total` column is created.

Existing columns can also be modified.

```python
df["Age"] = df["Age"] + 1
```

---

# 20. Reshaping Data

Pandas provides functions for changing the structure of data.

Two important functions are:

```python
pivot()
melt()
```

### `pivot()`

```python
result = df.pivot(
    index="Date",
    columns="Category",
    values="Sales"
)
```

### `melt()`

```python
result = df.melt()
```

These functions are used when the structure of a dataset needs to be changed for analysis.

---

# 21. Combining Data Manipulation and Visualization

Data manipulation and visualization can be used together.

For example:

```python
result = df.groupby("Sex")["Survived"].mean()

result.plot(
    kind="bar",
    title="Survival Rate by Gender"
)
```

Here:

1. `groupby()` groups the data.
2. `mean()` calculates the average.
3. `plot()` visualizes the result.

This allows us to transform raw data into a form that is easier to understand visually.

---

# 22. Typical Workflow

A basic Pandas data analysis workflow can be represented as:

```text
Load Dataset
     ↓
Inspect Data
     ↓
Clean Data
     ↓
Handle Missing Values
     ↓
Remove Duplicates
     ↓
Filter Data
     ↓
Sort Data
     ↓
Group / Aggregate
     ↓
Merge / Join
     ↓
Create / Modify Columns
     ↓
Reshape Data
     ↓
Visualize Data
     ↓
Analyze Insights
```

---

# 23. Important Pandas Functions

```python
pd.read_csv()
pd.read_excel()

df.fillna()
df.dropna()
df.drop_duplicates()

df.sort_values()
df.groupby()

pd.merge()
df.join()

df.pivot()
df.melt()

df.plot()
```

---

# Summary

* What visualization in Pandas means.
* How Pandas can be used to create graphs directly from DataFrames.
* How to create line plots using Pandas.
* How to create bar and horizontal bar plots.
* How histograms can be used to understand data distribution.
* How box plots can be used to visualize data distribution.
* How area plots can represent changes in data.
* How scatter plots can show relationships between variables.
* What data manipulation means.
* How to load CSV and Excel datasets.
* How to handle missing values using `fillna()` and `dropna()`.
* How to remove duplicate records using `drop_duplicates()`.
* How to filter and sort data.
* How to group and aggregate data using `groupby()`.
* How to merge and join datasets.
* How to create and modify columns.
* How to reshape data using `pivot()` and `melt()`.
* How data manipulation and visualization can be combined to extract insights.
