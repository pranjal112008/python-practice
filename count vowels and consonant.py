def count_vowels_consonants(s: str) -> tuple:
    vowels = set('aeiouAEIOU')
    v_count = c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count
if __name__ == "__main__":
    text = input("Enter a word: ").strip()
    vowels, consonants = count_vowels_consonants(text)
    print(f"Vowels: {vowels}, Consonants: {consonants}")
