def calculate(a, b, choice):
    if choice == "1":
        return a + b
    elif choice == "2":
        return a - b
    elif choice == "3":
        return a * b
    elif choice == "4":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Invalid choice"
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Choose operation: ")
    print("Result =", calculate(a, b, choice))
except ValueError:
    print("Please enter valid numbers!")
