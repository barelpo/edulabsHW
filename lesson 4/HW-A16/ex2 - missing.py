import random

partial_id_num = None
end_of_input = True
sum_digits = 0
id_list = []

while end_of_input:
    partial_id_num = input("insert any random id number or part od it: ").strip()
    count = 0
    if len(partial_id_num) > 8:
        partial_id_num = partial_id_num[0:8]
    for digit in partial_id_num:
        if digit.isdigit():
            count += 1
            id_list.append(int(digit))
    if count != len(partial_id_num):
        print("sorry wrong input")
        id_list = []
    else:
        end_of_input = False

while len(id_list) < 8:
    id_list.append(random.randint(0, 9))

for i, digit in enumerate(id_list):
    if i % 2 == 0:
        sum_digits += digit
    else:
        if digit in ['0', '1', '2', '3', '4']:
            sum_digits += digit * 2
        else:
            product_number = digit * 2
            sum_digits += product_number // 10 + product_number % 10

if sum_digits % 10 != 0:
    round_sum_digits = (sum_digits // 10 + 1) * 10
    id_list.append(round_sum_digits - sum_digits)
else:
    id_list.append(0)

for digit in id_list:
    print(digit, end='')