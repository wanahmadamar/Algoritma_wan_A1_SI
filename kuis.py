nama = input("Masukkan Nama: ")

if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    print("Nama tidak terdaftar!")
    exit()

print(f"Target nilai {nama}: {target}")

i = 1

while i <= 3:
    nilai = int(input(f"Masukkan Nilai {i}: "))

    if nilai >= target:
        print(f"{nama} berhasil lulus setelah {i} kali percobaan!")
        break
    else:
        print(f"Nilai belum mencapai target {target}.")

    if i == 3:
        print(f"{nama} tidak lulus setelah 3 kali percobaan!")

    i += 1
