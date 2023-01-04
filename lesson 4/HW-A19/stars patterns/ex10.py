n = int(input("insert a number: "))

for i in range(1, n):
    print((n - i) * ' ', end='')
    print(i * '*')
for i in range(n, 0, -1):
    print((n-i) * ' ', end='')
    print(i * '*')


