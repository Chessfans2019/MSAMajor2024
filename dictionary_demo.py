def main():
    #list [1, 4, 6, 7 ,78]
    scores = [1, 4, 6, 7 ,78]
    student_names = ["Ronaldo", "Messi", "Mbappe", "Griezmann", "Giroud"]
    for index in range(len(scores)):
        print(f"{student_names[index]}: {scores[index]}")

    #create a dictionary of names and scores
    student_scores = {
        "Ronaldo": 87,
        "Messi": 79,
        "Mbappe": 94,
        "Griezmann": 90
    }
    #print Roanldo and Messi's scores
    print("\n")
    print(student_scores["Ronaldo"])
    print(student_scores["Messi"])

    #get all the keys and values from the student score dictionary
    print("\n")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")
    
    #declare a car dictionary
    car = {"make": "Ferarri", "model": "F-50", "year": 2021, "value": 500000, "engine": 4.8}
    
    #get all the keys and values from the car dictionary
    print("\n")
    for key, value in car.items():
        print(f"{key}: {value}")

main()