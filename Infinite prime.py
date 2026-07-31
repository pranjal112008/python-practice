def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def infinite_primes():
    """Generator that yields prime numbers forever. Never terminates on its own —
    the caller decides when to stop pulling values (e.g. with itertools.islice,
    or by breaking out of a loop)."""
    n = 2
    while True:          # this is what makes it "infinite" — no stopping condition here
        if is_prime(n):
            yield n
        n += 1

if __name__ == "__main__":
    try:
        count = int(input("How many primes do you want? "))
        if count <= 0:
            print("Please enter a positive number.")
        else:
            gen = infinite_primes()
            primes = [next(gen) for _ in range(count)]
            print(f"First {count} primes: {primes}")
    except ValueError:
        print("Please enter a valid integer!")