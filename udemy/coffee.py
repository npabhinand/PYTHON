MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

def make_coffee(response,coffee):
    if response in MENU:
        required_ingredients = MENU[response]['ingredients']
        total=process_coins()
        if total>=MENU[response]['cost']:
            for item, quantity in required_ingredients.items():
                if coffee[item]>=quantity:
                    coffee[item]-=quantity
                else:
                    print(f"Sorry, there is not enough {item}.")
                    return
            coffee['money']+=MENU[response]['cost']
            print(f"Here is ${total-MENU[response]['cost']} in change.")
            print(f"Here is {response} enjoy")
        else:
            print("Sorry that's not enough money. money refunded")

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
profit=0
coffee={"water":300,"milk":200,"coffee":100,"money":0}
while True:
    response=input("What would you like? (espresso/latte/cappuccino): ").lower()
    make_coffee(response,coffee)
    if response=="report":
        for i in (coffee):
            print(i,':',coffee[i])
    
    
        
        