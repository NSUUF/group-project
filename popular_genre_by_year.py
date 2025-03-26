import pandas as pd #import pandas for data extraction

data = pd.read_csv('vgsales.csv') #reads and loads video game sales file content

unique_years = data["Year"].dropna().unique() # extracts unique years, not including games that have 'NA' 
year = unique_years.astype(int) #converts year data into int so we can form comparisons
year.sort() #sort function to sort year data in order from lowest to highest

print('\nList of years: ')
print(f"{year}") 

chosenYear = input('\nPlease select a year from the list above to view the most popular genre that year: ')
chosenYear = int(chosenYear) #converts input from string to int so that year data and input data can be compared

if chosenYear in year:
    year_data = data[data["Year"]== chosenYear] #filters and finds user input match with 'Year'
    
   
    global_sales = year_data['Global_Sales'] 
    # max_globalsales = max(global_sales)

    # genre = year_data[year_data['Global_Sales']] == max_globalsales]['Genre'].values[0]
    # print(genre)
  
    print(f"\n Highest global sales for that year: {max(global_sales)}") #produces max value within the global sales column that meet the year condition
    
    #have to still find genre match and print that
else:
  print('\nInvalid input.')

  print(f"\n{year}")

  chosenYear = input('\nPlease select a year from the list above to view the most popular genre that year: ')
  chosenYear = int(chosenYear)

  if chosenYear in year:
      year_data = data[data["Year"]== chosenYear]
    
      global_sales = year_data['Global_Sales']
    
      print(f"\n{global_sales}")
      print(f"Highest global sales for year: {max(global_sales)}")

