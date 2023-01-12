import pprint
people = {}


def insert(number: int) -> dict:
    fields = ('id_num', 'name', 'last name', 'birth date', 'address')
    id_num = None
    for i in range(1, number + 1):
        individual = {}
        for field in fields:
            user_input = input(f"insert {field}: ")
            individual[field] = user_input
            if field == 'id_num':
                id_num = int(user_input)
        people[id_num] = individual

    return people


num_of_people = int(input("insert number of people: "))
pprint.pprint(insert(num_of_people))

