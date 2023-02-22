import datetime


def str_to_date(string: str) -> datetime.date:
    date = datetime.datetime.strptime(string, "%d-%m-%Y")
    return date.date()


def saturday_filter(dates: list):
    converted_dates = map(str_to_date, dates)
    filtered_dates = filter(lambda a: a.weekday() != 5 and a.weekday() != 4, converted_dates)
    return filtered_dates


if __name__ == "__main__":
    print(list(saturday_filter(["12-12-2021", "18-12-2021", "19-12-2021"])))
    print(list(saturday_filter(["13-03-2021", "12-06-2001", "16-08-1985"])))
