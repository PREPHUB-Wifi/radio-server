import webserverserver as wss
import radio
import Queue

import time
import threading

#configured w/ list of who we expect to be conncted to

#state
#who am i currently connected to? last heard from?
#current time

#connect to radio
port = '/dev/cu.usbmodem1421'
baud = 9600
radio = radio.Radio(port, baud) #listen/send
print "created radio"

#start server to listen to webserver
ws_host, ws_port = "localhost", 9999
queue = Queue.Queue()
wsserver = wss.WebServerServer((ws_host, ws_port), wss.WSSHandler, queue=queue)
print "created wsserver"
wsserver_thread = threading.Thread(target = wsserver.serve_forever).start()
print "created wsserver thread"

while True:
	#poll radio
	#do radio stuff (read first), send to webserver

	print "checking queue..."
	#poll webserver
	if not queue.empty():
		message = queue.get()
		print message
	else:
		print "empty"
	time.sleep(2)

