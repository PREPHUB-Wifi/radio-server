import radio
import Queue
import SocketServer

class TCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


def listenToRadio(self, radio, queue):
    size = 1024
    while True:
        try:
            incoming_message = client.listen()
            if incoming_message:
                queue.put(incoming_message)
                return True
            else:
                return False
        except Queue.Full:
            print "i am dropping a message on the floor"


if __name == "__main__":
	radio_port = "/dev/cu.usbmodem1421"
	baud = 9600
	radio = Radio(radio_port, baud)
	max_queue_size = 10
	queue = Queue.Queue(max_queue_size)
	threading.Thread(target = listenToRadio,args = (radio, queue)).start()

	webserver_host = "localhost"
	webserver_port = 8080
	server_server = SocketServer.TCPServer((webserver_host, webserver_port), TCPHandler)
	threading.Thread(target = server_server.serve_forever,args = ())




