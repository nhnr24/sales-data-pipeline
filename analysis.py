import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_sales.csv")

# Graph 1: Revenue by Category
df.groupby("category")["revenue"].sum().plot(kind="bar")
plt.title("Revenue by Category")
plt.ylabel("Revenue")
plt.show()

# Graph 2: Revenue by Region
df.groupby("region")["revenue"].sum().plot(kind="bar")
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.show()