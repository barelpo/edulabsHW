n = int(input("insert a number: "))

for i in range(n, 0, -1):
    print((n-i) * ' ', end='')
    print(i * '*')
