from menu_resources import MENU, resources

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


def show_resources(resource_dict):
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
    print("+---------------+")


# TODO 1: Prompt user by asking what kind of coffee they would like.
# TODO 2: Turn off the Coffee Machine by entering “​off​” to the prompt.
# TODO 3: Print report.
# TODO 4: Check if resources are sufficient?
# TODO 5: Process Coins
# TODO 6: Check if transaction is successful?
# TODO 7: Make Coffee.
