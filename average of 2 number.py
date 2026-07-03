try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    average = (num1 + num2) / 2
    print(f"Average of the two numbers = {average:.2f}")
except ValueError:
    print("Please enter valid numbers!")
