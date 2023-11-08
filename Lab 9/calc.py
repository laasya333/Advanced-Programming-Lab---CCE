def add(x, y):
    try:
        result = x + y
        return result
    except TypeError:
        return "Invalid input. Please enter real-valued numbers."

def subtract(x, y):
    try:
        if x < y:
            raise ValueError("Subtraction result is negative.")
        result = x - y
        return result
    except (TypeError, ValueError):
        return "Invalid input. Please enter real-valued numbers, and ensure the first number is greater for subtraction."

def multiply(x, y):
    try:
        result = x * y
        return result
    except TypeError:
        return "Invalid input. Please enter real-valued numbers."

def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = x / y
        return result
    except (TypeError, ZeroDivisionError):
        return "Invalid input. Please enter real-valued numbers, and ensure the divisor is not zero."

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")
    
    if user_input == "quit":
        break
    
    if user_input in ["add", "subtract", "multiply", "divide"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if user_input == "add":
                print("Result:", add(num1, num2))
            elif user_input == "subtract":
                print("Result:", subtract(num1, num2))
            elif user_input == "multiply":
                print("Result:", multiply(num1, num2))
            elif user_input == "divide":
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input. Please enter real-valued numbers.")
    else:
        print("Unknown input. Please enter a valid operation.")
