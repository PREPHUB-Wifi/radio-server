import radio
import Queue
import time
import threading
import socket
import json

hubID = 0;
#configured w/ list of who we expect to be connected to

connected_to = []
online = []

#connect to radio
port = '/dev/cu.usbmodem1421'
baud = 9600
radio_in = Queue.Queue()
radio_out = Queue.Queue()
radio = radio.Radio(port, baud) #listen/send
print "created radio"

ws_in = Queue.Queue()
ws_out = Queue.Queue()

def radio_in():
	while True:
		radio_in.put(radio.listen())

def radio_out():
	while True:
		if not radio_out.empty():
			radio.send(radio_out.get())

def decode(radio_incoming):
	dict_incoming = json.loads(radio_incoming)
	sender = dict_incoming[sender]
	receiver = dict_incoming[receiver]
	sync = dict_incoming[sync]
	hashval = dict_incoming[hashval]
	index = dict_incoming[index]
	message = dict_incoming[message]
	return (sender, receiver, sync, hashval, index, message)

def encode(packet):
	return json.dumps(packet.get_dict)

def sync():
	#make sure new packet is stored
	pass

radio_in_thread = threading.Thread(target=radio_in, args=())
radio_out_thread = threading.Thread(target=radio_out, args=())
radio_in_thread.start()
radio_out_thread.start()

while True:
	#check incoming from radio
	while not radio_in.empty():
		new_radio = radio_in.get()
		(sender, receiver, sync, hashval, index, message) = decode(new_radio)
		packet = Packet(sender, receiver, sync, hashval, index, message)
		if packet.receiver != hubID: #not addressed to us
			continue
		ws_out.put(message) #pass it to ws
		#is it sync packet?
		if packet.sync:
			sync()
		else:
			synced = add_and_check_synced(packet)
			if not synced:
				#put a sync packet on the queue
				sync_packet = Packet(hubID, packet.sender, True, ?, ?, ?)
				json_sync_packet = encode(sync_packet)
				radio_out.put(sync_packet)


	#check incoming from ws
	#only do this when radio incoming queue is empty, 
	#otherwise likely out of sync
	if not ws_in.empty():
		new_ws = ws_in.get()
		#send to others


#need to access fields: sender, is_sync, hash, index












