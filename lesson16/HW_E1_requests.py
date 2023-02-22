import requests
import time


names = 'avi, moshe, mahmud, slava, sergey, james, dabash, mangusto, eithan, amir'.replace(" ", "")
names_list = names.split(",")
country_list = []
s = time.time()
for name in names_list:
    response = requests.get(" https://api.nationalize.io/", params={"name": name})
    if response.status_code == 200:
        country_code = response.json()["country"][0]["country_id"]
        response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code}")
        if response.status_code == 200:
            print(response.json()[0]["name"]["common"])
e = time.time()
print(e - s)


