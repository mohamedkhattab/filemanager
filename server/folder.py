import falcon
import os
import json
import shutil
import db
import magic
import file

class FolderMove:
	def on_post(self, req, resp):
		result = {
			'result': 'success'
		}
		body = json.loads(req.bounded_stream.read())
		
		srcPath = get_path(body['srcId'])
		dirPath = get_path(body['dirId'])
		
		try:
			db.soft_delete(srcPath)
			shutil.move(srcPath, dirPath)
			createTree(dirPath)
		except:
			db.undo_delete(srcPath)
			result['result'] = "failed"
		db.hard_delete(srcPath)
		resp.media = result

class FolderDelete:
	def on_post(self, req, resp):
		result = {
			'result': 'success'
		}	
		body = json.loads(req.bounded_stream.read())

		srcPath = get_path(body['srcId'])
		
		try:
			db.soft_delete(srcPath)
			shutil.rmtree(srcPath)
		except:
			db.undo_delete(srcPath)
			result['result'] = "failed"
		db.hard_delete(srcPath)
		resp.media = result

class FolderCreate:
	def on_post(self, req, resp):
		result = {
			'result': 'success'
		}
		body = json.loads(req.bounded_stream.read())
				
		dirPath = body['dirId']
		folderName = body['folderName']
		
		try:
			os.mkdir(os.path.join(dirPath, folderName))
			create_folder(os.path.join(dirPath, folderName), folderName)
		except:
			result['result'] = "failed"
		
		resp.media = result

class FolderCopy:
	def createTree(srcPath):
		for root, dirs, files in os.walk(srcPath):
			for name in dirs:
				create_folder(os.path.join(root, name), name)
			for name in files:
				mime = magic.Magic(mime = True)
				mime.from_file(os.path.join(root, name))	
				create_file(os.path.join(root, name), name)


	def on_post(self, req, resp):
		result = {
			'result': 'success'
		}
		body = json.loads(req.bounded_stream.read())
		
		srcPath = get_path(body['srcId'])
		dirPath = get_path(body['dirId'])
		folderName = body['folderName']	
		dstPath = os.path.join(dirPath, folderName)		

		try:
			shutil.copytree(srcPath, dstPath)
			createTree(dstPath)
		except:
			result['result'] = "failed"

		resp.media = result

api = falcon.API()
api.add_route('/api/folder/move', FolderMove())
api.add_route('/api/folder/delete', FolderDelete())
api.add_route('/api/folder/create', FolderCreate())
api.add_route('/api/folder/copy', FolderCopy())
api.add_route('/api/file/move', file.FileMove())
api.add_route('/api/file/delete', file.FileDelete())
api.add_route('/api/file/create', file.FileCreate())
api.add_route('/api/file/copy', file.FileCopy())