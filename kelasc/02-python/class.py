class Aritmatika(object):

    def jumlah(self,a,b):
        return a+b
    
    def kurang(self,a,b):
        return a-b

a = 20
b = 10
# Inisiasi object dari class Aritmatika
x = Aritmatika()
# Panggil method jumlah
c=x.jumlah(a,b)
print(c)
