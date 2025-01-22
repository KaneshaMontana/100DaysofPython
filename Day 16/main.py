from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

take_orders = True
wallet = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

while take_orders:
    options = menu.get_items()
    order = str(input(f" What would you like? ({options}): "))
    if order == "off":
        take_orders = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else: 
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                print("We'll start making your drink")
                coffee_maker.make_coffee(drink)
        else:
             for item in coffee_maker.is_resource_sufficient(drink.ingredients):
                print("*kisses teeth* {item} We doh hav enough ingredients for dat!!")