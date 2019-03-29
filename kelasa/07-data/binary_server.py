# import socket
import socket
import struct

# Inisiasi objek socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 7777) )

# Listen permintaan koneksi
sock.listen(100)

while True :
    # Terima permintaan koneksi
    # - Return value : variabel koneksi dan alamat client
    conn, client_addr = sock.accept()
    # Menerima data dari client
    data = conn.recv(8)
    # Unpack data
    data = struct.unpack(">II", data)
    data = 1000+data[0]+data[1]
    # Kirim balik ke client
    data = struct.pack(">I", data)
    conn.send(data)