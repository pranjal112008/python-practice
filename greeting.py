def greet():
    print("Hello! Welcome to Python.")
    print("Hope you're having a great day! 😊")
def main():
    name = input("Enter your name (optional): ").strip()
    if name:
        print(f"Hello, {name}!")
    greet()
if __name__ == "__main__":
    main()
