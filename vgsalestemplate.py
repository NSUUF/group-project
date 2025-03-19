
#template for the menu, everyone can add the code for their questions to each function

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vgsales.csv")

# placeholder functions for each team members question
def question_1():
    

def question_2():
    

def question_3():
    

def question_4():
    

def question_5():
    

def question_6():
    

def question_7():
    

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