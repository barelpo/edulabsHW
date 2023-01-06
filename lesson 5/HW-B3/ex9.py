def pascal_triangle(n: int):
    string1 = (n - 1) * ' ' + '1' + (n - 1) * ' '
    string2 = (n - 2) * ' ' + '1' + ' ' + '1' + (n - 2) * ' '
    if n == 1:
        print(string1)
    elif n >= 2:
        print(f"{string1}\n{string2}")
    if n > 2:
        for i in range(3, n + 1):
            string1 = ''
            for j, char in enumerate(string2):
                if j < len(string2) - 1:
                    if string2[j + 1] == ' ' and j != n + i - 2:
                        print(' ', end='')
                        string1 += ' '
                    elif j == n - i or j == n + i - 2:
                        print('1', end='')
                        string1 += '1'
                        if j == n + i - 2:
                            print(((len(string2) - 1) - (n + i - 2)) * ' ')
                            string1 += ((len(string2) - 1) - (n + i - 2)) * ' '
                            break
                    else:
                        num = int(string2[j - 1]) + int(string2[j + 1])
                        print(str(num), end='')
                        string1 += str(num)
            string2 = string1
        print('1')


lines = int(input("insert amount of lines: "))
pascal_triangle(lines)



