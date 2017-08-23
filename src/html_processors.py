"""
HtmlProcessor -  process html page with article to fetch and clean all
necessary data.
To process web pages from new sources, necessary to implement interfaces from
AbstractHtmlProcessor class.
"""
import logging

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class AbstractHtmlProcessor(object):
    def get_authors(self):
        raise NotImplementedError

    def get_headline(self):
        raise NotImplementedError

    def get_date(self):
        raise NotImplementedError

    def get_text(self):
        raise NotImplementedError


class ArticleParserException(BaseException):
    def __init__(self, msg):
        self.msg = msg


class TheGuardianHtmlProcessor(AbstractHtmlProcessor):
    def __init__(self, html=None):
        self.soup = None
        if html:
            self.soup = BeautifulSoup(html, "html.parser")

    def get_authors(self):
        authors = []
        for a in self.soup.find_all("a", {"rel": "author"}):
            authors.append(a.span.text)

        return authors

    def get_headline(self):
        return self.soup.find("h1", {"class": "content__headline"}) \
            .text.strip()

    def get_date(self):
        d = self.soup.find("time", {"itemprop": "datePublished"})
        return d.text.strip().replace(u"\xa0", u" ")

    def get_text(self):
        try:
            t = self.soup.find("div", {"itemprop": "articleBody"})
            [div.extract() for div in t.findAll("div")]
            [aside.extract() for aside in t.findAll("aside")]
            return t.get_text(strip=True)
        except AttributeError:
            logger.error("Something goes wrong with parsing {}".format(self.get_headline()))
