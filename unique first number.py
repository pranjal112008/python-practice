def unique_first_letters(names):
    return {name[0].upper() for name in names if name}

if __name__ == "__main__":
    text = input("Enter names separated by spaces: ")
    names = text.split()
    print("Unique first letters:", unique_first_letters(names))