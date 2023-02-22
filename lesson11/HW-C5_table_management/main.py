import datetime
from table_reservation_system import TableReservationSystem
from table_class import Table
from exceptions import *

if __name__ == '__main__':
    hudson = TableReservationSystem("HUDSON", "1:30")
    hudson.add_a_table(1, 6, 'd')
    hudson.add_a_table(2, 4, 'k')
    hudson.add_a_table(3, 8, 'k')
    hudson.add_a_table(4, 2, 'l')
    hudson.add_a_table(5, 7, 't')
    hudson.add_a_table(6, 4, 't')
    hudson.add_a_table(7, 5, 'k')
    while True:
        action = input("Menu:\n1.Add a table\n2.Reserve a table\n3.Release a table\n4.Add future reservation\n"
                       "5.Get available tables\n6.Check available tables within time limit\n"
                       "7.Get all future reservations for table\nchoose the option number: ")
        if action == '1':
            try:
                table_num = int(input("Insert table number: "))
                seats_num = int(input("Insert number of seats: "))
                table_location = input("Insert table location: ")
                hudson.add_a_table(table_num, seats_num, table_location)
            except TableAlreadyExists:
                print("Table already exist in the system")

        elif action == '2':

            try:
                table_id = int(input("Insert table number: "))
                people_amnt = int(input("Insert number of guests: "))
                hudson.reserve_a_table(table_id, people_amnt)
            except CanNotReserveTable:
                print("Not able to reserve the table. Already occupied or not enough seats.")

        elif action == '3':
            try:
                table_id = int(input("Insert table number: "))
                hudson.release_a_table(table_id)
            except CanNotReleaseTable:
                print("Not able to release table")

        elif action == '4':
            try:
                date_time_str = input('Please enter date and time of reservation (in format: d-m-yy H:MM): ')
                date_time = datetime.datetime.strptime(date_time_str, "%d/%m/%y %H:%M")
                name = input('Insert customer name: ')
                table_id = int(input('Insert table number: '))
                guests_num = int(input('Insert number of guests: '))
                hudson.add_future_reservation(date_time, name, table_id, guests_num)
            except CanNotReserveTable:
                print('Not able to reserve. Table not available at the time or table to small.')

        elif action == '5':
            guests_num = int(input('Insert num of guests: '))
            print(hudson.get_available_tables(guests_num))



