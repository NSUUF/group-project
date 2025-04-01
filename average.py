import pandas as pd 

dataSet= pd.read_csv('vgsales.csv') 

print("\n Average Global Sales Of All Games")

Global_Sales = dataSet["Global_Sales"]
total_games = (len(dataSet))
Average_Sales = ((Global_Sales.sum())/total_games)

print(Average_Sales)



