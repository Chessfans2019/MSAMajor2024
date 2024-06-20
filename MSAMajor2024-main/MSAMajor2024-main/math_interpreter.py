def main():
    
    while True:
        try:
            equation = str(input("Enter your equation: "))
            symbols = equation.split(" ")
            num1 = int(symbols[0])
            num2 = int(symbols[2])
            
            if len(equation) != 5:
                print("Please enter an equation with two numbers")
                continue
            
            if symbols[1] == "+":
                total = num1 + num2
            
            if symbols[1] == "-":
                total = num1 - num2
            
            if symbols[1] == "*":
                total = num1 * num2
            
            if symbols[1] == "/" and num2 != 0:
                total = num1 / num2
            
            if symbols[1] == "/" and num2 == 0:
                print("No solution")
            
            print(f"{total:.2f}")
            break
        
        except:
            print("Please enter a valid equation")
            continue

main()

while True:
    try:
        repeat = str(input("Do you want to go again? "))
        if repeat.lower() == "y":
            main()
        if repeat.lower() == "n":
            break
        else:
            print("Please enter yes or no")
    except:
        print("Please enter yes or no")