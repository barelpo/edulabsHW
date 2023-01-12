storage_amount = float(input("please insert storage amount: "))
storage_unit = input("insert storage unit: ")
storage_unit_convert = ""
possible = True

if storage_unit == "bytes":
    if storage_amount // (1024**4) > 0:
        storage_amount = storage_amount / (1024**4)
        storage_unit_convert = "tb"
    elif storage_amount // (1024**3) > 0:
        storage_amount = storage_amount / (1024**3)
        storage_unit_convert = "gb"
    elif storage_amount // (1024**2) > 0:
        storage_amount = storage_amount / (1024**2)
        storage_unit_convert = "mb"
    elif storage_amount // 1024 > 0:
        storage_amount = storage_amount / 1024
        storage_unit_convert = "kb"
    else:
        possible = False

elif storage_unit == "kb":
    if storage_amount // (1024**3) > 0:
        storage_amount = storage_amount / (1024**3)
        storage_unit_convert = "tb"
    elif storage_amount // (1024**2) > 0:
        storage_amount = storage_amount / (1024**2)
        storage_unit_convert = "gb"
    elif storage_amount // 1024 > 0:
        storage_amount = storage_amount / 1024
        storage_unit_convert = "mb"
    elif storage_amount * 1024 > 0:
        storage_amount = storage_amount * 1024
        storage_unit_convert = "bytes"
    else:
        possible = False

elif storage_unit == "mb":
    if storage_amount // (1024**2) > 0:
        storage_amount = storage_amount / (1024**2)
        storage_unit_convert = "tb"
    elif storage_amount // 1024 > 0:
        storage_amount = storage_amount / 1024
        storage_unit_convert = "gb"
    elif storage_amount * 1024 > 0:
        storage_amount = storage_amount * 1024
        storage_unit_convert = "kb"
    elif storage_amount * (1024**2) > 0:
        storage_amount = storage_amount * (1024**2)
        storage_unit_convert = "bytes"
    else:
        possible = False

elif storage_unit == "gb":
    if storage_amount // 1024 > 0:
        storage_amount = storage_amount / 10024
        storage_unit_convert = "tb"
    elif storage_amount * 1024 > 0:
        storage_amount = storage_amount * 1024
        storage_unit_convert = "mb"
    elif storage_amount * (1024**2) > 0:
        storage_amount = storage_amount * (1024**2)
        storage_unit_convert = "kb"
    elif storage_amount * (1024**3) > 0:
        storage_amount = storage_amount * (1024**3)
        storage_unit_convert = "bytes"
    else:
        possible = False

elif storage_unit == "tb":
    if storage_amount * 1024 > 0:
        storage_amount = storage_amount * 1024
        storage_unit_convert = "gb"
    elif storage_amount * (1024**2) > 0:
        storage_amount = storage_amount * (1024**2)
        storage_unit_convert = "mb"
    elif storage_amount * (1024**3) > 0:
        storage_amount = storage_amount * (1024**3)
        storage_unit_convert = "kb"
    elif storage_amount * (1024**4) > 0:
        storage_amount = storage_amount * (1024**4)
        storage_unit_convert = "bytes"
    else:
        possible = False

if possible:
    if storage_amount % 0.1 > 0.04:
        storage_amount = storage_amount - (storage_amount % 0.1) + 0.1
    else:
        storage_amount = storage_amount - (storage_amount % 0.1)
    print(storage_amount, storage_unit_convert)

else:
    print("theres no unit to convert to that the whole number will be grater than 0")









