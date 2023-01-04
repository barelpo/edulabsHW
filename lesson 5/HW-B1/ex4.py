def factorial(num: int) -> int:
    ret_fact = 1
    for i in range(1, num + 1):
        ret_fact *= i
    return ret_fact


print(factorial(5))
