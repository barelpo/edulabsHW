import string


def pangram(in_string: str) -> bool:
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter in in_string:
            pass
        else:
            return False
    return True


user_input = input("Insert string: ")
print(pangram(user_input))

