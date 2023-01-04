def tuple_product(nums: tuple) -> float:
    ret_product = 1
    for num in nums:
        ret_product *= num
    return ret_product


print(tuple_product((5, 3, 4)))
