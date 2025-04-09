import pandas as pd

def get_data():
    try:
        df = pd.read_csv("vgsales.csv")
    except FileNotFoundError:
        print("File not found")
        exit()

   
    df = df.dropna(subset=["Genre", "Platform"]) #drop rows missing stuff we need
    return df

