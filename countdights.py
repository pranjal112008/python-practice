def count_digits(num):
    if num == 0:
        return 1
    count = 0
    num = abs(num)
    while num > 0:
        count += 1
        num = num // 10
    return count
try:
    num = int(input("Enter a number: "))
    print(f"Number of digits = {count_digits(num)}")
except ValueError:
    print("Please enter a valid integer!")
