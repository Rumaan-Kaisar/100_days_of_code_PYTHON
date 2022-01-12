import coffee_maker
import money_machine
import menu

# alawys use "()" ti initiate class to objects
drink_menue = menu.Menu()
cofy_serv = coffee_maker.CoffeeMaker()
pay_bill = money_machine.MoneyMachine()

machine_run = True

while machine_run == True:
    ask = input(f"what drinks do you want : {drink_menue.get_items()}").lower()
    if ask == "report":
        # print(cofy_serv.report())
        cofy_serv.report()
    elif ask == "off":
        machine_run = False
    else:
        picked_drink = drink_menue.find_drink(ask)

        print(f"\n\nYou ordered for \"{picked_drink.name}\", its price is ${picked_drink.cost}")

        print("\n----------Current Available resource -----------\n")
        # printing "cofy_serv.report()" or "pay_bill.report()"only prints "NONE" its just calling a function/method
        # print(cofy_serv.report())
        # print(f"current profit : {pay_bill.report()}")
        cofy_serv.report()
        pay_bill.report()


        sufficient_ingredient = cofy_serv.is_resource_sufficient(picked_drink)
        if sufficient_ingredient == True :
            print("\n----------Make payment -----------")
            transaction = pay_bill.make_payment(picked_drink.cost)
            if transaction == True:
                cofy_serv.make_coffee(picked_drink)


# python cfy_mcn_oop.py