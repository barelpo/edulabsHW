import pprint


def store_new(company_stock_data: dict) -> dict:
    ticker = None
    properties: tuple = ('ticker', 'company name', 'employees num', 'address', 'ceo name')
    for prop in properties:
        user_input = input(f"Insert {prop}:")
        if prop == 'ticker':
            ticker = user_input
            company_stock_data[ticker] = {}
        company_stock_data[ticker][prop] = user_input
    company_stock_data[ticker]['stock data'] = {}
    return company_stock_data


def update_stocks_data(company_stock_data: dict) -> dict:
    date = None
    while True:
        ticker = input("Insert company ticker: ")
        if ticker in company_stock_data:
            break
        else:
            print("Company dose not exist in storage!")
    properties: tuple = ('date', 'open price', 'close price', 'volume')
    for prop in properties:
        if prop == 'date':
            while True:
                user_input = input(f"Insert {prop}: ")
                if user_input in company_stock_data[ticker]['stock data']:
                    print("date already exists")
                else:
                    break
            date = user_input
            company_stock_data[ticker]['stock data'][date] = {}
        else:
            user_input = input(f"Insert {prop}: ")
            company_stock_data[ticker]['stock data'][date][prop] = user_input
    return company_stock_data


def search(company_stock_data: dict) -> dict:
    while True:
        ticker = input("Insert company ticker: ")
        if ticker in company_stock_data:
            return company_stock_data[ticker]
        else:
            print("Company does not exist in storage.")


companies = {}
while True:
    action = input("would you like to store new company, update stock data, search stocks data history or quit?")
    if action == 'store':
        companies = store_new(companies)
        pprint.pprint(companies)
    elif action == 'update':
        companies = update_stocks_data(companies)
        pprint.pprint(companies)
    elif action == 'search':
        pprint.pprint(search(companies))
    elif action == 'quit':
        break
    else:
        print("Invalid input please choose an action.")
