def power_recursive(base, exp):
    if exp == 0:           # base case: anything to the power 0 is 1
        return 1
    if exp < 0:
        return 1 / power_recursive(base, -exp)
    return base * power_recursive(base, exp - 1)

if __name__ == "__main__":
    try:
        base = float(input("Enter base: "))
        exp = int(input("Enter exponent: "))
        print(f"{base} ^ {exp} = {power_recursive(base, exp)}")
    except ValueError:
        print("Please enter valid numbers!")