def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
input_string = input("Enter a string to find the length of the longest substring without repeating characters: ")
print(lengthOfLongestSubstring(input_string))