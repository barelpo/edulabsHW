import datetime
from lesson13.bus_comany_project.back_end.scheduled_ride import *

s = {'g': ScheduledRide(datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=45), "moshe", 1)}

a = {1: 'a',
     2: 'b',
     3: 'c'}

b = list(a.items())

print(dict(b))