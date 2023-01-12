n = int(input("insert number: "))

count = 1 + (n - 3)*2
for i in range(1, n + 1):
    if i == 1:
        print((n * 2 - 1) * '*')
    elif 1 < i < n:
        print((i - 1) * ' ', end='')
        print('*', end='')
        print(count * ' ', end='')
        print('*', end='')
        print((i - 1) * ' ')
        count -= 2
    else:
        print((n - 1) * ' ', end='')
        print('*')
