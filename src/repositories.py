import logging

import pymongo
from pymongo import MongoClient

logger = logging.getLogger(__name__)


class AbstractRepository(object):
    def connect(self, host=None, port=None):
        raise NotImplementedError

    def save(self, obj):
        raise NotImplementedError

    def bulk_save(self, objs):
        raise NotImplementedError

    def search_by_keywords(self, keywords):
        raise NotImplementedError


class ArticlesMongoDbRepository(AbstractRepository):
    client = None
    db = None
    col = None
    db_name = "newsfetcher"
    collection = "articles"

    def save(self, obj):
        exists = self.col.find_one({"id": obj["id"]})
        if not exists:
            id = self.col.insert_one(obj).inserted_id
            logger.info("Article: %s - SAVED.", obj["headline"])
            return id
        logger.info("Article: %s - EXISTS.", obj["headline"])

    def bulk_save(self, objs):
        self.col.insert(objs)

    def connect(self, host=None, port=None):
        if not host: host = "localhost"
        if not port: port = 27017
        self.client = MongoClient(host, port)
        self.db = self.client[self.db_name]
        self.col = self.db[self.collection]

    def search_by_keywords(self, keywords):
        indexes = self.col.get_indexex()
        if indexes:
            self.col.drop_index("text")
        self.col.create_index(("text", pymongo.TEXT))
        self.col.find((" ".join(k for k in keywords)))
