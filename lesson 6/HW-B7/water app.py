import pprint


def add_person(ret_dict: dict, username: str) -> dict:
    ret_dict[username] = {}
    return ret_dict


def add_glasses(username: str, ret_dict: dict) -> dict:
    glasses_per_date = {}
    date = input("insert date: ")
    glasses_amount = int(input("insert how many glasses: "))
    glasses_per_date[date] = glasses_amount
    ret_dict[username].update(glasses_per_date)
    return ret_dict


people = {}
while True:
    action = input("sign up, insert glasses for username or quit ? ")
    if action == "quit":
        break
    person_username = input("insert username? ")
    if action == "sign up":
        pprint.pprint(add_person(people, person_username))
    elif action == "insert":
        pprint.pprint(add_glasses(person_username, people))
