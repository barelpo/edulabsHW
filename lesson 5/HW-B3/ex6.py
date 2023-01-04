def palindrome(user_string: str) -> bool:
    rev_string = user_string[::-1]
    if rev_string == user_string:
        return True
    else:
        return False


user_input = input("Insert a string: ")
print(palindrome(user_input))
