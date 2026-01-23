print(
    "MENU MAKANAN : \n"
    "1. Nasi Goreng\n"
    "2. Nasi Padang\n"
    "3. Nasi Campur\n"
)

def a(Nasi_Goreng):
    nama = "Nasi Goreng"
    harga = 20000
    Jumlah =int(input("Masukkan Jumlah Yang Ingin Dibeli :"))
    total = harga * Jumlah
    print(f"Total Pembelian {nama} : ", total )
def b(Nasi_Padang):
    nama= "Nasi Padang"
    harga =15000
    Jumlah =int(input("Masukkan Jumlah Yang Ingin Dibeli : "))
    total =harga * Jumlah
    print(f"Total Pembelian {nama} : ",total)
def c(Nasi_Campur):
    nama= "Nasi Campur"
    harga = 17500
    Jumlah =int(input("Masukkan Jumlah Yang Ingin Dibeli : "))
    total = harga * Jumlah
    print(f"Total Pembelian {nama} : ", total)
pilihan = int(input("Masukkan Menu yang anda Inginkan : "))

while True:
    if pilihan == 1:
        a("Nasi Goreng")
    elif pilihan == 2:
        b("Nasi Padang")
    elif pilihan == 3:
        c("Nasi campur")
    else :
        print("Pilihan Tidak Ada Di Menu")
