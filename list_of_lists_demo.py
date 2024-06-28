def main():

    list_of_lists = [[3, 7, 9], [6, 9, 2], [1, 5, 7]]
    for item in list_of_lists:
        print(list_of_lists[0][2]) #will print out Giroud's jersey number
    for row in range(len(list_of_lists)):
        for column in range(len(list_of_lists[row])):
            print(list_of_lists[row][column])

main()