
class Packet:
	def __init__(self, sender, receiver, sync, hashval, index, message):
		self.sender = sender
		self.receiver = receiver
		self.sync = sync
		self.hashval = hashval
		self.index = index
		self.message = message

	def get_dict:
		#return something that can be encoded into json
		pass