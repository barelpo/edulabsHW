n = int(input("insert number: "))
k = 1

for i in range(n, 0, -1):
    for j in range(1, k):
        print(" ", end='')
    print(i * "* ")
    k += 1
    print("\n")

k = n-1

for i in range(1, n+1):
    for j in range(1, k + 1):
        print(" ", end='')
    print(i * "* ")
    k -= 1
    print("\n")