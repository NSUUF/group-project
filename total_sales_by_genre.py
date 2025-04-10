import pandas as pd #import pandas for data extraction

data = pd.read_csv('vgsales.csv') #reads and loads video game sales file content

print('\n ----- Total global sales by genre -----')


unique_genres = data["Genre"].unique() #reads genre column and extracts unique genres

print('\nList of genres: ')
print(f"{unique_genres}") #lists and prints unique genres

checker = True #boolean checker set to true to conduct a verification for user input
while checker: #while loop used (if checker is true) to repeatedly check and execute code
    chosenGenre = input('\nPlease enter a genre from the list above: ')  # takes in user input

    if chosenGenre in unique_genres:
        genre_data = data[data["Genre"] == chosenGenre]  # checks user input against matching words in the genre column

        total_sales = genre_data['Global_Sales'].sum()  # extracts global sales column and sums all sales generated by matching chosen genre
        print(f"The total global sales for {chosenGenre} is {total_sales}")
        checker = False # Sets checker to false, exiting the loop
    else:
        print("\nInvalid input.") #this line is executed if user input doesn't match
