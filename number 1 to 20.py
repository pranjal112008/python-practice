def print_numbers(start=1, end=20):
    print(f"Numbers from {start} to {end}:")
    for i in range(start, end + 1):
        print(i, end=" ")
    print()
print_numbers()
