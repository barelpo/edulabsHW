import os
import argparse
from vt_class import *
import datetime
import pprint

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('url', help="URL to scan")
    parser.add_argument('-k', '--apikey')
    parser.add_argument('-s', '--scan', action='store_true')

    args = parser.parse_args()
    args.url.replace(' ', '')
    url_list: list = args.url.split(",")

    url_found: list = []
    fail_scan_url: list = []

    if not os.path.exists('temp.json'):
        cache: dict = {}
    else:
        with open('temp.json', 'r') as f:
            cache = json.load(f)

    for url in url_list[-1::-1]:
        if url in cache and datetime.datetime.now().timestamp() - \
                cache[url]["data"]["attributes"]["last_analysis_date"] < \
                datetime.timedelta(days=180).total_seconds():
            url_found.append(url)
            url_list.remove(url)

        elif url in cache and datetime.datetime.now().timestamp() - \
                cache[url]["data"]["attributes"]["last_analysis_date"] > \
                datetime.timedelta(days=180).total_seconds():
            cache.pop(url)

    if len(url_list) > 0:
        vt_scan = VirusTot(url_list)
        cache, failed_get_url = vt_scan.get_url_analysis(cache)
        if failed_get_url > 0:
            cache, fail_scan_url = vt_scan.scan_url(cache)

    for url in url_list + url_found:
        pprint.pprint(f"{url}: {cache[url]}")

    if len(fail_scan_url) > 0:

        print(f"Error occurred while trying to scan the following urls:\n {fail_scan_url}")




    # print(type(args.url), args.apikey, args.scan)
    #
    # if not os.path.exists('temp.json'):
    #     cache: dict = {}
    # else:
    #     with open('temp.json', 'r') as f:
    #         cache = json.load(f)
    #
    # urls: list = args.url.split(",")
    # for url in urls:
    #     url_for_vt = VirusTot(url)
    #     if args.scan is False:
    #         response_get = url_for_vt.get_url_analysis()
    #         if response_get is not None:
    #             cache[url] = response_get
    #         else:
    #             response_scan = url_for_vt.scan_url()
    #             if response_scan == 200:
    #                 cache[url] = response_scan
    #     else:
    #         response_scan = url_for_vt.scan_url()
    #         if response_scan == 200:
    #             response_get = url_for_vt.get_url_analysis()
    #             if response_get is not None:
    #                 cache[url] = response_get

    with open('temp.json', 'w') as f:
        json.dump(cache, f)
