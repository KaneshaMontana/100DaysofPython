from main import MENU, resources

# TODO: Ask user what they would like to order

machine_is_on = True
profit = 0

def process_coins(drink, ingredients):
    cost = MENU[drink]["cost"]
    print(f"Your {drink} costs {cost} ")
    total_payment = 0
    total_payment = int(input("How many quarters are you inserting? ")) *0.25
    total_payment += int(input("How many dimes are you inserting? ")) *0.10
    total_payment += int(input("How many nickles are you inserting? ")) *0.05
    total_payment += int(input("How many pennies are you inserting? ")) *0.01
    print(total_payment)
    is_transaction_successful(total_payment, cost, drink, ingredients)


def is_transaction_successful(money_received, cost, drink, ingredients):
    if money_received >= cost:
        change = round(money_received - cost, 2)
        global profit
        profit += cost
        print(f"Here is you change: {change}")
        make_coffee(drink, ingredients)

    else:
        print("Sorry there is not enough money. Money refunded")

def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕️")


def check_resources(drink, ingredients):
    """ ingredients is MENU[drink_name]["ingredients"] simplified """
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
        else:
            print("You are getting coffee today")

    process_coins(drink, ingredients)


while machine_is_on:
    order = str(input(" What would you like to order? (espresso/latte/cappuccino) ")).lower()
    if order == "espresso" or order == "latte" or order == "cappuccino":
        order_ingredients = MENU[order]["ingredients"]
        check_resources(order, order_ingredients)
    if order == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"Resources remaining: \n water: {water}\n milk: {milk}\n coffee: {coffee}\n money: {profit}")
    if order == "off":
        print("This machine will turn off in \n..3\n..2\n..1")
        machine_is_on = False


