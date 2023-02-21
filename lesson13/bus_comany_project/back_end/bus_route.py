import datetime
from lesson13.bus_comany_project.back_end.scheduled_ride import *
import random
from lesson13.bus_comany_project.exceptions import *


class BusRoute:

    def __init__(self, line_number: int, origin: str, destination: str, stops: str):
        self._line_number: int = line_number
        self._origin: str = origin
        self._destination: str = destination
        self._stops: list[str] = stops.split(",")
        self._scheduled_rides: dict[int: ScheduledRide] = {}

    def __str__(self):
        return f"\nThe route number is: {self._line_number}\n" \
               f"The origin station is: {self._origin}.\n" \
               f"The destination station is: {self._destination}.\n" \
               f"The stops of the route are: {self._stops}"

    def set_origin(self, origin: str):
        self._origin = origin

    def set_destination(self, destination: str):
        self._destination = destination

    def set_stops(self, stops: str):
        self._stops: list[str] = stops.split(",")
        for stop in self._stops:
            stop.strip().lower()

    def print_scheduled_rides(self, role: str):
        scheduled_rides_list: list = list(self._scheduled_rides.items())

        def key_by_origin_hour(elem):
            return elem[1].get_origin_time()

        scheduled_rides_list.sort(key=key_by_origin_hour)
        self._scheduled_rides = dict(scheduled_rides_list)
        for ride in self._scheduled_rides:
            if role == 'manager':
                print(self._scheduled_rides[ride])
            elif role == 'customer':
                print(self._scheduled_rides[ride].print_ride_for_customer())

    def add_new_scheduled_ride(self, origin_time: datetime.time, destination_time: datetime.time, driver_name: str):
        if origin_time in self._scheduled_rides:
            raise RideAlreadyExist()
        else:
            while True:
                count: int = 0
                ride_id = random.randint(0, 10**3)
                for ride in self._scheduled_rides:
                    if self._scheduled_rides[ride].get_id() == ride_id:
                        count += 1
                if count == 0:
                    break
            self._scheduled_rides[ride_id] = ScheduledRide(origin_time, destination_time, driver_name, ride_id)

    def get_origin(self):
        return self._origin

    def get_destination(self):
        return self._destination

    def get_bus_stops(self):
        return self._stops

    def report_ride_delay(self, ride_id: int):
        if ride_id in self._scheduled_rides:
            self._scheduled_rides[ride_id].report_delay()
        else:
            raise RideNotExist()

