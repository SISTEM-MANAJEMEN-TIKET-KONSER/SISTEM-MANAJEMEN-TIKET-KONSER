# PA-DDP-KELOMPOK-1-SISTEM-MANAJEMEN-TIKET-KONSER

## Anggota & Peran

- Shaina Naila Raihana (2609116090) 
- Achmad Rozaaq Adiprayitno (2690116098) 
- Maika Izano Filzan (2609116099) 
- Firza Aulia Syahlin (26091160107)

# SISTEM MANAJEMEN TIKET KONSER

## Deskripsi

Sistem manajemen tiket konser ini merupakan aplikasi berbasis python yang dirancang untuk mempermudah proses penjualan dan pengelolaan tiket konser. Melalui sistem ini, user dapat melakukan registrasi, top up saldo, membeli tiket, melihat riwayat transaksi, serta mengajukan refund. Sementara itu, admin dapat mengelola data tiket (tambah, ubah, hapus), melihat laporan penjualan, dan melihat daftar user. Seluruh data disimpan dalam file JSON (admin.json, user.json, tiket.json, dan transaksi.json).

## Tujuan

- Mempermudah pengelolaan data tiket konser secara terstruktur.
- Mengotomatiskan proses pembelian, mulai dari pengecekan stok dan saldo hingga pencetekan invoice.
- Mencatat seluruh transaksi sehingga laporan penjualan dapat dilihat secara ringkas.
- Menerapkan aturan bisnis yang jelas yaitu pembelian, validasi akun, dan sanksi refund.

## Aturan Sistem Utama

| Aturan | Nilai |
| :---- | :---- |
| Maksimal tiket per transaksi | 4 Tiket |
| Username | Minimal 8 karakter |
| Password | Tanpa spasi, minimal 1 angka dan 1 karakter unik |
| Sanksi refund ≤ 24 jam sejak pembelian | 5% |
| Sanksi refund > 24 jam sejak pembelian | 10% |

# FLOWCHART

## Flowchart Menu Utama

<img width="1579" height="1131" alt="Flowchart_Tiket_Konser_revisi_v3-Alur Utama drawio" src="https://github.com/user-attachments/assets/0aa404fb-25bb-4007-9767-6f692cafa7a3" />

Flowchart alur utama menggambarkan jalannya program dari START hingga SELESAI. Program diawali dengan menampilkan menu utama yang berisi tiga pilihan yaitu, Login, Registrasi, dan Keluar.

Pada jalur Login, pengguna memasukkan username dan password, lalu sistem membaca data admin.json dan user.json untuk validasi akun. Jika login tidak valid, sistem menampilkan "Login gagal". Jika valid, sistem mengecek apakah akun ada di admin.json, jika ya, pengguna masuk ke menu admin, jika tidak pengguna masuk ke menu user.

Pada jalur registrasi, pengguna memasukkan username dan password, lalu sistem memvalidasi username terlebih dahulu. Jika valid atau sudah digunakan, muncul pesan "Username telah digunakan". Jika username valid, sistem memvalidasi password. Jika tidak sesuai aturan, sistem menampilkan pesan kesalahan password. Jika keduanya valid, sistem membuat akun baru dengan role = user dan saldo = 0, menyimpannya ke user.json. lalu menampilkan "Registrasi berhasil".

Pada jalur keluar, program berakhir (SELESAI). Selain keluar, setiap jalur akan kembali ke menu utama.

## Flowchart Menu User

<img width="2572" height="1803" alt="Flowchart_Tiket_Konser_revisi_v3-Flowchart Menu User drawio" src="https://github.com/user-attachments/assets/da515c95-d9ca-49b5-8f28-fe50d1ccbf4f" />

Flowchart ini menjelaskan alur aktivitas user. Menu user menampilkan nama dan saldo pengguna beserta enam pilihan (Lihat data tiket, top up, beli tiket, riwayat transaksi, refund tiket, dan logout). Input di luar 1-6 menampilkan pesan pilihan tidak valid.

- Lihat data tiket: sistem membaca tiket.json. Jika kosong tampil "belum ada tiket", jika ada tampil tabel tiket dengan kuota 0 ditulis SOLD OUT.
- Top up: user memasukkan nominal. Jika bukan angka atau tidak lebih dari 0, muncul pesan kesalahan. Jika valid, saldo ditambah, disimpan ke user.json, dan saldo terbaru ditampilkan.
- Beli tiket: sistem menampilkan daftar tiket, user memasukkan ID dan jumlah. Sistem lalu melakukan serangkaian pengecekan secara berurutan, jumlah 1-4, ID ditemukan, kuota lebih dari 0, kuota cukup, dan saldo cukup. Jika semua terpenuhi, user diminta konfirmasi (y/n). Setelah dikonfirmasi, saldo dan kuota dikurangin, transaksi disimpan ke transaksi.json dengan status berhasil, dan invoice ditampilkan.
- Riwayat transaksi: sistem membaca trankasi.json, memfilter transaksi berdasarkan username yang login, lalu menampilkannya beserta status.
- Refund tiket: sistem memfilter transaksi berstatus berhasil milik user, lalu user memasukkan No invoice. Sistem menghitung sanksi (5% jika dalam 24 jam sejak pembelian, jika lebih maka akan kena sanksi 10%), menampilkan total pembelian, sanksi, dan dana kembali, lalu meminta konfirmasi . Jika dikonfirmasi, kuota tiket dikembalikan, saldo ditambah sebesar dana kembali, status transaksi menjadi Refund, dan perubahan disimpan ke tiga file JSON.
- Logout: menampilkan pesan logout berhasil dan kembali ke menu utama.

## FLOWCHART MENU ADMIN

<img width="2984" height="1059" alt="Flowchart_Tiket_Konser_revisi_v3-Flowchart Menu Admin drawio" src="https://github.com/user-attachments/assets/a804e311-ff56-42f7-833f-1c539130aa3f" />

Flowchart ini menjelaskan alur kerja admin. Menu admin memiliki 7 pilihan (Lihat Data Tiket, Tambah Tiket, Ubah Data Tiket, Hapus Data Tiket, Laporan Penjualan, Daftar User, dan Logout).

- Lihat Data Tiket: membaca tiket.json dan menampilkan daftar tiket, atau pesan "belum ada tiket" jika kosong.
- Tambah Tiket: admin mengisi nama konser, tanggal, lokasi, harga, dan kuot. Jika ada data kosong atau harga/kuota bukan angka minimal 0, muncul pesan kesalahan. Jika valid, sistem membuat ID baru (T001, T002, dst), menyimpan ke tiket.json, dan menampilkan "Tiket berhasil ditambahkan".
- Ubah Data Tiket: admin memilih ID tiket. Jika tidak ditemukan tampil pesan tidak ditemukan. Jika ada, admin mengisi data baru (Enter = tidak diubah), harga dan kuota divalidasi, lalu tiket.json diperbarui.
- Hapus Tiket: admin memilih ID tiket, lalu diminta konfirmasi (y/n). jika setuju, tiket dihapus dari tiket.json. Jika tidak, penghapusan dibatalkan.
- Laporan Penjualan: sistem membaca transaksi.json, melewati transaksi berstatus Refund (sanksinya dihitung sebagai pendapatan), lalu menghitung tiket terjual dan pendapatan per konser. Hasilnya ditampilkan bersama total transaksi, total tiket, sanksi refund, dan total pendapatan.
- Daftar User: membaca user.json dan menampilkan username serta saldo setiap user.
- Logout: menampilkan pesan logout berhasil dan kembali ke menu utama.

## Daftar Fitur per Role

| Role | Fitur |
| :----: | :---- |
| Umum (sebelum login) | Login, Registrasi, Keluar |
| User | Lihat Data Tiket, Top Up, Beli Tiket (maks 4 per transaksi, dengan invoice), Riwayat Transaksi, Refund Tiket (dengan sanksi 5%/10%), Logout |
| Admin | Lihat Data Tiket, Tambah Tiket, Ubah Data Tiket, Hapus Tiket, Laporan Penjualan, Daftar User, Logout |

# PENJELASAN FUNGSI DAN OUTPUT PROGRAM

