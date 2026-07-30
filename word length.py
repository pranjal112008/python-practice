def word_lengths(words):
    return {word: len(word) for word in words}

if __name__ == "__main__":
    text = input("Enter words separated by spaces: ")
    words = text.split()
    print("Word lengths:", word_lengths(words))