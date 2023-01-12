num = None
list_of_num = []
min_num = None

while num != '$':
    num = input("insert number or $ to end: ")
    if num != '$':
        list_of_num.append(int(num))

for n in list_of_num:
    if min_num is None:
        min_num = n
    elif n < min_num:
        min_num = n

print(min_num)
