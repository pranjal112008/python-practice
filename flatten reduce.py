from functools import reduce

def flatten_with_reduce(nested_list):
    # reduce version: each step concatenates the accumulator list with the next sublist
    return reduce(lambda acc, sublist: acc + sublist, nested_list, [])

def flatten_with_comprehension(nested_list):
    # for comparison against Day 1's approach
    return [item for sublist in nested_list for item in sublist]

if __name__ == "__main__":
    nested = eval(input("Enter a nested list of lists: "))
    print("Original:", nested)
    print("Flattened (reduce):", flatten_with_reduce(nested))
    print("Flattened (comprehension):", flatten_with_comprehension(nested))