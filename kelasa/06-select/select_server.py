import socket
import select

# Inisiasi variabel socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )
# Listen 100 permintaan koneksi
tcp_sock.listen(100)

list_monitor = [ tcp_sock ]

while True :
    # Inisiasi select untuk mengecek aktifitas input pada socket/koneksi
    inputready,outputready,errorready = select.select(list_monitor, [ ], [ ])

    for conn in inputready:
        # Jika inputnya berhubungan dengan permintaan koneksi, maka accept
        if conn == tcp_sock:
            # Terima permintaan koneksi
            conn, client_addr = tcp_sock.accept()
            # Tambahkan koneksi baru ke list monitor
            list_monitor.append(conn)
        else :
            try:
                # Terima data dari client
                data = conn.recv(100)
                data = data.decode('ascii')
                data = "OK "+data
                # Kirim balik ke client
                conn.send( data.encode('ascii') )
            except(socket.error):
                # Tutup koneksi ke client
                conn.close()
                # Hapus dari list monitor agar tidak diamati lagi oleh select
                list_monitor.remove(conn)
                print("Koneksi dimatikan")

   
   