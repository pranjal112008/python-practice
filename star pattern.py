def print_star_pattern(rows=5):
    print("Star Pattern:")
    for i in range(1, rows + 1):
        print("*" * i)
try:
    rows = int(input("Enter number of rows (default 5): ") or 5)
    print_star_pattern(rows)
except ValueError:
    print_star_pattern() 
