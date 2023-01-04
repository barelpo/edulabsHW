def del_duplicates(values: tuple) -> tuple:
    temp_list = []
    for value in values:
        if value not in temp_list:
            temp_list.append(value)
        else:
            pass
    unique_val_tuple = tuple(temp_list)
    return unique_val_tuple


print(del_duplicates((1, 2, 9, 1, 'aba', 8, 2, 'aba')))
