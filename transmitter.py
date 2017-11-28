import sys, json as np
import socket 
import radio

if __name__ == '__main__':
	port = '/dev/cu.usbmodem1411'
	baud = 9600
	radio = radio.Radio(port, baud) 
	while True:
		radio.send(sys.argv[1])
