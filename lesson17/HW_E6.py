import time
import requests
from concurrent.futures import ThreadPoolExecutor


def print_time(sec):
    periods = int(sec // 0.1)
    s = time.time()
    for i in range(periods + 1):
        time.sleep(0.1)
        print(round(time.time() - s, 1))


def get_quote(sec):
    period = int(sec // 1)
    for i in range(period):
        time.sleep(1)
        response = requests.get("https://api.kanye.rest")
        print({'quote': response.json()['quote']})


if __name__ == "__main__":
    seconds = float(input("insert amount of seconds"))
    s = time.time()
    with ThreadPoolExecutor(2) as executor:
        executor.submit(print_time, seconds)
        executor.submit(get_quote, seconds)
    e = time.time()
    print(e - s)




