# Import library
import http.client

# Buat koneksi
conn = http.client.HTTPConnection("jsonplaceholder.typicode.com")
# Kirim request
conn.request("GET", "/users")
# Baca response
resp = conn.getresponse()
# Cetak responsenya
print(resp.read()) 

