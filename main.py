from menu_resources import MENU, resources


profit = 0


def show_menu(menu_dict):
    """Ticket that displays menu to the user when they input: 'menu'."""
    # Header of the Menu
    print("+-------------------+")
    print("| MENU    |   Price |")
    print("+-------------------+")
    
    # Meny Items
    for name, details in menu_dict.items():
        item_name = name.capitalize()
        price = f"${details['cost']:.2f}"
        print(f"| {item_name:<10} {price:>6} |")
    
    # Footer of the menu
    print("+-------------------+")


def show_report(resource_dict):
    """Ticket that displays resources to the user when they input: 'report'."""
    print("+---------------+")
    print("|   RESOURCES   |")
    print("+---------------+")
    for key in resource_dict:
        resource_name = key.capitalize()
        resource_qty = f"{resource_dict[key]}"
        if key == "water" or key == "milk":
            resource_qty += "ml"
        elif key == "coffee":
            resource_qty += "g"
        print(f"| {resource_name:<6} {resource_qty:>6} |")
    print(f"| Money   ${profit:>4.2f} |")
    print("+---------------+")


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False    # is_enough = False
        return True         # is_enough = True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("> How many quarters?: ")) * 0.25
    total += int(input("> How many dimes?: ")) * 0.10
    total += int(input("> How many nickels?: ")) * 0.05
    total += int(input("> How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change:.2f} in change.")
        
        global profit           # Access locally by calling it global
        profit += money_received
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


# ✓ TODO 1: Prompt user by asking what kind of coffee they would like.
is_coffee_machine_on = True

while is_coffee_machine_on:
    choice = input("What would you like (espresso/latte/cappuccino)?: ").lower()
    
    # ✓ TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        print("Shutting down...")
        is_coffee_machine_on = False
    # ✓ TODO 3: Print report.
    elif choice == "report":
        show_report(resources)
    elif choice == "menu":
        show_menu(MENU)
    elif choice in MENU:
        drink = MENU[choice]
        # print(drink)      # prints dict for that coffee drink
        # ✓ TODO 4: Check if resources are sufficient?
        if is_resource_sufficient(drink["ingredients"]):
            # ✓ TODO 5: Process Coins
            payment = process_coins()
            # ✓ TODO 6: Check if transaction is successful?
            is_transaction_successful(payment, drink["cost"])
            # ✓ TODO 7: Make Coffee.
            make_coffee(choice, drink["ingredients"])
    else:
        print(f"Sorry, we don't brew '{choice}'. Please select one of the listed options.")
