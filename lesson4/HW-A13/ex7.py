num = int(input("insert number: "))

for i in range(1, 11):
    if i < 10:
        print(' ', end='')
    print(f"{i}*{num}={i * num}")

