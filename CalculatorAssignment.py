

def calculator():
    """
    This function takes two numbers and an operation from the user
    and prints the result of the calculation.
    """
    try:
        num1 = float(input("Enter the first number: "))
        
        num2 = float(input("Enter the second number: "))
        
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")

    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

calculator()

input("Press Enter to exit...")

        