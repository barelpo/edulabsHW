class Apartment:

    def __init__(self, address: str, parking_type: str, rooms_num: int, size: float, floor: int, balcony: bool,
                 is_penthouse: bool, is_villa: bool, monthly_municipal_tax: float, deal_state: str, pets_allowed: bool):
        self._pets_allowed = pets_allowed
        self._deal_state = deal_state
        self._monthly_municipal_tax = monthly_municipal_tax
        self._is_villa = is_villa
        self._is_penthouse = is_penthouse
        self._balcony = balcony
        self._floor = floor
        self._size = size
        self._rooms_num = rooms_num
        self._parking_type = parking_type
        self._address = address

    def get_annual_municipal_tax(self):
        return 12 * self._monthly_municipal_tax

    def close_deal(self):
        return self._deal_state


class ApartmentForSale(Apartment):

    def __init__(self, address: str, parking_type: str, rooms_num: int, size: float, floor: int, balcony: bool,
                 is_penthouse: bool, is_villa: bool, monthly_municipal_tax: float, deal_state: str, pets_allowed: bool,
                 sale_price: float):
        super().__init__(address, parking_type, rooms_num, size, floor, balcony, is_penthouse, is_villa,
                         monthly_municipal_tax, deal_state, pets_allowed)
        self._sale_price = sale_price

    def get_agency_fee(self):
        return 0.02 * self._sale_price


class ApartmentForRent(Apartment):

    def __init__(self, address: str, parking_type: str, rooms_num: int, size: float, floor: int, balcony: bool,
                 is_penthouse: bool, is_villa: bool, monthly_municipal_tax: float, deal_state: str, pets_allowed: bool,
                 rent_price_per_month: float):
        super().__init__(address, parking_type, rooms_num, size, floor, balcony, is_penthouse, is_villa,
                         monthly_municipal_tax, deal_state, pets_allowed)
        self.rent_price_per_month = rent_price_per_month

    def get_annual_rent_price(self):
        return self.rent_price_per_month * 12

    def get_agency_fee(self):
        return self.rent_price_per_month


