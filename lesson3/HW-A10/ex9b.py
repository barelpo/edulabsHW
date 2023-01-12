num = int(input("insert num: "))

rev_num = []
while num > 0:
    rem = num % 10
    num = num // 10
    print(rem, end='')


