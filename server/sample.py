import falcon
import json
class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
	print("Hello World")
	print(req)
	data = req.get_param("Name")
	print(data)
		
        resp.media = quote

api = falcon.API()
api.add_route('/quote', QuoteResource())
