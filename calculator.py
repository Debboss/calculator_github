def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculator():
    print("Calculator")
    
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    choice = input("Choose a mathematical operation: 1)Addition, 2)Subtraction, 3)Multiplication, 4)Division: ")

    if choice == '1' or choice == 'Addition':
        result = add(number1, number2)
        print("Result:", result)
    elif choice == '2' or choice == 'Subtraction':
        result = subtract(number1, number2)
        print("Result:", result)
    elif choice == '3' or choice == 'Multiplication':
        result = multiply(number1, number2)
        print("Result:", result)
    elif choice == '4' or choice == 'Division':
        result = divide(number1, number2)
        print("Result:", result)
    else:
        print("Invalid input")

calculator()
