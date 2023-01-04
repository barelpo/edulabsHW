def del_list_duplicates(values: list) -> list:
    for j, value in enumerate(values):
        for i in range(len(values) - 1, j, -1):
            if values[i] == value:
                values.pop(i)
    return values


print(del_list_duplicates([1, 5, 'dad', 48, 5, 89, 'mom', 'dad']))
