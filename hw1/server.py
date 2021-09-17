import os
from time import sleep
from shutil import copyfile
from threading import Thread

from MySocket import MySocket


class Server:
	connectioins = [MySocket(f'socket{i}') for i in range(10)]

	def __init__(self):
		self.http_protocol = {
			'content-type': None,
			'content': None
		}
	# initialization if socket file is not exist

	def chatting(self, connection):
		while True:
			# get the data from the client
			data = connection.read()
			# check if it is an our 'http' protocol
			# ToDo make it as an object of Protocol class!
			if isinstance(data, dict):
				print(f"data ({type(data)}): {data}")
				if data.get('content-type') == 'command':
					exec(data.get('content'))
				elif data.get('content-type') == 'file':
					path_file = data.get('content')
					if os.path.exists(path_file):
						copyfile(path_file, os.getcwd())
				elif data.get('content-type') == 'text':
					print(data.get('content'))
				# clean the socket
				connection.write(None)
			# ToDo in future our server will sleep unit the new data incoming. Now it is just simplification
			sleep(1)

	def chatting_threads(self):
		for i in range(10):
			t = Thread(target=Server.chatting, args=(self, self.connectioins[i]))
			t.start()


serv = Server()
serv.chatting_threads()