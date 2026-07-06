from collections import Counter
def firstNonRepeating(s: str) -> str:
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None
input_string = input("Enter a string to find the first non-repeating character: ")
print(firstNonRepeating(input_string))  