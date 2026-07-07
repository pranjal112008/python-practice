def countVowelsConsonants(s: str):
    vowels = set('aeiouAEIOU')
    v_count = c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count
input_string = input("Enter a word: ")
print(countVowelsConsonants(input_string))  