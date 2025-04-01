import pandas as pd 
import matplotlib.pyplot as plt

dataSet= pd.read_csv('vgsales.csv')

All_Games = dataSet["Global_Sales"]

plt.pie(All_Games)
plt.show()