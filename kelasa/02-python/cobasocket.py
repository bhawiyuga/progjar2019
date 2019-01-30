import socket

# Inisiasi socket
sock = socket.socket()

# Buat koneksi TCP ke server
sock.connect( ("jsonplaceholder.typicode.com", 80) )

# Kirim request ke server HTTP
request = 'GET /users HTTP/1.1\r\n'+'Host: jsonplaceholder.typicode.com\r\n\r\n'
sock.send(str.encode(request))
# Baca responnya
while True:
    # Receive dari buffer
    buffer = sock.recv(100)
    # Jika semua data sudah selesai dibaca, break
    if not buffer :
        break
    # Cetak response
    print(buffer)
# Tutup koneksi
sock.close()