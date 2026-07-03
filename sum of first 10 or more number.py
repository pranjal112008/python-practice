def sum_of_natural_numbers(n=10):
    total = sum(range(1, n + 1))
    return total
try:
    n = int(input("Enter how many numbers to sum (default 10): ") or 10)
    total = sum_of_natural_numbers(n)
    print(f"Sum of first {n} natural numbers = {total}")
except ValueError:
    print("Sum of first 10 numbers =", sum_of_natural_numbers())
