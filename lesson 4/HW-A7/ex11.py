goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

sublist = []
new_list = []

for good in goods:
    for word in good:
        if len(word) >= 3:
            sublist.append(word[0:3])
        else:
            sublist.append(word)
    new_list.append(sublist)
    sublist = []

print(new_list)
