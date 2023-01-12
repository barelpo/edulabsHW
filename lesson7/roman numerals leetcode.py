import pprint


def convert_romans(roman_number: str) -> int:
    num = 0
    flag = True
    roman_value_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i, char in enumerate(roman_number):
        if flag is False:
            flag = True
        elif i < len(roman_number) - 1 and i == 0 and roman_value_dict[char] < roman_value_dict[roman_number[i+1]]:
            num = num + (roman_value_dict[roman_number[i+1]] - roman_value_dict[char])
            flag = False
        elif i == 0:
            num += roman_value_dict[char]
        elif i < len(roman_number) - 1 and roman_value_dict[roman_number[i+1]] > roman_value_dict[char]:
            num = num + (roman_value_dict[roman_number[i+1]] - roman_value_dict[char])
            flag = False
        elif i > 0 and roman_value_dict[char] <= roman_value_dict[roman_number[i-1]]:
            num += roman_value_dict[char]
    return num


number = input("insert roman number: ")
print(convert_romans(number))
