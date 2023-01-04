term = int(input("please insert term: "))
num_string = ''
num_sum = 0

for i in range(1, term + 1):
    for j in range(1, i+1):
        num_string += '2'
    if len(num_string) > 0:
        num_sum += int(num_string)
    num_string = ''

print(num_sum)
