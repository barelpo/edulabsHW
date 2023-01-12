def perfect_num(num: int) -> bool:
    sum_dev = 0
    for i in range(1, num):
        if num % i == 0:
            sum_dev += i

    if num == sum_dev:
        return True
    else:
        return False


print(perfect_num(8128))
