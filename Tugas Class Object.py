class Daftar :
    def __init__(self, nama ,harga , jenis):
        self.nama = nama
        self.harga= harga
        self.jenis = jenis
        
p1 = Daftar("Nama Makanan : Nasi Padang","Harga        : Rp 20000","Jenis        : Makanan")               
p2 = Daftar("Nama Makanan : Es Jeruk","Harga        : Rp 15000","Jenis        : Minuman")
p3 = Daftar("Nama Makanan : Puding","Harga        : Rp 10000","Jenis        : Snack")

print("Daftar Makanan")

print("--------------------")
print(p1.nama)
print(p1.harga)
print(p1.jenis)
print("--------------------")
print(p2.nama)
print(p2.harga)
print(p2.jenis)
print("--------------------")
print(p3.nama)
print(p3.harga)
print(p3.jenis)
print("--------------------")