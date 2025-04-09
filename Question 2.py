import pandas as pd
import matplotlib.pyplot as plt

# Question 2: How do FIFA games perform in EU vs JP, and globally?

data = pd.read_csv(r'C:\Uni Coursework\SEM 2\Computer Science Workshop\Individual Work\vgsales.csv')

data = data.dropna() #filter through data and drops any 'NA'

fifa_games = data[data['Name'].str.contains("FIFA", case=False)]

fifa_games = fifa_games.sort_values(by='Year')

print("\nFIFA games in the dataset:")
print(fifa_games[['Name', 'Year', 'EU_Sales', 'JP_Sales', 'Global_Sales']])

# EU vs JP sales in a Bar Chart
plt.figure(figsize=(12, 6))
plt.bar(fifa_games['Name'], fifa_games['EU_Sales'], label='EU Sales', color='green')
plt.bar(fifa_games['Name'], fifa_games['JP_Sales'], label='JP Sales', color='red', bottom=fifa_games['EU_Sales'])

plt.title('FIFA Game Sales: EU vs JP')
plt.xlabel('FIFA Title')
plt.ylabel('Sales (in millions)')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# Global sales of FIFA games on a plotted graph
plt.figure(figsize=(12, 6))
plt.plot(fifa_games['Year'], fifa_games['Global_Sales'], marker='o', color='blue', linestyle='--')
plt.title('Global Sales Trend of FIFA Games Over the Years')
plt.xlabel('Year')
plt.ylabel('Global Sales (in millions)')
plt.grid(True)
plt.tight_layout()
plt.show()

## The main reason for this EU dominance could be because football is more popular in Europe than Japan which could
## result in many more people buying games there than in Japan. 

## Another reason for EU dominance could be that EU has a much higher population than JP alone which could've had
## a big impact on the results.