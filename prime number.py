import math
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a Prime number.")
    else:
        print(f"{num} is Not a Prime number.")
except ValueError:
    print("Please enter a valid integer!")
