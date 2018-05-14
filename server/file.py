import falcon
import os
import json
import shutil
import db
import magic

class FileMove:
	def on_post(self, req, resp):
		#srcId = src file ID
		#dirId = dir ID
		result = {
			'result': 'success'
		}
		body = json.loads(req.bounded_stream.read())
		
		srcPath = db.get_path(body['srcId'])
		dirPath = db.get_path(body['dstId'])
		fileName = body['fileName']
		dstPath = os.path.join(dirPath, fileName)
		
		if(srcPath == -1 or dirPath == -1):
			result['result'] = "failed"
			return
		
		try:
			os.rename(srcPath, dstPath)
			db.update(srcId, dstPath)
		except:
			result['result'] = "failed"
		
		resp.media = result

class FileDelete:
	def on_post(self, req, resp):
		#srcId = src file id
		result = {
			'result': 'success'
		}
		body = json.loads(req.bounded_stream.read())
		
		srcPath = db.get_path(body['srcId'])
		if(srcPath == -1):
			result['result'] = "failed"
			return

		try:
			os.remove(srcPath)
			db.soft_delete(srcPath)
			db.hard_delete(srcPath)
		except:
			result['result'] = "failed"
		
		resp.media = result

class FileCreate:
	def on_post(self, req, resp):
		#srcName = new file name
		#dirId = the folder id where the file create
		result = {
			'result': 'success'
		}
		body = json.loads(req.bounded_stream.read())
		
		dirPath = get_path(body['dirId'])
		if(dirPath == -1):
			result['result'] = "failed"
		srcPath = os.path.join(dirPath, body['srcName'])

		try:
			os.mknod(srcPath)
			mime = magic.Magic(mime = True)
			mime.from_file(srcPath)
			db.create_file(srcPath, body['srcName'], mime)
		except:
			result['result'] = "failed"
		
		resp.media = result

class FileCopy:
	def on_post(self, req, resp):
		#srcId, dirId
		result = {
			'result': 'success'
		}
		body = json.loads(req.bounded_stream.read())
		
		srcPath = get_path(srcId)
		dirPath = get_path(dirId)
		if(srcPath == -1 or dirPath == -1):
			result['result'] = "failed"
			return
		fileName = get_name(srcId)
		dstPath = os.path.join(dirPath, fileName)
		#bug if the destination already exist the same file name will write on it
		try:
			shutil.copy2(srcPath, dstPath)
			mime = magic.Magic(mime = True)
			mime.from_file(dstPath)
			create_file(dstPath, fileName, mime) 			
		except:
			result['result'] = "failed"
		
		resp.media = result

"""
api = falcon.API()
api.add_route('/api/file/move', FileMove())
api.add_route('/api/file/delete', FileDelete())
api.add_route('/api/file/create', FileCreate())
api.add_route('/api/file/copy', FileCopy())
"""