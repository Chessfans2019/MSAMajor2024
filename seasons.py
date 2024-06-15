#function to return the season based on the month
#input: month number
#output: season name
def get_season_name(month_number):
    if month_number == 12 or month_number <= 2:
        return "Winter"
    elif month_number <= 5:
        return "Spring"
    elif month_number <= 8:
        return "Summer"
    elif month_number <= 11:
        return "Fall"
    
    return month_number

#create a decision structure to determine the season winter, spring, summer, fall based on the month
    #winter: 12, 1, 2; spring: 3, 4, 5; summer: 6, 7, 8; fall: 9, 10, 11
    #ask the user to enter the number of the month, then output the season based on the month
def main():
    while True:
        try:
            month = input("Enter a month: ")
            month = int(month)
            if month < 1 or month > 12:
                print("Error: please enter a number 1 - 12")
                continue
            else:
                break
        except:
            print("Error: please enter a real number")
            continue
    season_name = get_season_name(month)
    print(f"It is {season_name}")
    run_again = input("Do you want to run the program again? ")
    if run_again == "y" or run_again == "Y":
        main()
    else:
        exit()

main()
