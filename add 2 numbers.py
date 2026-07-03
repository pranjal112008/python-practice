def add(a, b):
    return a + b
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add(num1, num2)
    print(f"Sum = {result}")
except ValueError:
    print("Please enter valid numbers!")
