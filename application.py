import tornado.ioloop
import tornado.web
from health_handler import HealthHandler
from api_handler import APIHandler

app = tornado.web.Application([
    (r"/", HealthHandler),
    (r"/api", APIHandler),
])

if __name__ == "__main__":
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
