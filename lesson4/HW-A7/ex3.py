goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

new_list = []

for list_word in goods:
    for word in list_word:
        count = 0
        if 'b' in word:
            new_list.append(word)

print(new_list)
