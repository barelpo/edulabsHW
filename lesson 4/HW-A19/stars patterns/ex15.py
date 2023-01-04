n = int(input("insert number: "))

count = 1
for i in range(1, 2 * n):
    if i <= n:
        if i == 1:
            print((n - i) * ' ', end='')
            print('*')
        if 1 < i <= n:
            print((n - i) * ' ', end='')
            print('*', end='')
            print(count * ' ', end='')
            print('*', end='')
            print((n - i) * ' ')
            count += 2
    else:
        if i == n + 1:
            count -= 4
        if n + 1 < i < 2 * n:
            print((i - n - 1) * ' ', end='')
            print('*', end='')
            print(count * ' ', end='')
            print('*', end='')
            print((i - n - 1) * ' ')
            count -= 2
        if i == (2 * n) - 1:
            print((n - 1) * ' ', end='')
            print('*')
