# import socket
import socket

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
    data = conn.recv(100)
    # Decode jadi string
    data = data.decode("ascii")
    data = "OK "+data
    # Kirim lagi ke client
    conn.send(data.encode("ascii"))
