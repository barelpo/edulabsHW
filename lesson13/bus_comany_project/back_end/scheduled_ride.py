import datetime


class ScheduledRide:

    def __init__(self, origin_time: datetime.time, destination_time: datetime.time, driver_name: str, ride_id: int):
        self._ride_id: int = ride_id
        self._origin_time: datetime.time = origin_time
        self._destination_time: datetime.time = destination_time
        self._driver_name: str = driver_name
        self._delays: int = 0

    def __str__(self):
        return f"\nOrigin time is: {self._origin_time}\n" \
               f"Destination time is: {self._destination_time}\n" \
               f"Driver's name is: {self._driver_name}\n" \
               f"Ride's ID is: {self._ride_id}\n"

    def print_ride_for_customer(self):
        return f"\nOrigin time is: {self._origin_time}\n" \
               f"Destination time is: {self._destination_time}\n" \
               f"Ride's ID is: {self._ride_id}\n" \
               f"Amount of delays for this ride: {self._delays}\n"

    def get_id(self):
        return self._ride_id

    def get_origin_time(self):
        return self._origin_time

    def report_delay(self):
        self._delays += 1
