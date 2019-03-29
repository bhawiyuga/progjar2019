# import socket
import socket
import struct

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke alamat IP dan port server
sock.connect( ("127.0.0.1", 7777) )

# Representasikan variabel dalam bentuk integer
a = 100
b = 200
data = struct.pack(">II", a, b)

# Kirim data ke server
sock.send(data)

# Terima balasan dari server
data = sock.recv(4)
# Unpack dan cetak
data = struct.unpack(">I", data)[0]
print(data)