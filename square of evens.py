def squares_of_evens(numbers):
    return {n: n ** 2 for n in numbers if n % 2 == 0}

if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("Squares of even numbers:", squares_of_evens(nums))
    except ValueError:
        print("Please enter valid integers separated by spaces!")