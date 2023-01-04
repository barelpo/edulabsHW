n = int(input("insert number: "))

count = 1
for i in range(1, n + 1):
    if i == 1:
        print((n - i) * ' ', end='')
        print('*')
    elif 1 < i < n:
        print((n - i) * ' ', end='')
        print('*', end='')
        print(count * ' ', end='')
        print('*', end='')
        print((n - i) * ' ')
        count += 2
    else:
        print((n * 2 - 1) * '*')
