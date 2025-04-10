import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('vgsales.csv')

data = data[pd.to_numeric(data['Year'], errors= 'coerce').notnull()]
data['Year'] = data['Year'].astype(int)

genres = ["Sports" , "Platform", "Racing" , "Role-Playing" , "Puzzle" , "Misc" ,
          "Shooter" , "Simulation" , "Action" , "Fighting" , "Adventure" , "Strategy"]     
data = data[data["Genre"].isin(genres)]

sales_by_genre = data.groupby(["Year" , "Genre"]) ["Global_Sales"].sum().unstack()

plt.figure(figsize=(14,7))

for genre in genres:
    if genre in sales_by_genre.columns:
        plt.plot(sales_by_genre.index , sales_by_genre[genre] ,label=genre)



plt.xlabel("Year")
plt.ylabel("Global Sales (in millions)")
plt.title("Sales Growth of Video Game Genres Over the Years")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()