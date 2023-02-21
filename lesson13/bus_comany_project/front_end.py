from lesson13.bus_comany_project.exceptions import *
import datetime
import re


def identify() -> str:
    role = input("Are you a manager or a customer? ").strip().lower()
    if role == "customer":
        return role
    elif role == "manager":
        for i in range(1, 4):
            password = input("Insert manager password: ").strip()
            if password == "RideWithUs!":
                return role
            else:
                print("Wrong. Try again.")
            if i == 3:
                raise WrongManagerPassword()


def choose_action(role: str) -> int | str:
    action: str = ''
    if role == 'manager':
        action: str = input("\nPlease choose action number or type quit to exit:\n1.Add route\n"
                            "2.Delete route\n3.Update route\n4.Add scheduled ride\n").strip()
    elif role == 'customer':
        action: str = input("Please choose action number or type quit to exit:\n1.Search route\n2.Report delay\n").strip()
    if role == 'customer' and action in ("1", "2"):
        return int(action)
    if role == 'manager' and action in ("1", "2", "3", "4"):
        return int(action)
    elif action == 'quit':
        return action
    else:
        raise NotValidAction()


def add_route_params() -> tuple:
    while True:
        line_num = input("Please enter route number: ").strip()
        origin = input("Please enter origin station: ").strip().lower()
        destination = input("Please enter final destination: ").strip().lower()
        stops = input("Please enter all route stops separated by commas:\n").replace(' ', '').lower()
        if line_num.isnumeric() and origin and destination and stops:
            return int(line_num), origin, destination, stops
        else:
            print("Route number should represented by digits and all fields should full!")


def get_route_num_from_user() -> int:
    while True:
        line_num = input("Please insert route number:\n").strip()
        if line_num.isnumeric():
            return int(line_num)


def update_route_params() -> dict:
    params_dict: dict = {}
    param_to_update: str = ''
    while True:
        param_to_update: str = input("Please insert what would you like to change or quit: ").strip().lower()
        if param_to_update == 'origin':
            new_origin: str = input("Please insert the new origin for the route: ").strip().lower()
            params_dict[param_to_update] = new_origin
        elif param_to_update == 'destination':
            new_destination: str = input("Please insert new destination for the route: ").strip().lower()
            params_dict[param_to_update] = new_destination
        elif param_to_update == 'stops':
            new_stops: str = input("Please insert new stops for the route separated by commas:\n").strip().lower()
            params_dict[param_to_update] = new_stops
        elif param_to_update == 'quit':
            break
        else:
            print("Not valid parameter. Try again.")

    return params_dict


def get_new_scheduled_ride() -> tuple | None:
    while True:
        check = input("Would you like to add a new ride ? Y/N: ").strip().upper()
        if check == 'Y':
            while True:
                origin_time = input("Please enter the origin time in format hh:mm: ").strip()
                destination_time = input("Please enter the destination time in format hh:mm: ").strip()
                drivers_name = input("Please insert driver's name: ").strip().lower()
                if re.match("^[0-2]?[0-9]:[0-5][0-9]$", origin_time) and \
                        re.match("^[0-2]?[0-9]:[0-5][0-9]$", destination_time):
                    origin_time_converted = datetime.datetime.strptime(origin_time, "%H:%M").time()
                    destination_time_converted = datetime.datetime.strptime(destination_time, "%H:%M").time()
                    if destination_time_converted > origin_time_converted:
                        return origin_time_converted, destination_time_converted, drivers_name
                    else:
                        print("Origin time must be earlier than destination time !")
                else:
                    print("Wrong input !")
        elif check == "N":
            return
        else:
            print("Invalid answer!")


def search_route_by_param() -> tuple:
    while True:
        param = input("Please enter by which parameter you would like to search:\n"
                      "(line number, origin, destination, stop):\n").strip().lower()
        if param in (['line number', 'origin', 'destination', 'stop']):
            search_word = input(f"Please enter {param}: ").strip().lower()
            if param == 'line number' and search_word.isnumeric():
                return param, search_word
            elif param == 'line number' and not search_word.isnumeric():
                print("Line number should be digits!")
            else:
                return param, search_word
        else:
            print("Wrong input! Try again...")


def get_ride_id() -> int:
    while True:
        ride_id = input("Please specify ride by entering ID number: ").strip()
        if ride_id.isnumeric():
            return int(ride_id)
        else:
            print("Ride ID should be numbers!")








































