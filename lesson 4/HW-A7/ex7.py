goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

goods2 = [[], []]

for i, good in enumerate(goods):
    for j, word in enumerate(good):
        if j % 2 == 1:
            word += '2'
        goods2[i].append(word)

print(goods2)
