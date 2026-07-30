def remove_vowels(text):
    vowels = set("aeiouAEIOU")
    # List comprehension to keep only non-vowel characters, then join back into a string
    return "".join([char for char in text if char not in vowels])

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Without vowels:", remove_vowels(sentence))