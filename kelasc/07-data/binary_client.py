# import socket
import socket
import struct

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi
sock.connect( ("127.0.0.1", 7777) )

# Kirim data ke server
data = 1000000

# Pack angkanya sebagai unsigned integer dengan big endian
data = struct.pack(">I", data)
sock.send(data)

# Terima balasan dari server
data = sock.recv(4)
data = struct.unpack(">I", data)[0]
print(data)