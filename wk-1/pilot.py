# Basic Calculator Program

# Asking for user input
num1 = int(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

# Performing the calculation
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")