def insert(words: list[str]) -> list[str]:
    word: str = input("Insert a word you would like to store: ")
    if word not in words:
        words.append(word)
    return words


def search(words: list[str]) -> list[str]:
    letter: str = input("Insert a letter you would like to search: ")
    num_of_appear: int = int(input("Insert number of appearances: "))
    count = 0
    words_with_letter = []
    for word in words:
        if letter in word:
            for char in word:
                if char == letter:
                    count += 1
        if count == num_of_appear:
            words_with_letter.append(word)
        count = 0
    return words_with_letter


words_list = []
while True:
    action: str = input("Would you like to insert, to search or to quit? ")
    if action == 'insert':
        words_list = insert(words_list)
        print(words_list)
    elif action == 'search':
        print(search(words_list))
    elif action == 'quit':
        break
    else:
        print('Invalid input')

