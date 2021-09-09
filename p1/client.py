import pickle

# just a template of the "protocol" which will be used for filling
import shutil

http_protocol = {
	'content-type': None,
	'content': None
}

# init the socket stream


class Client():
	def __init__(self, path):
		self.work_directory = path
		self.socket = open(f'{path}socket', 'rb+')

	def write(self, protocol):
		# move the pointer to the beginning
		self.socket.seek(0)
		# write the bytes as pic,kle
		pickle.dump(protocol, self.socket)
		# truncate the file's size based on written data
		self.socket.truncate()

	def read(self):
		# move the pointer to the beginning
		self.socket.seek(0)
		return pickle.load(self.socket)

client_socket = Client('/home/grigoriy/work/for-ITIS-by-Grisha/p1/')
while client_socket.socket.readable():
	content_type = input('type of content ')
	content = input('content ')
	print('-' * 10)

	request = http_protocol.copy()
	request['content-type'] = content_type

	request['content'] = content

	client_socket.write(request)

print('end')