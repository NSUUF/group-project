import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/south/Downloads/vgsales.csv")
df = df.dropna(subset=["Publisher", "NA_Sales", "EU_Sales", "JP_Sales"])

#get user input
valid_regions = ["NA_Sales", "EU_Sales", "JP_Sales"]
print("Choose a region from:", ", ".join(valid_regions))
region = input("Enter region exactly as shown: ")

if region not in valid_regions:
    print("Invalid region! Please enter one of:", valid_regions)
else:
    #group by publisher for specified region
    region_sales = (
        df.groupby("Publisher")[region]
        .sum()
        .sort_values(ascending=False)
        .head(10)  #top 10 publishers in that region
    )

    plt.figure(figsize=(8, 8))
    plt.pie(region_sales, labels=region_sales.index, autopct="%1.1f%%", startangle=140)
    plt.title(f"Top 10 Publishers by Proportion of {region}")
    plt.tight_layout()
    plt.show()