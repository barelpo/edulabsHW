goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

min_len = None
ind_list = []

for i, good in enumerate(goods):
    for j, word in enumerate(good):
        if min_len is None:
            min_len = len(word)
            ind_list = [f"({i},{j})"]
        elif len(word) < min_len:
            min_len = len(word)
            ind_list = [f"({i},{j})"]
        elif len(word) == min_len:
            ind_list.append(f"({i},{j})")


print(ind_list)
