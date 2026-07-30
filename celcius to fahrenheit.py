def celsius_list_to_fahrenheit(temps):
    return list(map(lambda c: (c * 9 / 5) + 32, temps))

if __name__ == "__main__":
    try:
        temps = list(map(float, input("Enter Celsius temperatures separated by spaces: ").split()))
        print("Fahrenheit:", [round(f, 2) for f in celsius_list_to_fahrenheit(temps)])
    except ValueError:
        print("Please enter valid numbers separated by spaces!")