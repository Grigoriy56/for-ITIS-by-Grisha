import pickle, os, shutil
from time import sleep

# just a template of the "protocol" which will be used for filling
http_protocol = {
	'content-type': None,
	'content': None
}

# init the socket stream
# socket = open('socket', 'rb+')


class Server():
	def __init__(self, path):
		self.work_directory = path
		self.socket = open(f'{path}socket', 'rb+')

	def write(self, protocol):
		# move the pointer to the beginning
		self.socket.seek(0)
		# write the bytes as pickle
		pickle.dump(protocol, self.socket)
		# truncate the file's size based on written data
		self.socket.truncate()

	def read(self):
		# move the pointer to the beginning
		self.socket.seek(0)
		return pickle.load(self.socket)


server_socket = Server('/home/grigoriy/work/for-ITIS-by-Grisha/p1/')

while server_socket.socket.readable():
	# get the data from the client
	data = server_socket.read()
	print(f"data ({type(data)}): {data}")

	# check if it is an our 'http' protocol
	# ToDo make it as an object of Protocol class!
	if isinstance(data, dict):
		if data.get('content-type') == 'command':
			exec(data.get('content'))
		elif data.get('content-type') == 'file':
			# ToDo if user send the type as 'file', and the content is a str (filepath), then copy the
			#  file to the current directory (googling 'os' library, copying the files)
			shutil.copy(data.get('content'), '/home/grigoriy/work/for-ITIS-by-Grisha/p1/')

		elif data.get('content-type') == 'text':
			print(data.get('content'))
		# clean the socket
		server_socket.write(None)
	# ToDo in future our server will sleep unit the new data incoming. Now it is just simplification
	sleep(2)

print('end')