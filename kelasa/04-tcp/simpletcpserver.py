# import socket
import socket

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
    data = conn.recv(100)
    # Decode jadi string dan ditambah OK di depannya
    data = data.decode("ascii")
    data = "OK "+data
    # Kirim balik ke client
    conn.send(data.encode("ascii"))