def tambah():
 try:
     nilai1 = int(input("Masukkan angka pertama : "))
     nilai2 = int(input("Masukkan angka kedua   : "))
     hasil = nilai1 + nilai2
     print("Jadi hasil dari kedua angka adalah:",hasil)
 except ValueError:
    print("Harap masukkan input dengan angka")
def kurang():
    try:
          nilai1 = int(input("Masukkan angka pertama yang ingin dikurangi : "))
          nilai2 = int(input("Masukkan angka kedua   : "))
          hasil = nilai1 - nilai2
          print("Jadi hasil dari kedua angka adalah:",hasil)
    except ValueError:
        print("Harap masukkan input dengan angka")
while True:
    print("Selamat Datang di Kalkulator")
    print("==Menu Kalkulator==",
    "1.Tambah\n",
    "2.Kurang\n",
    "3.Keluar\n",
    )
    if pilihan == 1:
        tambah()
    elif pilihan == 2:
        kurang()
    elif pilihan == 3:
        print("Terimakasih telah menggunakan")
        break