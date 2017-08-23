import unittest

from src.entities import Article
from test.constants import TG_AUTHORS, TG_HEADLINE, TG_TEXT, TG_ARTICLE_URL, TG_DATE, TG_ID


class TestArticle(unittest.TestCase):
    def setUp(self):
        self.article = Article(TG_AUTHORS, TG_HEADLINE, TG_TEXT, TG_ARTICLE_URL, TG_DATE)

    def test_new_article(self):
        self.assertEqual(self.article.id, TG_ID)
        self.assertEqual(len(self.article.authors), len(TG_AUTHORS))
        self.assertEqual(self.article.authors, TG_AUTHORS)
        self.assertEqual(self.article.headline, TG_HEADLINE)
        self.assertEqual(self.article.text, TG_TEXT)
        self.assertEqual(self.article.url, TG_ARTICLE_URL)
        self.assertEqual(self.article.date, TG_DATE)

    def test_equality_article_passed(self):
        a = Article(TG_AUTHORS, TG_HEADLINE, TG_TEXT, TG_ARTICLE_URL, TG_DATE)
        self.assertTrue(self.article == a)

    def test_equality_article_authors_violation(self):
        a = Article(["A B"], TG_HEADLINE, TG_TEXT, TG_ARTICLE_URL, TG_DATE)
        self.assertFalse(self.article == a)


if __name__ == '__main__':
    unittest.main()
