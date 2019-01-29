import socket

# Inisiasi socket TCP
sock = socket.socket()
sock.connect(("ip.jsontest.com", 80))

request = 'GET / HTTP/1.1\r\n'+'Host: ip.jsontest.com\r\n\r\n'
sock.sendall(str.encode(request))

while True :
    buffer = sock.recv(1000)
    if not buffer :
        break
    print(buffer)
sock.close()