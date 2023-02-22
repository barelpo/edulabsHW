def vowel_filter(char: str) -> bool:
    return char not in ['a', 'e', 'u', 'o', 'i']


string = input("Insert any string").lower()
print(list(filter(vowel_filter, string)))
