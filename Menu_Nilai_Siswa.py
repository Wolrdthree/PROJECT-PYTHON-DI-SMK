try:
    nama_siswa = str(input("Masukkan nama anda :"))
    nilai_siswa = float(input("Masukkan nilai anda (0-100):  "))
    if nilai_siswa > 100 or nilai_siswa < 0:
        print("Tolong masukkan nilai sesuai yang diarahkan(0-100)")
    else:
        print("===HASIL===")
        print("Nama :",nama_siswa)
        print("Nilai:",nilai_siswa)
except ValueError:
    print("Tolong hanya masukkan angka")
