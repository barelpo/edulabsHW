seconds = input("insert time in seconds")
seconds_as_int = int(seconds)
hours = seconds_as_int // 60 // 60
minutes = seconds_as_int // 60 % 60
seconds_left = seconds_as_int % 60
print(f"{hours}:{minutes}:{seconds_left}")


