import socket

sock = socket.socket()
sock.bind(('localhost', 8080))
sock.listen(1)

conn, addr = sock.accept()

print('connected:', addr)


while True:
    data = conn.recv(1024)
    print(data.decode('UTF-8'))
    if not data:
        break
    conn.send(data.upper())

conn.close()