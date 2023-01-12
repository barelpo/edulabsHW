largest = None
second_largest = None

for i in range(1, 6):
    num = int(input("insert number: "))
    if largest is None:
        largest = num
    else:
        if num <= largest and second_largest is None:
            second_largest = num
        elif num > largest:
            second_largest = largest
            largest = num
        elif second_largest < num < largest:
            second_largest = num
if largest == second_largest:
    second_largest = None

print(second_largest)