import json
import os
import time
import pwinput
from prettytable import PrettyTable

FILE_TIKET = r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\tiket.json"
FILE_USER = r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\user.json"
FILE_TRANSAKSI = r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\transaksi.json"

MAKS_BELI = 4            # maksimal tiket per sekali pembelian
SANKSI_CEPAT = 5         # sanksi refund (%) jika refund dalam batas jam
SANKSI_LAMBAT = 10       # sanksi refund (%) jika lewat batas jam
BATAS_JAM_REFUND = 24    # batas jam sejak pembelian untuk sanksi cepat

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def baca_data(nama_file):
    try:
        with open(nama_file, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except ValueError:
        return[]

def simpan_data(nama_file, data):
    try:
        with open(nama_file, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except:
        print("Gagal menyimpan data!")
        return False

def validasi_password(password):
    angka = False
    unik = False

    for huruf in password:
        if huruf.isdigit():
            angka = True
        if not huruf.isalnum():
            unik = True

    return angka and unik

def tampilkan_tiket():
    tiket = baca_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\tiket.json")

    if len(tiket) == 0:
        print("Belum ada tiket")
        return

    tabel = PrettyTable()
    tabel.field_names = (
        "ID", "Nama Konser", "Tanggal",
        "Lokasi", "Harga", "Kuota Tiket"
    )

    for data in tiket:
        kuota = data ["kuota tiket"]
        if kuota == 0:
            kuota = "SOLD OUT"

        tabel.add_row([
            data["id"],
            data["nama"],
            data["tanggal"],
            data["lokasi"],
            f"Rp{data['harga']:,}".replace(",", "."), 
            kuota
        ])

    print(tabel)

def registrasi():
    print("========================================")
    print("               REGISTRASI               ")
    print("========================================")

    admin = baca_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\admin.json")
    users = baca_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\user.json")

    username = input("Masukkan username: ")
    if username == "":
        print("Username tidak boleh kosong!")
        return

    if len(username) < 8:
        print("Username minimal 8 karakter!")
        return

    while True:
        password = pwinput.pwinput("Masukkan password: ")

        if password == "":
            print("Password tidak boleh kosong!")
        elif " " in password:
            print("Password tidak boleh mengandung spasi!")
        elif not validasi_password(password):
            print("Password harus memiliki minimal 1 angka dan 1 karakter unik!")
        else:
            break

    if len(username) < 8:
        print("Username minimal 8 karakter!")
        return

    if not validasi_password(password):
        print("Password harus memiliki minimal 1 angka dan 1 karakter unik!")
        return
    
    for akun in admin + users:
        if akun.get("username") == username:
            print("Username sudah digunakan!")
            return

    akun_baru = {
        "username": username,
        "password": password,
        "role": "user",
        "saldo": 0
    }

    users.append(akun_baru)

    if simpan_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\user.json", users):
        print("Selamat, Registrasi berhasil!")

def login():
    print("========================================")
    print("                 LOGIN                  ")
    print("========================================")

    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")

    admin = baca_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\admin.json")
    users = baca_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\user.json")

    for akun in admin:
        if akun.get("username") == username and akun["password"] == password:
            print("Login admin berhasil!")
            time.sleep(1)
            menu_admin()

            return

    for akun in users:
        if akun.get("username") == username and akun["password"] == password:
            print("Login user berhasil!")
            time.sleep(1)
            menu_user(username)
            return

    print("Username atau password salah!")

def tambah_tiket():
    print("========================================")
    print("              TAMBAH TIKET              ")
    print("========================================")

    tiket = baca_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\tiket.json")

    nama = input("Nama konser: ")
    tanggal = input("Tanggal konser: ")
    lokasi = input("Lokasi konser: ")

    if nama == "" or tanggal == "" or lokasi == "":
        print("Nama konser, tanggal, dan lokasi tidak boleh kosong!")
        return

    try:
        harga = int(input("Harga tiket: "))
        kuota_tiket = int(input("Kuota tiket: "))

        if harga < 0 or kuota_tiket < 0:
            print("Harga dan kuota tiket tidak boleh negatif!")
            return

    except ValueError:
        print("Harga dan kuota tiket harus berupa angka!")
        return

    id_baru = 1

    for data in tiket:
        try:
            angka = int(data["id"][1:])
            if angka >= id_baru:
                id_baru = angka + 1
        except (ValueError, IndexError):
            pass
        
    id_baru_str = f"T{id_baru:03d}"

    tiket_baru = {
        "id": id_baru_str,
        "nama": nama,
        "tanggal": tanggal,
        "lokasi": lokasi,
        "harga": harga,
        "kuota tiket": kuota_tiket
    }       

    tiket.append(tiket_baru)

    if simpan_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\tiket.json", tiket):
        print("Tiket berhasil ditambahkan!")

def ubah_tiket():
    print("========================================")
    print("              UBAH TIKET                ")    
    print("========================================")

    tiket = baca_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\tiket.json")
    tampilkan_tiket()

    if len(tiket) == 0:
        return

    try:
        id_input = int(input("Masukkan ID tiket yang ingin diubah (angka saja, misal 1 untuk T001): "))
        id_cari = f"T{id_input:03d}"
    except ValueError:
        print("ID harus berupa angka!")
        return

    for data in tiket:
        if data["id"] == id_cari:
            print("Memasukkan data tiket yang baru")
            print("(Kosongkan lalu tekan Enter jika tidak ingin mengubah)")

            nama = input(f"Nama konser baru [{data['nama']}]: ").strip() or data["nama"]
            tanggal = input(f"Tanggal konser baru [{data['tanggal']}]: ").strip() or data["tanggal"]
            lokasi = input(f"Lokasi konser baru [{data['lokasi']}]: ").strip() or data["lokasi"]

            try:
                harga_input = input(f"Harga tiket baru [{data['harga']}]: ").strip()
                kuota_input = input(f"Kuota tiket baru [{data['kuota tiket']}]: ").strip()

                harga = int(harga_input) if harga_input != "" else data["harga"]
                kuota_tiket = int(kuota_input) if kuota_input != "" else data["kuota tiket"]

                if harga < 0 or kuota_tiket < 0:
                    print("Harga dan kuota tiket tidak boleh negatif!")
                    return

            except ValueError:
                print("Harga dan kuota tiket harus berupa angka!")
                return

            data["nama"] = nama
            data["tanggal"] = tanggal
            data["lokasi"] = lokasi
            data["harga"] = harga
            data["kuota tiket"] = kuota_tiket

            if simpan_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\tiket.json", tiket):
                print("Data tiket berhasil diubah!")
            return

    print("ID tiket tidak ditemukan!")

def hapus_tiket():
    print("========================================")
    print("              HAPUS TIKET               ")    
    print("========================================")

    tiket = baca_data(r"C:\Users\hp\OneDrive\Documents\vscode shaina\SISTEM MANAJEMEN TIKET KONSER\tiket.json")
    tampilkan_tiket()

    if len(tiket) == 0:
        return

    try:
        id_input = int(input("Masukkan ID tiket yang ingin dihapus (angka saja, misal 1 untuk T001): "))
        id_cari = f"T{id_input:03d}"
    except ValueError:
        print("ID harus berupa angka!")
        return

    for data in tiket:
        if data["id"] == id_cari:
            konfirmasi = input("Apakah Anda yakin ingin menghapus tiket ini? (y/n): ").lower()

            if konfirmasi == "y":
                tiket.remove(data)
                if simpan_data(FILE_TIKET, tiket):
                    print("Tiket berhasil dihapus!")
            else:
                print("Penghapusan tiket dibatalkan!")
            return

    print("ID tiket tidak ditemukan!")

def cek_saldo(username):
    users = baca_data(FILE_USER)

    for akun in users:
        if akun ["username"] == username:
            print(f"Saldo Anda: Rp{akun.get('saldo', 0):,}".replace(",", "."))
            return

def ambil_saldo(username):
    for akun in baca_data(FILE_USER):
        if akun["username"] == username:
            return akun.get("saldo", 0)
    return 0

def top_up(username):
    print("========================================")
    print("                  TOP UP                ")    
    print("========================================")

    users = baca_data(FILE_USER)

    try:
        nominal = int(input("Nominal top up: "))

        if nominal <= 0:
            print("Nominal harus lebih dari 0!")
            return

    except ValueError:
        print("Nominal harus berupa angka!")
        return

    for akun in users:
        if akun["username"] == username:
            akun["saldo"] = akun.get("saldo", 0) + nominal

            if simpan_data(FILE_USER, users):
                print(f"Top up berhasil! Saldo sekarang: Rp{akun['saldo']:,}".replace(",", "."))
                return

def cetak_invoice(transaksi):
    print("========================================")
    print("                INVOICE                 ")
    print("========================================")
    print(f"No Invoice : {transaksi['no']}")
    print(f"Waktu      : {transaksi['waktu']}")
    print(f"Pembeli    : {transaksi['username']}")
    print(f"Konser     : {transaksi['konser']}")
    print(f"Jumlah     : {transaksi['jumlah']} x Rp{transaksi['harga']:,}".replace(",", "."))
    print(f"Total      : Rp{transaksi['total']:,}".replace(",", "."))
    print(f"Sisa Saldo : Rp{transaksi['sisa_saldo']:,}".replace(",", "."))
    print("========================================")

def beli_tiket(username):
    print("========================================")
    print("              BELI TIKET                ")
    print("========================================")

    tiket = baca_data(FILE_TIKET)
    users = baca_data(FILE_USER)
    tampilkan_tiket()

    if len(tiket) == 0:
        return

    try:
        id_input = int(input("Masukkan ID tiket yang ingin dibeli (angka saja, misal 1 untuk T001): "))
        id_cari = f"T{id_input:03d}"
        jumlah = int(input(f"Jumlah tiket (maks {MAKS_BELI}): "))

        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return

    except ValueError:
        print("Input harus berupa angka!")
        return

    if jumlah > MAKS_BELI:
        print(f"Maksimal pembelian {MAKS_BELI} tiket per transaksi!")
        return

    item = None
    for data in tiket:
        if data["id"] == id_cari:
            item = data

    akun = None
    for data in users:
        if data["username"] == username:
            akun = data

    if item is None:
        print("ID tiket tidak ditemukan!")
        return

    if item["kuota tiket"] == 0:
        print("Maaf, tiket SOLD OUT!")
        return

    if jumlah > item["kuota tiket"]:
        print("Stok tiket tidak cukup!")
        return

    total = item["harga"] * jumlah

    if akun.get("saldo", 0) < total:
        print("Saldo tidak cukup, silahkan top up terlebih dahulu!")
        return

    konfirmasi = input(f"Total Rp{total:,}. Lanjutkan pembelian? (y/n): ".replace(",", ".")).lower()

    if konfirmasi != "y":
        print("Pembelian dibatalkan!")
        return

    item["kuota tiket"] -= jumlah
    akun["saldo"] = akun.get("saldo", 0) - total

    transaksi = baca_data(FILE_TRANSAKSI)

    transaksi_baru = {
        "no": f"INV{len(transaksi) + 1:04d}",
        "id_tiket": item["id"],
        "status": "Berhasil",
        "waktu": time.strftime("%Y-%m-%d %H:%M:%S"),
        "username": username,
        "konser": item["nama"],
        "jumlah": jumlah,
        "harga": item["harga"],
        "total": total,
        "sisa_saldo": akun["saldo"]
    }

    transaksi.append(transaksi_baru)

    if simpan_data(FILE_TIKET, tiket) and simpan_data(FILE_USER, users) and simpan_data(FILE_TRANSAKSI, transaksi):
        print("Pembelian berhasil!")
        cetak_invoice(transaksi_baru)

def riwayat_transaksi(username):
    print("========================================")
    print("            RIWAYAT TRANSAKSI           ")
    print("========================================")

    semua = baca_data(FILE_TRANSAKSI)
    milik_user = []

    for trx in semua:
        if trx.get("username") == username:
            milik_user.append(trx)

    if len(milik_user) == 0:
        print("Belum ada transaksi")
        return

    tabel = PrettyTable()
    tabel.field_names = ("No Invoice", "Waktu", "Konser", "Jumlah", "Total", "Status")

    for trx in milik_user:
        tabel.add_row([
            trx["no"],
            trx["waktu"],
            trx["konser"],
            trx["jumlah"],
            f"Rp{trx['total']:,}".replace(",", "."),
            trx.get("status", "Berhasil")
        ])

    print(tabel)

def laporan_penjualan():
    print("========================================")
    print("            LAPORAN PENJUALAN           ")
    print("========================================")

    transaksi = baca_data(FILE_TRANSAKSI)

    if len(transaksi) == 0:
        print("Belum ada transaksi")
        return

    per_konser = {}
    total_pendapatan = 0
    total_tiket = 0
    total_transaksi = 0
    total_sanksi = 0

    for trx in transaksi:
        if trx.get("status") == "Refund":
            total_sanksi += trx.get("sanksi", 0)
            continue
        
        nama = trx["konser"]

        if nama not in per_konser:
            per_konser[nama] = {"terjual": 0, "pendapatan": 0}

        per_konser[nama]["terjual"] += trx["jumlah"]
        per_konser[nama]["pendapatan"] += trx["total"]
        total_pendapatan += trx["total"]
        total_tiket += trx["jumlah"]
        total_transaksi += 1

    if len(per_konser) == 0:
        print("Belum ada transaksi yang berhasil")
        return

    tabel = PrettyTable()
    tabel.field_names = ("Nama Konser", "Tiket Terjual", "Pendapatan")

    for nama in per_konser:
        tabel.add_row([
            nama,
            per_konser[nama]["terjual"],
            f"Rp{per_konser[nama]['pendapatan']:,}".replace(",", ".")
        ])

    print(tabel)
    print(f"Total transaksi  : {total_transaksi}")
    print(f"Total tiket      : {total_tiket}")
    print(f"Sanksi refund    : Rp{total_sanksi:,}".replace(",", "."))
    print(f"Total pendapatan : Rp{total_pendapatan + total_sanksi:,}".replace(",", "."))

def daftar_user():
    print("========================================")
    print("               DAFTAR USER              ")
    print("========================================")

    users = baca_data(FILE_USER)

    if len(users) == 0:
        print("Belum ada user terdaftar")
        return

    tabel = PrettyTable()
    tabel.field_names = ("No", "Username", "Saldo")

    nomor = 1
    for akun in users:
        tabel.add_row([nomor, akun["username"], f"Rp{akun.get('saldo', 0):,}".replace(",", ".")])
        nomor += 1

    print(tabel)

def hitung_sanksi_persen(trx):
    try:
        waktu_beli = time.mktime(time.strptime(trx["waktu"], "%Y-%m-%d %H:%M:%S"))
    except (ValueError, KeyError):
        return SANKSI_LAMBAT

    selisih_jam = (time.time() - waktu_beli) / 3600

    if selisih_jam <= BATAS_JAM_REFUND:
        return SANKSI_CEPAT
    return SANKSI_LAMBAT

def refund_tiket(username):
    print("========================================")
    print("                REFUND                  ")
    print("========================================")

    semua = baca_data(FILE_TRANSAKSI)
    bisa_refund = []

    for trx in semua:
        if trx.get("username") == username and trx.get("status", "Berhasil") == "Berhasil":
            bisa_refund.append(trx)

    if len(bisa_refund) == 0:
        print("Tidak ada transaksi yang bisa direfund!")
        return

    tabel = PrettyTable()
    tabel.field_names = ("No Invoice", "Waktu", "Konser", "Jumlah", "Total")

    for trx in bisa_refund:
        tabel.add_row([
            trx["no"],
            trx["waktu"],
            trx["konser"],
            trx["jumlah"],
            f"Rp{trx['total']:,}".replace(",", ".")
        ])

    print(tabel)

    nomor = input("Masukkan No Invoice yang ingin direfund: ").upper()

    target = None
    for trx in bisa_refund:
        if trx["no"] == nomor:
            target = trx

    if target is None:
        print("No Invoice tidak ditemukan!")
        return

    sanksi_persen = hitung_sanksi_persen(target)
    sanksi = target["total"] * sanksi_persen // 100
    dikembalikan = target["total"] - sanksi

    print(f"Total pembelian : Rp{target['total']:,}".replace(",", "."))
    print(f"Sanksi {sanksi_persen}%".ljust(16) + f": Rp{sanksi:,}".replace(",", "."))
    print(f"Dana kembali    : Rp{dikembalikan:,}".replace(",", "."))
    konfirmasi = input("Lanjutkan refund? (y/n): ").lower()

    if konfirmasi != "y":
        print("Refund dibatalkan!")
        return

    tiket = baca_data(FILE_TIKET)
    users = baca_data(FILE_USER)

    for data in tiket:
        cocok_id = data["id"] == target.get("id_tiket")
        cocok_nama = target.get("id_tiket") is None and data["nama"] == target["konser"]
        if cocok_id or cocok_nama:
            data["kuota tiket"] += target["jumlah"]

    for akun in users:
        if akun["username"] == username:
            akun["saldo"] = akun.get("saldo", 0) + dikembalikan

    target["status"] = "Refund"
    target["sanksi_persen"] = sanksi_persen
    target["sanksi"] = sanksi
    target["dikembalikan"] = dikembalikan

    if simpan_data(FILE_TIKET, tiket) and simpan_data(FILE_USER, users) and simpan_data(FILE_TRANSAKSI, semua):
        print(f"Refund berhasil! Rp{dikembalikan:,} dikembalikan ke saldo (sanksi {sanksi_persen}%).".replace(",", "."))


def menu_admin():
    while True:
        print("========================================")
        print("               MENU ADMIN               ")    
        print("========================================")
        print("1. Lihat Data Tiket")
        print("2. Tambah Tiket")
        print("3. Ubah Data Tiket")
        print("4. Hapus Tiket")
        print("5. Laporan Penjualan")
        print("6. Daftar User")
        print("7. Logout")
        print("========================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_tiket()
        elif pilihan == "2":
            tambah_tiket()
        elif pilihan == "3":
            ubah_tiket()
        elif pilihan == "4":
            hapus_tiket()
        elif pilihan == "5":  
            laporan_penjualan()
        elif pilihan == "6":
            daftar_user()
        elif pilihan == "7":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")

        input("\nTekan Enter untuk kembali...")

def menu_user(username):
    while True:
        print("========================================")
        print("                MENU USER               ")    
        print("========================================")
        print(f"Pengguna : {username}")
        print(f"Saldo    : Rp{ambil_saldo(username):,}".replace(",", "."))
        print("----------------------------------------")
        print("1. Lihat Data Tiket")
        print("2. Top Up")
        print("3. Beli tiket")
        print("4. Riwayat Transaksi")
        print("5. Refund Tiket")
        print("6. Logout")
        print("========================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_tiket()
        elif pilihan == "2":
            top_up(username)
        elif pilihan == "3":
            beli_tiket(username)
        elif pilihan == "4":
            riwayat_transaksi(username)
        elif pilihan == "5":
            refund_tiket(username)
        elif pilihan == "6":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")

        input("\nTekan Enter untuk kembali...")

def menu_utama():
    while True:
        bersihkan_layar()

        print("========================================")
        print("              TIKET KONSER              ")
        print("========================================")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        print("========================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            login()
        elif pilihan == "2":
            registrasi()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program!")
            break
        else:
            print("Pilihan tidak valid!")

        input("\nTekan Enter untuk kembali ke menu utama...")

while True:
    try:
        menu_utama()
        break
    except KeyboardInterrupt:
        print("\nKembali ke menu utama...")