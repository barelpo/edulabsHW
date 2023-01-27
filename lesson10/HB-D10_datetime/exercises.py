import datetime

# # ex1
# print(datetime.timedelta(seconds=float(input('Insert num of seconds: '))))


# ex2
# def ex2(date_in: str):
#     date = datetime.datetime.strptime(date_in, "%Y-%m-%d, %a, %H:%M")
#     return datetime.datetime.isoweekday(date + datetime.timedelta(days=4))
#
#
# print(ex2("2021-12-08, Wed, 10:00"))


# ex3
# def ex3(date_in: str):
#     date = datetime.datetime.strptime(date_in, "%a, %b %d, %Y %I:%M %p")
#     today = datetime.datetime.now()
#     return date - today
#
#
# print(ex3("Mon, Jan 30, 2023 06:00 PM"))


# ex4
# def ex4(date_in: str):
#     date = datetime.datetime.strptime(date_in, "%d-%m-%y")
#     while True:
#         if datetime.datetime.isoweekday(date) == 5:
#             break
#         date += datetime.timedelta(days=1)
#
#     return date.strftime("%d-%m-%Y")
#
#
# print(ex4("26-01-23"))


# ex5
# def ex5(time_in: str):
#     end_of_lecture = datetime.datetime.strptime(time_in, "%H:%M").time()
#     time_left = datetime.datetime.combine(datetime.date.today(), end_of_lecture) - datetime.datetime.now()
#     return time_left
#
#
# print(ex5("20:00"))


# ex6
# def ex6():
#     today = datetime.datetime.now().date()
#     end_of_year = datetime.datetime(today.year, 12, 31).date()
#     days_left = (end_of_year - today).days
#     return days_left
#
#
# print(ex6())


# ex7
# def ex7(day_in: str):
#     today = datetime.datetime.now().date()
#     counter = 0
#     while today.month == datetime.datetime.now().month:
#         if today.strftime("%a") == day_in:
#             counter +=1
#         today += datetime.timedelta(days=1)
#     return counter
#
#
# print(ex7("Wed"))

