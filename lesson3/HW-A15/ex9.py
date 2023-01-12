num1 = None
num_list = []
end_of_input = True
even_count = 0
odd_count = 0

while end_of_input:
    num = input("insert number or $ for ending: ")
    if num == '$':
        end_of_input = False
    else:
        num_list.append(num)

for num2 in num_list:
    if int(num2) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"the amount of even numbers is: {even_count} \nthe amount of odd numbers is: {odd_count}")
