import unittest

from src.adapters import article_dict_adapter
from src.entities import Article
from test.constants import TG_AUTHORS, TG_HEADLINE, TG_TEXT, TG_ARTICLE_URL, \
    TG_DATE, TG_ID


class TestArticleDictAdapter(unittest.TestCase):
    def test_article_dict_adapter(self):
        a_dict = {"authors": TG_AUTHORS,
                  "headline": TG_HEADLINE,
                  "text": TG_TEXT,
                  "url": TG_ARTICLE_URL,
                  "date": TG_DATE,
                  "id": TG_ID}
        article = Article(TG_AUTHORS, TG_HEADLINE, TG_TEXT,
                          TG_ARTICLE_URL, TG_DATE)

        self.assertEqual(a_dict, article_dict_adapter(article))

if __name__ == "main":
    unittest.main()
