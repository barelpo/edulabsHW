num = input("insert number")
if num != "$$$":
    num = int(num)

sum_num = 0
avg = 0
count = 0

while num != "$$$":
    sum_num += num
    count += 1
    num = input("insert number")
    if num != "$$$":
        num = int(num)

if count > 0:
    avg = sum_num / count

print(f"sum is: {sum_num} \naverage is: {avg}")
