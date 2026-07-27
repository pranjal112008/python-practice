def binary_search_recursive(sorted_list, target, low=0, high=None):
    """
    Recursively searches for target in sorted_list.
    Returns the index of target, or -1 if not found.
    """
    if high is None:
        high = len(sorted_list) - 1

    if low > high:          # base case: search space is empty, target not found
        return -1

    mid = (low + high) // 2
    if sorted_list[mid] == target:      # base case: found it
        return mid
    elif sorted_list[mid] < target:
        return binary_search_recursive(sorted_list, target, mid + 1, high)  # search right half
    else:
        return binary_search_recursive(sorted_list, target, low, mid - 1)   # search left half

if __name__ == "__main__":
    try:
        numbers = list(map(int, input("Enter a SORTED list of numbers separated by spaces: ").split()))
        if numbers != sorted(numbers):
            print("Warning: list is not sorted. Binary search requires a sorted list.")
        target = int(input("Enter the number to search for: "))
        index = binary_search_recursive(numbers, target)
        if index != -1:
            print(f"Found {target} at index {index}.")
        else:
            print(f"{target} not found in the list.")
    except ValueError:
        print("Please enter valid integers!")