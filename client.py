import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input("Server hostname or ip? ")
port = input("Server port? ")
sock.connect((host,port))

while True:
    data = raw_input("message: ")
    sock.send(data)
    print "response: ", sock.recv(1024)