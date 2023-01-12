def alphabet_sort(words: str) -> str:
    words_list = words.split('-')
    words_list.sort()
    sorted_string = ''
    for word in words_list:
        sorted_string += word + '-'
    return sorted_string[:-1]


print(alphabet_sort("yellow-green-red-white-car-dog"))
