from functools import reduce

def longest_word(words):
    if not words:
        return ""
    return reduce(lambda longest, w: w if len(w) > len(longest) else longest, words)

if __name__ == "__main__":
    text = input("Enter words separated by spaces: ")
    words = text.split()
    if words:
        print("Longest word:", longest_word(words))
    else:
        print("Please enter at least one word!")