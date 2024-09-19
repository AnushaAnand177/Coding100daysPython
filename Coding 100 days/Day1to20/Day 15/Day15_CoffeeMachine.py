import Day15_CoffeeData
from Day15_CoffeeData import resources

# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def user_prompt(user_choice):
    return {
        "choice": user_choice,
        "price": Day15_CoffeeData.MENU[user_choice]["cost"],
        "water": Day15_CoffeeData.MENU[user_choice]["ingredients"].get("water", 0),  # Use get to handle missing keys
        "milk": Day15_CoffeeData.MENU[user_choice]["ingredients"].get("milk", 0),    # Default milk to 0 if not present
        "coffee": Day15_CoffeeData.MENU[user_choice]["ingredients"]["coffee"]
    }

# calculate resources and check if resources are sufficient
def check_resources(water, milk, coffee):
    left_water = resources["water"] - water
    left_milk = resources["milk"] - milk
    left_coffee = resources["coffee"] - coffee

    if left_water < 0:
        print("Sorry, not enough water.")
        return False
    if left_milk < 0:
        print("Sorry, not enough milk.")
        return False
    if left_coffee < 0:
        print("Sorry, not enough coffee.")
        return False

    return True

# process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total = quarters + dimes + nickels + pennies
    return total

#  make coffee and update resources
def make_coffee(coffee_resources):
    resources["water"] -= coffee_resources["water"]
    resources["milk"] -= coffee_resources["milk"]
    resources["coffee"] -= coffee_resources["coffee"]

def coffee_maker():
    drinking = True
    while drinking:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice not in Day15_CoffeeData.MENU:
            print("Invalid choice. Please select from espresso, latte, or cappuccino.")
            continue

        coffee_resources = user_prompt(user_choice)

        # Check if enough resources are available
        if not check_resources(coffee_resources["water"], coffee_resources["milk"], coffee_resources["coffee"]):
            print("Not enough resources to make this coffee.")
            break

        # Report the current state
        report = input("Do you want to see the report (y/n)? ").lower()
        if report == "y":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${coffee_resources['price']}")

        # Process coins and check if payment is sufficient
        user_money = process_coins()
        if user_money >= coffee_resources["price"]:
            change = round(user_money - coffee_resources["price"], 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            print("Here is your ☕. Enjoy!")
            make_coffee(coffee_resources)  # Update resources after making coffee
        else:
            print("Sorry, that's not enough money. Money refunded.")
            continue  # Start over in the loop

        # Ask if user wants to make another coffee
        drink_again = input("Would you like to make another coffee (y/n)? ").lower()
        if drink_again != "y":
            drinking = False
        else:
            # Final report before ending
            print(f"Final report:\nWater: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            continue  # Start over in the loop

coffee_maker()
