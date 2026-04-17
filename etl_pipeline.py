import pandas as pd

df = pd.read_csv("sales.csv")

df = df.dropna()
df["revenue"] = df["price"] * df["quantity"]
df["date"] = pd.to_datetime(df["date"])
df["category"] = df["category"].str.lower()

df.to_csv("cleaned_sales.csv", index=False)

print("ETL DONE")