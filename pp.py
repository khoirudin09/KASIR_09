print("--------------- WARUNG MAKAN PAK UDIN ---------------")
pembeli = input("Masukkan nama Pembeli: ")

def tampilkan_menu_makanan():
    print("\n----------------- Menu -----------------")
    print("1. MIE BAKSO - Rp 12000")
    print("2. MIE AYAM - Rp 11000")
    print("3. MIE AYAM GORENG - Rp 10000")
    print("4. MIE AYAM BAKSO - Rp 20000")
    print("5. KWETIAU - Rp 18000")

def tampilkan_menu_minuman():
    print("\n----------------- Menu Minuman -----------------")
    print("1. Teh Hangat - Rp 3000")
    print("2. Es teh - Rp 3000")
    print("3. Es jeruk - Rp 5000")

def fungsimakanan():
    tampilkan_menu_makanan()
    while True:
        try:
            nomor = int(input("Masukan Pilihan: "))
            if nomor not in range(1, 6):
                raise ValueError("Pilihan tidak ada, silahkan masukan lagi!!")
            break
        except ValueError as e:
            print(e)

    porsi = int(input("Berapa Porsi: "))
    if nomor == 1:
        totalmakan = porsi * 12000
        makan = "MIE BAKSO"
    elif nomor == 2:
        totalmakan = porsi * 11000
        makan = "MIE AYAM"
    elif nomor == 3:
        totalmakan = porsi * 10000
        makan = "MIE AYAM GORENG"
    elif nomor == 4:
        totalmakan = porsi * 20000
        makan = "MIE AYAM BAKSO"
    elif nomor == 5:
        totalmakan = porsi * 18000
        makan = "KWETIAU"
    
    print(f"{porsi} porsi {makan} = Rp {totalmakan}")
    return totalmakan, porsi, makan

def fungsiminuman():
    tampilkan_menu_minuman()
    while True:
        try:
            nomor = int(input("Masukan Pilihan: "))
            if nomor not in range(1, 4):
                raise ValueError("Pilihan tidak ada, silahkan masukan lagi!!")
            break
        except ValueError as e:
            print(e)

    gelas = int(input("Berapa Gelas: "))
    if nomor == 1:
        totalminum = gelas * 3000
        minum = "Teh Hangat"
    elif nomor == 2:
        totalminum = gelas * 3000
        minum = "Es Teh"
    elif nomor == 3:
        totalminum = gelas * 5000
        minum = "Es Jeruk"
    
    print(f"{gelas} gelas {minum} = Rp {totalminum}")
    return totalminum, gelas, minum

totalmakan, porsi, makan = fungsimakanan()
totalminum, gelas, minum = fungsiminuman()
totalsemua = totalmakan + totalminum

print("\nTotal harus Dibayar: Rp", totalsemua)
while True:
    try:
        uang = int(input("Uang Tunai Pembeli: Rp "))
        if uang < totalsemua:
            raise ValueError("Uang tidak cukup. Silakan masukkan jumlah yang sesuai.")
        break
    except ValueError as e:
        print(e)

kembalian = uang - totalsemua
print("Kembalian: Rp", kembalian)

print("\n=====================================")
print("========== STRUK PEMBAYARAN =========")
print("=====================================")
print("Nama\t\t:", pembeli)
print("Beli\t\t:", porsi, makan, "( Rp", totalmakan, ")")
print("\t\t ", gelas, minum, "( Rp", totalminum, ")")
print("Tagihan\t\t: Rp", totalsemua)
print("Dibayar\t\t: Rp", uang)
print("Kembalian\t: Rp", kembalian)
print("=====================================")
print("=====================================")
