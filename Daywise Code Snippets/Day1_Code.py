# Date: 11 Nov 2024
# Author: Lakhan Kumar
# Description: Program to understand the basic function of pandas library
#              1. Create DataFrame
#              2. Getting Basic Info about DataFrame

# importing pandas library
import pandas as pd

# 1. Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'HR'],
    'Salary': [50000, 60000, 55000, 52000, 58000]
}

df = pd.DataFrame(data)

# 2. Getting Basic Info about DataFrame
# Display the DataFrame
print("DataFrame:")
print(df)

# Display basic information (like column names, non-null counts, data types)
print("\nBasic Info:")
print(df.info())

# Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Display the first few rows of the DataFrame
print("\nFirst Few Rows:")
print(df.head())
