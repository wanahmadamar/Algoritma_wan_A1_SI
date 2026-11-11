MENU = {
    1: ("Nasi Goreng", 25000),
    2: ("Mie Ayam", 15000),
    3: ("Ayam Geprek", 20000),
    4: ("Sate Ayam", 30000),
    5: ("Bakso", 18000),
}

def rupiah(angka):
    return "Rp " + f"{angka:,}".replace(",", ".")

def tampilkan_menu():
    print("\n--- DAFTAR MENU MAKANAN ---")
    for no, (nama, harga) in MENU.items():
        print(f"{no}. {nama:<12} - {rupiah(harga)}")
    print("0. Selesai Memilih")
    print("---------------------------")

def minta_jumlah(nama):
    teks = input(f"Jumlah {nama}: ").strip()
    if not teks.isdigit() or int(teks) <= 0:
        print(f"  Jumlah tidak valid, {nama} dilewati.")
        return 0
    return int(teks)

print("=========================================")
print("     APLIKASI KASIR RESTORAN BARU        ")
print("=========================================")

keranjang = {}  # {nomor_menu: jumlah}

while True:
    tampilkan_menu()
    masukan = input("Pilih menu (contoh: 1,3,5 | 0 = selesai): ").strip()

    if masukan == "0":
        if not keranjang:
            print("Belum ada pesanan, silakan pilih menu dulu.")
            continue
        break

    # Pisahkan berdasarkan koma, hapus duplikat tapi pertahankan urutan
    bagian = [p.strip() for p in masukan.split(",") if p.strip()]
    pilihan_valid, tidak_valid = [], []
    for p in bagian:
        if p.isdigit() and int(p) in MENU:
            if int(p) not in pilihan_valid:
                pilihan_valid.append(int(p))
        else:
            tidak_valid.append(p)

    if tidak_valid:
        print(f"Pilihan tidak tersedia: {', '.join(tidak_valid)}")
    if not pilihan_valid:
        continue

    # Tanya jumlah untuk tiap menu yang dipilih
    for no in pilihan_valid:
        nama = MENU[no][0]
        jumlah = minta_jumlah(nama)
        if jumlah:
            keranjang[no] = keranjang.get(no, 0) + jumlah
            print(f"-> {jumlah} {nama} ditambahkan")

# Hitung total
total_belanja = sum(MENU[no][1] * qty for no, qty in keranjang.items())

# Diskon 20% jika total > Rp200.000
persen_diskon = 20 if total_belanja > 200000 else 0
potongan = total_belanja * persen_diskon // 100
total_bayar = total_belanja - potongan

# Struk
print("\n=========================================")
print("           STRUK PEMBAYARAN              ")
print("=========================================")
for no, qty in keranjang.items():
    nama, harga = MENU[no]
    print(f"{nama:<12} {qty:>2} x {rupiah(harga):>10} = {rupiah(harga * qty):>12}")
print("-----------------------------------------")
print(f"Total Belanja : {rupiah(total_belanja)}")
print(f"Diskon        : {persen_diskon}%")
print(f"Potongan      : {rupiah(potongan)}")
print("-----------------------------------------")
print(f"Total Bayar   : {rupiah(total_bayar)}")
print("=========================================")
print("              Terima Kasih               ")
print("=========================================")