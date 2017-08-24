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


class ArticleMongoDbRepository(AbstractRepository):
    client = None
    db = None
    col = None
    db_name = "newsfetcher"
    collection = "articles"

    def save(self, obj):
        exists = self.col.find_one({"id": obj["id"]})
        if not exists:
            mdb_id = self.col.insert_one(obj).inserted_id
            # logger.info("Article: %s - SAVED.", obj["headline"])
            return mdb_id
        # logger.info("Article: \"%s\" - EXISTS.", obj["headline"])

    def bulk_save(self, objs):
        self.col.insert_many(objs)

    def connect(self, host=None, port=None, db=None):
        if not host: host = "localhost"
        if not port: port = 27017
        if not db: db = self.db_name
        self.client = MongoClient(host, port)
        self.db = self.client[db]
        self.col = self.db[self.collection]
        indexes = self.col.index_information()
        if "text" not in indexes.keys():
            self.col.create_index([("text", pymongo.TEXT)])

    def search_by_keywords(self, keywords):
        return self.col.find({"$text": {"$search": " ".join(k for k in keywords)}})

    def drop_db(self, db):
        self.client.drop_database(db)

    def get_by_id(self, idx):
        return self.col.find_one({"id": idx})

    def get_all(self):
        return self.col.find()
