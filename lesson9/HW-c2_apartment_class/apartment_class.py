class Apartment:

    def __init__(self, address: dict, floors_in_building: int, apt_floor: int, rooms: dict, bathrooms: dict,
                 kitchen: dict, balconies: dict = None):

        self.__kitchen = kitchen
        self.__bathrooms = bathrooms
        self.__rooms = rooms
        self.__apt_floor = apt_floor
        self.__floors_in_building = floors_in_building
        self.__address = address
        if balconies is None:
            self.__balconies = {}
        else:
            self.__balconies = balconies

    def get_num_of_rooms(self) -> int:
        return len(self.__rooms)

    def is_last_floor(self) -> bool:
        return self.__floors_in_building == self.__apt_floor

    def get_total_size(self) -> float:
        size_count: float = 0
        for room in self.__rooms:
            size_count += self.__rooms[room]
        for bathroom in self.__bathrooms:
            size_count += self.__bathrooms[bathroom]['size']
        for balcony in self.__balconies:
            size_count += self.__balconies[balcony]
        size_count += self.__kitchen['size']
        return size_count

    def get_living_space(self) -> float:
        size_count: float = 0
        for room in self.__rooms:
            size_count += self.__rooms[room]
        return size_count

    def get_balconies_area(self) -> float | None:
        if self.__balconies != {}:
            size_count: float = 0
            for balcony in self.__balconies:
                size_count += self.__balconies[balcony]
            return size_count
        else:
            return None

    def get_annual_arnona(self, base_tarif: float) -> float:
        tot_area = self.get_total_size()
        balconies_area = self.get_balconies_area()
        arnona_price: float = base_tarif * (tot_area - balconies_area) + base_tarif * 0.75 * balconies_area
        return arnona_price


if __name__ == "__main__":
    my_apartment = Apartment(
        {'country': 'USA', 'city': 'New York', 'street': 'Main St', 'house_num': '1', 'flat_num': '5'},
        10, 8,
        {'bedroom1': 15, 'bedroom2': 12, 'living_room': 20},
        {'bathroom1': {'size': 5, 'toilet': True, 'sink': True, 'bath': True, 'shower': False},
            'bathroom2': {'size': 3, 'toilet': True, 'sink': True, 'bath': False, 'shower': True}},
        {'size': 8},
        {'balcony1': 4, 'balcony2': 2})

    print(my_apartment.get_num_of_rooms())
    print(my_apartment.is_last_floor())
    print(my_apartment.get_total_size())
    print(my_apartment.get_living_space())
    print(my_apartment.get_balconies_area())
    print(my_apartment.get_annual_arnona(1))
