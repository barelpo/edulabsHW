class BankAccount:

    def __init__(self, account_num: int, holder_name: str, pp_num: int, address: str, phone: str,
                 allowed_to_usd: bool, nis_balance: float, usd_balance: float, max_cred_lim: int):
        self.__transaction_data = {}
        self.__allowed_to_usd = allowed_to_usd
        self.__max_cred_lim = max_cred_lim
        self.__usd_balance = usd_balance
        self.__nis_balance = nis_balance
        self.__phone = phone
        self.__address = address
        self.__pp_num = pp_num
        self.__holder_name = holder_name
        self.__account_num = account_num

    def deposit(self, money_to_add: float, coin: str, date: str) -> bool:
        if coin.lower() == 'usd' and self.__allowed_to_usd:
            self.__usd_balance += money_to_add
        elif coin.lower() == 'nis':
            self.__nis_balance += money_to_add
        else:
            return False
        if date not in self.__transaction_data:
            self.__transaction_data[date] = []
        self.__transaction_data[date].append({'type': 'deposit', 'amount': money_to_add, 'currency': coin})
        return True

    def withdraw(self, money_to_withdraw: float, coin: str, date: str) -> bool:
        if coin.lower() == 'nis' and \
                self.__nis_balance - money_to_withdraw + self.__usd_balance * 3.4 >= self.__max_cred_lim:
            self.__nis_balance -= money_to_withdraw
        elif coin.lower() == 'usd' and self.__allowed_to_usd is True and \
                (self.__usd_balance - money_to_withdraw) * 3.4 + self.__nis_balance >= self.__max_cred_lim:
            self.__usd_balance -= money_to_withdraw
        else:
            return False
        if date not in self.__transaction_data:
            self.__transaction_data[date] = []
        self.__transaction_data[date].append({'type': 'withdraw', 'amount': money_to_withdraw, 'currency': coin})
        return True

    def convert(self, money_to_transfer: float, coin: str, date: str) -> bool:
        if self.__allowed_to_usd is True:
            if coin == 'nis' and self.__nis_balance >= money_to_transfer:
                self.__nis_balance -= money_to_transfer
                self.__usd_balance += money_to_transfer / 3.40
            elif coin == 'usd' and self.__usd_balance >= money_to_transfer:
                self.__usd_balance -= money_to_transfer
                self.__nis_balance += money_to_transfer * 3.40
            else:
                return False
        else:
            return False
        if date not in self.__transaction_data:
            self.__transaction_data[date] = []
        self.__transaction_data[date].append({'type': 'convert', 'amount': money_to_transfer, 'currency': coin})
        return True

    def get_current_balance(self) -> float | list[str]:
        if self.__allowed_to_usd is True:
            current_balance = [f"NIS balance: {self.__nis_balance}, USD balance: {self.__usd_balance}"]
        else:
            current_balance = f"NIS balance: {self.__nis_balance}"
        return current_balance

    def get_transaction_per_date(self, date: str) -> dict | bool:
        if date in self.__transaction_data:
            return self.__transaction_data[date]
        else:
            return False

    def get_monthly_cash_flow(self, month: str) -> str:
        tot_income: float = 0
        tot_outcome: float = 0
        for date in self.__transaction_data:
            if month in date:
                for transaction in self.__transaction_data[date]:
                    if transaction['type'] == 'deposit':
                        tot_income += transaction['amount']
                    if transaction['type'] == 'withdraw':
                        tot_outcome += transaction['amount']
        return f"Income tot: {tot_income}, Outcome tot: {tot_outcome}"

    def get_annual_cash_flow(self, year: str) -> str:
        tot_income: float = 0
        tot_outcome: float = 0
        for date in self.__transaction_data:
            if year in date:
                for transaction in self.__transaction_data[date]:
                    if transaction['type'] == 'deposit':
                        if transaction['currency'] == 'usd':
                            tot_income += 3.4 * transaction['amount']
                        else:
                            tot_income += transaction['amount']
                    if transaction['type'] == 'withdraw':
                        if transaction['currency'] == 'usd':
                            tot_outcome -= 3.4 * transaction['amount']
                        else:
                            tot_outcome -= transaction['amount']
        return f"Income tot: {tot_income}, Outcome tot: {tot_outcome}"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return self.__account_num == other.__account_num

    def __ne__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return self.__account_num != other.__account_num

    def __int__(self):
        return int(self.__account_num)

    def __add__(self, other):
        return self.__nis_balance + other

    def __iadd__(self, other):
        self.__nis_balance += other
        return self


if __name__ == "__main__":
    ba1 = BankAccount(154, "Israel Moshe", 15247896825, "Mitzpe st. 22/8, Shoham, Israel",
                      "050-9163635", True, 0, 0, -5000)
    print(ba1.deposit(1200.2, "nis", "22.1.2022"))
    print(ba1.deposit(9000, "nis", "23.2.2022"))
    print(ba1.withdraw(1000, 'nis', "23.2.2022"))
    print(ba1.deposit(154.24, "usd", "26.6.2022"))
    print(ba1.convert(1500, "nis", "28.5.2023"))
    print(ba1.convert(200, "usd", "25.7.2022"))
    print(ba1.withdraw(500000, "nis", "21.1.2023"))
    print(ba1.get_monthly_cash_flow("2.2022"))
    print(ba1.get_annual_cash_flow("2022"))
    print(ba1.get_current_balance())
    print(ba1.get_transaction_per_date("23.2.2022"))
    print(int(ba1))
    print(ba1.get_current_balance())
    ba1 += 1000
    print(ba1.get_current_balance())




