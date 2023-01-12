num = input("insert 4 digits number: ")
num_as_int = int(num)
left_dig = num_as_int // 1000
right_dig = num_as_int % 10
print(f"left dig is: {left_dig} right digit is: {right_dig}")