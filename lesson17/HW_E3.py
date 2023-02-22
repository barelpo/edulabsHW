import requests
from concurrent.futures import ThreadPoolExecutor, Future, as_completed
import time


def nationalize(name):
    response = requests.get(" https://api.nationalize.io/", params={"name": name})
    if response.status_code == 200:
        country_code = response.json()["country"][0]["country_id"]
        response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code}")
        if response.status_code == 200:
            return response.json()[0]["name"]["common"]
        else:
            raise Exception("Error")


def callback_fn(future):
    try:
        print(future.result())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # names = input("enter names separated by commas:\n").replace(" ", "")
    names = 'avi, moshe, mahmud, slava, sergey, james, dabash, mangusto, eithan, amir'.replace(" ", "")
    names_list = names.split(",")
    s = time.time()
    with ThreadPoolExecutor(10) as executor:
        for i in range(len(names_list)):
            future = executor.submit(nationalize, names_list[i])
            future.add_done_callback(callback_fn)
    e = time.time()
    print(e - s)
