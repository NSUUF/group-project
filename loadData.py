import pandas as pd

dataSet= pd.read_csv('vgsales.csv') #

print("\nRole Playing games by Percentage ")

RPGs = dataSet[dataSet["Genre"] == "Role-Playing"]
 
OverallGames = (len(dataSet))
RPGs = (len(RPGs))

RGPsPercentage =( RPGs/ OverallGames)*  100

print(f" Total games in the data set: {OverallGames}")
print(f"total number og role playing games: {RPGs}")
print(f"percentage of role playing games: {RGPsPercentage :.2f}%")




    