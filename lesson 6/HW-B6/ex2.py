def insert_birthday(name: str, date: str, dates: dict) -> dict:
    birth_date = {name: date}
    dates.update(birth_date)
    return dates


def lookup(name: str, dates: dict) -> str:
    return dates[name]


birthday_dates = {}
while True:
    action = input("insert or look up or stop ?").lower().strip()
    if action == "stop":
        break
    person_name = input("insert name: ").strip()
    if action == "insert":
        new_date = input("insert date: ").strip()
        print(insert_birthday(person_name, new_date, birthday_dates))
    elif action == "look up":
        print(lookup(person_name, birthday_dates))
    else:
        print("incorrect input!")

