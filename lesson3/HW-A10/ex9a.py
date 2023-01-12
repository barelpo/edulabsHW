num = input("insert number: ")

ind = -1
rev_num = []

while True:
    if num[ind] == num[0]:
        print(num[ind])
        break
    print(num[ind], end='')
    ind -= 1

