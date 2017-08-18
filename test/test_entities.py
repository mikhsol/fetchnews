import hashlib
import unittest

from src.entities import Author, Article

FIRST_NAME = "Katharine"
SECOND_NAME = "Murphy"
POSITION = "Political Editor"
TWITTER = "@murpharo"


class TestAuthor(unittest.TestCase):
    def test_new_author(self):
        author = Author(FIRST_NAME, SECOND_NAME, POSITION, TWITTER)
        self.assertEqual(author.first_name, FIRST_NAME)
        self.assertEqual(author.second_name, SECOND_NAME)
        self.assertEqual(author.position, POSITION)
        self.assertEqual(author.twitter, TWITTER)


HEADLINE = "Labor questions if Joyce and Nash can make legally " \
           "valid decisions as ministers"
AUTHOR = Author(FIRST_NAME, SECOND_NAME, POSITION, TWITTER)
TEXT = "Labor has opened a new front in the Turnbull government’s" \
       " citizenship crisis, raising the prospect that ministers " \
       "may be unable to validly execute their ministerial duties" \
       " under the constitution while there is a question about " \
       "whether they have been validly elected."
URL = "https://www.theguardian.com/australia-news/2017/aug/18/" \
      "labor-questions-if-joyce-and-nash-can-make-legally-valid" \
      "-decisions-as-ministers"
DATE = "Friday 18 August 2017 12.36 BST"
ID = hashlib.sha3_256(bytes(URL+DATE, 'utf-16be')).hexdigest()


class TestArticle(unittest.TestCase):
    def test_new_article(self):
        article = Article(AUTHOR, HEADLINE, TEXT, URL, DATE)
        self.assertEqual(article.id, ID)
        self.assertEqual(article.author, AUTHOR)
        self.assertEqual(article.headline, HEADLINE)
        self.assertEqual(article.text, TEXT)
        self.assertEqual(article.url, URL)
        self.assertEqual(article.date, DATE)


if __name__ == '__main__':
    unittest.main()
