import struct

def send_term(conn, data):
    # Tambahkan termination character \r\n
    data = data + "\r\n"
    # Kirim data
    conn.send( data.encode("ascii") )

def recv_term(conn):
    # variabel sebagai buffer
    buffer = ""
    data = ""
    # Baca sampai ketemu \r\n
    while "\r\n" not in data :
        # Baca data dari socket
        data = conn.recv(10)
        data = data.decode("ascii")
        # Tambahkan ke buffer
        buffer = buffer+data
    # Bersihkan termination characternya dari buffer
    buffer.replace("\r\n", "")
    return buffer

def send_size(conn, data):
    # Hitung size data
    size = len(data)
    # Pack size sebagai integer
    header = struct.pack(">I", size)
    # Tambahkan payload ke header
    alldata = header + data.encode("ascii")
    # Kirim data
    conn.send(alldata)

def recv_size(conn):
    # Baca headernya
    header = conn.recv(4)
    size = struct.unpack(">I", header)[0]
    # Baca payload
    data = conn.recv(size)
    data = data.decode("ascii")
    return data