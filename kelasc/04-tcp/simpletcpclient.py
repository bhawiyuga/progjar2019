# import socket
import socket

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi
sock.connect( ("127.0.0.1", 7777) )

# Kirim data ke server
data = "Selamat sore"
sock.send(data.encode("ascii"))

# Terima balasan dari server
data = sock.recv(100)
print(data.decode("ascii"))