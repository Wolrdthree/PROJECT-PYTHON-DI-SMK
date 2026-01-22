barang_belanja = []
kategori_barang = ("Makanan", "Minuman", "Alat Rumah Tangga")
merek_unik = set()
detail_barang = dict()

while True:
    print("Menu:")
    print("1: Tambah Barang Belanja")
    print("2: Lihat semua barang")
    print("3: Hapus barang")
    print("0: Keluar")

    pilihan = int(input("Pilih pilihan: "))

    if pilihan == 1:
        nama_barang = input("Masukkan nama barang: ")
        kategori = input("Masukkan kategori {kategori_barang}: ")
        merek = input("Masukkan merek barang: ")
        harga = int(input("Masukkan harga barang: "))
        jumlah = int(input("Masukkan jumlah barang: "))

        barang_belanja.append(nama_barang)
        merek_unik.add(merek)
        detail_barang[nama_barang] = {"harga": harga, "jumlah": jumlah}

        print("Barang berhasil ditambahkan!")

    elif pilihan == 2:
        print("Daftar Belanja:", barang_belanja)
        print("Kategori Barang:", kategori_barang)
        print("Merek Unik:", merek_unik)
        print("Detail Barang:", detail_barang)

    elif pilihan == 3:
        nama_hapus = input("Masukkan nama barang yang ingin dihapus: ")
        if nama_hapus in barang_belanja:
            barang_belanja.remove(nama_hapus)
            merek_terhapus = None
            if nama_hapus in detail_barang:
                merek_terhapus = next(iter(merek_unik))
                del detail_barang[nama_hapus]
            if merek_terhapus and merek_terhapus in merek_unik:
                merek_unik.remove(merek_terhapus)
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan!")

    elif pilihan == 0:
        print("Final Output:")
        print("Daftar Belanja:", barang_belanja)
        print("Kategori Barang:", kategori_barang)
        print("Merek Unik:", merek_unik)
        print("Detail Barang:", detail_barang)
        break

    else:
        print("Pilihan tidak valid!")
