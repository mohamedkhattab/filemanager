
client = MongoClient('mongodb://localhost:27017/')
db = client['fr-model']
file_manager = db['file_manager']
def ero():
	Ga = 'Ga'
	db.file_manager.update_many({"$and":[{'age': 22}, {'name' :{'$regex': '^' + Ga}}]}, {'$set':{'age': 90}})
def undo_delete(path):
	db.file_manager.update_many({"$and":[{'del': 1}, {'name': {'$regex': '^' + path}}]}, {'$set':{'del': 0}})

def soft_delete(path):
	db.file_manager.update_many({'name': {'$regex': '^' + path}}, {'$set':{'del': 1}})

def hard_delete(path):
	db.file_manager.remove({'$and':[{'del': 1}, {'name': {'$regex': '^' + path}}]})
	#remove folder content

	
if __name__ == "__main__":
	ero()
	
