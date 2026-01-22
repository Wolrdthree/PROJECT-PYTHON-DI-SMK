print("Selamat datang di Kalkulator Mini Kami!")
def tambah ():
    try:
        nilai1= int (input("Masukkan nilai pertama : "))
        nilai2= int(input("Masukkan nilai kedua : "))
        hasil_tambah = nilai1 + nilai2
        print(f"Hasil dari {nilai1} + {nilai2} adalah {hasil_tambah}")
    except ValueError:
        print("Input harus berupa angka!")

def kurang():
    try:
        nilai1= int(input("Masukkan nilai pertama yang ingin dikurang:"))
        nilai2 = int(input("Dikurang nilai :"))
        hasil_kurang = nilai1 - nilai2
        print(f"Hasil dari {nilai1}-{nilai2} adalah {hasil_kurang}")
    except ValueError:
        print("Input harus berupa angka!")

def kali ():
    try:
        nilai1= int(input("Masukkan nilai pertama :"))
        nilai2 = int(input("Dikali nilai :"))
        hasil_kali = nilai1 * nilai2
        print(f"Hasil dari {nilai1} x {nilai2} adalah {hasil_kali}")
    except ValueError:
        print("Input harus berupa angka!")

def bagi():
    try:
        nilai1= int(input("Masukkan nilai yang ingin dibagi:"))
        nilai2 = int(input("Dibagi :"))
        hasil_bagi = nilai1 / nilai2
        print(f"Hasil dari {nilai1}/{nilai2} adalah {hasil_bagi}")
    except ValueError:
        print("Input harus berupa angka!")
    except ZeroDivisionError:
        print("Nilai tidak bisa dibagi dengan nol")

def pangkat():
    try:
        nilai1= int(input("Masukkan nilai basis yang ingin dipangkatkan :  "))
        nilai2 = int(input("Dipangkat :"))
        hasil_pangkat = nilai1 ** nilai2
        print(f"Hasil dari {nilai1} dipangkat {nilai2} adalah {hasil_pangkat}")
    except ValueError:
        print("Input harus berupa angka!")

def main():
    while True :
        try:
            print("")
            print(" +-+-+-+-+-+-+-+-+")
            print(" |MENU-KALKULATOR|\n",
                  "|===============|\n",
                  "|1.Tambah       |\n",
                  "|2.Kurang       |\n",
                  "|3.Kali         |\n",
                  "|4.Bagi         |\n",
                  "|5.Pangkat      |\n",
                  "|6.Keluar       |\n",
                  "+-+-+-+-+-+-+-+-+\n"
      )
            pilihan = int(input("Masukkan pilihan apa yang anda inginkan :"))
            if pilihan == 1:
                tambah()
            elif pilihan == 2:
                kurang()
            elif pilihan == 3:
                kali()
            elif pilihan == 4:
                bagi()
            elif pilihan == 5:
                pangkat()
            elif pilihan == 6:
                print("terimakasih telah menggunakan kalkulator mini kami😁")
                break
            else :
                print("Pilihan tidak tersedia!")
        except ValueError:
             print("Pilihan hanya dapat berupa angka!")
                
main()