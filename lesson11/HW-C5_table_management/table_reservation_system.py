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

    def get_available_tables(self, num_of_people: int) -> dict[int, list[int]]:
        available_tables: dict[int, int] = {}
        for table in self._table_log:
            if self._table_log[table].is_available() and self._table_log[table].get_seats_num() >= num_of_people:
                available_tables[table] = self._table_log[table].get_seats_num()
        sorted_table_list = sorted(zip(available_tables.values(), available_tables.keys()))
        available_tables_sorted: dict[int, list[int]] = {}
        for table in sorted_table_list:
            if table[0] not in available_tables_sorted:
                available_tables_sorted[table[0]] = []
            available_tables_sorted[table[0]].append(table[1])
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
        sorted_seats_list = sorted(zip(available_tables.keys(), available_tables.values()))
        available_tables = dict(sorted_seats_list)
        for seats_num in available_tables:
            sorted_hour_list = sorted(zip(available_tables[seats_num].keys(), available_tables[seats_num].values()))
            available_tables[seats_num] = dict(sorted_hour_list)
        sorted_available_tables = {}
        for seats_num in available_tables:
            sorted_available_tables[seats_num] = {}
            for remaining_time in available_tables[seats_num]:
                sorted_available_tables[seats_num][str(remaining_time)] = available_tables[seats_num][remaining_time]
        return sorted_available_tables

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
        if ':' in max_waiting_time_str:
            max_waiting_time = max_waiting_time_str.split(":")
            max_waiting_time = datetime.timedelta(hours=int(max_waiting_time[0]), minutes=int(max_waiting_time[1]))
        else:
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


if __name__ == '__main__':
    hudson = TableReservationSystem('HUDSON', '1:30')
    hudson.add_a_table(1, 4, 'inside')
    hudson.add_a_table(2, 8, 'terrace')
    hudson.add_a_table(3, 3, 'inside', 'near a toilet')
    hudson.add_a_table(4, 6, 'inside')
    hudson.add_a_table(5, 5, 'terrace')
    hudson.add_a_table(6, 4, 'inside', 'near the exit')
    hudson.add_a_table(7, 2, 'terrace')
    hudson.add_a_table(8, 2, 'bar')
    hudson.add_a_table(9, 2, 'bar')
    hudson.add_a_table(10, 2, 'bar', 'nest to the kitchen')
    hudson.add_a_table(11, 25, 'vip room')
    # print(hudson.get_tables_time_limit())
    # print(hudson._table_log[7]._time_limit)
    hudson.update_tables_time_limit("1:45")
    # print(hudson._table_log[1]._time_limit)
    # pprint.pprint(hudson.get_available_tables(4))
    hudson.reserve_a_table(2, 7)
    # pprint.pprint(hudson.get_available_tables(4))
    hudson.reserve_a_table(8, 2)
    pprint.pprint(hudson.get_available_tables(1))
    hudson.reserve_a_table(4, 4)
    hudson.release_a_table(8)
    pprint.pprint(hudson.get_soonest_available_tables(2))
    # pprint.pprint(hudson.get_tables_within_time_limit('120', 2))
