import unittest

from bs4 import BeautifulSoup

AUTHORS = ["Calla Wahlquist", "Gareth Hutchens"]
HEADLINE = "Coalition says citizenship crisis will last months but MPs " \
           "will keep voting"


class HtmlProcessor(object):
    def __init__(self, html=None):
        self.soup = BeautifulSoup(html, "html.parser")

    def get_authors(self):
        authors = []
        for a in self.soup.find_all("a", {"rel": "author"}):
            authors.append(a.span.text)

        return authors

    def get_headline(self):
        return self.soup.find("h1", {"class": "content__headline"})\
            .text.strip()


class TestArticleProcessor(unittest.TestCase):
    def setUp(self):
        with open("test/data/raw_html.txt", "r") as f:
            raw_html = f.read()
        self.p = HtmlProcessor(raw_html)
        self.authors = self.p.get_authors()

    def test_get_author_details(self):
        self.assertTrue(self.authors[0] in AUTHORS)

    def test_get_few_authors_details(self):
        for a in self.authors:
            self.assertTrue(a in AUTHORS)

    def test_get_headline(self):
        self.assertEqual(self.p.get_headline(), HEADLINE)
