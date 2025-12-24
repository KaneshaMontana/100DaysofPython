from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_on = True


# MenuItem: needs drink name and ingredients
# Attributes for name of drink, cost and dictionary of ingredients
# item = MenuItem()

# Menu: Methods returning all menu items names,
menu = Menu()

# This method doesn't require you to give it parameters.
# it returns a string of menu items
drinks_available = menu.get_items()


# CoffeeMaker: Methods report, resource sufficiency, makes order
# Make a copy of the CoffeeMaker Class
machine_actions = CoffeeMaker()

#Money maker
money_machine = MoneyMachine()


while machine_on:
    order = str(input(f" What would you like to order? ({drinks_available}) ")).lower()
    if order == "off":
        machine_on = False
    elif order == "report":
        # show coffee maker report and money machine report
        machine_actions.report()
        money_machine.report()
    else:
        # ask menu to find a drink with that name
        # find_drink method requires you to pass in the parameter the drink
        # Then it returns None or a menu item object aka attributes: name, cost, ingredients
            drink = menu.find_drink(order)
            if drink is None:
                print("Sorry that item is not available.")
            else:
            ## if the coffee make has enough resources for this drink
                if machine_actions.is_resource_sufficient(drink):
            ## If user has given enough money to pay for the cost of this specific drink, make coffee
                    if money_machine.make_payment(drink.cost):
                        machine_actions.make_coffee(drink)
                        print(f"Here is your {order}")