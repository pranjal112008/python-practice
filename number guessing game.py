import random

def play_game(lower=1, upper=100, max_attempts=7):
    secret = random.randint(lower, upper)
    attempts = 0

    print(f"Guess a number between {lower} and {upper}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid integer!")
            continue

        attempts += 1

        if guess == secret:
            print(f"Correct! You won in {attempts} attempt(s).")
            return
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Out of attempts! The number was {secret}.")

if __name__ == "__main__":
    play_game()
