# Import library socket
import socket

# Inisiasi objek socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind ke alamat IP dan port tertentu
sock.bind( ("0.0.0.0", 6666) )

MAX_SIZE_UDP = 65536

while True :
    # Terima data dari client
    data, address = sock.recvfrom(MAX_SIZE_UDP)
    # Tambahkan string OK di depan data yang diterima
    # - Decode bytes jadi string terlebih dahulu untuk Python 3
    data = "OK "+data.decode("ascii")
    # Kirim balik ke client
    sock.sendto(data.encode("ascii"), address)
sock.close()
