num = int(input("insert number: "))

if num < 10:
    print("1 digit")
elif 10 <= num < 100:
    print("2 digit")
elif 100 <= num < 1000:
    print("3 digit")
else:
    print("4 digit")