import random

def main():
    
    #print a random number between 1 and 10
    print("Random number: 1 - 10")
    random_value = random.randint(1, 10)
    print(f"Random value: {random_value}")

    #generate 10 random numbers between 1 and 10
    print("\nRandom 10 numbers: 1 - 10\n------------")
    for i in range(10):
        print(f"Random number {i + 1}: {random.randint(1, 10)}")

    #choose a random value from a list of values
    print("\nChoose random value from list\n------------")
    random_list = [1, 2, 5, 7, 10]
    random_index = random.randint(0, len(random_list) - 1)
    print(f"Random index: {random_index}")
    print(f"Random list value: {random_list[random_index]}")

    #ask a user for the start and stop values to generate a random number between
    #ask user how many random numbers to generate, and then generate that many random numbers
    print("\nUser generated random numbers\n------------")
    start_value = int(input("Enter start value: "))
    stop_value = int(input("Enter stop value: "))
    number_of_random_values = int(input("How many random numbers do you want? "))

    for i in range(number_of_random_values):
        print(f"Random value {i + 1}: {random.randint(start_value, stop_value)}")

main()