# NumPy
NumPy is a lib used for working with arrays. 

* Python has lists, but they are slow to process, so we use arrays.
* NumPy aims to provide an array object 50x faster than Python lists.

`import numpy as np` -- np is an alias for numpy.

# Pandas
Is a lib on top of NumPy. 

* Provides DS (Data Structures) and operations for it.
* Import and analyze data easily.
* Fast and has good performance.
* Clean data: handle missing data, duplicates, and transform raw data for modeling.
* Use DataFrames to manage large datasets.
* EDA: explore relations between data.
* Integrate with other libs like scikit-learn and matplotlib for a smooth ML workflow.
* Deal with time data like forecasting and finance apps.

`import pandas as pd`

* A DataFrame is a 2-dimensional DS.
* A Pandas series is a column in a table.

## Functions

* `read_csv()`
```python
df = pd.read_csv('filepath')
```

* `df.head()`
Displays the first five rows.

* `df.tail()`
Displays the last five rows.

* `df.head(2)`
The first 2 rows.

* `df.info()`
Provides a summary of the DataFrame, including the number of rows and columns, column names, data types, and the count of non-null values in each column.

* `df.shape` returns a tuple representing the dimensions of the DataFrame in the format `(rows, columns)`.

* `df.describe()` generates summary statistics for numerical columns in the DataFrame, including count, mean, standard deviation, min, max, and quartiles (25%, 50%, 75%).

* `df['Name']` returns a pandas Series, containing values from the "Name" column.

* `df[['Name']]` returns a pandas DataFrame, containing the "Name" column but as a DataFrame.

* `df["Breed"].value_counts()` counts the occurrences of each unique value in the "Breed" column and returns a sorted list in descending order.
```python
df["Breed"].value_counts()
```

* `df.groupby('Color')['Height_cm'].mean()` groups the DataFrame by the "Color" column and calculates the average (mean) height for each color category.
```python
df.groupby('Color')['Height_cm'].mean()
```

# Data Cleaning

* Remove duplicates:
```python
df.drop_duplicates()
```

* Drop irrelevant data.

# Matplotlib
* Data visualization lib.
* Mostly uses pyplot.
```python
import matplotlib.pyplot as plt
```

# Scikit-learn
* Built on top of NumPy, SciPy, and Matplotlib.
