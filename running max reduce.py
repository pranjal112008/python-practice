from functools import reduce

def find_max(numbers):
    if not numbers:
        raise ValueError("Cannot find max of an empty list")
    return reduce(lambda acc, n: acc if acc > n else n, numbers)

if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    except ValueError:
        print("Please enter valid integers separated by spaces!")
    else:
        try:
            print("Maximum:", find_max(nums))
        except ValueError as e:
            print(f"Error: {e}")