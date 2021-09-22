import socket
from threading import Thread
SIZE_OF_PART = 10

# list_licalhost = 8082
sock = socket.socket()

sock.bind(('localhost', 8083))
sock.listen(1)


def get_file(connection):
	file = open('data.png', 'wb')
	data = connection.recv(1024)

	while data:
		file.write(data)
		data = connection.recv(1024)
	file.close()




def recieve(connection):
	answer = []
	while True:  # collect the full packet
		part_of_data = connection.recv(SIZE_OF_PART)
		answer.append(part_of_data)
		# print(part_of_data)
		if len(part_of_data) < SIZE_OF_PART or not part_of_data:
			break
		# print('merge')
	# print('merged!')
	return b''.join(answer)


def chatting():


	conn, addr = sock.accept()
	with conn:
		while True:
			result = recieve(conn)
			if b'file()' in result:
				conn.send(b'filename: ')
				get_file(conn)
				text = bytes('saved in data.txt'.encode('UTF-9'))
				conn.send(text)
				continue
			print('connected:', addr)
			text = bytes(f'{addr} say: {result}'.encode('UTF-8'))
			conn.send(b'OK')
			print(text)
			if b'quit()' in result:
				text = f'goodbye {addr}'
				print(text.encode('UTF-8'))
				break


	print('exit')

	sock.close()


def chatting_threads():
	for i in range(5):
		t = Thread(target=chatting, args=())
		t.start()

# chatting_threads()
chatting()