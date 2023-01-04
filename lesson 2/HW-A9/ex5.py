str1 = input("insert first row: ")


rows = str1.split(" ")


if len(rows) == 3:
    print(f"the layout is: {len(rows[0]), len(rows[1]), len(rows[2])}")
elif len(rows) == 1:
    print(f"the layout is: {len(rows[0])}")
else:
    print(f"the layout is: {len(rows[0]), len(rows[1])}")
