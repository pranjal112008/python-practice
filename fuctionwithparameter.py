def greet(name):
    print(f"Hello, {name}! Welcome.")
name = input("Enter your name: ").strip()
if name:
    greet(name)
else:
    print("Hello, Guest!")
