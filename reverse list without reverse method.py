def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

try:
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    print("Original List:", numbers)
    print("Reversed List:", reverse_list(numbers))
except ValueError:
    print("Please enter valid integers separated by spaces!")
