from pymongo import MongoClient


DEBUG = True
client = MongoClient('mongodb://%s:%s@127.0.0.1' % ('xyz', 'xyz123'))
DATABASE =client['restfulapi'] # DB_NAME
