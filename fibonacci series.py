def print_fibonacci_iterative(n):
    if n <= 0:
        print("Please enter a positive number.")
        return
    a, b = 0, 1
    print("Fibonacci Series (iterative):")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def fibonacci_recursive(n):
    # Base cases: the 0th term is 0, the 1st term is 1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def print_fibonacci_recursive(n):
    if n <= 0:
        print("Please enter a positive number.")
        return
    print("Fibonacci Series (recursive):")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")
    print()

try:
    terms = int(input("How many terms? "))
    print_fibonacci_iterative(terms)
    if terms > 30:
        print("(Skipping recursive version for large n — naive recursion is exponential time,")
        print(" recomputing the same values over and over. This is exactly the kind of")
        print(" inefficiency memoization/dynamic programming fixes, which we'll hit later.)")
    else:
        print_fibonacci_recursive(terms)
except ValueError:
    print("Please enter a valid number!")
