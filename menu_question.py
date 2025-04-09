import pandas as pd

def platform_sales_consistency():
    try:
        data = pd.read_csv("C:/Users/watta/Documents/repo group/group-project/vgsales.csv")
    except FileNotFoundError:
        print("vgsales.csv not found")
        return
    data = data.dropna(subset=["Platform", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])

   
    totals = data.groupby("Platform")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum() # calculates total regional sales per platform

 
    spread = totals.std(axis=1).sort_values()   # sees how spread out the sales are

    print("\nPlatform Sales Consistency (the lower the number the more balanced the platform is across regions):\n")
    for platform, value in spread.round(3).head(10).items():
        print(f"{platform}: {value}")

#def main():
    #while True:
        #print("\n menu")
        #print("1 - platform sales consistency")
        #print("q - Quit")

        #choice = input("Enter your choice: ").strip().lower()   # to see if it works

        #if choice == "1":
            #platform_sales_consistency()
        #elif choice == "q":
            #print("Exiting.")
            #break
        #else:
            #print("invalid input")

#if __name__ == "__main__":
    #main()

