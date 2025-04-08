import pandas as pd 
import matplotlib.pyplot as plt 

dataSet= pd.read_csv('vgsales.csv')


OverallGames= dataSet["Genre"].value_counts()
Games= dataSet["Genre"]
games = ["Action", "Sports", "Misc", "Role-Playing", "Shooter", "Adventure", "Racing", "Platform", "Simulation", "Fighting", "Strategy", "Puzzle"]
myexplode = [0,0,0,0.3,0,0,0,0,0,0,0,0,]
mycolors = ["Red", "lightblue", "blue", "purple", "pink", "grey", "green", "yellow", "orange", "hotpink", "lightgreen", "indigo"]
plt.pie(OverallGames, labels = games, explode = myexplode, shadow = True, colors= mycolors, autopct="%.2f%%")
plt.show()
