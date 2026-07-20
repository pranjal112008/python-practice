try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if number1 > number2:
        number1, number2 = number2, number1

    ask = input("Enter 'even' or 'odd': ").strip().lower()

    if ask not in ("even", "odd"):
        print("Please enter either 'even' or 'odd'.")
    else:
        print(f"{ask.capitalize()} numbers between {number1} and {number2}:")
        for i in range(number1, number2 + 1):
            if ask == "even" and i % 2 == 0:
                print(i, end=" ")
            elif ask == "odd" and i % 2 != 0:
                print(i, end=" ")
        print("\n")
except ValueError:
    print("Please enter valid integers!")
