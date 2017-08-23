"""
Fetcher Runner - class which allow to encapsulate complexity of article
fetching and storing data.
Fetcher Runner have one public method run, which evaluate data fetching,
cleaning, combining and storing process.
If you want to add Fetcher Runner for specific source, necessary implement
AbstractFetcherRunner private api.
"""

import logging

import requests
from bs4 import BeautifulSoup

from src.entities import Article
from src.html_processors import TheGuardianHtmlProcessor

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class AbstractFetcherRunner(object):
    def _fetch_articles_links(self):
        raise NotImplementedError

    def _fetch_article_data(self, url):
        raise NotImplementedError

    def _create_article(self, html, url):
        raise NotImplementedError

    def run(self):
        links = self._fetch_articles_links()
        for link in links:
            html = self._fetch_article_data(link)
            article = self._create_article(html, link)
            # self.repository.save(article)
            logger.info("Article: %s - was saved.", article.headline)


class TheGuardianFetcherRunner(AbstractFetcherRunner):
    def __init__(self, repository=None):
        self.url = "https://www.theguardian.com/au"
        self.html_processor = TheGuardianHtmlProcessor()
        self.repository = repository

    def _fetch_articles_links(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        links = [a["href"] for a in soup.find_all("a", {"data-link-name": "article"})]
        return links

    def _fetch_article_data(self, url):
        r = requests.get(url)
        return r.text

    def _create_article(self, html, url):
        self.html_processor.__init__(html)
        return Article(self.html_processor.get_authors(),
                       self.html_processor.get_headline(),
                       self.html_processor.get_text(),
                       url,
                       self.html_processor.get_date())
