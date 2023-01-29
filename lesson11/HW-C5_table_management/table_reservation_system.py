from table_class import Table
import pprint
import datetime


class TableReservationSystem:

    def __init__(self, restaurant_name: str, max_time_limit_str: str):
        hours_minutes = max_time_limit_str.split(":")
        max_time_limit = datetime.timedelta(hours=int(hours_minutes[0]), minutes=int(hours_minutes[1]))
        self._max_time_limit = max_time_limit
        self._restaurant_name = restaurant_name
        self._table_log: dict[int, Table] = {}

    def get_available_tables(self, num_of_people: int) -> dict[int, int]:
        available_tables: dict[int, int] = {}
        for table in self._table_log:
            if self._table_log[table].is_available() and self._table_log[table].get_seats_num() >= num_of_people:
                available_tables[table] = self._table_log[table].get_seats_num()
        sorted_table_list = sorted(zip(available_tables.values(), available_tables.keys()))
        available_tables_sorted = dict(sorted_table_list)
        return available_tables_sorted

    def get_soonest_available_tables(self, num_of_people: int) -> dict[int, dict[datetime.timedelta, int]]:
        available_tables: dict[int, dict[datetime.timedelta, int]] = {}
        for table in self._table_log:
            if self._table_log[table].get_seats_num() >= num_of_people and \
                    self._table_log[table].is_available() is False:
                if self._table_log[table].get_seats_num() not in available_tables:
                    available_tables[self._table_log[table].get_seats_num()] = {}
                available_tables[self._table_log[table].get_seats_num()]. \
                    update({self._table_log[table].get_time_left(): table})
        return available_tables

    def add_a_table(self, table_id: int, seats_num: int, table_location: str, less_pref_place: str = ''):
        if table_id not in self._table_log:
            self._table_log[table_id] = Table(table_id, seats_num, self._max_time_limit, table_location,
                                              less_pref_place)
            return True
        else:
            return False

    def reserve_a_table(self, table_id: int, num_of_people: int) -> bool:
        if self._table_log[table_id].get_seats_num() >= num_of_people and \
                self._table_log[table_id].is_available() is True:
            self._table_log[table_id].reserve_a_table(num_of_people)
            return True
        else:
            return False

    def release_a_table(self, table_id) -> bool:
        if self._table_log[table_id].is_available() is False:
            self._table_log[table_id].release_a_table()
            return True
        else:
            return False

    def get_tables_within_time_limit(self, max_waiting_time_str: str, num_of_people: int) -> list[int] | bool:
        max_waiting_time = datetime.timedelta(minutes=int(max_waiting_time_str))
        possible_table_options: list = []
        for table in self._table_log:
            if self._table_log[table].get_time_left() <= max_waiting_time and \
                    self._table_log[table].get_seats_num() >= num_of_people and \
                    self._table_log[table].is_available() is False:
                possible_table_options.append(table)
        if len(possible_table_options) > 0:
            return possible_table_options
        else:
            return False

    def get_tables_time_limit(self) -> datetime.timedelta:
        return self._max_time_limit

    def update_tables_time_limit(self, new_time_limit_str: str) -> bool:
        hours_minutes = new_time_limit_str.split(':')
        new_time_limit = datetime.timedelta(hours=int(hours_minutes[0]), minutes=int(hours_minutes[1]))
        self._max_time_limit = new_time_limit
        for table in self._table_log:
            self._table_log[table].update_time_limit(new_time_limit)
        return True
