import tornado.web

class HealthHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")