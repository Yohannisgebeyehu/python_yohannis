

import math

def calculator():
    print("Scientific Calculator")
    print("Operations: +, -, *, /, sin, cos, tan")
    print("Note: Trigonometric functions take input in degrees")

    try:
        op = input("Enter operation (+, -, *, /, sin, cos, tan): ")

        if op in ["+", "-", "*", "/"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if op == "+":
                print("Result:", num1 + num2)
            elif op == "-":
                print("Result:", num1 - num2)
            elif op == "*":
                print("Result:", num1 * num2)
            elif op == "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Division by zero is not allowed.")

        elif op in ["sin", "cos", "tan"]:
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)  # convert degrees to radians

            if op == "sin":
                print("Result:", math.sin(rad))
            elif op == "cos":
                print("Result:", math.cos(rad))
            elif op == "tan":
                print("Result:", math.tan(rad))

        else:
            print("Invalid operation!")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
calculator()

