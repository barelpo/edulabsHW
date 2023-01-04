goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

new_list = []

for good in goods:
    for word in good:
        if 'p' in word:
            reverse_word_temp = list(reversed(word))
            reverse_word = ''.join(str(element) for element in reverse_word_temp)
            new_list.append(reverse_word)

print(new_list)


