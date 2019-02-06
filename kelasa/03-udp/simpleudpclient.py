# Inisiasi socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX_SIZE = 65536

# Kirim data
data = "Selamat pagi"
sock.sendto(data.encode("ascii"), ("127.0.0.1", 6666) )
# Terima data
data = sock.recv(MAX_SIZE)
print(data)