total = []
print("............................................")
print("              Kasir Swalayan UDP            ")
print("............................................")


# fungsi untuk menambah barang
def tanya():
    while True:
        print("\n-----------------------------------")
        tanya = input("Ingin tambah barang? [y/t]   : ")
        print("-------------------------------------")
        if tanya.lower() == 'y': # penggunaan {.lower} berguna mengubah huruf apapun menjadi kecil
            daftar_barang()
        elif tanya.lower() == 't':
            akhir()
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' untuk ya atau 't' untuk tidak.")

# fungsi menampilkan barang
def daftar_barang():
    print("NO | Nama Barang | Harga")
    print("============================================")
    print("1  | beras/kg    | 12100")
    print("2  | tempe       | 5000")
    print("3  | garam halus | 2000")
    print("____________________________________________")

    kode = int(input("Masukkan angka barang: "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah barang: "))
        total1 = 12100 * jumlah1
        total.append(total1)
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah barang: "))
        total2 = 5000 * jumlah2
        total.append(total2)
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah barang: "))
        total3 = 2000 * jumlah3
        total.append(total3)
    else:
        print("Kode barang tidak valid, silakan coba lagi.")

# fungsi penotalan barang dan diskon
def akhir():
    if total:
        print("Sub Total    : ", sum(total)) # fungsi sum yaitu menjumlahkan semua yang ada dalam variable sum
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8 / 100
        elif a > 300000:
            diskon = a * 5 / 100
        print("Potongan Harga : ", diskon)
        totalakhir = a - diskon
        print("Total          : ", totalakhir)
        print("----------------------------------------------")
        bayar = int(input("Bayar          : "))
        kembalian = bayar - totalakhir
        print("Kembalian      : ", kembalian)
        print("----------------------------------------------")
        print("------------->   Terima Kasih   <-------------")
        print("----------------------------------------------")
    else:
        print("Tidak ada barang yang dibeli.")

# Memulai program dengan memanggil fungsi untuk pertama kaliF
daftar_barang()
tanya()
