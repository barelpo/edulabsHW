goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

max_length = 0

for good in goods:
    for word in good:
        if len(word) > max_length:
            max_length = len(word)

vowel_count = 0
for i, good in enumerate(goods):
    for j, word in enumerate(good):
        if len(word) == max_length:
            print(f"({i},{j})")
        for char in word:
            if char in ['a', 'u', 'y', 'o', 'e']:
                vowel_count += 1

print(f"amount of vowels in longest words is: {vowel_count}")

