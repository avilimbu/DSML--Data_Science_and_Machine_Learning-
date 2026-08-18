# Day 33 — Data Manipulation & Outlier Handling

# 1. Data Manipulation

**Data Manipulation** is the process of modifying, organizing, cleaning, and transforming data into a format that is easier to analyze or use.

Data manipulation can involve:

* Creating data
* Arranging data
* Deleting data
* Cleaning data
* Transforming data
* Filtering data

The main purpose of data manipulation is to make the data easier to work with and extract useful insights from it.

---

# 2. Data Manipulation in Pandas

**Pandas** is one of the most popular Python libraries for data manipulation.

Pandas provides functions for:

* Loading datasets
* Cleaning missing values
* Removing duplicates
* Filtering data
* Sorting data
* Grouping and aggregating data
* Merging and joining datasets
* Creating and modifying columns
* Reshaping data

---

# 3. Loading Datasets

Pandas can be used to load datasets from different file formats.

### Loading a CSV File

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df)
```

The `read_csv()` function is used to load data from a CSV file into a Pandas DataFrame.

---

### Loading an Excel File

```python
df = pd.read_excel("data.xlsx")

print(df)
```

The `read_excel()` function is used to load data from an Excel file.

---

# 4. Handling Missing Values

Real-world datasets can contain missing values.

Pandas provides functions such as:

```python
fillna()
dropna()
```

for handling missing data.

---

### `fillna()`

`fillna()` is used to replace missing values.

```python
df["Age"] = df["Age"].fillna(0)
```

Here, missing values in the `Age` column are replaced with `0`.

---

### `dropna()`

`dropna()` is used to remove rows or columns containing missing values.

```python
df = df.dropna()
```

This removes rows containing missing values.

---

# 5. Removing Duplicate Data

Duplicate records can exist in a dataset.

Pandas provides:

```python
drop_duplicates()
```

to remove duplicate rows.

### Example

```python
df = df.drop_duplicates()

print(df)
```

This removes duplicate records from the DataFrame.

---

# 6. Filtering Data

Filtering allows us to select only the rows that satisfy a particular condition.

### Example

```python
female = df[df["Sex"] == "female"]

print(female)
```

Here, only the rows where the `Sex` column contains `"female"` are selected.

Filtering is useful when we want to analyze a specific portion of a dataset.

---

# 7. Sorting Data

Pandas provides `sort_values()` to arrange data according to the values of a column.

### Ascending Order

```python
df = df.sort_values("Age")

print(df)
```

### Descending Order

```python
df = df.sort_values("Age", ascending=False)

print(df)
```

Sorting can make it easier to identify the smallest or largest values in a dataset.

---

# 8. Grouping and Aggregating Data

The `groupby()` function is used to divide data into groups based on one or more columns.

### Example

```python
result = df.groupby("Sex")["Survived"].mean()

print(result)
```

Here, the data is grouped according to `Sex` and the mean of `Survived` is calculated for each group.

Common aggregation functions include:

```python
mean()
sum()
count()
min()
max()
```

Grouping and aggregation are useful for summarizing datasets and finding patterns.

---

# 9. Merging Datasets

Sometimes information is stored in different DataFrames.

Pandas provides `merge()` to combine related datasets.

### Example

```python
merged_df = pd.merge(df1, df2, on="ID")

print(merged_df)
```

The `on` parameter specifies the column used to match the records.

---

# 10. Joining Datasets

Pandas also provides the `join()` function for combining DataFrames.

### Example

```python
joined_df = df1.join(df2)

print(joined_df)
```

Joining is useful when related information is stored in separate DataFrames.

---

# 11. Creating and Modifying Columns

New columns can be created directly in a DataFrame.

### Creating a Column

```python
df["Total"] = df["Price"] * df["Quantity"]

print(df)
```

A new `Total` column is created using existing columns.

---

### Modifying a Column

Existing columns can also be modified.

```python
df["Age"] = df["Age"] + 1
```

This changes the values in the `Age` column.

---

# 12. Reshaping Data

Pandas provides functions such as:

```python
pivot()
melt()
```

for reshaping data.

---

### `pivot()`

`pivot()` can be used to reshape data.

```python
result = df.pivot(
    index="Date",
    columns="Category",
    values="Sales"
)

print(result)
```

---

### `melt()`

`melt()` can be used to transform data into another structure.

```python
result = df.melt()

print(result)
```

These functions are useful when the structure of a dataset needs to be changed for analysis.

---

# 13. Outlier Handling

An **outlier** is an extreme data point that deviates significantly from the rest of the dataset.

Outliers can occur because of:

* Measurement errors
* Data-entry mistakes
* Natural variability

Outlier handling involves several important steps:

1. Identify the outliers.
2. Determine their cause.
3. Choose an appropriate treatment strategy.
4. Evaluate the impact of the treatment on the model.

---

# 14. Outlier Detection Methods

There are several ways to detect outliers.

The methods covered in this chapter are:

* Interquartile Range (IQR)
* Z-Score
* Visualization

---

# 15. Interquartile Range (IQR)

The **Interquartile Range (IQR)** method is useful for non-normal or skewed data.

IQR represents the middle 50% of the dataset.

The first quartile is represented by `Q1` and the third quartile is represented by `Q3`.

### IQR Formula

```text
IQR = Q3 - Q1
```

An observation is generally considered an outlier if it is below:

```text
Q1 - 1.5 × IQR
```

or above:

```text
Q3 + 1.5 × IQR
```

---

### Example

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

print(outliers)
```

This identifies values outside the calculated lower and upper boundaries.

---

# 16. Z-Score

The **Z-Score** measures how many standard deviations a data point is from the mean.

Z-Score is ideal for normally distributed data.

The formula is:

```text
Z = (x - μ) / σ
```

Where:

```text
x = Data point
μ = Mean
σ = Standard deviation
```

Points with a Z-score greater than `3` or less than `-3` are typically flagged as potential outliers.

---

### Example

```python
from scipy.stats import zscore

df["Z_Score"] = zscore(df["Age"])

outliers = df[
    (df["Z_Score"] > 3) |
    (df["Z_Score"] < -3)
]

print(outliers)
```

The Z-score allows us to determine how far a value is from the mean in terms of standard deviations.

---

# 17. Visualization for Outlier Detection

Visualization is another useful method for identifying extreme values.

Common visualizations include:

* Scatter plots
* Box plots
* Histograms

These visualizations can help us identify unusual values quickly.

---

# 18. Box Plot

A box plot is particularly useful for identifying potential outliers.

### Example

```python
import matplotlib.pyplot as plt

df["Age"].plot(kind="box")

plt.show()
```

The box plot provides a visual representation of the distribution of the data and can help identify values that lie far from the rest of the observations.

---

# 19. Scatter Plot

A scatter plot can also help identify extreme observations.

```python
import matplotlib.pyplot as plt

plt.scatter(df["Age"], df["Fare"])

plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare")

plt.show()
```

Scatter plots are useful when examining relationships between two numerical variables and identifying unusual observations.

---

# 20. Histogram

A histogram shows the distribution of numerical data.

```python
import matplotlib.pyplot as plt

df["Age"].plot(kind="hist")

plt.xlabel("Age")
plt.title("Age Distribution")

plt.show()
```

A histogram can help us visually understand the distribution and identify values that appear unusually far from the main group.

---

# 21. Data Manipulation Workflow

A typical data manipulation and outlier-handling workflow can be represented as:

```text
Load Dataset
     ↓
Inspect Data
     ↓
Handle Missing Values
     ↓
Remove Duplicates
     ↓
Filter Data
     ↓
Sort Data
     ↓
Create / Modify Columns
     ↓
Group / Aggregate Data
     ↓
Merge / Join Data
     ↓
Reshape Data
     ↓
Detect Outliers
     ↓
Handle Outliers
     ↓
Analyze Data
```

---

# 22. Important Pandas Functions

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
```

---

# 23. Important Outlier Concepts

```text
Outlier
IQR
Q1
Q3
Z-Score
Mean
Standard Deviation
Box Plot
Scatter Plot
Histogram
```

---

# Summary

* What data manipulation means.
* How data can be modified, organized, cleaned, and transformed.
* How Pandas is used for data manipulation.
* How to load CSV and Excel datasets using Pandas.
* How to handle missing values using `fillna()` and `dropna()`.
* How to remove duplicate records using `drop_duplicates()`.
* How to filter data using conditions.
* How to sort data using `sort_values()`.
* How to group and aggregate data using `groupby()`.
* How to merge and join datasets.
* How to create and modify DataFrame columns.
* How to reshape data using `pivot()` and `melt()`.
* What an outlier is and why outliers can occur.
* The major steps involved in outlier handling.
* How to detect outliers using the IQR method.
* How to detect potential outliers using Z-Score.
* How box plots, scatter plots, and histograms can help identify extreme values.
