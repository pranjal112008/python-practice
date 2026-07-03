num=int(input("Enter a number:"))
rev=0
while num>0:
    digit = num%10
    rev=rev*10+digit
    num=num//10
print("Reverse=",rev)
def reverse_number(num):
    original = num
    reversed_num = 0
    is_negative = num < 0
    num = abs(num)
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return -reversed_num if is_negative else reversed_num
try:
    num = int(input("Enter a number: "))
    rev = reverse_number(num)
    print(f"Reverse of {num} is {rev}")
except ValueError:
    print("Please enter a valid integer!")
