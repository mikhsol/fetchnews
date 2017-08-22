import hashlib
import unittest

from src.entities import Article

AUTHOR = ["Katharine Murphy"]

HEADLINE = "Labor questions if Joyce and Nash can make legally " \
           "valid decisions as ministers"
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
        self.assertEqual(len(article.authors), len(AUTHOR))
        self.assertEqual(article.authors, AUTHOR)
        self.assertEqual(article.headline, HEADLINE)
        self.assertEqual(article.text, TEXT)
        self.assertEqual(article.url, URL)
        self.assertEqual(article.date, DATE)


if __name__ == '__main__':
    unittest.main()
