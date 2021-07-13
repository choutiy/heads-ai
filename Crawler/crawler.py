import requests as requests


class Crawler:
    def __init__(self, name, source_url, storage):
        self.name = name
        self.source_url = source_url
        self.storage = storage
        self.cache = requests.get(self.source_url)

    def refresh(self):
        self.cache = requests.get(self.source_url)

    def parse(self):
        raise NotImplementedError(f'{self.__class__.__name__}.parse not implemented')


