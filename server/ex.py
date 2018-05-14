import falcon

class FileResource:
	def on_get(self, req, resp):
		result = {
			'result': 'success'
		}
		resp.media = result
		print(req.get_param('name'))
api = falcon.API()
api.add_route('/api/file', FileResource())
