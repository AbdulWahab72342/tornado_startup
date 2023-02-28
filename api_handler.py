import tornado.web
import json

class APIHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is the GET method of the APIHandler")

    def post(self):
        data = json.loads(self.request.body)
        self.write({'message': data})
