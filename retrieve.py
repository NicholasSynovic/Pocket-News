from requests import request


class Retrieve:
    def __init__(self, consumerKey: str, tag: str) -> None:
        self.consumerKey = consumerKey
        self.tag = tag

    def retrieveTagItems(self) -> dict:
        request()
