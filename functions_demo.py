#create a function to add 2 numbers
#input: (int)number_1, (int)number_2
#output: (int)total
def add_numbers(number_1, number_2):
    total = number_1 + number_2
    c = 7
    return total

def main():
    a = 5
    b = 4
    c = 3

    #call the add_numbers function and assign the returned value to answer
    answer = add_numbers(a, b)
    print(f"P{a} + {b} = {answer}")
    print(f"Variable c = {c}")

main()