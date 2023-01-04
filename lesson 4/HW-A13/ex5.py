winter_dates = []
autumn_dates = []
summer_dates = []
spring_dates = []

for i in range(1, 11):
    date = input("insert a date: ")
    dd_mm_yy = date.split('.')
    day, month, year = int(dd_mm_yy[0]), int(dd_mm_yy[1]), int(dd_mm_yy[2])
    if 3 <= month <= 5:
        spring_dates.append(date)
    elif 6 <= month <= 8:
        summer_dates.append(date)
    elif 9 <= month <= 11:
        autumn_dates.append(date)
    else:
        winter_dates.append(date)

print(f"there are {len(spring_dates)} spring dates are:")
for date in spring_dates:
    print(date)

print(f"there are {len(summer_dates)} summer dates are:")
for date in summer_dates:
    print(date)

print(f"there are {len(autumn_dates)} autumn dates are:")
for date in autumn_dates:
    print(date)

print(f"there are {len(winter_dates)} winter dates are:")
for date in winter_dates:
    print(date)
