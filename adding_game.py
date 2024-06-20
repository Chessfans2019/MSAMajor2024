import random
    
def main():
    
    while True:
        try:
            difficulty_level = int(input("Please choose a difficulty level from 1 to 3: "))
            if difficulty_level not in [1, 2, 3]:
                print("Please enter a correct number")
                continue
            else:
                break
        except:
            print("Please enter a valid number")

    while True:
        try:
            number_of_questions = int(input("Please enter the number of questions from 3 to 10: "))
            if number_of_questions not in [3, 4, 5, 6, 7, 8, 9, 10]:
                print("Please enter a correct number")
                continue
            else:
                break
        except:
            print("Please enter a valid number")

    correct = 0
    wrong_total = 0
    if difficulty_level == 1:
        for i in range (number_of_questions):
            wrong = 0
            equation_numbers1 = random.randint(1,9)
            equation_numbers2 = random.randint(1,9)
            while True:
                try:
                    answer = int(input(f"{equation_numbers1} + {equation_numbers2} = "))
                    total = equation_numbers1 + equation_numbers2
                    if answer == total:
                        correct += 1
                        print("Correct!\n")
                        break
                    if answer != total:
                        wrong += 1
                        print("Wrong!\n")
                    if wrong == 3:
                        wrong_total += 1
                        print(f"Correct answer: {answer}\n")
                        if wrong_total == 3:
                            print(f"You got {correct} out of {correct + wrong}: {correct*100/(correct+wrong)}%")
                            exit()
                        else:
                            break
                except:
                    print("Please enter a valid answer\n")
                    continue
    
    if difficulty_level == 2:
        for i in range (number_of_questions):
            wrong = 0
            equation_numbers1 = random.randint(10,99)
            equation_numbers2 = random.randint(10,99)
            while True:
                try:
                    answer = int(input(f"{equation_numbers1} + {equation_numbers2} = "))
                    total = equation_numbers1 + equation_numbers2
                    if answer == total:
                        correct += 1
                        print("Correct!\n")
                        break
                    if answer != total:
                        wrong += 1
                        print("Wrong\n")
                    if wrong == 3:
                        wrong_total += 1
                        print(f"Correct answer: {answer}\n")
                        if wrong_total == 3:
                            print(f"You got {correct} out of {correct + wrong}: {correct*100/(correct+wrong)}%")
                            exit()
                        else:
                            break
                except:
                    print("Please enter a valid answer\n")
                    continue
    
    if difficulty_level == 3:
        for i in range (number_of_questions):
            wrong = 0
            equation_numbers1 = random.randint(100,999)
            equation_numbers2 = random.randint(100,999)
            while True:
                try:
                    answer = int(input(f"{equation_numbers1} + {equation_numbers2} = "))
                    total = equation_numbers1 + equation_numbers2
                    if answer == total:
                        correct += 1
                        print("Correct!\n")
                        break
                    if answer != total:
                        wrong += 1
                        print("Wrong\n")
                    if wrong == 3:
                        wrong_total += 1
                        print(f"Correct answer: {answer}\n")
                        if wrong_total == 3:
                            print(f"You got {correct} out of {correct + wrong}: {correct*100/(correct+wrong)}%")
                            exit()
                        else:
                            break
                except:
                    print("Please enter a valid answer\n")
                    continue

    print(f"You got {correct} out of {correct + wrong}: {correct*100/(correct+wrong)}%")

main()