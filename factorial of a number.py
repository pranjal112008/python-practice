def factorial_iterative(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def factorial_recursive(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    if num <= 1:          # base case: 0! and 1! are both 1
        return 1
    return num * factorial_recursive(num - 1)   # recursive case

try:
    num = int(input("Enter a number: "))
    result_iter = factorial_iterative(num)
    result_rec = factorial_recursive(num)
    print(f"Factorial of {num} (iterative) = {result_iter}")
    print(f"Factorial of {num} (recursive) = {result_rec}")
except ValueError:
    print("Please enter a valid positive integer!")
except RecursionError:
    print("Number too large for recursion — Python's call stack has a limit (~1000 by default).")
