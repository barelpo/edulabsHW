def list_sum(nums: list) -> float:
    ret_sum = 0
    for num in nums:
        ret_sum += num
    return ret_sum


print(list_sum([0, 5, 45, 8, 9, 47]))
