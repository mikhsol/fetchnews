import hashlib


class Article(object):
    def __init__(self, authors=[], headline=None, text=None,
                 url=None, date=None):
        self.authors = authors
        self.headline = headline
        self.text = text
        self.url = url
        self.date = date
        self.id = hashlib.sha3_256(bytes(url + date, 'utf-16be')).hexdigest()

    def __eq__(self, other):
        return self._compare_authors(other) and \
               self.headline == other.headline and \
               self.text == other.text and self.url == other.url and \
               self.date == other.date

    def _compare_authors(self, other):
        for author in self.authors:
            if author not in other.authors: return False
        return True
