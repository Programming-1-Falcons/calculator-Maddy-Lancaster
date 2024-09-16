while True:

    operation = input("What operation is being done?: ")

    num1 = float(input("Number 1: "))

    num2 = float(input("Number 2: "))

    addition = (num1 + num2)

    subtraction = (num1 - num2)

    division = (num1 / num2)

    multiplication = (num1 * num2)

    exponent = (num1 ** num2)
    
    if operation == "addition":
        print(num1, "+", num2, "=", addition)

    elif operation == "subtraction":
        print(num1, "-", num2, "=", subtraction)

    elif operation == "division":
        print(num1, "/", num2, "=", division)

    elif operation == "multiplication":
        print(num1, "*", num2, "=", multiplication)

    elif operation == "exponent":
        print(num1, "**", num2, "=", exponent)
    
    else:
        print("That is not an operation")