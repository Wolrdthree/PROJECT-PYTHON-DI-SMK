#need file.txt to store the data 
def tampil():
    file = open("tes.txt", "r")
    isi =  file.read()
    file.close
    if isi.strip() == "":
        print("Catatan masih kosong silakan diisi terlebih dahulu")
    else:
        print("Isi Catatan:")
        print(isi)
def hapus():
    file = open("tes.txt", "w")
    file.write("")
    print("Catatan berhasil dikosongkan!")

def Tambah():
    tulisan = str(input("Apa yang ingin anda masukkan didalam catatan:\n"))
    file = open("tes.txt", "a")
    file.write(f"{tulisan}\n")

def main():
    while True :
        try:
            print("\n",
            "====MENU CATATAN SEDERHANA====\n",
            "1. Lihat Catatan\n",
            "2. Tambah Catatan\n",
            "3. Hapus semua Catatan\n",
            "4. Keluar\n",
            "==============================\n"
        )
            inputan = int(input("Massukkan pilihan menu yang anda inginkan:"))
            if inputan == 1:
                tampil()
            elif inputan == 2:
                Tambah()
            elif inputan == 3:
                pilihan =input("Apakah kamu yakin ingin menghapus isi catatan(y/n):")
                if pilihan == "y":
                    hapus()
                elif pilihan == "n":
                    main()
            elif inputan == 4:
                print ("Selamat tinggal")
                break
            else:
                print("Pilihan Tidak ada di Menu!(Silakan pilih antara 1-4)")
        except ValueError:
            print("Input tidak valid!")                                    

main()        
