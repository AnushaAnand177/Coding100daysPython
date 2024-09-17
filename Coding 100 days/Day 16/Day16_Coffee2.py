from Day16_Coffeemenu import Menu, MenuItem
from Day16_Coffee_maker import CoffeeMaker
from Day16_Coffeemoney_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like?  ({options}) \nor 'off' to turn off or\n'report' to check resources: \n")
    if choice == "off":
        print("""Goodbye!""")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



