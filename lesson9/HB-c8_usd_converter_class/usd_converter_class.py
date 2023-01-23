import pprint


class UsdConvert:

    def __init__(self):
        self.convert_usd = {}

    def add_exchange_rate(self, currency: str, amount: float, direction: str) -> bool:

        if currency not in self.convert_usd:
            if direction == 'from usd':
                self.convert_usd[currency] = amount
                return True
            elif direction == 'to usd':
                self.convert_usd[currency] = 1 / amount
                return True
            else:
                return False
        else:
            return False

    def update_exchange_rate(self, currency: str, amount: float, direction: str) -> bool:
        if currency in self.convert_usd:
            if direction == 'from usd':
                self.convert_usd[currency] = amount
                return True
            elif direction == 'to usd':
                self.convert_usd[currency] = 1 / amount
                return True
            else:
                return False
        else:
            return False

    def get_exchange_rate_from_usd(self, currency: str):
        if currency in self.convert_usd:
            return self.convert_usd[currency]
        else:
            return False

    def get_exchange_rate_to_usd(self, currency: str):
        if currency in self.convert_usd:
            return 1 / self.convert_usd[currency]
        else:
            return False

    def delete_exchange_rate(self, currency: str) -> bool:
        if currency in self.convert_usd:
            self.convert_usd.pop(currency)
            return True
        else:
            return False

    def convert_from_usd(self, currency: str, amount: float) -> float | bool:
        if currency in self.convert_usd:
            return amount * self.convert_usd[currency]
        else:
            return False

    def convert_to_usd(self, currency: str, amount: float) -> float | bool:
        if currency in self.convert_usd:
            return amount * (1 / self.convert_usd[currency])
        else:
            return False

    def print_all_exchange_rates_from_usd(self):
        for currency in self.convert_usd:
            print(f"USD = {self.convert_usd[currency]} {currency}")
        return True

    def print_all_exchange_rates_to_usd(self):
        for currency in self.convert_usd:
            print(f"{currency} = {1 / self.convert_usd[currency]} USD")
        return True


if __name__ == '__main__':
    usd_converter = UsdConvert()
    usd_converter.add_exchange_rate('NIS', 3.16, 'from usd')
    usd_converter.add_exchange_rate('Japanese Yen', 113.73, 'from usd')
    usd_converter.add_exchange_rate('Euro', 0.89, 'from usd')
    pprint.pprint(usd_converter.convert_usd)
    print(usd_converter.get_exchange_rate_from_usd('Japanese Yen'))
    print(usd_converter.get_exchange_rate_to_usd('Japanese Yen'))
    print(usd_converter.convert_to_usd('Japanese Yen', 30000))
    print(usd_converter.convert_from_usd('Euro', 134))
    usd_converter.update_exchange_rate('Euro', 0.96, 'from usd')
    pprint.pprint(usd_converter.convert_usd)
    usd_converter.delete_exchange_rate('Japanese Yen')
    pprint.pprint(usd_converter.convert_usd)
    print(usd_converter.convert_to_usd('Euro', 3000))
    usd_converter.print_all_exchange_rates_from_usd()
    usd_converter.print_all_exchange_rates_to_usd()


