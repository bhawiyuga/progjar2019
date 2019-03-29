import struct

def send_term(conn, data):
    # Tambahkan termination character pada akhir sebuah string
    data = data + "\r\n"
    # Encode dan kirim lewat socket
    conn.send(data.encode("ascii"))

def recv_term(conn):
    # Variabel buffer untuk menampung data
    buffer = ""
    data = ""
    # Loop selama tidak mengandung termination character
    while "\r\n" not in data:
        # Baca data 10 bytes
        data = conn.recv(10)
        data = data.decode("ascii")
        # Tambahkan ke buffer
        buffer = buffer + data
    # Buang termination characternya
    buffer = buffer.replace("\r\n", "")
    # return
    return buffer

def send_size(conn, data):
    # Hitung ukuran payload data
    size = len(data)
    # Pack headernya dalam tipe data
    header = struct.pack(">I", size)
    # Tambahkan header ke payload data
    data = header + data.encode("ascii")
    # Kirim ke penerima
    conn.send(data)

def recv_size(conn):
    # Baca dulu headernya
    header = conn.recv(4)
    size = struct.unpack(">I", header)[0]
    # Baca sesuai dengan ukuran packet
    data = conn.recv(size)
    data = data.decode("ascii")
    # Return
    return data