def main():
    name = input("Enter your name: ").strip()
    if name:
        print(f"Hello, {name}!")
        print(f"Welcome to Python programming, {name}!")
    else:
        print("Hello, Guest!")
if __name__ == "__main__":
    main()
