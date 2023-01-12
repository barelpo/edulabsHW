goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

new_list = []
letter_count = 0

for good in goods:
    for word in good:
        new_list.append(word)
        letter_count += len(word)

print(new_list)
print(f"the amount of letters is: {letter_count}")
