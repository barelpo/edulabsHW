num1 = 0
num2 = 1

print(num1, num2, end=' ')
for i in range(0, 8):
    num3 = num2 + num1
    num1 = num2
    num2 = num3
    print(num3, end=' ')
