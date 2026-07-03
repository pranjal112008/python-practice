try:
    side = float(input("Enter the side of the square: "))
    if side < 0:
        print("Side cannot be negative!")
    else:
        area = side ** 2
        print(f"Area of the square = {area}")
except ValueError:
    print("Please enter a valid number!")
