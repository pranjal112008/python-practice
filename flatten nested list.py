def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

if __name__ == "__main__":
    nested = eval(input("Enter a nested list of lists: "))
    print("Original:", nested)
    print("Flattened:", flatten(nested))