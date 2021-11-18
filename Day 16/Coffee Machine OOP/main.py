from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
check_money = MoneyMachine()

while True:
    user_input = input(f"Please enter your order from the following {menu.get_items()}: ") 
    order = menu.find_drink(user_input)
    if user_input == 'report':
        print("\n")
        coffeemaker.report()
        check_money.report()
        print("\n")
    elif user_input == 'off':
        break
    elif order is not None:
        if coffeemaker.is_resource_sufficient(order) is True and check_money.make_payment(order.cost) is True: 
            coffeemaker.make_coffee(order)
