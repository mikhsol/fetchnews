import unittest

from bs4 import BeautifulSoup

AUTHORS = ["Calla Wahlquist", "Gareth Hutchens"]


class HtmlProcessor(object):
    def __init__(self, html=None):
        self.html = html

    def get_authors(self):
        soup = BeautifulSoup(self.html, "html.parser")
        authors = []
        for a in soup.find_all("a", {"rel": "author"}):
            authors.append(a.span.text)

        return authors


class TestArticleProcessor(unittest.TestCase):
    def setUp(self):
        with open("test/data/raw_html.txt", "r") as f:
            raw_html = f.read()
        p = HtmlProcessor(raw_html)
        self.authors = p.get_authors()

    def test_get_author_details(self):
        self.assertTrue(self.authors[0] in AUTHORS)

    def test_get_few_authors_details(self):
        for a in self.authors:
            self.assertTrue(a in AUTHORS)
