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


# Task 3: Visualization
sns.set(style="whitegrid")

# Line Chart: Revenue over Time
plt.figure(figsize=(8, 4))
sns.lineplot(x="Date", y="Revenue ($)", data=df, marker="o")
plt.title("📈 Revenue Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Bar Chart: Avg Revenue per Product
plt.figure(figsize=(6, 4))
grouped.plot(kind="bar", color='skyblue')
plt.title("💰 Average Revenue by Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.show()



# Histogram: Quantity Sold Distribution
plt.figure(figsize=(6, 4))
sns.histplot(df["Quantity Sold"], bins=5, color="orange")
plt.title("📊 Quantity Sold Distribution")
plt.tight_layout()
plt.show()

# Scatter Plot: Quantity vs Revenue
plt.figure(figsize=(6, 4))
sns.scatterplot(x="Quantity Sold", y="Revenue ($)", hue="Product", data=df)
plt.title("🔵 Quantity Sold vs Revenue")
plt.tight_layout()
plt.show()

# Save summary to TXT
summary = df.describe().to_string()
with open("sales_summary.txt", "w") as f:
    f.write("Sales Data Summary:\n\n")
    f.write(summary)
print("\n📁 Summary saved to 'sales_summary.txt'")
