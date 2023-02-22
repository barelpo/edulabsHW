import datetime
from exceptions import *


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
        self._reservation_log: dict[datetime.datetime, [str, int]] = {}

    def is_available(self) -> bool:
        if self._is_occupied is False:
            if self._reservation_log:
                if list(self._reservation_log.keys())[0] - datetime.datetime.now() >= self._time_limit:
                    return True
            return True
        else:
            return False

    def reserve_a_table(self, seats_num: int):
        self._is_occupied = True
        self._seats_occupied = seats_num
        self._start_time = datetime.datetime.now()
        for res in self._reservation_log:
            if res <= datetime.datetime.now():
                self._reservation_log.pop(res)

    def release_a_table(self):
        self._is_occupied = False
        self._seats_occupied = 0

    def get_available_hour(self) -> datetime.datetime | bool:
        if self._is_occupied is True:
            return self._start_time + self._time_limit
        else:
            return False

    def get_seats_num(self) -> int:
        return self._seats_num

    def get_time_left(self) -> datetime.timedelta:
        key_list = list(self._reservation_log.keys())
        time_left = datetime.timedelta()
        if self.is_available() is False:
            if self._is_occupied is False:
                time_left = (key_list[0] - datetime.datetime.now()) + self._time_limit
            elif self._is_occupied is True:
                time_left = self._start_time + self._time_limit - datetime.datetime.now()
                if key_list[0] - (self._start_time + self._time_limit) < self._time_limit:
                    time_left += key_list[0] - (self._start_time + self._time_limit) + self._time_limit
                else:
                    return time_left
            if len(key_list) > 1:
                for i in range(1, len(key_list)):
                    if key_list[i] - key_list[i - 1] < self._time_limit:
                        time_left += key_list[i] - key_list[i - 1] + self._time_limit
                    else:
                        break
        return time_left

    def update_time_limit(self, new_time_limit: datetime.timedelta) -> bool:
        self._time_limit = new_time_limit
        return True

    def __str__(self):
        return f"Table id: {self._table_id}\nSeats number: {self._seats_num}\nLocation: {self._table_location}"

    def add_future_reservation(self, date_time: datetime.datetime, name: str, num_of_guests: int) -> bool:
        init_len = len(self._reservation_log)
        if date_time not in self._reservation_log and date_time > datetime.datetime.now():
            self._reservation_log[date_time] = [name, num_of_guests]
            sorted_res_list = sorted(zip(self._reservation_log.keys(), self._reservation_log.values()))
            self._reservation_log = dict(sorted_res_list)
            if len(self._reservation_log) > 2:
                keys_list = list(self._reservation_log.keys())
                for i in range(1, len(keys_list) - 1):
                    if keys_list[i] == date_time:
                        if keys_list[i] - keys_list[i - 1] < self._time_limit or\
                                keys_list[i+1] - keys_list[i] < self._time_limit:
                            self._reservation_log.pop(date_time)
                    break
                if (keys_list[0] == date_time and keys_list[1] - keys_list[0] < self._time_limit) or \
                        (keys_list[-1] == date_time and keys_list[-1] - keys_list[len(keys_list) - 2] < self._time_limit):
                    self._reservation_log.pop(date_time)
        if len(self._reservation_log) > init_len:
            return True
        else:
            return False

    def get_reservation_log(self):
        return self._reservation_log




