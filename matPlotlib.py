import matplotlib.pyplot as plt
import pandas as pd

data = {
    "name":["Enyew", "Allexiande", "Andargachew"],
    "age":[23,25,30]

}
df = pd.DataFrame(data)
plt.bar(df["name"],df["age"])
plt.xlabel("Name")
plt.ylabel("Age")
plt.title("name vs age plot")
plt.show()

