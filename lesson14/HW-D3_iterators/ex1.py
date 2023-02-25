import datetime


class DateIterator:

    def __init__(self, start_date: datetime.date):
        self._start_date: datetime.date = start_date

    def my_gen(self):
        ret_val = self._start_date + datetime.timedelta(days=1)
        while ret_val.month == self._start_date.month:
            yield ret_val
            ret_val += datetime.timedelta(days=1)


if __name__ == "__main__":
    temp = DateIterator(datetime.date(year=2024, month=11, day=13))
    for elem in temp.my_gen():
        print(elem)
    for elem in temp.my_gen():
        print(elem)
