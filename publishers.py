import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("vgsales.csv")

#drop rows with missing values in Publisher or Global Sales
df = df.dropna(subset=["Publisher", "Global_Sales"])

#get total sales by publisher and take the top 15
top_publishers = (
    df.groupby("Publisher")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
    .reset_index()
)

top_publishers["Colour"] = top_publishers["Publisher"]


plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_publishers,
    x="Global_Sales",
    y="Publisher",
    hue="Colour",              
    palette="crest",
    legend=False           #avoids hue warning
)
plt.title("Top 15 Publishers by Global Sales")
plt.xlabel("Global Sales (millions)")
plt.ylabel("Publisher")
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()