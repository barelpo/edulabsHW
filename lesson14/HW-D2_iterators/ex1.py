import datetime


class DateIterator:

    def __init__(self, start_date: datetime.date):
        self._start_date: datetime.date = start_date
        self._iter_counter: int = 0

    def __iter__(self):
        self._iter_counter = 0
        return self

    def __next__(self):
        cur_val = self._start_date + datetime.timedelta(days=self._iter_counter)
        if cur_val.month > self._start_date.month:
            raise StopIteration()
        self._iter_counter += 1
        return cur_val


if __name__ == "__main__":
    for i in DateIterator(datetime.date(year=2024, month=11, day=13)):
        print(i)
    for i in DateIterator(datetime.date(year=2024, month=11, day=13)):
        print(i)
