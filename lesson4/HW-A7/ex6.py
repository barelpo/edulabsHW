goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

berry_count = 0
ind_list = []

for i, good in enumerate(goods):
    for j, word in enumerate(good):
        if 'berry' in word:
            berry_count += 1
            ind_list.append(f"({i},{j})")

print(f"the amount of words include berry is: {berry_count}")
print(f"their indexes are: {ind_list}")
