import falcon
import os
import json

class DirectoryResource:
    def on_post(self, req, resp):
        """Handles GET requests"""
        result = {
            'result': 'success'
        }

        body = json.loads(req.bounded_stream.read())
        path = '/home/mohamed/workspace/networks/'

        try:
            os.mkdir(path + body['name'])
        except:
            result['result'] = "folder already exists!"

        resp.media = result

api = falcon.API()
api.add_route('/api/directory/create', DirectoryResource())
