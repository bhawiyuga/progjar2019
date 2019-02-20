# import socket
import socket

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke alamat IP dan port server
sock.connect( ("127.0.0.1", 7777) )

# Kirim data ke server
data = "Selamat pagi"
sock.send(data.encode("ascii"))

# Terima balasan dari server
data = sock.recv(100)
# Decode dan cetak
data = data.decode("ascii")
print(data)