from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_from_machine = MoneyMachine()
menu = Menu()
coffee = CoffeeMaker()
machine_on = True

while machine_on:
    options = menu.get_items()
    order = input(f"please input your order: ({menu.get_items()})")

    if order == "off":
        machine_on = False
    elif order == "report":
        coffee.report()
        money_from_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink) and money_from_machine.make_payment(drink.cost):
            coffee.make_coffee(drink)
