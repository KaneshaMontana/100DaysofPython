MENU = {
    "espresso":{
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost":1.50,
    },
    "latte":{
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost":2.50,
    },
    "cappuccino":{
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost":3.0,
    }
}

profit = 0

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

next_order = True

def sufficient_resources(order_ingredients):
    """ Returns true if there is enough resources to make drink or False if insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True
        

def process_coins():
    """Returns total from coins inserted"""
    print("Let's take payment")

    total_payment = int(input("How many quarters are you inserting? ")) *0.25
    total_payment += int(input("How many dimes are you inserting? ")) *0.10
    total_payment += int(input("How many nickles are you inserting? ")) *0.05
    total_payment += int(input("How many pennies are you inserting? ")) *0.01

    return total_payment

def is_transaction_successful(money_received, cost):
    """Returns whether or not the user has enough money to purchase a drink"""
    if money_received >= cost:
        change = round(money_received - cost, 2)
        global profit
        profit += cost

        print(f"Here is your change ${change}")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
        

def make_coffee(drink_name, order_ingredients):
    """Returns how much resources it has left in the machine"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")

while next_order:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        print("Turning off")
        next_order = False
    elif order == "report":
        print(f"Water:{resources['water']}ml]")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, float(drink["cost"])):
                make_coffee(order, drink["ingredients"])
            

 