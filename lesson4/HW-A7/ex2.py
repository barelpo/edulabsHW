goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

ind_list = []

for i, good in enumerate(goods):
    for j, word in enumerate(good):
        if word[0] in ['a', 'u', 'y', 'o', 'e']:
            ind = f"({i},{j})"
            ind_list.append(ind)

print(ind_list)
