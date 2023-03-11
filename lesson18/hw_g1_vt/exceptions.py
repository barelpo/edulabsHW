class GetRequestFail(Exception):

    def __init__(self, url: str):
        self._url = url

    def message(self):
        return f"Error with url: {self._url}"

    def get_url(self):
        return self._url


class ScanRequestFail(Exception):

    def __init__(self, url: str):
        self._url = url

    def get_url(self):
        return self._url
