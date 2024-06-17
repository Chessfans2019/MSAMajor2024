def main():
    #capitalize a string
    my_name = "mark"
    print(my_name.capitalize())

    #make a string uppercase
    print(my_name.upper())

    #make a string lowercase
    last_name = "LI"
    print(f"{my_name.capitalize()} {last_name.lower()}")

    #determine if a string starts with a set of characters
    print(my_name.startswith("m")) #returns true

    if(not my_name.startswith("ma") and not my_name.startswith("Ma")):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly") #will print

    #determine if a string ends with a specified set of characters
    print(my_name.endswith("rk")) #returns true

    #find a set of characters in a string
    print(my_name.find("k, 7")) #prints out -1

    #loop through a string
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters") #mark has 13 letters

    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index + 1}: {my_name[letter_index]}")

    print("\n")
    sentence = "I have a cat. My cat is cute. Do you want a cat?"
    #write code that counts the number of occurences of the word dog in sentence
    start_index = 0
    counter = 0
    while True:
        start_index = sentence.find("cat", start_index) + 1
        if start_index == 0: #stops when program reaches the end of the sentence
            break
        counter += 1
    print(f"There are {counter} cats in the sentence")

    #how to use the split method
    car_info = "Ferrari, f-50, 2021, 500000, 4.8"
    car_data = car_info.split()
    print(car_data)

main()