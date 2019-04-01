# import socket
import socket
import struct

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 7777) )
# Listen
sock.listen(100)

while True :
    # Terima permintaan koneksi
    conn, client_addr = sock.accept()
    # Terima data yang dikirimkan oleh client
    data = conn.recv(4)
    # Unpack data
    data = struct.unpack(">I", data)[0]
    data = data + 1000000
    # Pack hasil penjumlahan
    data = struct.pack(">I", data)
    # Kirim lagi ke client
    conn.send(data)
