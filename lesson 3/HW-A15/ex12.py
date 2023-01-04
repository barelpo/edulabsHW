rows = int(input("insert number of rows: "))
columns = int(input("insert number of columns: "))

for row in range(1, rows + 1):
    for column in range(1, columns + 1):
        print('$', end='')
    print('\n')
