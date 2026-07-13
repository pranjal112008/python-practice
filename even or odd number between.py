number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
ask = input("Enter 'even' or 'odd': ").strip().lower()
print(f"{ask.capitalize()} numbers between {number1} and {number2}:")
for i in range(number1, number2 + 1):
    if ask == "even" and i % 2 == 0:
        print(i, end=" ")
    elif ask == "odd" and i % 2 != 0:
        print(i, end=" ")
print("\n")  