str1 = input("please insert a word: ")

str2 = "aeiouy"

if str1[-1] in str2:
    print("it ends with a vowel")
else:
    print("it's not end with a vowel")

num_of_spaces = str1.count(" ")

if num_of_spaces == len(str1):
    print("string of white spaces")
else:
    print("not a string of white spaces")

str3 = input("insert a sentence: ")
print(str3.title())

