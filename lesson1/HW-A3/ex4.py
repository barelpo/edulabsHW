age = int(input("insert your age: "))
height = int(input("insert your height"))

if (age >= 8 or age <= 18) and height >= 115:
    print("you can ride")
elif age > 18 and height >= 100:
    print("you can ride")
else:
    print("you can't ride")
