def words_longer_than(words, min_length=5):
    return list(filter(lambda w: len(w) > min_length, words))

if __name__ == "__main__":
    text = input("Enter words separated by spaces: ")
    words = text.split()
    min_length = int(input("Enter the minimum length: "))
    print(f"Words longer than {min_length} characters:", words_longer_than(words, min_length))