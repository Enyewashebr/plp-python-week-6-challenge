# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# ---------------------------
# 1. NumPy: Create an array and calculate the mean
# ---------------------------
array = np.arange(1, 11)  # Numbers from 1 to 10
mean_value = np.mean(array)
print("NumPy Array:", array)
print("Mean of the array:", mean_value)

# ---------------------------
# 2. Pandas: Load a small dataset and display summary statistics
# ---------------------------
data = {
    "Name": ["Enyew", "Allexiander", "Alemayehu", "Abebe"],
    "Age": [25, 30, 22, 28],
    "Grade": [67, 90, 45, 80]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())

# ---------------------------
# 3. Requests: Fetch data from a public API
# ---------------------------
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    bitcoin_data = response.json()
    print("\nCurrent Bitcoin Price (USD):", bitcoin_data['bpi']['USD']['rate'])
else:
    print("\nFailed to fetch API data.")

# ---------------------------
# 4. Matplotlib: Plot a simple line graph
# ---------------------------
numbers = [1, 2, 3, 4, 5]
plt.plot(numbers, [n**2 for n in numbers], marker='o', color='blue')
plt.title("Simple Line Graph: n vs n^2")
plt.xlabel("n")
plt.ylabel("n squared")
plt.grid(True)
plt.show()
