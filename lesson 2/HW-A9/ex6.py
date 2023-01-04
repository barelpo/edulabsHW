seat_no = input("insert seat number: ")
seat_layout = input("insert seat layout: ")

if len(seat_no) > 2:
    print(f"your raw number is: {seat_no[0:2]}")
    print(f"your seat character is: {seat_no[2]}")
else:
    print(f"your raw number is: {seat_no[0]}")
    print(f"your seat character is: {seat_no[1]}")

if seat_layout.find(seat_no[-1]) == 0 and seat_layout[seat_layout.find(seat_no[-1]) + 1] == " ":
    print("window and aisel")
elif seat_layout.find(seat_no[-1]) == len(seat_layout) - 1 and seat_layout[seat_layout.find(seat_no[-1]) - 1] == " ":
    print("window and aisel")
elif seat_layout[seat_layout.find(seat_no[-1]) + 1] == " " or seat_layout[seat_layout.find(seat_no[-1]) - 1] == " ":
    print("aisel")
elif seat_layout.find(seat_no[-1]) == 0 or seat_layout.find(seat_no[-1]) == len(seat_layout) - 1:
    print("window")
else:
    print("middle")
