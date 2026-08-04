def reverse_string_recursive(s):
    if len(s) <= 1:        # base case: empty or single character is already "reversed"
        return s
    return reverse_string_recursive(s[1:]) + s[0]   # reverse the rest, then tack the first char on the end

if __name__ == "__main__":
    text = input("Enter a string to reverse: ")
    print("Reversed:", reverse_string_recursive(text))