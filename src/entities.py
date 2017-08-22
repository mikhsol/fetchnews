import hashlib


class Article(object):
    def __init__(self, author=[], headline=None, text=None,
                 url=None, date=None):
        self.author = author
        self.headline = headline
        self.text = text
        self.url = url
        self.date = date
        self.id = hashlib.sha3_256(bytes(url + date, 'utf-16be')).hexdigest()
