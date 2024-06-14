def main():

    a = 5
    b = 7
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    elif a == b:
        print(f"{a} is equal to {b}")

    #print the appropriate letter grade based on the test score
    #A: 100 - 90, B: 89-80, C: 79-70, D: 69-60, F: everything else
    test_score = 89.9
    print("\nGrade decision 1:")
    if ((test_score <= 100) and (test_score >= 90)):
        print(f"{test_score} --> A")
    elif test_score <= 90 and test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score <= 80 and test_score >= 70:
        print(f"{test_score} --> C")
    elif test_score <= 70 and test_score >= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

    #grade decision statement restructured
    print("\nGrade decision 2:")
    if ((test_score <= 100) and (test_score >= 90)):
        print(f"{test_score} --> A")
    elif test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score >= 70:
        print(f"{test_score} --> C")
    elif test_score >= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

main()