def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
try:
    num = float(input("Enter a number: "))
    result = check_number(num)
    print(f"The number is: {result}")
except ValueError:
    print("Please enter a valid number!")
