#Perpustakaan Python

buku = ["Laskar Pelangi", "Bumi Manusia", "Negeri 5 Menara","48 LAWS OF POWER"]
pinjaman = []
nama_user=input("masukan nama anda :")
print(f"halo {nama_user},selamat datang di perpustakaan kami👋!\n")

def tampilkan_menu():
    print("\n===== MENU PERPUSTAKAAN =====")
    print("1. Lihat Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Cari Buku")
    print("5. Tambah Buku")
    print("6. Keluar")

def lihat_buku():
    if len(buku) == 0:
        print("Tidak ada buku di perpustakaan 😔.")
    else:
        print("\nDaftar Buku:")
        for i, judul in enumerate(buku, 1):
            print(f"{i}. {judul}")


def pinjam_buku():
    lihat_buku()
    try:
        pilih = int(input("Pilih nomor buku yang ingin dipinjam: "))
        if 1 <= pilih <= len(buku):
            pinjaman.append(buku[pilih-1])
            print(f"Buku '{buku[pilih-1]}' berhasil dipinjam.")
            print(f"Jangan lupa mengembalikan buku tepat waktu ya  🤗 ")
            del buku[pilih-1]
        else:
            print("Nomor tidak valid 😒.")
    except e as e: 
        print("Input harus angka!", e)


def kembalikan_buku():
    if len(pinjaman) == 0:
        print("Tidak ada buku yang sedang dipinjam.")
    else:
        for i, judul in enumerate(pinjaman, 1):
            print(f"{i}. {judul}")
        try:
            pilih = int(input("Pilih nomor buku yang ingin dikembalikan: "))
            if 1 <= pilih <= len(pinjaman):
                buku.append(pinjaman[pilih-1])
                print(f"Buku '{pinjaman[pilih-1]}' berhasil dikembalikan 👌.")
                print(f"Terimakasih telah mengembalikan buku tersebut👺")
                del pinjaman[pilih-1]
            else:
                print("Nomor tidak valid 😒.")
        except e as e:
            print("Input harus angka!", e)


def cari_buku():
    kata = input("Masukkan judul/keyword buku: ").lower()
    hasil = [judul for judul in buku if kata in judul.lower()]
    if hasil:
        print("Hasil pencarian:")
        for judul in hasil:
            new_var = print("-", judul)
            new_var
    else:
        print("Buku tidak ditemukan 🧐.")


def tambah_buku():
    judul = str(input("Masukkan judul buku baru: "))
    penulis =str(input("Masukkan nama penulis buku baru :"))
    penerbit=str(input("Masukkan penerbit buku baru :"))
    buku.append({judul,penulis,penerbit})
    print(f"Buku '{judul}' berhasil ditambahkan 🤩.")


while True:
    tampilkan_menu()
    try:
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            lihat_buku()
        elif pilihan == 2:
            pinjam_buku()
        elif pilihan == 3:
            kembalikan_buku()
        elif pilihan == 4:
            cari_buku()
        elif pilihan == 5:
            tambah_buku()
        elif pilihan == 6:
            print("Terima kasih telah menggunakan sistem perpustakaan kami",nama_user,"😆")
            break
        else:
            print("Pilihan tidak valid!")
    except e as e:
        print("Input harus angka!",e)
