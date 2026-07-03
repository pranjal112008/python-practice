def print_fibonacci(n):
    if n <= 0:
        print("Please enter a positive number.")
        return
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  
try:
    terms = int(input("How many terms? "))
    print_fibonacci(terms)
except ValueError:
    print("Please enter a valid number!")
