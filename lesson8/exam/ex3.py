def my_sqrt(num: int) -> int:
    product1 = None
    product2 = None
    if num == 0:
        return 0
    else:
        for i in range(1, num + 1):
            if product1 is None:
                product1 = i * i
            elif product2 is None:
                product2 = i * i
            elif product1 < num and product2 < num:
                product1 = product2
                product2 = i * i
            elif product1 < num < product2 or product1 == num:
                return i - 2
            elif product2 == num:
                return i - 1


print(my_sqrt(3))
print(my_sqrt(4))
print(my_sqrt(8))
print(my_sqrt(9))
print(my_sqrt(15))
print(my_sqrt(16))
print(my_sqrt(20))
print(my_sqrt(0))