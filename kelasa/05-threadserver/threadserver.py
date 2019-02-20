# import socket
import socket
# import library untuk threading
import threading

# Inisiasi objek socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 7777) )

# Listen permintaan koneksi
sock.listen(100)

# Fungsi yang akan dieksekusi pada thread baru
def handle_thread(conn):
    while True :
        try :
            # Menerima data dari client
            data = conn.recv(100)
            # Decode jadi string dan ditambah OK di depannya
            data = data.decode("ascii")
            data = "OK "+data
            # Kirim balik ke client
            conn.send(data.encode("ascii"))
        except(socket.error):
            # Tutup koneksi ketika client menutup koneksi secara paksa
            conn.close()
            print("Client menutup koneksi")
            break

while True :
    # Terima permintaan koneksi
    # - Return value : variabel koneksi dan alamat client
    conn, client_addr = sock.accept()
    # Buat thread baru
    t = threading.Thread(target=handle_thread, args=(conn,))
    t.start()
    