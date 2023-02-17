import datetime


class ScheduledRide:

    def __init__(self, origin_time: datetime.time, destination_time: datetime.time, driver_name: str, ride_id: int):
        self._ride_id: int = ride_id
        self._origin_time: datetime.time = origin_time
        self._destination_time: datetime.time = destination_time
        self._driver_name: str = driver_name
        self._delays: int = 0

    def __str__(self):
        return f"Origin time is: {self._origin_time}\n" \
               f"Destination time is: {self._destination_time}\n" \
               f"Driver's name is: {self._driver_name}\n" \
               f"Ride's ID is: {self._ride_id}"

    def get_id(self):
        return self._ride_id
