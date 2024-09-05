def calculator():
    # Initialize the result variable to None
    result = None

    while True:
        # If it's the first calculation, prompt for a number
        if result is None:
            num1 = float(input("Enter the first number: "))
        else:
            # If there's a previous result, use it as num1
            num1 = result

        operator = input("Enter an operator (+, -, *, /) or 'exit' to quit: ")

        if operator == 'exit':
            print("Exiting the calculator.")
            break

        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error! Division by zero.")
                continue
        else:
            print("Invalid operator. Please try again.")
            continue

        print(f"Result: {result}")
        print("The result is stored and will be used for the next calculation.")

# Run the calculator
calculator()
