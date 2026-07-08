from collections import defaultdict
def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
words = input("Enter words separated by spaces: ").split()
result = groupAnagrams(words)
print(result) 