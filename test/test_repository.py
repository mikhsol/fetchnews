import logging
import unittest

from src.repositories import ArticleMongoDbRepository

logger = logging.basicConfig(level=logging.WARNING)

SINGLE_ARTICLE = {
    "id": 1,
    "authors": ["John Von Neumann"],
    "headline": "About computers",
    "text": "Blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah computer blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah",
    "url": "test.com",
    "date": "15 December 1932"
}

BULK = [
    {"id": 1,
     "authors": ["John Von Neumann"],
     "headline": "About computers",
     "text": "Blah blah blah blah blah blah blah blah blah blah blah blah "
             "blah blah blah blah computer blah blah blah blah blah blah blah blah "
             "blah blah blah blah blah blah blah blah blah",
     "url": "test.com",
     "date": "15 December 1932"},
    {"id": 2,
     "authors": ["John Lennon"],
     "headline": "About love",
     "text": "Blah blah blah blah blah blah blah blah blah blah blah blah "
             "blah blah blah blah love blah blah blah blah blah blah blah blah "
             "blah blah blah blah blah blah blah blah blah",
     "url": "test.com",
     "date": "15 December 1967"},
    {"id": 3,
     "authors": ["John Steinbeck"],
     "headline": "About war",
     "text": "Blah blah blah blah blah blah blah blah blah blah blah blah "
             "blah blah blah blah war blah blah blah blah blah blah blah blah "
             "blah blah blah blah blah blah blah blah blah",
     "url": "test.com",
     "date": "15 December 1932"},
    {"id": 4,
     "authors": ["Leo Tolstoy"],
     "headline": "About war and peace",
     "text": "Blah blah blah blah blah blah blah blah blah blah blah blah "
             "blah blah blah blah war blah blah blah blah blah blah blah blah "
             "blah blah blah blah blah peace blah blah blah blah",
     "url": "test.com",
     "date": "15 December 1872"},
]


class TestArticleMongoDbRepositoryIntegration(unittest.TestCase):
    test_db = "test_newsfetcher"

    def setUp(self):
        self.r = ArticleMongoDbRepository()
        self.r.connect(db=self.test_db)

    def tearDown(self):
        self.r.drop_db(self.test_db)

    def test_save_single_article(self):
        self.r.save(SINGLE_ARTICLE)
        db_obj = self.r.get_by_id(1)
        self.assertEqual(SINGLE_ARTICLE["id"], db_obj["id"])
        self.assertEqual(SINGLE_ARTICLE["authors"], db_obj["authors"])
        self.assertEqual(SINGLE_ARTICLE["headline"], db_obj["headline"])
        self.assertEqual(SINGLE_ARTICLE["url"], db_obj["url"])
        self.assertEqual(SINGLE_ARTICLE["date"], db_obj["date"])

    def test_save_bulk_articles(self):
        self.r.bulk_save(BULK)
        db_obj = self.r.get_all()
        self.assertEqual(len(BULK), db_obj.count())

    def test_search_by_keyword_single_word(self):
        self.r.bulk_save(BULK)
        db_obj = self.r.search_by_keywords(["war"])
        self.assertEqual(2, db_obj.count())
        db_obj = self.r.search_by_keywords(["bomb"])
        self.assertEqual(0, db_obj.count())

    def test_search_by_keyword_multiple_word(self):
        self.r.bulk_save(BULK)
        db_obj = self.r.search_by_keywords(["computer", "peace"])
        self.assertEqual(2, db_obj.count())
        db_obj = self.r.search_by_keywords(["war", "love", "computer"])
        self.assertEqual(4, db_obj.count())
        db_obj = self.r.search_by_keywords(["bomb", "cafe"])
        self.assertEqual(0, db_obj.count())


if __name__ == "__main__":
    unittest.main()
