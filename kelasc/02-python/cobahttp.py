# Import library http
import http.client

# Inisiasi koneksi HTTP
conn = http.client.HTTPConnection("ip.jsontest.com")
# Kirim request
conn.request("GET", "/")
resp = conn.getresponse()
# Cetak response
print(resp.status)
print(resp.read())

