coffee_list = ["Espresso", "Doppio", "Lungo", "Ristretto", "Macchiato", "Corretto", "Con Panna", "Romano", "Cappucino",
               "Americano", "Cafe Latte", "Flat White", "Marocchino", "Mocha", "Bicerin", "Breve", "Raf Coffee",
               "Mead Raf", "Vienna Coffe", "Chocolate Milk", "Latte Macchiato", "Glace", "Freddo", "Irish Coffee",
               "Frappe", "Cappuccino Freddo", "Caramel Frappe", "Espresso Laccino"]
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#time input
time = None
end_of_input = True
hour = None
minute = None

while end_of_input:
    if time is None:
        time = input("Please insert the time when you want to drink the coffee: ")
    else:
        time = input("Wrong input. Please insert the time when you want to drink the coffee again: ")
    hours_minutes = time.split(':')
    count = 0
    for i in hours_minutes:
        for j in i:
            if j not in digits:
                count += 1
    if count == 0:
        if len(hours_minutes) == 2 and hours_minutes[1] != '':
            hour = int(hours_minutes[0])
            minute = int(hours_minutes[1])
            if 0 <= hour <= 24 and 0 <= minute <= 60:
                end_of_input = False

#number of people input
num_of_people = None
end_of_input = True
start_num = None

while end_of_input:
    if num_of_people is None:
        num_of_people = input("Please insert number of people who drink coffee: ")
    else:
        num_of_people = input("Wrong input. Insert number of people again: ")
    count = 0
    for i in num_of_people:
        if i not in digits:
            count += 1
    if count == 0:
        if int(num_of_people) > 0:
            end_of_input = False

#start number input
end_of_input = True
while end_of_input:
    if start_num is None:
        start_num = input("If you want a start number enter the number other wise insert 'no': ")
    elif start_num == 'no':
        break
    else:
        start_num = input("Wrong start number. If you want a start number insert the number other wise insert 'no': ")
    count = 0
    for i in start_num:
        if i not in digits:
            count += 1
    if count == 0:
        if int(num_of_people) > 0:
            hour += int(start_num)
            end_of_input = False

#excluded coffee input
coffee_excluded = []
exclude = None
end_of_input = True
while end_of_input:
    if exclude is None:
        exclude = input("If you would like to exclude some coffee insert it's number. Other wise, insert 'no': ")
    elif exclude == 'no':
        end_of_input = False
    else:
        exclude = input("If you would like to exclude some more coffee insert it's number. Other wise, insert 'no': ")
    count = 0
    for i in exclude:
        if i not in digits:
            count += 1
    if count == 0:
        if 1 <= int(exclude) <= 28:
            coffee_excluded.append(int(exclude))
    elif count > 0:
        print("Wrong coffee number!")

for coffee in coffee_excluded:
    del coffee_list[coffee]




#coffee for user #1
print(f"User #1 should have: {coffee_list[hour % len(coffee_list) - 1]}")

#coffee for all other users
if int(num_of_people) > 1:
    for friend in range(2, int(num_of_people) + 1):
        print(f"User #{friend} should have: {coffee_list[(hour + minute) % len(coffee_list) - 1]}")
