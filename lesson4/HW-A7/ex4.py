goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]


sublist1 = 0
sublist2 = 0
for i, good in enumerate(goods):
    for j, word in enumerate(good):
        for letter in word:
            if letter in ['a', 'u', 'y', 'o', 'e']:
                if i == 0:
                    sublist1 += 1
                else:
                    sublist2 += 1

if sublist1 > sublist2:
    print('0')
else:
    print('1')
