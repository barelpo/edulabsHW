import pprint


def remove_empty(original_dict: dict, inplace=False) -> dict:
    second_dict = {}
    count = 0
    for key in sorted(original_dict, reverse=True):
        if inplace:
            count = 1
            if original_dict[key] != [] and original_dict[key] != () and original_dict[key] != '' \
                    and original_dict[key] is not None:
                second_dict[key] = original_dict[key]
        else:
            if original_dict[key] == [] or original_dict[key] == () or original_dict[key] == '' \
                    or original_dict[key] == {} or original_dict[key] is None:
                original_dict.pop(key)
    if count == 1:
        return second_dict
    else:
        return original_dict


a = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': ''}
pprint.pprint(remove_empty(a))
