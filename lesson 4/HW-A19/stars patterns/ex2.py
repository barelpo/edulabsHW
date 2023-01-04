n = int(input("insert number: "))
k = n-1

for i in range(1, n+1):
    for j in range(1, k + 1):
        print(" ", end='')
    print(i * "* ")
    k -= 1
    print("\n")


