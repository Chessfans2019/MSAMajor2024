#create a program to track the payments of a vending machine selling snacks for 50 cents
#prompts user to enter coin amount; accepts 1, 5, 10, and 25 cents
#program should ignore any input that is not a valid input and reprompt the user to input a coin
#process the input and display the updated amount due
#once the user has inputted at least 50 cents, output how many cents in change the user is owed
def main():
    due = 50
    while due > 0:
        try:
            print(f"Please pay {due} in coins")
            payment = input("Please enter you coin payment: ")
            if payment in ["1", "5", "10", "25"]:
                due = due - int(payment)
            else:
                print("Error: please enter a correct coin amount")
                continue
        except:
            print("Error: please enter a real number")
            continue
    
    if due <= 0:
        print(f"You are owed {abs(due)} cents")

main()
