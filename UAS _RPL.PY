while True:
   print("===KASIR SEDERHANA===")
   print("1. Belanja")
   print("2. Cetak struk & keluar")
   pilihan = int(input("Masukkan pilihan anda: "))
   if pilihan == 1 :
    nama = str(input("Masukkan nama barang : "))
    harga = int(input("Masukkan harga barang ; "))
    jumlah = int(input("Masukkan jumlah barang : "))
    harga2 = harga *jumlah
    if harga2 >= 100000:
       diskon=0.1
    else:
       diskon=0
    harga_Total = int(harga2 + (harga2*diskon))

   elif pilihan == 2:
    print("\n =====STRUK SEDERHANA====="
         ,"\nNama Barang :",nama
         ,f"\nHarga barang  :{harga}"
         ,f"\nJumlah yang dibeli :{jumlah}"
         ,f"\nHarga Sementara :{harga2}"
         ,"\n==========================="
       ,f"\nHARGA TOTAL : {harga_Total}"
            )
    print("TERIMAKASIH TELAH MENGGUNAKAN SISTEM KAMI")
    break
   else:
      print("Pilihan tidak ada dimenu!")   
