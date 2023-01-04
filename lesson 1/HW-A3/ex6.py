day = int(input("insert day: "))
month = int(input("insert month: "))
year = int(input("insert year: "))

if 1 <= month <= 2 or month == 12:
    print("it's winter")
elif 3 <= month <= 5:
    print("it's spring")
elif 6 <= month <= 8:
    print("it's summer")
else:
    print("it's autumn")

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("there are 31 days in this month")
elif month == 2:
    print("there are 28/29 days in this month")
else:
    print("there are 30 days in this month")