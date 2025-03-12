import pandas as pd #imports 

data = pd.read_csv('vgsales.csv')

unique_genres = data["Genre"].unique()

print(unique_genres)

chosenGenre = input('Please enter a genre from the list above: ')


if chosenGenre == data["K"]:
     
 
     total_sales = genre_data.sum
     print(total_sales)

# else:
 # print('Invalid input. Please enter a genre from the list above: ')