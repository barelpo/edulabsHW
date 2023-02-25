def batches(n, my_list):
    dynamic_list = []
    for i, val in enumerate(my_list):
        dynamic_list.append(val)
        if len(dynamic_list) < n and i < len(my_list) - 1:
            pass
        elif len(dynamic_list) <= n:
            yield dynamic_list
            dynamic_list = []


if __name__ == "__main__":
    nums = [1]
    for batch in batches(2, nums):
        print(batch)
