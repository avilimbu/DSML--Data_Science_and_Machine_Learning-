# Day 35 | Data Cleaning, Chi-Square, Understanding of Machine Learning

# 1. Data Cleaning

**Data Cleaning** is the process of identifying, correcting, removing, or transforming incorrect, incomplete, duplicate, or inconsistent data.

It is an important step in Data Science because the quality of the data directly affects the quality of analysis and Machine Learning models.

## 1.1 Renaming Columns

Renaming columns helps make a dataset more **readable, consistent, and easier to work with**.

### Example

```python
df.rename(columns={"old_name": "new_name"}, inplace=True)
```

For example:

```python
df.rename(columns={"income": "annual_income"}, inplace=True)
```

### Why Rename Columns?

* Improves readability
* Makes code easier to understand
* Maintains consistent naming conventions
* Removes unnecessary spaces or characters

---

## 1.2 Handling Incorrect Data

Incorrect data refers to values that do not follow the expected format, range, or meaning of a variable.

### Example

```text
Age
18
25
32
-5
250
```

If the dataset represents human age, values such as `-5` and `250` are likely incorrect.

### Ways to Handle Incorrect Data

* Correct the value if the original value is known
* Replace the value
* Remove the affected record
* Set valid boundaries
* Investigate the source of the error

---

## 1.3 `abs()`

The `abs()` function returns the **absolute value** of a number.

It converts a negative number into its positive equivalent.

### Example

```python
abs(-10)
```

Output:

```text
10
```

With Pandas:

```python
df["age"] = df["age"].abs()
```

This can be useful when negative values are not meaningful for a particular variable.

---

## 1.4 Setting Boundaries

Setting boundaries means defining the **minimum and maximum acceptable values** for a variable.

For example, if an age column should contain values between 0 and 100:

```python
df = df[(df["age"] >= 0) & (df["age"] <= 100)]
```

This helps identify and handle values outside the expected range.

### Benefits

* Detects invalid values
* Helps identify data-entry errors
* Controls unexpected values
* Improves data quality

---

## 1.5 `isin()`

The `isin()` function checks whether values belong to a specified list of values.

### Example

```python
df[df["gender"].isin(["Male", "Female"])]
```

This returns rows where the `gender` value is either `Male` or `Female`.

### Common Use

`isin()` is particularly useful when filtering a dataset based on **multiple acceptable values**.

---

# 2. Saving DataFrames After Cleaning

After cleaning a dataset, the processed DataFrame can be saved for future analysis.

### Save DataFrame as CSV

```python
df.to_csv("cleaned_data.csv", index=False)
```

### Why Save the Cleaned Data?

* Reuse the processed dataset
* Avoid repeating cleaning operations
* Perform further analysis
* Prepare data for Machine Learning
* Maintain a clean version of the original dataset

---

# 3. Statistical Concepts

Understanding basic statistics is important in Data Science and Machine Learning because statistical methods help us **analyze data, identify patterns, test assumptions, and make informed decisions**.

---

## 3.1 Chi-Square Contingency Test

The **Chi-Square Contingency Test** is a statistical test used to determine whether there is a significant association between **two categorical variables**.

### Example

We may want to determine whether:

* Gender and product preference are related
* Education level and employment status are related
* Customer type and purchase category are related

The test compares:

* **Observed Values** → Values actually present in the dataset
* **Expected Values** → Values expected if there were no association between the variables

### Python Example

```python
from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(contingency_table)
```

The function returns:

| Value      | Meaning              |
| ---------- | -------------------- |
| `chi2`     | Chi-Square statistic |
| `p`        | p-value              |
| `dof`      | Degrees of freedom   |
| `expected` | Expected frequencies |

### Interpretation

A commonly used significance level is:

```text
α = 0.05
```

If:

```text
p < 0.05
```

we generally **reject the null hypothesis** and conclude that there is statistically significant evidence of an association.

If:

```text
p >= 0.05
```

we generally **fail to reject the null hypothesis**.

> The Chi-Square test indicates an association between categorical variables; it does not prove causation.

---

## 3.2 Degrees of Freedom

**Degrees of Freedom (DoF)** represent the number of independent values that are free to vary in a statistical calculation.

For a Chi-Square contingency table:

```text
Degrees of Freedom = (Rows - 1) × (Columns - 1)
```

### Example

For a table with 3 rows and 4 columns:

```text
DoF = (3 - 1) × (4 - 1)
    = 2 × 3
    = 6
```

Degrees of freedom are used when determining the statistical significance of a Chi-Square statistic.

---

# 4. Missing Data

**Missing Data** refers to values that are absent or unavailable in a dataset.

### Example

| Name | Age | Income |
| ---- | --: | -----: |
| Ram  |  22 |  30000 |
| Hari | NaN |  40000 |
| Sita |  25 |    NaN |

Here, `NaN` represents missing values.

Missing data can occur in:

* Numerical columns
* Categorical columns
* Text data
* Time-series data

---

## 4.1 Reasons for Missing Data

Missing values can occur for several reasons:

### Data Entry Errors

A value may accidentally be left blank during data entry.

### User Did Not Provide Information

A person may choose not to provide an answer.

### System Errors

Technical problems may prevent information from being stored correctly.

### Data Collection Problems

The required information may not have been collected.

### Information Was Unavailable

The required information may not have been known or available during data collection.

---

## 4.2 Implications of Missing Data

Missing data can negatively affect data analysis and Machine Learning.

Potential implications include:

* Reduced dataset size
* Biased analysis
* Incorrect statistical conclusions
* Loss of important information
* Reduced model performance
* Distorted relationships between variables

Therefore, missing data should be **properly investigated and handled** rather than automatically removed.

---

# 5. Z-Score

A **Z-Score** indicates how far a value is from the mean in terms of **standard deviations**.

### Formula

```text
Z = (X - μ) / σ
```

Where:

* `X` = Observed value
* `μ` = Mean
* `σ` = Standard deviation

### Interpretation

**Z = 0**
The value is exactly at the mean.

**Positive Z-Score**
The value is above the mean.

**Negative Z-Score**
The value is below the mean.

A large absolute Z-score can indicate an unusual observation and can be useful for **outlier detection**.

---

# 6. Handling Missing Data

There are several approaches for handling missing values.

## 6.1 Listwise Deletion

**Listwise Deletion** removes an entire row if it contains missing data.

### Example

If a row contains:

```text
Name = Ram
Age = NaN
Income = 30000
```

the entire row may be removed.

### Advantages

* Simple to implement
* Easy to understand

### Disadvantages

* Can significantly reduce the dataset size
* May introduce bias if missingness is not random

---

## 6.2 Pairwise Deletion

**Pairwise Deletion** uses all available values for each specific statistical calculation.

Instead of removing an entire row from every calculation, available values are used whenever possible.

### Advantages

* Preserves more available information
* Can use more observations for individual calculations

### Disadvantages

* Different calculations may use different subsets of observations
* Results can become less consistent

---

## 6.3 Single Imputation Techniques

**Single Imputation** replaces each missing value with one estimated or observed value.

Common techniques include:

| Technique                     | Description                                                                |
| ----------------------------- | -------------------------------------------------------------------------- |
| **Mean Imputation**           | Replaces missing numerical values with the mean                            |
| **Median Imputation**         | Replaces missing numerical values with the median                          |
| **Mode Imputation**           | Replaces missing categorical values with the most frequent value           |
| **Constant Value Imputation** | Replaces missing values with a predefined value such as `0` or `"Unknown"` |
| **Forward Fill**              | Uses the previous available value                                          |
| **Backward Fill**             | Uses the next available value                                              |
| **Hot Deck Imputation**       | Uses a value from a similar observed record                                |
| **Cold Deck Imputation**      | Uses a value from another dataset or reference source                      |
| **Random Imputation**         | Randomly selects an observed value from the same variable                  |
| **Regression Imputation**     | Uses a regression model to estimate the missing value                      |
| **Interpolation**             | Estimates missing values using surrounding observations                    |

The appropriate technique depends on the **data type, distribution, missing-data pattern, and purpose of the analysis**.

---

# 7. Understanding of Machine Learning

Data cleaning is an essential part of the Machine Learning workflow.

A simplified Machine Learning workflow can be represented as:

```text
Raw Data
    ↓
Data Cleaning
    ↓
Handle Missing Values
    ↓
Handle Incorrect Data
    ↓
Outlier Detection
    ↓
Data Transformation
    ↓
Exploratory Data Analysis
    ↓
Feature Engineering
    ↓
Model Training
    ↓
Model Evaluation
```
>> Simplier version
```Raw Dataset
     ↓
Initial Data Inspection
     ↓
EDA (Explore & Understand)
     ↓
Data Cleaning
     ↓
EDA Again (Check the cleaned data)
     ↓
Feature Engineering
     ↓
Data Preprocessing
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Evaluation
```
This shows that **Machine Learning does not begin directly with model training**.

Before training a model, the data needs to be understood, cleaned, and prepared properly.

### Key Understanding

> **Better data preparation → Better analysis → Better insights → Better Machine Learning models**

