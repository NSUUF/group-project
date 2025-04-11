import pandas as pd
import matplotlib.pyplot as plt

# Question 1: Which region’s sales have the most impact on total sales on average?

data = pd.read_csv(r'C:\Uni Coursework\SEM 2\Computer Science Workshop\Individual Work\vgsales.csv')

data = data.dropna()

region_averages = data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].mean()

print("\nAverage sales per region (in millions):")
print(region_averages)

# Visualising the average sales for each region (excluding Global sales) in a bar chart
plt.figure(figsize=(10, 6)) 
region_averages[:-1].plot(kind='bar', color='skyblue') 
plt.title('Average Video Game Sales by Region') 
plt.xlabel('Region') 
plt.ylabel('Average Sales (in millions)')
plt.grid(True) 
plt.tight_layout() 
plt.show() 

# Calculating the percentage contribution of each region to Global Sales
total_avg_sales = region_averages['Global_Sales']
region_percentage_contribution = (region_averages[:-1] / total_avg_sales) * 100

# Displaying the percentage contribution of each region to global sales
print("\nPercentage contribution to global average sales:")
print(region_percentage_contribution.round(2))
