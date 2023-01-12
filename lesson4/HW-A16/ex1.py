id_num = None
end_of_input = True
sum_digits = 0

while end_of_input:
    id_num = input("insert your id number: ").strip()
    count = 0
    for digit in id_num:
        if digit.isdigit():
            count += 1
    if len(id_num) < 9 or count != 9:
        print("sorry wrong input")
    else:
        end_of_input = False

for i, digit in enumerate(id_num):
    if i == 8:
        break
    elif i % 2 == 0:
        sum_digits += int(digit) * 1
    else:
        if digit in ['0', '1', '2', '3', '4']:
            sum_digits += int(digit) * 2
        else:
            product_number = int(digit) * 2
            sum_digits += product_number // 10 + product_number % 10

if sum_digits % 10 != 0:
    round_sum_digits = (sum_digits // 10 + 1) * 10
    check_digit = round_sum_digits - sum_digits
else:
    check_digit = 0
if check_digit == int(id_num[8]):
    print("The ID number is correct.")
else:
    print("Invalid ID number")
