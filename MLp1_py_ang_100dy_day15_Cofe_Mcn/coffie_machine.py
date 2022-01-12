
user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

# use dictionary
resource = {
    "water" : 1000,
    "milk" : 500,
    "coffee" : 500,
    "money" : 0
}


def esprso():
    global resource
    resource["water"] -= 50
    resource["coffee"] -= 18
    resource["money"] += 1.5
    for i in resource:
        if resource[i] < 0 : 
            resource["water"] += 50
            resource["coffee"] += 18
            resource["money"] -= 1.5
            print(f"sorry {i} is low")
            return


def late():
    global resource
    resource["water"] -= 200
    resource["coffee"] -= 24
    resource["milk"] -= 150
    resource["money"] += 2.5
    for i in resource:
        if resource[i] < 0 :  
            resource["water"] += 200
            resource["coffee"] += 24
            resource["milk"] += 150
            resource["money"] -= 2.5
            print(f"sorry {i} is low")
            return


def caPcino():
    global resource
    resource["water"] -= 250
    resource["coffee"] -= 24
    resource["milk"] -= 200
    resource["money"] += 3.0
    for i in resource:
        if resource[i] < 0 : 
            resource["water"] += 250
            resource["coffee"] += 24
            resource["milk"] += 200
            resource["money"] -= 3.0
            print(f"sorry {i} is low")
            return


def show_resrc():
    print(f"""
            water= {resource["water"]} \n 
            milk = {resource["milk"]} \n 
            coffee = {resource["coffee"]} \n 
            money = {resource["money"]}""")



def coin_enter():
    pNy = float(input("Enter number of Peny : "))
    niKl = float(input("Enter number of Nickl : "))
    dIme = float(input("Enter number of Dime : "))
    qrTr = float(input("Enter number of Quarter : "))
    
    total = (0.01*pNy) + (0.05*niKl) + (0.1*dIme) + (0.25*qrTr)

    if (total < 1.5) and (user_input == "espresso"):
        print("Not Enough money. Coins are returned")
    elif (total < 2.5) and (user_input == "latte"):
        print("Not Enough money. Coins are returned")
    elif (total < 3.0) and (user_input == "cappuccino"):
        print("Not Enough money. Coins are returned")

    return total

while user_input != "off":
    if user_input == "resource":
        show_resrc()
    elif user_input == "espresso":
        coIn = coin_enter()
        if coIn >= 1.5:
            esprso()
            print(f"Here is change : {coIn - 1.5}")
        show_resrc()
    elif user_input == "latte":
        coIn = coin_enter()
        if coIn >= 2.5:
            late()
            print(f"Here is change : {coIn - 2.5}")
        show_resrc()
    elif user_input == "cappuccino":
        coIn = coin_enter()
        if coIn >= 3.0:
            caPcino()
            print(f"Here is change : {coIn - 3.0}")
        show_resrc()
    else:
        print("Not a valid Code")

    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

# def resRc():
#     water= 100
#     milk= 50
#     coffee= 76
#     money= 2.5

# python coffie_machine.py