def sum_of_digits(num):
    num = abs(num)
    if num < 10:          # base case: single digit, sum is itself
        return num
    return (num % 10) + sum_of_digits(num // 10)   # last digit + recurse on the rest

if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        print(f"Sum of digits of {n} = {sum_of_digits(n)}")
    except ValueError:
        print("Please enter a valid integer!")