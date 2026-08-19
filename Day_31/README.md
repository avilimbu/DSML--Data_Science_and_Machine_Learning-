# Day 31 — Data Visualization with Pandas

# 1. Visualization in Pandas

**Pandas** is a powerful open-source Python library used for data analysis and manipulation.

It is particularly well-suited for working with **labeled data**, such as tables containing rows and columns.

Pandas also provides built-in functions that allow us to create different types of graphs directly from our data.

---

# 2. Pandas Visualization

Pandas provides the `plot()` function for creating visualizations directly from a DataFrame or Series.

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Score": [80, 65, 90, 75]
})

df.plot()
```

The `plot()` function can be used to create different types of charts by specifying the appropriate `kind`.

---

# 3. Line Plot

A **line plot** is useful for showing trends and changes in values.

```python
df.plot(
    x="Name",
    y="Score",
    kind="line"
)
```

A line connects the data points, making changes in the values easier to observe.

---

# 4. Bar Plot

A **bar plot** is useful for comparing values between different categories.

```python
df.plot(
    x="Name",
    y="Score",
    kind="bar"
)
```

Each category is represented by a separate bar.

---

# 5. Histogram

A **histogram** is used to visualize the distribution of numerical data.

```python
df["Score"].plot(
    kind="hist"
)
```

A histogram divides values into intervals and shows how frequently values occur within those intervals.

---

# 6. Box Plot

A **box plot** is used to visualize the distribution and spread of numerical data.

It can also help identify potential extreme values.

```python
df["Score"].plot(
    kind="box"
)
```

Box plots are particularly useful when comparing the distribution of a numerical variable across different categories.

---

# 7. Scatter Plot

A **scatter plot** displays individual data points based on two variables.

```python
df.plot(
    x="Age",
    y="Fare",
    kind="scatter"
)
```

Scatter plots are useful for observing relationships and patterns between numerical variables.

---

# 8. Titanic Dataset Visualization

The Day 31 practice uses the **Titanic dataset** to apply visualization concepts.

The practice questions focus on visualizing passenger information such as:

* Fare
* Passenger Class
* Numerical variable correlations
* Survival
* Siblings / spouses (`SibSp`)
* Age
* Embarkation Port (`Embarked`)

---

# 9. Box Plot of Fare by Passenger Class

Create a box plot to compare the distribution of `Fare` across different `Pclass` values.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(
    data=titanic_df,
    x="Pclass",
    y="Fare"
)

plt.title("Fare by Passenger Class")
plt.show()
```

This visualization allows us to compare the distribution of passenger fares across passenger classes.

---

# 10. Correlation Heatmap

A **heatmap** can be used to visualize correlations between numerical variables.

```python
import seaborn as sns
import matplotlib.pyplot as plt

correlation = titanic_df.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")
plt.show()
```

The heatmap represents the correlation values using different visual intensities.

The Day 31 practice specifically asks for a heatmap showing correlations between numerical variables.

---

# 11. Survival Count with and without SibSp

`SibSp` represents the number of siblings or spouses associated with a passenger.

The practice asks us to compare the survival count of passengers with and without siblings/spouses.

```python
import seaborn as sns
import matplotlib.pyplot as plt

titanic_df["Has_SibSp"] = titanic_df["SibSp"] > 0

sns.countplot(
    data=titanic_df,
    x="Has_SibSp",
    hue="Survived"
)

plt.title("Survival Count with and without SibSp")
plt.show()
```

The boolean column separates passengers into:

```text
False → No siblings/spouses
True  → Has siblings/spouses
```

---

# 12. Violin Plot of Age vs Survival

A **violin plot** combines information about the distribution and density of numerical data across categories.

The Day 31 practice asks for a violin plot comparing `Age` against `Survived`.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.violinplot(
    data=titanic_df,
    x="Survived",
    y="Age"
)

plt.title("Age vs Survival")
plt.show()
```

This visualization helps compare the distribution of passenger ages between survival categories.

---

# 13. Embarkation Port Count Plot

`Embarked` represents the embarkation port of a passenger.

A **count plot** can be used to visualize the number of passengers from each embarkation port.

The Day 31 practice specifically asks to visualize the `Embarked` distribution using a count plot.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(
    data=titanic_df,
    x="Embarked"
)

plt.title("Embarkation Port Distribution")
plt.show()
```

This allows us to compare the number of passengers associated with each embarkation port.

---

# 14. Important Visualization Functions

### Pandas

```python
df.plot()
```

### Seaborn

```python
sns.boxplot()
sns.heatmap()
sns.countplot()
sns.violinplot()
```

### Matplotlib

```python
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()
```

---

# 15. Visualization Workflow

A basic visualization workflow can be represented as:

```text
Load Dataset
     ↓
Inspect Dataset
     ↓
Select Required Columns
     ↓
Clean Data if Required
     ↓
Choose Appropriate Visualization
     ↓
Create Plot
     ↓
Add Title / Labels
     ↓
Display Visualization
     ↓
Analyze the Result
```

---

# 16. Choosing the Right Visualization

| Visualization | Common Purpose                                              |
| ------------- | ----------------------------------------------------------- |
| Line Plot     | Show trends and changes                                     |
| Bar Plot      | Compare categories                                          |
| Histogram     | Understand numerical distribution                           |
| Box Plot      | Compare distributions and identify potential extreme values |
| Scatter Plot  | Observe relationships between numerical variables           |
| Heatmap       | Visualize correlation values                                |
| Count Plot    | Compare category counts                                     |
| Violin Plot   | Compare numerical distributions across categories           |