list_tuple = [(1, "Walkers", 0.50), (2, "Squares", 0.50), (3, "Lion Bar", 0.75), (4, "Dairy Milk", 0.80), (5, "Haribo Goldbears", 0.60), (6, "Warhead Sours", 0.60), (7, "Tuna mayo sandwich", 1.20), (8, "BLT sandwich", 1.40), (9, "Sports drink", 0.95), (10, "Lucozade original", 1.50)]

selected_items = []
item = ""
total = 0
choose = ""
change = 0
money = 0

def option():
    global add_money
    global buying
    try:
        if choose == "1":
            add_money()  
        elif choose == "2":
            buying()
        elif choose == "3":
            quit()
        else:
            raise IndexError
    except IndexError as e:
        print("Please choose either 1, 2, or 3")
        option()


def add_money():
    global money
    money = input("Enter the amount of money: £")
    if money.isnumeric():
        print("You now have: £", money)
        money = int(money)
        for i in list_tuple:
            print(f"{i[0]} | {i[1]} - £{i[2]} ")
        buying()
    else:
        print("Please select a whole number.")
        add_money() 
 

def purchase():
    global total
    global money
    global change
    global choose
    global selected_items
    if money >= total:
        buy = input("Would you like to buy the items? yes or no: ")
        if buy == "yes":
                change = money - total
                print("You have bought the items.")
                if change > 0:
                    print("Here is your £", change, "back in change")
        elif buy == "no":
            total = 0                    
            selected_items = []
            print(
            "[1] Add More Money" +  
            " [2] Change chosen items" + 
            " [3] End ")
            print("Choose either 1, 2, or 3.")
            choose = (input(""))
            option()
    elif money < total:
        total = 0
        selected_items = []
        print(
        "You do not have enough money." +
        "[1] Add More Money" +  
        " [2] Change chosen items" + 
        " [3] End ")
        print("Choose either 1, 2, or 3.")
        choose = (input(""))
        option()

def buying():
    global item
    global total
    try:
        item = int(input("Select your item: "))
        item = int(item)
        selected_items.append(list_tuple[item-1])
        continue_buying = input("Do you want another item? Choose yes or no: \n")
        if continue_buying == "no":
            print("")
            for i in selected_items:
                total += i[2]
                print(f"You have chosen {i[1]} ")
            print(f"Your total is £ {total:g} \n")
            purchase()
        else:
            buying()
    except ValueError as e:
        print("Please select a real item")
        buying()
add_money()
