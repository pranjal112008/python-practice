from functools import reduce

def product(numbers):
    if not numbers:
        return 0
    return reduce(lambda acc, n: acc * n, numbers, 1)

if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("Product:", product(nums))
    except ValueError:
        print("Please enter valid integers separated by spaces!")