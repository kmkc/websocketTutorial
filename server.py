import os
from tornado import ioloop, web, websocket

approot = os.path.dirname(__file__)
clients = []

class mainHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')

class webSocketHandler(websocket.WebSocketHandler):
    def open(self):
        if self not in clients: clients.append(self)

    def on_close(self):
        if self in clients: clients.remove(self)

    def on_message(self, message):
        for c in clients: c.write_message(message)

def createApp():
    return web.Application([
        (r'/', mainHandler),
        (r'/websocket', webSocketHandler),

        # This should be descripted last
        (r'/(.*)', web.StaticFileHandler, {'path': approot}),
    ])

if __name__ == '__main__':
    app = createApp()
    app.listen(3000)
    ioloop.IOLoop.current().start()
