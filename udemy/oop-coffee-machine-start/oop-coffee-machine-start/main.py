from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Create a menu with items
menu = Menu()
menu_item_list = menu.get_items()

while True:
    response=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if response=="report":
        coffee_maker.report()
        money_machine.report()
    elif response=="exit":
        break
    else: 
        drink = menu.find_drink(response)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                payment_successful=money_machine.make_payment(drink.cost)
                if payment_successful:
                    coffee_maker.make_coffee(drink)
                
            
        
