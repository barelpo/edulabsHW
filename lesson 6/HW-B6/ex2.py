def insert_birthday(name: str, date: str, dates: dict) -> dict:
    if name in dates:
        while True:
            command = input('The name already exists. would you like to overwrite?')
            if command == 'yes':
                break
            elif command == 'no':
                return dates
            else:
                print('invalid choice.')
    birth_date = {name: date}
    dates.update(birth_date)
    return dates


def lookup(name: str, dates: dict) -> str | None:
    possible_names_list = []
    for key in dates:
        if name in key:
            possible_names_list.append(key)
    if len(possible_names_list) == 1 and possible_names_list[0] == name:
        return dates[name]
    elif len(possible_names_list) == 0:
        print('name does not exist')
    else:
        command = input("we can't find the exact values, would you like suggestions?")
        if command == 'yes':
            print('we have: ', end='')
            for option in possible_names_list:
                print(f"{option}", end=', ')
            while True:
                accurate_name = input('if you see the name you need, type the name, else, type no.')
                if accurate_name == 'no':
                    return
                elif accurate_name in possible_names_list:
                    return dates[accurate_name]
                else:
                    print('Invalid choice.')


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

