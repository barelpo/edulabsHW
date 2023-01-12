total_minutes = int(input("insert movie length in minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
if minutes < 10:
    print(f"movie length is {hours}:0{minutes}")
else:
    print(f"movie length is {hours}:{minutes}")
