def even_numbers_up_to(n):
    for i in range(0, n + 1, 2):
        yield i

if __name__ == "__main__":
    try:
        n = int(input("Enter upper limit: "))
        print("Even numbers:", list(even_numbers_up_to(n)))
    except ValueError:
        print("Please enter a valid integer!")