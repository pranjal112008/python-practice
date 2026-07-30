from functools import reduce

def alternating_join(words):
    """Joins words together, alternating between '-' and '_' as separators."""
    if not words:
        return ""
    separators = ["-", "_"]

    def combine(acc_and_index, word):
        acc, index = acc_and_index
        sep = separators[index % len(separators)]
        return (f"{acc}{sep}{word}", index + 1)

    result, _ = reduce(combine, words[1:], (words[0], 0))
    return result

if __name__ == "__main__":
    text = input("Enter words separated by spaces: ")
    words = text.split()
    if words:
        print("Joined:", alternating_join(words))
    else:
        print("Please enter at least one word!")