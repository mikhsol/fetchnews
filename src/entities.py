import hashlib


class Author(object):
    def __init__(self, first_name=None, second_name=None,
                 position=None, twitter=None):
        self.first_name = first_name
        self.second_name = second_name
        self.position = position
        self.twitter = twitter


class Article(object):
    def __init__(self, author=None, headline=None, text=None,
                 url=None, date=None):
        self.author = author
        self.headline = headline
        self.text = text
        self.url = url
        self.date = date
        self.id = hashlib.sha3_256(bytes(url + date, 'utf-16be')).hexdigest()
