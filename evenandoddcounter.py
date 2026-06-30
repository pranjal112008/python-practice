n=int(input("How many numbers?"))
numbers=[]
for i in range(n):
    num=int(input(f"Enter number {i+1}:"))
    numbers.append(num)
even = 0 
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Numbers:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd) 