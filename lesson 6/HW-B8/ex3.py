import pprint


def bad_stock_day(dates: list[str], tickers: list[str]) -> dict:
    date_ticker_dict = {}
    ticker_date_dict = {}
    for date in dates:
        current_date_list = []
        current_ticker_list = []
        if date not in date_ticker_dict:
            for i, ticker in enumerate(tickers):
                if dates[i] == date:
                    current_date_list.append(ticker)
            date_ticker_dict[date] = current_date_list
    return date_ticker_dict


dates_list = ["11-05-22",    "12-05-22", "13-05-22", "12-05-22", "11-05-22", "11-05-22"]
tickers_list = ["TSLA",        "TSLA",     "AAPL",     "MSFT",     "AAPL",     "IBM"]
pprint.pprint(bad_stock_day(dates_list, tickers_list))
