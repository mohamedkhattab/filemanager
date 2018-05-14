from pymongo import MongoClient
from bson.json_util import dumps
import pprint
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['fr-model']
file_manager = db['file_manager']
cntr = db['g']

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
	nxtId = cnt.find_one({'id': 1})["counter"]
	file_manager.insert({'id': nxtId,'path': path, 'type': 'f', 'name': name, 'mime': mime, 'del': 0})
	cnt.update({'id': 1}, {'$set': {'counter': nxtId + 1}})
	#add folder content

def create_folder(path, name):
	nxtId = cnt.find_one({'id': 1})["counter"]
	file_manage.insert({'id': nxtId,'path': path, 'type': 'd', 'name': name, 'del': 0})
	cnt.update({'id': 1}, {'$set': {'counter': nxtId + 1}})
	#add folder content	

def get_path(id):
	print("type of id: " + str(type(id)))
	result = file_manager.find_one()
	res2 = file_manager.find()
	for r in res2:
		print(r)
	print(id)
	if result == None:
		return -1
	return json.dumps({'path': result['path']})

def get_name(id):
	result = file_manager.find_one({'id': id})
	if result.count() == 0:
		return -1
	return json.dumps({'name': result['name']})

def update(srcId, newPath):
	db.file_manager.update({'id': id}, {'%set': {'path': newPath}})

if __name__ == "__main__":
	ero()
	
