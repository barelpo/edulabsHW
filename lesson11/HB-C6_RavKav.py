import pprint
import datetime


class RavKav:

    def __init__(self, holder_id: int, holder_name: str):
        self._holder_name = holder_name
        self._holder_id = holder_id
        self._balance = 0
        self._rides_log = {}

    def top_up(self, amount: float) -> bool:
        self._balance += amount
        return True

    def get_current_balance(self) -> float:
        return self._balance

    def ride(self, km: float, ride_date_time_str: str):
        ride_type = ''
        if km <= 15:
            ride_type = 'short'
        elif 15 < km <= 40:
            ride_type = 'medium'
        elif 40 < km:
            ride_type = 'long'
        if (ride_type == 'short' and self._balance < 5.5) or (ride_type == 'medium' and self._balance < 12) or\
                (ride_type == 'long' and self._balance < 23):
            return False
        ride_date_time = datetime.datetime.strptime(ride_date_time_str, "%d-%m-%y %H:%M")
        if ride_date_time.date() not in self._rides_log:
            self._rides_log[ride_date_time.date()] = {}
        self._rides_log[ride_date_time.date()][ride_date_time.time()] = ride_type
        return True

    def get_rides_by_date(self, date_str: str) -> int:
        rides_at_date: int = 0
        date = datetime.datetime.strptime(date_str, "%d-%m-%y").date()
        for i in self._rides_log:
            if i == date:
                rides_at_date = len(self._rides_log[i])
        return rides_at_date

    def get_rides_by_type(self, ride_type: str) -> int:
        type_rides_amount: int = 0
        for i in self._rides_log:
            for j in self._rides_log[i]:
                if self._rides_log[i][j] == ride_type:
                    type_rides_amount += 1
        return type_rides_amount


if __name__ == '__main__':
    barel = RavKav(315825620, 'Barel Polak')
    barel.top_up(1500)
    barel.ride(17, '22-02-23 15:30')
    barel.ride(86, '25-03-23 20:56')
    barel.ride(19, '22-02-23 16:30')
    barel.ride(4, '29-08-23 04:21')
    barel.ride(56, '25-03-23 22:15')
    pprint.pprint(barel._rides_log)
    print(barel.get_rides_by_date('29-08-23'))
    print(barel.get_rides_by_type('medium'))
