import logging
import unittest
from unittest import mock

from src.entities import Article
from src.fetcher_runner import TheGuardianFetcherRunner
from test.constants import TG_LINKS, TG_ARTICLE_URL, TG_AUTHORS, TG_HEADLINE, TG_TEXT, TG_DATE


class MockResponse:
    def __init__(self, t, status_code):
        self.text = t
        self.status_code = status_code


def mocked_the_guardian_fetch_articles_links_get(*args, **kwargs):
    with open("test/data/the_guardian_links_html.txt") as f:
        text = f.read()
    return MockResponse(text, 200)


def mocked_the_guardian_fetch_article_data(*args, **kwargs):
    with open("test/data/the_guardian_article_raw_html.txt", "r") as f:
        raw_html = f.read()
    return MockResponse(raw_html, 200)


class TestTheGuardianFetcherRunner(unittest.TestCase):
    def setUp(self):
        self.fr = TheGuardianFetcherRunner()

    def test_run_method_exist(self):
        self.assertTrue("run" in dir(TheGuardianFetcherRunner))

    @mock.patch('requests.get', side_effect=mocked_the_guardian_fetch_articles_links_get)
    def test_fetch_articles_links(self, mock_get):
        links = self.fr._fetch_articles_links()

        for link in links:
            self.assertTrue(link in TG_LINKS)

    @mock.patch('requests.get', side_effect=mocked_the_guardian_fetch_article_data)
    def test_fetch_article_data(self, mock_get):
        html = self.fr._fetch_article_data(TG_ARTICLE_URL)

        with open("test/data/the_guardian_article_raw_html.txt", "r") as f:
            raw_html = f.read()

        self.assertEqual(raw_html, html)

    def test_create_article(self):
        with open("test/data/the_guardian_article_raw_html.txt", "r") as f:
            raw_html = f.read()

        expected_article = Article(TG_AUTHORS, TG_HEADLINE, TG_TEXT, TG_ARTICLE_URL, TG_DATE)
        article = self.fr._create_article(raw_html, TG_ARTICLE_URL)

        self.assertEqual(expected_article, article)


if __name__ == '__main__':
    unittest.main()
