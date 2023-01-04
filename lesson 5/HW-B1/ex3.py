def max_num(num1: float, num2: float, num3: float) -> float:
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(9.98, 9.8, 1.23))
