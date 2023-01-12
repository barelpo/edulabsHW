str = input("please insert a sentence: ")

print(f"amount of words is: {str.count(' ') + 1}")

print(f"amount of chars is: {len(str)}")

print(f"amount of non whitespace chars: {len(str) - str.count(' ')}")

print(f'amount of vowels is: {str.count("a") + str.count("e") + str.count("i") + str.count("o") + str.count("u") + str.count("y")}')

