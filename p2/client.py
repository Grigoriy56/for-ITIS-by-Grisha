import socket

# prepare
sock = socket.socket()
sock.connect(('localhost', 8080))

# connection <-> data
msg = 'hello, world!'

sock.send(msg.encode('UTF-8')) # ->
data = sock.recv(1024) # <-
sock.close()

print(data)