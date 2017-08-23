"""
HtmlProcessor -  process html page with article to fetch and clean all
necessary data.
To process web pages from new sources, necessary to implement interfaces from
AbstractHtmlProcessor class.
"""

from bs4 import BeautifulSoup


class AbstractHtmlProcessor(object):
    def get_authors(self):
        raise NotImplementedError

    def get_headline(self):
        raise NotImplementedError

    def get_date(self):
        raise NotImplementedError

    def get_text(self):
        raise NotImplementedError


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
        t = self.soup.find("div", {"itemprop": "articleBody"})
        [div.extract() for div in t.findAll("div")]
        [aside.extract() for aside in t.findAll("aside")]
        return t.get_text(strip=True)
