goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

new_list = []

for good in goods:
    for word in good:
        if len(word) > 3:
            new_list.append(word[0:len(word)-3])
            new_list[len(new_list) - 1] = word[-1:-4:-1] + new_list[len(new_list) - 1]
        else:
            new_list.append(word[-1::-1])

print(new_list)


