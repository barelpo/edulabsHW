import string


class AlphaBetIterator:

    def __init__(self, letter: str):
        if (letter.islower() or letter.isupper()) and len(letter) == 1:
            self._letter = letter
        else:
            raise ValueError
        self._lower_case = list(string.ascii_lowercase)
        self._upper_case = list(string.ascii_uppercase)
        self._iter_index: int = 0

    def __iter__(self):
        for i, letter in enumerate(self._lower_case):
            if self._letter.lower() == letter:
                self._iter_index = i
        return self

    def __next__(self):
        curr_iter_index = self._iter_index
        self._iter_index += 1
        if curr_iter_index >= len(self._lower_case):
            raise StopIteration()
        if self._letter.isupper():
            return self._upper_case[curr_iter_index]
        else:
            return self._lower_case[curr_iter_index]


if __name__ == "__main__":
    while True:
        try:
            char = input("insert a letter: ").strip()
            my_alphabet = AlphaBetIterator(char)
            for j in my_alphabet:
                print(j)
            for j in my_alphabet:
                print(j)
            break
        except ValueError:
            print("Input must be english letter!")
