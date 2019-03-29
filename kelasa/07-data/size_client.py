# import socket
import socket
from fungsi import send_size, recv_size

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke alamat IP dan port server
sock.connect( ("127.0.0.1", 7777) )

# Kirim data ke server
#data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
data = "Ini Ibu Budi"
send_size(sock, data)
# Baca data
data = recv_size(sock)
print(data)