num = None
list_of_num = []
reverse_list = []


while num != '$':
    num = input("insert number or $ to end: ")
    if num != '$':
        list_of_num.append(int(num))

for n in range(len(list_of_num)-1, -1, -1):
    reverse_list.append(list_of_num[n])

print(reverse_list)
