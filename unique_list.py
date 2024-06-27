def main():
    person1 = {"name": "Ronaldo", "age": 39}
    person2 = {"name": "Messi", "age": 37}
    person3 = {"name": "Mbappe", "age": 25}
    person4 = {"name": "Miku", "age": 16}

    #add person to a list
    person_list = []
    person_list.append(person1)
    person_list.append(person2)
    person_list.append(person3)
    person_list.append(person4)

    #write out code that produces a list of unique names
    unique_names = []
    for person in person_list:
        print(person)
        if person["name"] not in unique_names:
            unique_names.append(person)
        else:
            continue
    print(unique_names)

main()