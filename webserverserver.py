import Queue
from socketserver import *

class WebServerServer(ThreadingMixIn, TCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True,
                 queue=None):
        print "init wss"
        self.queue = queue
        TCPServer.__init__(self, server_address, RequestHandlerClass,
                           bind_and_activate=bind_and_activate)

class WSSHandler(DatagramRequestHandler):
    def __init__(self, request, client_address, server):
        print "init wshandler"
        self.queue = server.queue
        DatagramRequestHandler.__init__(self, request, client_address, server)

    def handle(self):
        print "in handle function"
        self.data = self.rfile.readline().strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        self.queue.put(self.data)
        self.request.sendall(self.data.upper())