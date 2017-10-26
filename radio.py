import serial

class Radio(Object):
	def __init__(port, baud):
		self.port = port
		self.baud = baud
		ser = serial.Serial(port, baud)
		time.sleep() # give time to initialize

	def listen():
		return ser.readline() #read(num) for bytes. timeout?

	def send(message):
		ser.write(message)


if __name == "__main__":
	port = '/dev/cu.usbmodem1421'
	baud = 9600
	radio = Radio(port, baud)