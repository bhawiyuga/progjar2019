# Inisiasi socket
import socket

# Inisiasi objek socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding ke alamat IP dan port tertentu
sock.bind( ("0.0.0.0", 6666) )

MAX_SIZE = 65536

while True :
    # Terima data dari client
    data, addr = sock.recvfrom(MAX_SIZE)
    # Tambah "OK" di depan data yang diterima
    # - Ubah bytes menjadi string dengan fungsi decode
    data = "OK "+data.decode("ascii")
    # Kirim balik ke client
    sock.sendto(data.encode("ascii"), addr)