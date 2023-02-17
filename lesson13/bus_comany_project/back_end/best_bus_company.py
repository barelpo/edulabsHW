from lesson13.bus_comany_project.back_end.bus_route import *
from lesson13.bus_comany_project.exceptions import *
import pprint


class BestBusCompany:

    def __init__(self):
        self._bus_route_log: dict[int: BusRoute] = {}

    def add_bus_route(self, line_number: int, origin: str, destination: str, stops: str):
        if line_number not in self._bus_route_log:
            self._bus_route_log[line_number] = BusRoute(line_number, origin, destination, stops)
        else:
            raise RouteAlreadyExists()

    def delete_bus_route(self, line_number: int):
        if line_number in self._bus_route_log:
            self._bus_route_log.pop(line_number)
        else:
            raise RouteNotExist()

    def print_specific_route(self, line_number: int):
        if line_number in self._bus_route_log:
            print(self._bus_route_log[line_number])
        else:
            raise RouteNotExist()

    def update_route_params(self, route_num: int, param_to_update: dict):
        for k, v in param_to_update.items():
            if k == 'origin':
                self._bus_route_log[route_num].set_origin(v)
            elif k == 'destination':
                self._bus_route_log[route_num].set_destination(v)
            elif k == 'stops':
                self._bus_route_log[route_num].set_stops(v)

    def print_scheduled_rides(self, route_num: int):
        return self._bus_route_log[route_num].get_scheduled_rides()

    def add_new_ride_for_route(self, route_num: int, origin_time: datetime.time, destination_time: datetime.time,
                               driver_name: str):
        self._bus_route_log[route_num].add_new_scheduled_ride(origin_time, destination_time, driver_name)
