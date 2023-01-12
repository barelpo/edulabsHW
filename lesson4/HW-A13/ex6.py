num = int(input("insert number: "))

factorial = 1

if num >= 0:
    if num == 0:
        pass
    else:
        for i in range(1, num + 1):
            factorial *= i
    print(factorial)
else:
    print("there is no factorial for negative num")
