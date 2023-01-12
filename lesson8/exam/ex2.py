def fizzbuzz(num: int) -> list[str]:
    ret_val: list[str] = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            ret_val.append("FizzBuzz")
        elif i % 3 == 0:
            ret_val.append("Fizz")
        elif i % 5 == 0:
            ret_val.append("Buzz")
        else:
            ret_val.append(f"{i}")
    return ret_val


print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(type(fizzbuzz(15)[0]))
