def find_greatest(a, b, c):
    return max(a, b, c)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    greatest = find_greatest(num1, num2, num3)
    print(f"Greatest number is: {greatest}")
except ValueError:
    print("Please enter valid numbers!")
