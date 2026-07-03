def print_multiplication_table(num, upto=10):
    print(f"Multiplication Table of {num} (up to {upto}):")
    for i in range(1, upto + 1):
        print(f"{num} x {i:2} = {num * i}")
try:
    num = int(input("Enter a number: "))
    upto = int(input("Up to which number? (default 10): ") or 10)
    print_multiplication_table(num, upto)
except ValueError:
    print("Please enter valid numbers!")
    
