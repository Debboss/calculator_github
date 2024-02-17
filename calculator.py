def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculator():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    
    choice = input("Choose one of the above options (1 or 2): ")

    number1 = (input("Enter first number: "))
    number2 = (input("Enter second number: "))

    if choice == '1':
        result = add(number1, number2)
        print("Result:", result)
    elif choice == '2':
        result = subtract(number1, number2)
        print("Result:", result)
    else:
        print("Invalid input")

calculator()
