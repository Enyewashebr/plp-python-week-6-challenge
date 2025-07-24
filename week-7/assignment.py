import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create sample sales data
data = {
    'Date': ['2025-07-01', '2025-07-01', '2025-07-02', '2025-07-03', '2025-07-03', '2025-07-04'],
    'Product': ['Phone', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone'],
    'Quantity Sold': [10, 5, 8, 6, 7, 12],
    'Revenue ($)': [5000, 7000, 4000, 3000, 6800, 6000]
}

df = pd.DataFrame(data)

# Load the dataset
try:
    df = pd.read_csv("sales_data.csv")
    print("Loaded Dataset:\n", df.head())
except FileNotFoundError:
    print("File not found.")


print("\n Missing values:\n", df.isnull().sum())


# Task 2: Basic Stats
print("\n Descriptive Stats:\n", df.describe())

# Group by product and average revenue
grouped = df.groupby("Product")["Revenue ($)"].mean()
print("\n Avg Revenue per Product:\n", grouped)
