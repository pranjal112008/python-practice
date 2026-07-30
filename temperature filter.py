def above_freezing(temps):
    return list(filter(lambda t: t > 0, temps))

if __name__ == "__main__":
    try:
        temps = list(map(float, input("Enter temperatures (Celsius) separated by spaces: ").split()))
        print("Above freezing:", above_freezing(temps))
    except ValueError:
        print("Please enter valid numbers separated by spaces!")