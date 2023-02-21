import os
import pickle
from front_end import *
from lesson13.bus_comany_project.back_end.best_bus_company import *
from lesson13.bus_comany_project.exceptions import *


if __name__ == "__main__":

    if not os.path.exists('bus_company.pickle'):
        bus_company = BestBusCompany()
    else:
        with open('bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)

    try:
        role: str = ''
        while role != "customer" and role != "manager":
            try:
                role = identify()
            except WrongManagerPassword:
                print("Three times wrong password!")

        action = None
        while action != 'quit':
            try:
                action = choose_action(role)

                if role == 'manager':
                    if action == 1:
                        params = add_route_params()
                        bus_company.add_bus_route(params[0], params[1], params[2], params[3])

                    elif action == 2:
                        route_num = get_route_num_from_user()
                        bus_company.delete_bus_route(route_num)

                    elif action == 3:
                        route_num = get_route_num_from_user()
                        bus_company.print_specific_route(route_num)
                        params_to_update = update_route_params()
                        bus_company.update_route_params(route_num, params_to_update)

                    elif action == 4:
                        route_num = get_route_num_from_user()
                        bus_company.print_scheduled_rides(route_num, 'manager')
                        new_ride_details = get_new_scheduled_ride()
                        if new_ride_details:
                            bus_company.add_new_ride_for_route(route_num, new_ride_details[0], new_ride_details[1],
                                                               new_ride_details[2])
                        else:
                            pass

                elif role == 'customer':

                    if action == 1 or action == 2:
                        param, search_word = search_route_by_param()
                        if param == 'line number':
                            bus_company.print_specific_route(int(search_word))
                            bus_company.print_scheduled_rides(int(search_word), 'customer')
                        elif param == 'origin' or param == 'destination':
                            bus_company.search_route_origin_destination(param, search_word)
                        elif param == 'stop':
                            bus_company.search_by_bus_stop(search_word.replace(" ", ""))
                        if action == 2:
                            ride_id = get_ride_id()
                            bus_company.report_route_delay(ride_id)

            except NotValidAction:
                print("Invalid action was chosen!")
            except RouteAlreadyExists:
                print("Route you tried to add already exists!")
            except RouteNotExist:
                print("Route you chose does not exist!")
            except RideAlreadyExist:
                print("There is already ride scheduled for this hour!")
            except RideNotExist:
                print("The ride you entered does not exist!")

    except Exception:
        print("Error occurred!")

    finally:
        with open('bus_company.pickle', 'wb') as fh:
            pickle.dump(bus_company, fh)

