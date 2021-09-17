import socket

# prepare
sock = socket.socket()
sock.connect(('localhost', 8080))


while True:
    # connection <-> data
    msg = input()

    if msg == "quit":
        sock.close()
        break
    sock.send(msg.encode('UTF-8')) # ->
    data = sock.recv(1024) # <-


    # print(data)