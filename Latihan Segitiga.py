Baris = int(input("Masukkan jumlah baris :"))

for i in range(Baris):
    spasi = ' ' *(Baris - i )
    Bintang = "*" * (2 * i + 1)
    print(spasi + Bintang)

