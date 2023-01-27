import datetime


class Table:

    def __init__(self, table_id: int, seats_num: int, time_limit_str: str, table_location: str, less_pref_place: str = ''):
        self._less_pref_place = less_pref_place
        self._table_location = table_location
        hours_minutes = time_limit_str.split(':')
        time_limit = datetime.timedelta(hours=int(hours_minutes[0]), minutes=int(hours_minutes[1]))
        self._time_limit = time_limit
        self._seats_num = seats_num
        self._table_id = table_id
        self._is_occupied: bool = False
        self._seats_occupied: int = 0
        self._start_time: datetime.datetime = datetime.datetime.min

    def is_available(self) -> bool:
        if self._is_occupied is False:
            return True
        else:
            return False

    def reserve_a_table(self, seats_num: int):
        self._is_occupied = True
        self._seats_occupied = seats_num
        self._start_time = datetime.datetime.now()

    def release_a_table(self):
        self._is_occupied = False
        self._seats_occupied = 0

    def time_left(self) -> datetime.timedelta | bool:
        if self._is_occupied is True:
            return self._start_time + self._time_limit - datetime.datetime.now()
        else:
            return False

    def get_available_hour(self) -> datetime.datetime | bool:
        if self._is_occupied is True:
            return self._start_time + self._time_limit
        else:
            return False


