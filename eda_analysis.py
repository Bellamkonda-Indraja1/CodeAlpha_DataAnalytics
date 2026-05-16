import pandas as pd

# Load CSV file
df = pd.read_csv("books_data.csv")

# First 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Data types
print("\nDATA TYPES")
print(df.dtypes)

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Shape of dataset
print("\nDATASET SHAPE")
print(df.shape)

# Statistics
print("\nSTATISTICS")
print(df.describe(include='all'))