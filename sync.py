
default_hash = 0

# can we assume all sync packets from the same hub are part of the same sync
# session?

# what do we do if we get a packet that doesn't make sense for the phase 
# we're at? KeyError means packets are being read at the wrong time.

def sync(is_initiator, in_queue, out_queue, mismatch_index, mismatch_hash):
	# phase 0: initiate sync with other hub from index i
	if isInitiator:
		out_queue.put({sync: True, index: i, hashval: mismatch_hash, match: False})

	# phase 1: search newest to oldest for last point hubs agree
	last_good_index = -1
	receiver_of_match = False
	while True:
		message = in_queue.get() # block here until other hub responds
		if message[match]:
			last_good_index = message.index
			receiver_of_match = True
			break
		elif (message[hashval] == getHash(message[index]):
			last_good_index = message[index]
			out_queue.put({sync: True, index: message[index], \
					hashval: message[hashval], match: True, timestamp: None, timestamp: None})
			break
		else:
			if message.index == 0: #hubs never agree:
				#last_good_index remains -1
				out_queue.put({sync: True, index: - 1, \
					hashval: defaul_hash, match: True})
				break
			else:
				out_queue.put({sync: True, index: message[index] - 1, \
						hashval: getHash(message[index] - 1), match: False})

	# TODO: think very carefully about whether race conditions can happen 
	# during transition from phase 1 to phase 2, esp. re: bool control flags
	# causing problems

	# phase 2: having found divergence point, correct missing messages
	if receiver_of_match: #this hub got match = True message
		# initiate next phase
		out_queue.put({sync: True, index: last_good_index + 1, \
			hashval: getHash(last_good_index + 1), \
			data: getData(last_good_index), end: False})

	while True:
		message = in_queue.get()
		if message[end]:
			break
		their_data = message[data]
		their_time = their_data.timestamp
		index = message[index]
		our_data = getData(index)
		our_time = data.timestamp

		(new_hashval, last_index) = datawrapper.add(their_data)
		if new_hashval == mismatch_hash and last_index = mismatch_index:
			# adding this packet brings us in sync with other hub
			out_queue.put({end:True})
			break
		if their_time < our_time:
			out_queue.put({sync: True, end: False, index: index + 1, \
					hashval: getHash(index + 1), data: getData(index + 1)})
		elif their_time > our_time:
			out_queue.put({sync: True, end: False, index: index, \
					hashval: getHash(index), data: getData(index)})
		elif their_time == our_time:
			if their_data == our_data:
				# end up here if we hit > block but it's not the only error
				# force index increment
				# TODO: think carefully about this also
				out_queue.put({sync: True, end: False, index: index + 1, \
					hashval: getHash(index + 1), data: getData(index + 1)})
			else:
				# rip













