limit = int(input("insert number: "))

for num in range(1, limit + 1):
    count = 0
    for factor in range(1, num + 1):
        if num % factor == 0:
            count += 1
    if count <= 2:
        print(num)
        