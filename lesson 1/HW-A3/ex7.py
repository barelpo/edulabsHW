year = int(input("insert year: "))

if (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("it's a leap year")
else:
    print("it's not a leap year")
