import random

def main():
    
    while True:
        try:
            difficulty_level = int(input("Please choose a difficulty level from 1 to 3: "))
            if difficulty_level not in [1, 2, 3]:
                print("Error")
                continue
            else:
                break
        except:
            print("Please enter a valid number")

    while True:
        try:
            number_of_questions = int(input("Please enter the number of questions from 3 to 10: "))
            if number_of_questions not in [3, 4, 5, 6, 7, 8, 9, 10]:
                print("Error")
                continue
            else:
                break
        except:
            print("Please enter a valid number")

main()