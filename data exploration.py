import pandas as pd

#Loading of the dataset
file_path = '/Users/macbookpro/Documents/ML Project 1/garments_worker_productivity.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

#Displaying the first few rows of the dataset
print(data.head())

#Displaying basic information
print(data.info())

# Getting statistical summary of numerical columns
print(data.describe())

# Identifying categorical and numerical columns
categorical_cols = data.select_dtypes(include=['object']).columns
numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns

print("Categorical Columns:", categorical_cols)
print("Numerical Columns:", numerical_cols)

# Checking for missing values
print(data.isnull().sum())
