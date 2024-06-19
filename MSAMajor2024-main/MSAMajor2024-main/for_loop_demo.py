def main():
    #print integers between 0 and 10
    for number in range(11):
        print(number)

    #print integers between 5 and 10
    print("\n\n")
    for number in range(5, 11):
        print(number)

    #print even numbers between 0 and 10
    print ("\n\n")
    for number in range (0, 11, 2):
        print(number)

    #prompt the user for start and stop values and print the numbers between start and stop
    #get the start and stop values from the user and convert to an integer
    #use start and stop values in a for loop
    start_value = input("Please enter a number: ")
    start_value = int(start_value)
    stop_value = input("Please enter another number: ")
    stop_value = int(stop_value)
    for number in range(start_value, stop_value):
        print(number)

main()