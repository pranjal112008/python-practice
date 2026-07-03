def factorial(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
try:
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"Factorial of {num} = {result}")
except ValueError:
    print("Please enter a valid positive integer!")
