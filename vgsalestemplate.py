
#template for the menu, everyone can add the code for their questions to each function

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/csmwsout/Downloads/vgsales.csv")

# placeholder functions for each team members question
def question_1():
    df_clean = df.dropna(subset=["Publisher", "Global_Sales"])

    top_publishers = (
        df_clean.groupby("Publisher")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    #hue for color palette
    top_publishers["Colour"] = top_publishers["Publisher"]

    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=top_publishers,
        x="Global_Sales",
        y="Publisher",
        hue="Colour", #avoids hue warning
        palette="viridis",
        legend=False
    )
    plt.title("Top 15 Publishers by Global Sales")
    plt.xlabel("Global Sales (millions)")
    plt.ylabel("Publisher")
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

def question_2():  
    df_clean = df.dropna(subset=["Publisher", "NA_Sales", "EU_Sales", "JP_Sales"])
    regions = ["NA_Sales", "EU_Sales", "JP_Sales"]

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for i, region in enumerate(regions):
        region_sales = (
            df_clean.groupby("Publisher")[region]
            .sum()
            .sort_values(ascending=False)
            .head(10) #chooses top 10
        )

        axes[i].pie(
            region_sales,
            labels=region_sales.index,
            autopct="%1.1f%%",
            startangle=140
        )
        axes[i].set_title(f"Top 10 Publishers - {region.replace('_', ' ')}")

    plt.tight_layout()
    plt.show()

def question_3():
    pass

def question_4():
    pass

def question_5():
    pass    

def question_6():
    pass

def question_7():
    pass

def main_menu():
    while True:
        print("\n==== Video Game Analysis ====")
        print("1. Question 1: [Brief Description Here]")
        print("2. Question 2: [Brief Description Here]")
        print("3. Question 3: [Brief Description Here]")
        print("4. Question 4: [Brief Description Here]")
        print("5. Question 5: [Brief Description Here]")
        print("6. Question 6: [Brief Description Here]")
        print("7. Question 7: [Brief Description Here]")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            question_1()
        elif choice == "2":
            question_2()
        elif choice == "3":
            question_3()
        elif choice == "4":
            question_4()
        elif choice == "5":
            question_5()
        elif choice == "6":
            question_6()
        elif choice == "7":
            question_7()
        elif choice == "8":
            print("Exiting...")
            sys.exit()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()