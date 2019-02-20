# import socket
import socket
# import library threading
import threading

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 7777) )
# Listen
sock.listen(100)

# Fungsi untuk menghandle 1 thread 
# (Fungsi yang dijalankan pada sebuah thread baru)
# Parameter fungsi ini adalah variabel koneksi ke client
def handle_thread(conn):
    while True :
        try :
            # Terima data yang dikirimkan oleh client
            data = conn.recv(100)
            # Decode jadi string
            data = data.decode("ascii")
            data = "OK "+data
            # Kirim lagi ke client
            conn.send(data.encode("ascii"))
        # Jika terjadi pemutusan koneksi oleh client
        # Tangkap exceptionnya, kemudian tutup koneksi dan break
        except(socket.error):
            conn.close()
            break

while True :
    # Terima permintaan koneksi
    conn, client_addr = sock.accept()
    # Buat thread baru, panggil fungsi handle_thread
    t = threading.Thread(target=handle_thread, args=(conn,))
    # Start thread baru
    t.start()
