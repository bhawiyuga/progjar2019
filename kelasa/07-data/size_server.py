# import socket
import socket
from fungsi import send_size, recv_size

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
    data = recv_size(conn)
    # Decode jadi string dan ditambah OK di depannya
    data = "OK "+data
    # Kirim balik ke client
    send_size(conn, data)