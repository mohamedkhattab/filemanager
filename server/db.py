from pymongo import MongoClient
from bson.json_util import dumps
import pprint
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['fr-model']
file_manager = db['file_manager']
def ero():
	Ga = 'Ga'
	results = file_manager.find_one({"$and":[{'age': 90}, {'name' :{'$regex': '^' + Ga}}]})
	pprint.pprint(results['name'])
	#print(dumps(results))

def undo_delete(path):
	db.file_manager.update_many({"$and":[{'del': 1}, {'name': {'$regex': '^' + path}}]}, {'$set':{'del': 0}})

def soft_delete(path):
	db.file_manager.update_many({'name': {'$regex': '^' + path}}, {'$set':{'del': 1}})

def hard_delete(path):
	db.file_manager.remove({'$and':[{'del': 1}, {'name': {'$regex': '^' + path}}]})
	#remove folder content

def create_file(path, name, mime):
	file_manager.insert({'path': path, 'type': 'f', 'name': name, 'mime': mime, 'del': 0})
	#add folder content

def create_folder(path, name):
	file_manage.insert({'path': path, 'type': 'd', 'name': name, 'del': 0})
	#add folder content	

def get_path(id):
	result = file_manager.find_one({'_id': id})
	return json.dumps({'path': result['path']})

def get_name(id)
	result = file_manager.find_one({'_id': id})
	return json.dumps({'name': result['name']})

def update(srcId, newPath)
	db.file_manager.update({'_id': id}, {'%set': {'path': newPath}})

if __name__ == "__main__":
	ero()
	
