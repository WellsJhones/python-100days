MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 2900,
    "milk": 2900,
    "coffee": 1000,
}
print("Welcome to the Coffee Machine!")
selection = []
for item in MENU:
    selection.append(item)
    coffee = MENU[item]
    cost = MENU[item]["cost"]
    print(f"{item}: {cost}")
print(selection)


def check_resorses():
    if user_choice == "espresso":
        if resources["water"] < 50 or resources["coffee"] < 18:
            print("Sorry there is not enough water.")
            exit()
    elif user_choice == "latte":
        if resources["water"] < 200 or resources["milk"] < 150 or resources["coffee"] < 24:
            print("Sorry there is not enough water.")
            exit()
    elif user_choice == "cappuccino":
        if resources["water"] < 250 or resources["milk"] < 100 or resources["coffee"] < 24:
            print("Sorry there is not enough water.")
            exit()


get_anotherF_Y = True
while get_anotherF_Y:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    if user_choice not in selection:
        print("Invalid selection")
        exit()

    else:
        if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            check_resorses()
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = (quarters * 0.25) + (dimes * 0.10) + \
                (nickles * 0.05) + (pennies * 0.01)
            cost = MENU[user_choice]["cost"]
            print(f"You have ${total}.")
            if total >= cost:
                resources["water"] -= MENU[user_choice]["ingredients"]["water"]
                resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
                resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
                if total - cost == 0:
                    print("Thank you!")
                else:
                    print(f"Here is ${total - cost} in change.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
                exit()
        get_another = input("Would you like another coffee? (y/n): ")
        if get_another == "n":
            get_anotherF_Y = False
            print("Goodbye")
            exit()
