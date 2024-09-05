# Define individual operation functions
import os


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Function to calculate the result
def calculate(first_num, b, operation):
    if operation == 1:
        return add(first_num, b)
    elif operation == 2:
        return subtract(first_num, b)
    elif operation == 3:
        return multiply(first_num, b)
    elif operation == 4:
        return divide(first_num, b)

# Function to display the options
def display_options():
    print("1 for ADD")
    print("2 for SUBTRACT")
    print("3 for MULTIPLY")
    print("4 for DIVIDE")
    print("5 for EXIT")

# Main calculator function
def calculator():
    print("WHAT DO YOU WANT TO DO?")
    want_to_calculate = True
    first_num = float(input("ENTER THE FIRST NUMBER: "))

    while want_to_calculate:
        display_options()
        choice = int(input("ENTER YOUR CHOICE: "))

        if choice in [1, 2, 3, 4]:
            b = float(input("ENTER THE SECOND NUMBER: "))
            result = calculate(first_num, b, choice)
            print(f"\nTHE ANSWER IS: {result}")
            first_num = result
            print(f"\nYOU WILL CONTINUE CALCULATING WITH: {first_num}")
        elif choice == 5:
            want_to_calculate = False
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("INVALID CHOICE")

# Run the calculator
calculator()






