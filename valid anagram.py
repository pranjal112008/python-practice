from collections import Counter
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)  
if __name__ == "__main__":
    s = input("Enter first string: ").strip().lower()
    t = input("Enter second string: ").strip().lower()
    print(is_anagram(s, t))
