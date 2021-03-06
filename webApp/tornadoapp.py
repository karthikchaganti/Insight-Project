#! /usr/bin/env python

# Tornado Server on one of the Master Nodes
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
from app import app

class MainHandler(RequestHandler):
 def get(self):
   self.write("This message comes from Tornado ^_^")

tr = WSGIContainer(app)

application = Application([
(r"/tornado", MainHandler),(r".*", FallbackHandler, dict(fallback=tr)),])

# listen on port 80
if __name__ == "__main__":
 application.listen(80)
 IOLoop.instance().start()
