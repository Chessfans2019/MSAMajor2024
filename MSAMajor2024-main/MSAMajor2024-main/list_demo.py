def main():
    #list demo
    #create a list of string names
    list_of_names = ["Messi", "Ronaldo", "Mbappe"]
    list_of_integers = [10, 7, 9]
    random_type_list = ["Chess", 7, 10.5, "Soccer"]
    print(list_of_names)

    #add values to a list
    list_of_names.append("Griezmann")
    print(list_of_names)

    #get the number of items in a list
    number_of_names = len(list_of_names)
    print("\n\n")
    print(f"Number of names: {number_of_names}")

    #get values from our list
    #get the first value from the list of names
    print(f"\nFirst name in list: {list_of_names[0]}")

    #print all items in the list of names
    print("\nInteger list items:")
    for item in list_of_names:
        print(item)

    print("\n")
    #get the number of items in the names list
    number_of_names = len(list_of_names)
    for index in range(number_of_names):
        print(f"Item {index+1}: {list_of_names[index]}")

main()