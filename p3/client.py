import socket
# prepare
SIZE_OF_PART = 10
sock = socket.socket()
sock.connect(('localhost', 8085))

def recieve(connection):
	answer = []
	while True:  # collect the full packet
		part_of_data = connection.recv(SIZE_OF_PART)
		answer.append(part_of_data)
		if len(part_of_data) < SIZE_OF_PART:
			break
	return ''.join(part.decode('UTF-8') for part in answer)

with sock:
	while True:
		msg = input('write a msg: ')
		sock.send(msg.encode('UTF-8'))
		answer = recieve(sock)
		print("get from server: ", answer)
		if 'quit()' in msg:
			break
