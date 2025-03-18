import pandas as pd 

data = pd.read_csv('vgsales.csv')

print('\n ----- Total global sales by genre -----')


unique_genres = data["Genre"].unique()

print('\nList of genres: ')
print(f"{unique_genres}")

chosenGenre = input('\nPlease enter a genre from the list above: ')


if chosenGenre in unique_genres:
    genre_data = data[data["Genre"] == chosenGenre]

    total_sales = genre_data[['Global_Sales']].sum()
    for x in total_sales:
        print(f"The total global sales for {chosenGenre} is {x}")


else:
    print('\nInvalid input.')
    print(f"\n{unique_genres}")

    chosenGenre = input('\nPlease enter a genre from the list above: ')
    
    if chosenGenre in unique_genres:
     genre_data = data[data["Genre"] == chosenGenre]
 
    total_sales = genre_data[['Global_Sales']].sum()
    for x in total_sales:
        print(f"The total global sales for {chosenGenre} is {x}")