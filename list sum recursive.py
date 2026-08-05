def list_sum_recursive(numbers):
    if not numbers:         # base case: empty list sums to 0
        return 0
    return numbers[0] + list_sum_recursive(numbers[1:])   # first element + recurse on the rest

if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("Sum:", list_sum_recursive(nums))
    except ValueError:
        print("Please enter valid integers separated by spaces!")