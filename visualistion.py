import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('vgsales.csv')

region_sales={
    "North America": data["NA_Sales"].sum(),
    "Europe" :data["EU_Sales"].sum(),
    "Japan" : data["JP_Sales"].sum(),
    "Other" : data["Other_Sales"].sum()
}

plt.figure(figsize= (8,5))
plt.bar(region_sales.keys(), region_sales.values(),color=['red', 'blue', 'green', 'orange'])

plt.xlabel("Region")
plt.ylabel("Total Sales (in millions)")
plt.title("Region with the Highest Video Game Sales")

plt.show()