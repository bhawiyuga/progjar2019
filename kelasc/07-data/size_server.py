# import socket
import socket
from fungsi import send_size, recv_size

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 7778) )
# Listen
sock.listen(100)

while True :
    # Terima permintaan koneksi
    conn, client_addr = sock.accept()
    # Terima data yang dikirimkan oleh client
    data = recv_size(conn)
    # Decode jadi string
    data = "OK "+data
    # Kirim lagi ke client
    send_size(conn, data)
