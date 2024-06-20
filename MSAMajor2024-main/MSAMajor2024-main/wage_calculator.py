#write a program called that accepts user input from the keyboard for the hours worked and hourly wage
#the program calculates the total wages for the year, assuming the person works 350 days per year and 12% taxes are deducted from the wages.

#write a function to get a positive number from the user
def get_positive_hours_worked():
    #ask user to enter a positive number, will reprompt them if positive number not entered
    hours_worked = 0
    while(True):
        try:
            hours_worked = input("Enter your hours worked per day: ")
            hours_worked = float(hours_worked)
            #checks if hours worked is greater than zero. If not, reprompt the user
            if hours_worked <= 0 or hours_worked >= 24:
                print("Error: please enter a number greater than 0 and less than 24")
                continue
            else:
                break
        except:
            print("Error: please enter a number")

    return hours_worked

def get_positive_wage():

    hourly_wage = 0
    while(True):
        try:
            hourly_wage = input("Enter your wage in dollars per hour: ")
            hourly_wage = float(hourly_wage)
            break
        except:
            print("Error: please enter a number")
    return hourly_wage             

hours_worked = get_positive_hours_worked()
hourly_wage = get_positive_wage()

total_hours = hours_worked * 350
total_wage = hourly_wage * total_hours
tax_amount = total_wage * 0.12
wage_after_tax = total_wage - tax_amount

print(f"Hours worked: {total_hours:.2f} hours")
print(f"Hourly wage: ${hourly_wage:.2f}")
print(f"Wages before tax: ${total_wage:.2f}")
print(f"Tax amount: ${tax_amount}")
print(f"Wage after tax: ${wage_after_tax}")