from uuid import uuid4

from pymongo import MongoClient

from .db_abc import DBTemplete
'''
start application
주어지는 정보들
- workspace path
- port
initialize db
get workspace 
get_db
wor
클래스를 만드는데 init에서 ip, port를 받아오고
connect를 해 본 다음에
아무것도 없으면 initial setting을 해 주는 것 까지 한 다음에

기본 기능을 하는 것들이 필요할 것 같다
'''
# import pymongo
# MONGO_SERVER_IP = '127.0.0.1'
# MONGO_SERVER_PORT = 27017 # mongoDB default port

# conn = pymongo.MongoClient(MONGO_SERVER_IP, MONGO_SERVER_PORT)
# db = conn.AAA
# collection = db.test

# db = conn.get_database('AAA')
# db.create_collection('test')
# collection_list = db.collection_names()
# print(collection_list)

# collection = db.get_collection('test')

class MongoDB(DBTemplete):

    def create_project(self, project_name, project_id, description, **kwargs):
        client = MongoClient('mongodb://localhost', 27017)
        db = client.celery_db
        collection = db.projects
        project_info = {
            'project_name': project_name,
            'project_id': project_id,
            'description': description
        }
        collection.insert(project_info)
        results = collection.find({'project_name': project_name})
        client.close()

        return results
