import pprint


class EBook:

    def __init__(self, book_path: str, words_num: int):

        self.book_path = book_path
        self.pages: dict[int: str] = {}
        self._iter_counter: int = 1

        with open(book_path, 'r') as fh:
            content = fh.read()

        all_words: list[str] = content.split()
        page_num = 1
        for i in range(0, len(all_words), words_num):
            page_words = all_words[i: i+words_num]
            self.pages[page_num] = " ".join(page_words)
            page_num += 1

    def get_total_pages(self):
        return len(self.pages)

    def get_page_content(self, page_num) -> str | None:
        if page_num not in self.pages:
            return None
        return self.pages[page_num]

    def __iter__(self):
        self._iter_counter = 1
        return self

    def __next__(self):
        cur_val = self.pages[self._iter_counter]
        if self._iter_counter >= len(self.pages):
            raise StopIteration()
        self._iter_counter += 1
        return cur_val


if __name__ == '__main__':
    book = EBook('../../../evening-ninjas/lesson12/files/data/alice_in_wonderland.txt', 100)
    # print(f"Total pages: {book.get_total_pages()}")
    # print(f"Page 10: {book.get_page_content(27)}")
    # print(book.__dict__)
    # pprint.pprint(book.pages)
    try:
        for i in book:
            print(f"{i}\n")
    except StopIteration:
        pass

