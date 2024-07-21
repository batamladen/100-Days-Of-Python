MENU = {
    "espresso": {
        "ingredients": {
            "water": 100,
            "milk": 0,
            "coffee": 75
        },
        "cost": 2.5
    },
    "latte": {
        "ingredients": {
            "water": 80,
            "milk": 80,
            "coffee": 55
        },
        "cost": 2
    },
    "cappuccino": {
        "ingredients": {
            "water": 100,
            "milk": 50,
            "coffee": 65
        },
        "cost": 1.5
    }
}

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500
}

money = 0

def what_would_you_like():
    pick = input("What would you like? (espresso, latte, cappuccino): ").lower()

    if pick in MENU:
        return pick
    elif pick == 'off':
        machine_off()
    elif pick == 'report':
        report()
    else:
        print("Invalid coffee pick")
        return None

def machine_off():
    print("Turning off the machine...")
    exit()

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def resources_check(coffee_choice):
    ingredients = MENU[coffee_choice]['ingredients']
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry. Not enough {item} in the machine.")
            return False
    return True

def add_coins():
    print("Insert coins:")
    quarters = int(input("quarters: ")) * 0.25
    dimes = int(input("dimes: ")) * 0.10
    nickels = int(input("nickels: ")) * 0.05
    pennies = int(input("pennies: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

def process_transaction(coffee_choice, money_received):
    global money
    coffee_cost = MENU[coffee_choice]['cost']
    if money_received >= coffee_cost:
        change = round(money_received - coffee_cost, 2)
        print(f"Here is ${change} in change.")
        money += coffee_cost
        return True
    else:
        print(f"Not enough money. You need ${coffee_cost - money_received} more.")
        print("Money refunded.")
        return False

def ingredients_deduction(coffee_choice):
    ingredients = MENU[coffee_choice]['ingredients']
    for item in ingredients:
        resources[item] -= ingredients[item]

def coffee_machine():
    while True:
        choice = what_would_you_like()
        if choice is None:
            continue
        if choice == 'report':
            report()
            continue
        if choice == 'off':
            machine_off()
            continue
        if resources_check(choice):
            money_received = add_coins()
            if process_transaction(choice, money_received):
                ingredients_deduction(choice)
                print(f"Here is your {choice}. Enjoy!")

if __name__ == "__main__":
    coffee_machine()
