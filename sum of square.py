def sum_of_squares(numbers):
    return sum(map(lambda n: n ** 2, numbers))

if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("Sum of squares:", sum_of_squares(nums))
    except ValueError:
        print("Please enter valid integers separated by spaces!")