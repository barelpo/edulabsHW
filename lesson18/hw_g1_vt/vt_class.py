import json
import base64
import requests
from concurrent.futures import ThreadPoolExecutor, Future, as_completed
from exceptions import *
import time
from threading import Lock
import datetime

vt_url = "https://www.virustotal.com/api/v3/urls"


def get_request(url: str, headers: dict):
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip('=')

    response = requests.get(vt_url + '/' + url_id, headers=headers)
    if response.status_code < 400:
        return url, response.json()
    else:
        raise GetRequestFail(url)


def scan_request(url: str, headers: dict):
    body = {
        "url": url
    }
    response = requests.post(vt_url, data=body, headers=headers)
    if response.status_code < 400:
        return url
    else:
        raise ScanRequestFail(url)


class VirusTot:

    def __init__(self, url_list: list[str], apikey: str = ""):
        self._url_list: list[str] = url_list
        self._headers = {
            "x-apikey": apikey
        }

    def get_url_analysis(self, url_dict_for_user: dict, max_time: float):
        future_list: list = []
        fail_get_url: int = 0
        completed_urls: list = []
        with ThreadPoolExecutor(max_workers=len(self._url_list)) as executor:
            for url in self._url_list:
                future = executor.submit(get_request, url, self._headers)
                future_list.append(future)
        for future in as_completed(future_list):
            try:
                if datetime.datetime.now().timestamp() - \
                        future.result()[1]["data"]["attributes"]["last_analysis_date"] < \
                        max_time:
                    url_dict_for_user[future.result()[0]] = future.result()[1]
                    self._url_list.remove(future.result()[0])
                    completed_urls.append(future.result()[0])
                else:
                    fail_get_url += 1
            except GetRequestFail:
                fail_get_url += 1
        return url_dict_for_user, fail_get_url, completed_urls

    def scan_url(self, url_dict_for_user: dict):

        future_list: list = []
        fail_scan_url: list = []
        url_to_get: list = []
        lock = Lock()
        completed_urls: list = []
        with ThreadPoolExecutor(max_workers=len(self._url_list)) as executor:
            for url in self._url_list:
                future = executor.submit(scan_request, url, self._headers)
                future_list.append(future)
            for future in as_completed(future_list):
                try:
                    url_to_get.append(future.result())
                except ScanRequestFail as e:
                    fail_scan_url.append(e.get_url())
            for url in url_to_get:
                flag = True
                while flag:
                    try:
                        time.sleep(10)
                        future = executor.submit(get_request, url, self._headers)
                        time.sleep(3)
                        if "last_analysis_date" in future.result()[1]["data"]["attributes"]:
                            with lock:
                                url_dict_for_user[future.result()[0]] = future.result()[1]
                                completed_urls.append(future.result()[0])
                            flag = False
                    except GetRequestFail:
                        pass
            return url_dict_for_user, fail_scan_url, completed_urls

    def check_apikey(self):
        url_id = base64.urlsafe_b64encode(self._url_list[0].encode()).decode().strip('=')
        response = requests.get(vt_url + '/' + url_id, headers=self._headers)
        return response.status_code
