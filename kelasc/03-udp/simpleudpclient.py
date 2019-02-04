# Import lib socket
import socket

# Inisiasi objek socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Kirim data
sock.sendto( "Selamat sore".encode("ascii"), ("127.0.0.1", 6666) )
# Menerima kembalian data
data = sock.recv(65536)
# Cetak hasilnya
print(data)