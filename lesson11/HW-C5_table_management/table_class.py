import datetime


class Table:

    def __init__(self, table_id: int, seats_num: int, time_limit: datetime.timedelta, table_location: str,
                 less_pref_place: str = ''):
        self._less_pref_place = less_pref_place
        self._table_location = table_location
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

    def get_seats_num(self) -> int:
        return self._seats_num

    def get_time_left(self) -> datetime.timedelta:
        time_left = self._start_time + self._time_limit - datetime.datetime.now()
        return time_left

    def update_time_limit(self, new_time_limit: datetime.timedelta) -> bool:
        self._time_limit = new_time_limit
        return True


