import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('vgsales.csv')



genres = data['Genre']
sales = data['Global_Sales']



plt.bar(genres, sales)
plt.title('Sales By Genre')
plt.xlabel('Genre')
plt.ylabel('Sales')
plt.bar(genres, sales, color = "hotpink")
plt.show()
