import csv
import pandas as pd
import matplotlib.pyplot as plt


data = [
    ["Date", "Product", "Quantity sold", "Revenue ($)"],
    ["2023-01-01", "Widget A", 100, 1500],
    ["2023-01-02", "Widget B", 200, 3000],
    ["2023-01-03", "Widget C", 150, 2250],
    ["2023-01-04", "Widget D", 300, 4500]
]

with open('sales_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
with open('sales_summary.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV file created successfully.")

df = pd.read_csv('sales_data.csv')
print(df)
print(df["Revenue ($)"].sum())
max_sold=df["Quantity sold"].max()
print(f"Maximum quantity sold in a day: {max_sold}")
df2=df[df["Quantity sold"] == max_sold]
print(df2["Product"])


heighest_sales=df["Revenue ($)"].max()
print(f"Highest sales revenue in a day: {heighest_sales}")

