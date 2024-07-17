from pymongo import MongoClient

class DB(object):

    def __init__(self, dbName, collectionName):
        self.client = MongoClient('seenable-db', 27017, username='root', password='password')
        self.db = self.client[dbName] #DB名を設定
        self.collection = self.db.get_collection(collectionName)

    def collection_names(self):
        return self.db.collection_names()

    def list_collection_names(self):
        return self.db.list_collection_names()

    def find(self, projection=None,filter=None, sort=None):
        return self.collection.find(projection=projection,filter=filter,sort=sort)

    def insert_one(self, document):
        return self.collection.insert_one(document)