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
        self._scheduled_rides: list[dict[int: ScheduledRide]] = []
        for stop in self._stops:
            stop.strip().lower()

    def __str__(self):
        return f"The origin station is: {self._origin}.\n" \
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

    def get_scheduled_rides(self):
        self._scheduled_rides = sorted(self._scheduled_rides)
        print(self._scheduled_rides)

    def add_new_scheduled_ride(self, origin_time: datetime.time, destination_time: datetime.time, driver_name: str):
        if origin_time in self._scheduled_rides:
            raise RideAlreadyExist()
        else:
            while True:
                count: int = 0
                ride_id = random.randint(0, 10**1000)
                for ride in self._scheduled_rides:
                    if self._scheduled_rides[ride].get_id() == ride_id:
                        count += 1
                if count == 0:
                    break
            self._scheduled_rides.append({ride_id: ScheduledRide(origin_time, destination_time, driver_name, ride_id)})

