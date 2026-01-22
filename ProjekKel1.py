import datetime

def hitung_diskon(total):
    if total >= 500000:
        return total * 0.10 
    elif total >= 250000:
        return total * 0.05 
    else:
        return 0

def simpan_ke_file(data):
    try:
        with open("tugasnov.txt", "a") as file:
            file.write(data + "\n")
        print("Data berhasil disimpan ke 'tugasnov.txt'")
    except FileNotFoundError:
        print("File tidak ditemukan!")

def main():
    print("=== APLIKASI KASIR SEDERHANA ===\n")

    daftar_belanja = []
    total_harga = 0

    while True:
        nama = input("Nama barang : ")
        harga = int(input("Harga barang : "))
        jumlah = int(input("Jumlah : "))

        subtotal = harga * jumlah
        total_harga += subtotal

        daftar_belanja.append((nama, harga, jumlah, subtotal))

        lagi = input("Tambahkan barang lain? (y/n): ").lower()
        if lagi == "n":
            break

    
    diskon = hitung_diskon(total_harga)
    total_bayar = total_harga - diskon

    print("\n===== STRUK BELANJA =====")
    waktu = datetime.datetime.now().strftime("-%m-%Y %H:%M")
    print("Waktu :", waktu)
    print("------------------------------")

    struk = f"STRUK BELANJA\nWaktu: {waktu}\n\n"

    for item in daftar_belanja:
        nama, harga, jumlah, subtotal = item
        print(f"{nama} x{jumlah} = Rp{subtotal}")
        struk += f"{nama} x{jumlah} = Rp{subtotal}\n"

    print("------------------------------")
    print(f"Total Belanja : Rp{total_harga}")
    print(f"Diskon        : Rp{int(diskon)}")
    print(f"Total Bayar   : Rp{int(total_bayar)}")
    print("==============================")

    struk + (
        "------------------------------\n"
        f"Total Belanja : Rp{total_harga}\n"
        f"Diskon        : Rp{int(diskon)}\n"
        f"Total Bayar   : Rp{int(total_bayar)}\n"
        "==============================\n"
    )

    simpan_ke_file(struk)

main()
