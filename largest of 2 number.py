try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    largest = max(a, b)
    print(f"Largest number is: {largest}")
except ValueError:
    print("Please enter valid numbers!")
