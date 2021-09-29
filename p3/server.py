import socket

SIZE_OF_PART = 10
sock = socket.socket()
sock.bind(('localhost', 8080))
sock.listen(1)

conn, addr = sock.accept()


def recieve(connection):
	answer = []
	while True:  # collect the full packet
		part_of_data = connection.recv(SIZE_OF_PART)
		answer.append(part_of_data)
		print(part_of_data)
		if len(part_of_data) < SIZE_OF_PART or not part_of_data:
			break
		print('merge')
	print('merged!')
	return b''.join(answer)


with conn:
	while True:
		print('connected:', addr)
		result = recieve(conn)
		conn.send(b'OK')
		print(result)
		if 'quit()' in result:
			break

print('exit')

sock.close()
