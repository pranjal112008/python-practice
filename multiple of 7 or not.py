try:
    num = int(input("Enter a number: "))
    if num % 7 == 0:
        print(f"{num} is a multiple of 7.")
    else:
        print(f"{num} is NOT a multiple of 7.")
except ValueError:
    print("Please enter a valid integer!")
