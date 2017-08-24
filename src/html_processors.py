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
    def __init__(self, html=None):
        self.soup = None
        if html:
            self.soup = BeautifulSoup(html, "html.parser")

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
            logger.error("Probably this article has no text content (comics like article).")


class BbcHtmlProcessor(AbstractHtmlProcessor):
    def get_text(self):
        try:
            t = self.soup.find("div", {"class": "story-body__inner"})
            [div.extract() for div in t.findAll("div")]
            [h1.extract() for h1 in t.findAll("h1")]
            [h2.extract() for h2 in t.findAll("h2")]
            [ul.extract() for ul in t.findAll("ul")]
            [figure.extract() for figure in t.findAll("figure")]
            [hr.extract() for hr in t.findAll("hr")]
            return t.get_text(strip=True)
        except AttributeError:
            logger.error("Probably this article has no text content (comics like article).")

    def get_headline(self):
        h = self.soup.find("h1", {"role": "heading"})
        if h: return h.text.strip()
        h = self.soup.find("h1", {"class": "story-body__h1"})
        if h: return h.text.strip()
        h = self.soup.find("h1", {"class": "story-headline"})
        if h: return h.text.strip()
        return ""

    def get_authors(self):
        a = self.soup.find("span", {"class": "index-body"})
        if a: return [a.text]
        a = self.soup.find("span", {"class": "byline__name"})
        if a: return [a.text]
        return []

    def get_date(self):
        # d = self.soup.find("span", {"class": "publication-date"})
        # if not d:
        #     d = self.soup.find("div", {"class": "date"})
        #     if d: return d.
        return ""
