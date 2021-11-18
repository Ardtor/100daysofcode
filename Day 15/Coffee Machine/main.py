from resources import MENU, resources

# https://replit.com/@appbrewery/coffee-machine-final?embed=1&output=1#main.py


# set up variables

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def menu(user_choice):
    """
    Takes in the user input and checks that it's a valid option or returns insufficient resources
    """

    enough_resources = True
    missing_resources = ''

    if user_choice in MENU:
        for item, amount in MENU[user_choice]['ingredients'].items():
            if resources[item] < amount:
                enough_resources = False
                missing_resources += item + ', '
    elif user_choice == 'report':
        return False

    else:
        print("That is not a valid choice please try again")
        return False

    if not enough_resources:
        print(f"Sorry we do not enough of the following: {missing_resources}")

    return enough_resources


def money(user_choice):
    """
    Takes in the users choice, checks the cost and asks for money to pay, returns 0 if not enough or the total entered if sufficient 
    """

    print(f"Your {user_choice} costs:${MENU[user_choice]['cost']}")
    quarters = int(
        input("Please enter the amount of Quarters you'd like to use: ")) * 0.25
    dimes = int(
        input("Please enter the amount of Dimes you'd like to use: ")) * 0.10
    nickles = int(
        input("Please enter the amount of Nickles you'd like to use: ")) * 0.05
    pennies = int(
        input("Please enter the amount of Pennies you'd like to use: ")) * 0.01

    total = quarters+dimes+nickles+pennies

    if total >= MENU[user_choice]['cost']:
        return round(total, 2)
    else:
        print("You have not entered enough money to pay for this drink, your coins have been refunded. Please order again and enter the correct amount")
        return 0


def transaction(user_choice, total, total_in_machine):
    """
    Takes in the users choice, the total amount, and the total in the machine.
    Will deduct the resources from MENU and then work out how much to refund the user, and how much to add to the device
    """

    total_in_machine = total_in_machine

    for item, amount in MENU[user_choice]['ingredients'].items():
        resources[item] -= amount

    user_total = (total - MENU[user_choice]['cost'])
    total_in_machine = total_in_machine + MENU[user_choice]['cost']

    return user_total, total_in_machine


def main():
    total_in_machine = 0
    while True:
        user_input = input(
            "\nPlease enter your request (Espresso/Latte/Cappuccino): ").lower()
        if user_input == 'off':
            break
        elif user_input == 'report':
            print(
                f"Current resources:\n\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney:${total_in_machine:,.2f}")

        if menu(user_input) == True:
            user_total = money(user_input)
            if user_total != 0:
                change, total_in_machine = transaction(
                    user_input, user_total, total_in_machine)
                total_in_machine = total_in_machine
                print(
                    f"Thanks for buying your {user_input} your change is ${change:,.2f}")


main()
