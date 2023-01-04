str1 = input("insert a string: ")

count = 1
ind = -1

while True:
    if str1[ind] == str1[0]:
        break
    count += 1
    ind -= 1

print(count)
