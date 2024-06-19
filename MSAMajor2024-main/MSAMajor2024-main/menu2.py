#function to load menu items from the file and create a dictionary
#input: none
#output: dictionary of menu items
def get_menu_items():
    #create a file handle that gives us access to the file
    data_file = open("menu.txt", "r")
    
    #create an empty dictionary to store menu itmes and prices
    menu_items = {}
    
    #loop through data in the file and read the file line one line at a time
    for line_of_data in data_file:
        
        #split the line of data at the comma using .split()
        keys_and_values = line_of_data.split(",")
    
        #get item and price from the resulting list and store in the dictionary
        item = keys_and_values[0]
        price = float(keys_and_values[1])
        menu_items[item] = price

    #close the file
    data_file.close()

    return menu_items

def main():
    food_prices = get_menu_items()

    total = 0
    while True:
        try:
            order = str(input("Item: ")).title()
            if order in food_prices:
                total = total + food_prices[order]
                print(f"{order}: ${food_prices[order]}")
                print(f"Total: ${total}")
            elif order.lower() == "end":
                break
            else:
                print("Please enter a correct item")
                continue
        except:
            print("Please enter a correct item")
            continue
main()