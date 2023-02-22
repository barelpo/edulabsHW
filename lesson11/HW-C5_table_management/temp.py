import datetime
import pprint

#
# start = datetime.datetime(2023, 1, 31, 15, 1)
# a = datetime.timedelta(hours=1, minutes=45)
# print(start + a - datetime.datetime.now())
#
#
# durations = {
#     datetime.timedelta(hours=1): 'one hour',
#     datetime.timedelta(hours=1, minutes=45): 'puuuuu',
#     datetime.timedelta(minutes=45): 'forty five minutes'
# }
#
# pprint.pprint(durations)
# for duration, name in durations.items():
#     print(f"{duration}: {name}")

a = input('insert: ')
b = datetime.datetime.strptime(a, '%-d/%m/%y %H:%M')
print(b)
