def reverse_string(s: str) -> str:
    """Reverse a string using two pointers (in-place on list)."""
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)
if __name__ == "__main__":
    text = input("Enter a string to reverse: ").strip()
    print("Reversed:", reverse_string(text))
