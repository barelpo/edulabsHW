storage_amount = float(input("please insert storage amount: "))
storage_unit = input("insert storage unit: ")
storage_unit_convert = input("insert the unit you want: ")

if storage_unit == "bytes":
    if storage_unit_convert == "kb":
        storage_amount = storage_amount/1024
    elif storage_unit_convert == "mb":
        storage_amount = storage_amount/(1024**2)
    elif storage_unit_convert == "gb":
        storage_amount = storage_amount/(1024**3)
    elif storage_unit_convert == "tb":
        storage_amount = storage_amount/(1024**4)

elif storage_unit == "kb":
    if storage_unit_convert == "bytes":
        storage_amount = storage_amount*1024
    elif storage_unit_convert == "mb":
        storage_amount = storage_amount/1024
    elif storage_unit_convert == "gb":
        storage_amount = storage_amount/(1024**2)
    elif storage_unit_convert == "tb":
        storage_amount = storage_amount/(1024**3)

elif storage_unit == "mb":
    if storage_unit_convert == "bytes":
        storage_amount = storage_amount*(1024**2)
    elif storage_unit_convert == "kb":
        storage_amount = storage_amount*1024
    elif storage_unit_convert == "gb":
        storage_amount = storage_amount/1024
    elif storage_unit_convert == "tb":
        storage_amount = storage_amount/(1024**2)

elif storage_unit == "gb":
    if storage_unit_convert == "bytes":
        storage_amount = storage_amount*(1024**3)
    elif storage_unit_convert == "kb":
        storage_amount = storage_amount*(1024**2)
    elif storage_unit_convert == "mb":
        storage_amount = storage_amount*1024
    elif storage_unit_convert == "tb":
        storage_amount = storage_amount/1024

elif storage_unit == "tb":
    if storage_unit_convert == "bytes":
        storage_amount = storage_amount*(1024**4)
    elif storage_unit_convert == "kb":
        storage_amount = storage_amount*(1024**3)
    elif storage_unit_convert == "mb":
        storage_amount = storage_amount*(1024**2)
    elif storage_unit_convert == "gb":
        storage_amount = storage_amount*1024

print(f"{storage_amount} {storage_unit_convert}")
