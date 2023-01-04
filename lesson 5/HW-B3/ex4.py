def upper_lower_count(string: str) -> tuple[int, int]:
    count_lower: int = 0
    count_upper: int = 0
    for letter in string:
        if letter.isupper():
            count_upper += 1
        if letter.islower():
            count_lower += 1
    return count_upper, count_lower


word = input("insert a string: ")
print(upper_lower_count(word))

