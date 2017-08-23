import unittest

from src.html_processors import TheGuardianHtmlProcessor
from test.constants import TG_AUTHORS, TG_HEADLINE, TG_DATE, TG_TEXT


class TestTheGuardianHtmlProcessor(unittest.TestCase):
    def setUp(self):
        with open("test/data/the_guardian_article_raw_html.txt", "r") as f:
            raw_html = f.read()
        self.p = TheGuardianHtmlProcessor(raw_html)
        self.authors = self.p.get_authors()

    def test_get_author_details(self):
        self.assertTrue(self.authors[0] in TG_AUTHORS)

    def test_get_few_authors_details(self):
        for a in self.authors:
            self.assertTrue(a in TG_AUTHORS)

    def test_get_headline(self):
        self.assertEqual(self.p.get_headline(), TG_HEADLINE)

    def test_get_date(self):
        self.assertEqual(self.p.get_date(), TG_DATE)

    def test_get_text(self):
        self.assertEqual(self.p.get_text(), TG_TEXT)


if __name__ == '__main__':
    unittest.main()
