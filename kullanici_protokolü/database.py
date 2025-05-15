from pymongo import MongoClient

class MongoDB:
    def __init__(self,db_name="kullanici_verileri",collection_name="user"):
        self.client=MongoClient("mongodb://localhost:27017/")
        self.db=self.client[db_name]
        self.collection=self.db[collection_name]
        print(self.client.list_database_names())
        print(self.db.list_collection_names())
    
    def close_connection(self):
        self.client.close()