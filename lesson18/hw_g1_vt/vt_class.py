import json
import base64
import requests
from concurrent.futures import ThreadPoolExecutor, Future, as_completed
from exceptions import *
import time
from threading import Lock

vt_url = "https://www.virustotal.com/api/v3/urls"

headers = {
        "x-apikey": "93347ea7b5df6d15486bbdc250d71d0282973aec75e6316b379dac69ffcee2fc"
    }


def get_request(url: str):
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip('=')

    response = requests.get(vt_url + '/' + url_id, headers=headers)
    if response.status_code < 400:
        return url, response.json()
    else:
        raise GetRequestFail(url)


def scan_request(url: str):

    body = {
        "url": url
    }
    response = requests.post(vt_url, data=body, headers=headers)
    if response.status_code < 400:
        return url
    else:
        raise ScanRequestFail(url)


class VirusTot:

    def __init__(self, url_list: list[str]):
        self._url_list: list[str] = url_list

    def get_url_analysis(self, url_dict_for_user: dict):
        future_list: list = []
        fail_get_url: int = 0
        with ThreadPoolExecutor(max_workers=len(self._url_list)) as executor:
            for url in self._url_list:

                future = executor.submit(get_request, url)
                future_list.append(future)
        for future in as_completed(future_list):
            try:
                url_dict_for_user[future.result()[0]] = future.result()[1]
                self._url_list.remove(future.result()[0])
            except GetRequestFail:
                fail_get_url += 1
        return url_dict_for_user, fail_get_url

    def scan_url(self, url_dict_for_user: dict):

        future_list: list = []
        fail_scan_url: list = [0]
        url_to_get: list = []
        flag = True
        with ThreadPoolExecutor(max_workers=len(self._url_list)) as executor:
            for url in self._url_list:
                future = executor.submit(scan_request, url)
                future_list.append(future)
            for future in as_completed(future_list):
                try:
                    url_to_get.append(future.result())
                except ScanRequestFail as e:
                    fail_scan_url.append(e.get_url())
            for url in url_to_get:
                while flag is True:
                    try:
                        time.sleep(3)
                        future = executor.submit(get_request, url)
                        url_dict_for_user[future.result()[0]] = future.result()[1]
                        flag = False
                    except GetRequestFail:
                        pass
            return url_dict_for_user, fail_scan_url









