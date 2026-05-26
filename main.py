# DATA BARANG
barang = {
    "Makanan": [["Indomie", 4000,10],["Roti",12000,8],["Beras",15000,5],["Telur",25000,7],["Sosis",10000,6]],

    "Minuman": [["Susu",15000,10],["Teh",5000,12],["Kopi",8000,9],["Air Mineral",4000,15],["Jus",10000,7]],

    "Snack": [["Chitato",12000,6],["Biskuit",9000,8],["Wafer",7000,10],["Coklat",15000,5],["Permen",3000,20]],

    "Kebersihan": [["Sabun",8000,9],["Shampoo",17000,6],["Pasta Gigi",12000,7],["Sikat Gigi",10000,10],["Detergen",20000,4]],

    "Peralatan": [["Piring",25000,5],["Gelas",15000,8],["Sendok",5000,15],["Tisu",10000,12],["Botol",20000,6]]
}
pesanan = []
member = False

# MENU
def tampilkan_menu():

    print("\n==============================")
    print("      Kasir Supermarket 🛒 ")
    print("==============================")
    print("1. Lihat Daftar Barang")
    print("2. Tambah Pesanan")
    print("3. Member Diskon")
    print("4. Cetak Struk")
    print("5. Hitung Kembalian")
    print("6. Keluar")


# LIHAT BARANG
def lihat_barang():

    for kategori, daftar in barang.items():

        print(f"\n===== {kategori.upper()} =====")
        print(f"{'Nama':<15}{'Harga':<12}{'Stok'}")
        print("-" * 35)

        for item in daftar:
            print(f"{item[0]:<15}Rp{item[1]:<12}{item[2]}")


# TAMBAH PESANAN
def tambah_pesanan():

    nama = input("\nMasukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah: "))

    ditemukan = False

    for daftar in barang.values():

        for item in daftar:

            if nama.lower() == item[0].lower():

                ditemukan = True

                if jumlah <= item[2]:

                    total = item[1] * jumlah

                    pesanan.append([item[0], jumlah, total])

                    item[2] -= jumlah

                    print(f"\n{item[0]} berhasil ditambahkan!")

                else:
                    print("\nStok tidak cukup!")

    if not ditemukan:
        print("\nBarang tidak ditemukan!")


# MEMBER
def member_diskon():

    global member

    pilihan = input("\nApakah punya member? (y/n): ")

    if pilihan == "y":
        member = True
        print("\nDiskon member 10% berhasil digunakan!")

    else:
        member = False
        print("\nAnda tidak menggunakan member.")


# CETAK STRUK
def cetak_struk():

    total_belanja = 0

    print("\n========== STRUK BELANJA ==========")

    for data in pesanan:

        print(f"{data[0]} x{data[1]} = Rp{data[2]}")

        total_belanja += data[2]

    diskon = total_belanja * 0.10 if member else 0
    pajak = total_belanja * 0.05

    total_akhir = total_belanja - diskon + pajak

    print("\n===================================")
    print(f"Subtotal : Rp{int(total_belanja)}")
    print(f"Diskon   : Rp{int(diskon)}")
    print(f"Pajak    : Rp{int(pajak)}")
    print(f"Total    : Rp{int(total_akhir)}")
    print("===================================")


# HITUNG KEMBALIAN
def hitung_kembalian():

    total = 0

    for data in pesanan:
        total += data[2]

    uang = int(input("\nMasukkan uang pembayaran: "))

    kembalian = uang - total

    print(f"\nKembalian : Rp{kembalian}")


# PROGRAM UTAMA
while True:

    tampilkan_menu()

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        lihat_barang()

    elif pilihan == "2":
        tambah_pesanan()

    elif pilihan == "3":
        member_diskon()

    elif pilihan == "4":
        cetak_struk()

    elif pilihan == "5":
        hitung_kembalian()

    elif pilihan == "6":
        print("\nTerima kasih sudah berbelanja di Supermarket!")
        break

    else:
        print("\nMenu belum tersedia!")