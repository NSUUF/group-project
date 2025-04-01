import pandas as pd 
import matplotlib.pyplot as plt 

dataSet= pd.read_csv('vgsales.csv')


OverallGames= dataSet["Genre"].value_counts()
Games= dataSet["Genre"]
games = ["sports", "Plaform", "Racing", "Role-Playing", "Puzzle", "Misc", "Shooter", "Simulation", "Action", "Fighting", "Adventure", "Strategy"]
myexplode = [0,0,0,0.3,0,0,0,0,0,0,0,0,]
mycolors = ["Red", "black", "blue", "purple", "pink", "grey", "green", "yellow", "orange", "hotpink", "lightgreen", "indigo"]
plt.pie(OverallGames, labels = games, explode = myexplode, shadow = True, colors= mycolors)
plt.show()
