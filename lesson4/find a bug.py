num1 = int(input("Insert num 1: "))
num2 = int(input("Insert num 2: "))
num3 = int(input("Insert num 3: "))

min_num, middle_num, max_num = None, None, None

if num1 <= num2 and num1 <= num3:
    # the first num is the minimum
    min_num = num1
    if num2 < num3:
        middle_num, max_num = num2, num3
    else:
        middle_num, max_num = num3, num2

elif num2 <= num1 and num2 <= num3:
    # the second num is the minimum
    min_num = num2
    if num1 < num3:
        middle_num, max_num = num1, num3
    else:
        middle_num, max_num = num3, num1

else:
    # the third num is the minimum
    min_num = num3
    if num1 < num2:
        middle_num, max_num = num1, num2
    else:
        middle_num, max_num = num2, num1

print(min_num, middle_num, max_num)