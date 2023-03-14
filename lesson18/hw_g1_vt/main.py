import os
import argparse
from vt_class import *
import datetime
import pprint
import re

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('url', help="URL to scan")
    parser.add_argument('-k', '--apikey')
    parser.add_argument('-s', '--scan', action='store_true')
    parser.add_argument('-t', '--time')

    args = parser.parse_args()
    args.url.replace(' ', '')
    url_list: list = args.url.split(",")

    url_found: list = []
    fail_scan_url: list = []
    completed_get_urls: list = []
    completed_scan_urls: list = []

    if not os.path.exists('cache.json'):
        cache: dict = {}
    else:
        with open('cache.json', 'r') as f:
            cache = json.load(f)

    apikey = "93347ea7b5df6d15486bbdc250d71d0282973aec75e6316b379dac69ffcee2fc"

    if args.apikey:
        vt_scan = VirusTot(['https://www.netflix.com/browse'], args.apikey)
        if vt_scan.check_apikey() == 401:
            pass
        else:
            apikey = args.apikey

    if args.scan:
        vt_scan = VirusTot(url_list, apikey)
        cache, fail_scan_url, completed_scan_urls = vt_scan.scan_url(cache)

    else:
        time = datetime.timedelta(days=180).total_seconds()
        if args.time:
            if re.match(r"^[0-2]\.?[0-9]?$", args.time):
                time = datetime.timedelta(days=float(args.time)*30).total_seconds()

        for url in url_list[-1::-1]:
            if url in cache and datetime.datetime.now().timestamp() - \
                    cache[url]["data"]["attributes"]["last_analysis_date"] < \
                    time:
                url_found.append(url)
                url_list.remove(url)

        if len(url_list) > 0:
            vt_scan = VirusTot(url_list, apikey)
            cache, failed_get_url, completed_get_urls = vt_scan.get_url_analysis(cache, time)
            if failed_get_url > 0:
                cache, fail_scan_url, completed_scan_urls = vt_scan.scan_url(cache)

    for url in url_found + completed_get_urls + completed_scan_urls:
        if url in cache:
            pprint.pprint(f"{url}: {cache[url]}\n\n----------------------------------------------------------\n\n")

    if len(fail_scan_url) > 0:

        print(f"Error occurred while trying to scan the following urls:\n {fail_scan_url}")

    with open('cache.json', 'w') as f:
        json.dump(cache, f)
