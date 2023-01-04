counter_tot = 0
counter_even = 0

while counter_tot < 10:
    str1 = input("insert string: ")
    counter_tot += 1
    if len(str1) % 2 == 0:
        counter_even += 1

print(f"you've entered {counter_even} strings with even length")



