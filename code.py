#Code1:

import pandas as pd
df_csv=pd.read_csv("C:/Users/Sohel's PC/Desktop/DSML_Practical/Datasets(1)/Datasets/Titanic.csv")
df_csv.head()
#selecting
print(df_csv['Age'])  # Selects the Age column
print(df_csv[['Age', 'Fare']])  # Selects Age and Fare columns
print(df_csv[df_csv['Age'] > 30])  # Rows where Age > 30

#indexing
# printing 4th row
print(df_csv.iloc[4])
print("______________________________\n\n\n")
# printing element at 1st row and 4th column
print(df_csv.iloc[1,4])
print("______________________________\n\n\n")
# Select a specific row by label
print(df_csv.loc[0])  # Row with index 0
print("______________________________\n\n\n")
# Select a specific value by row and column labels
print(df_csv.loc[1, 'Sex'])  # Row 1, Column 'City'
print("______________________________\n\n\n")
print(df_csv.loc[0:7])
print("______________________________\n\n\n")
print(df_csv.loc[0:7,"PassengerId":"Sex"])
print(df_csv.loc[3,"Age"])
print("______________________________\n\n\n")
print(df_csv.iloc[3:6])
print("______________________________\n\n\n")
print(df_csv.loc[3:6])

#To sort by a column, we can use the sort_values() method:
df_csv_sorted = df_csv.sort_values("Age")  # Sort by Age in Ascending order
print(df_csv_sorted)

df_csv.describe()  # Returns count, mean, std, min, 25%, 50%, 75%, max for numerical columns

df_csv.dtypes  # Returns the data type of each column

#Theory Questions:
"""
1. Basic Concepts
Q: What is the difference between loc and iloc in pandas?
A:

loc: Selects rows and columns by label (name or index).
iloc: Selects rows and columns by position (integer indices).


Q: How do you read a CSV file into a pandas DataFrame?
A: Use pd.read_csv()

Q: What are some common data formats supported by pandas for reading and writing?
A:
CSV: pd.read_csv()
Excel: pd.read_excel()
JSON: pd.read_json()
SQL: pd.read_sql()
Parquet: pd.read_parquet()

Q: What is the purpose of using .head() or .tail() methods in pandas?
A:
.head(): Displays the first 5 rows of the DataFrame (or a specified number).
.tail(): Displays the last 5 rows.

---------------------------------------------------------------------------------------------------------------------------------------------------------
2. Data Selection and Indexing
Q: How would you select a single row by its label in a DataFrame?
A: Use the loc method:
row = data.loc['row_label']


Q: How can you access specific columns or a range of columns in pandas?
A:

Specific column: data['column_name'] or data.column_name
Range of columns: data.loc[:, 'col1':'col3']


Q: Explain how boolean indexing works in pandas. Provide an example.
A: Filters rows based on a condition.
python
Copy code
filtered_data = data[data['Age'] > 25]  # Rows where Age > 25


Q: How do at and iat differ from loc and iloc?
A:
at/iat: Faster scalar access for single elements.
loc/iloc: More versatile for accessing ranges or subsets.

Example:
data.at[0, 'Name']  # Fast access by label
data.iat[0, 0]      # Fast access by position

---------------------------------------------------------------------------------------------------------------------------------------------------------

3. Data Sorting
Q: How do you sort a DataFrame by a specific column in ascending and descending order?
A: Use the sort_values method:

python
Copy code
data.sort_values('Age', ascending=True)  # Ascending
data.sort_values('Age', ascending=False)  # Descending
Q: Can you sort a DataFrame by multiple columns? If so, how?
A: Yes, by passing a list of column names:

python
Copy code
data.sort_values(['City', 'Age'], ascending=[True, False])
4. Data Description and Types
Q: What does the .describe() method in pandas do?
A: Provides summary statistics for numerical columns (e.g., mean, min, max, count).

python
Copy code
data.describe()
Q: How do you check the data types of each column in a DataFrame?
A: Use the dtypes attribute:

python
Copy code
print(data.dtypes)
Q: If you find incorrect data types in a column, how can you fix them?
A: Use pd.to_numeric() or astype() for conversion:

python
Copy code
data['column_name'] = pd.to_numeric(data['column_name'], errors='coerce')  # Convert to numeric
data['column_name'] = data['column_name'].astype('int')  # Convert to integer
5. Indexing Techniques
Q: How do you set a specific column as the index of a DataFrame?
A: Use set_index:

python
Copy code
data.set_index('column_name', inplace=True)
Q: What happens when you reset the index of a DataFrame?
A: The index is converted back to a regular column:

python
Copy code
data.reset_index(inplace=True)
Q: What is the difference between positional indexing and label-based indexing?
A:

Positional (iloc): Uses integer indices.
Label-based (loc): Uses labels or names.
6. Practical Applications
Q: How can you filter rows based on multiple conditions?
A: Use logical operators:

python
Copy code
filtered = data[(data['Age'] > 25) & (data['City'] == 'New York')]
Q: What is the difference between selecting a column with data['column_name'] and data[['column_name']]?
A:

data['column_name']: Returns a Series.
data[['column_name']]: Returns a DataFrame.
Q: How would you slice a DataFrame to select rows from index 3 to 7 and columns 'A' to 'C'?
A:

python
Copy code
data.loc[3:7, 'A':'C']
7. Error Handling
Q: What error might occur if you try to access a non-existent column using data.loc or data.iloc?
A:

KeyError for loc if the label doesn't exist.
IndexError for iloc if the position is out of range.
Q: How can you handle missing or null values in a DataFrame?
A: Use dropna() to remove them or fillna() to replace them:

python
Copy code
data.dropna()  # Remove rows with missing values
data.fillna(0)  # Replace missing values with 0
8. Optimization and Best Practices
Q: When would you use at/iat over loc/iloc?
A: When accessing or modifying a single value for performance optimization.

Q: What are the advantages of pandas' indexing operations over traditional Python data structures?
A:

Easier to work with structured data.
Efficient memory usage and performance.
Built-in functionality for filtering, aggregation, and manipulation.
9. Advanced Concepts
Q: How can you sort a DataFrame by the index instead of columns?
A: Use the sort_index method:

python
Copy code
data.sort_index()
Q: Explain the difference between a pandas Series and a DataFrame.
A:

Series: 1-dimensional labeled array.
DataFrame: 2-dimensional labeled data structure (table).
"""
