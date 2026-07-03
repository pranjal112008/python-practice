def check_voting_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Please enter a valid age!")
        elif age >= 18:
            print("You are eligible to vote. 🗳️")
        else:
            print(f"You are not eligible to vote. You will be eligible in {18 - age} years.")
    except ValueError:
        print("Please enter a valid age!")
if __name__ == "__main__":
    check_voting_eligibility()
