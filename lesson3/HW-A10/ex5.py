string = None
end_of_input = True
char_count = 0
dig_count = 0
str_count = 0
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
while end_of_input:
    string = input("insert string or $ for ending: ")
    if string == '$':
        end_of_input = False
    else:
        str_count += 1
        char_count += len(string)
    count = 0
    count_dig_in_string = 0
    while count < len(string):
        if string[count] in digits:
            count_dig_in_string += 1
        count += 1
    if count_dig_in_string == count:
        dig_count += len(string)

print(f"num of strings: {str_count} \nnum of chars: {char_count} \nnum of digits in digits strings: {dig_count}")