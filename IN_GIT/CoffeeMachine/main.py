from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
menu = Menu()
mm = MoneyMachine()

is_on = True

while (is_on):



    item_choice = input("What would you like? (espresso/latte/cappuccino/):\n")

    match item_choice:
        case "off":
            is_on = False
        case "report":
            cm.report()
            mm.report()



    drink = menu.find_drink(item_choice)

    if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
        cm.make_coffee(drink)



