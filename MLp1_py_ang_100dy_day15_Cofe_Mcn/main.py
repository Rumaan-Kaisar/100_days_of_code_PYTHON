MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns Total of the inserted coins"""
    print("Please insert the coins")
    pNy = float(input("Enter number of Peny : "))
    niKl = float(input("Enter number of Nickl : "))
    dIme = float(input("Enter number of Dime : "))
    qrTr = float(input("Enter number of Quarter : "))
    total = (0.01 * pNy) + (0.05 * niKl) + (0.1 * dIme) + (0.25 * qrTr)
    return total


def is_transection_sucess(money_recived, drink_cost):
    """True when accepted or False if insufficient"""
    if money_recived >= drink_cost:
        global profit
        change = round(money_recived - drink_cost, 2)
        print(f"Here is ${change} in change")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffiee(drink_name, order_ingredients):
    """Deduct the ingredients from resources """
    for itM in order_ingredients:
        resources[itM] -= order_ingredients[itM]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water {resources['water']}")
        print(f"Milk {resources['milk']}")
        print(f"Coffee {resources['coffee']}")
        print(f"Money ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transection_sucess(payment, drink["cost"]):
                make_coffiee(choice, drink["ingredients"])
