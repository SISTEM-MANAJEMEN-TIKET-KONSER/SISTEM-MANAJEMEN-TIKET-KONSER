# KELOMPOK-1-SISTEM-MANAJEMEN-TIKET-KONSER

## Anggota & Peran

| No | Nama | NIM | Peran |
| :---- | :---- | :---- | :---- |
| 1. | Shaina Naila Raihana | 2609116090 | Perancang konsep sistem, programmer (seluruh kode main.py), pembuat flowchart, dan penyusun laporan, mengelola repository GitHub |
| 2. | Achmad Rozaaq Adiprayitno | 2609116098 | Pembuat flowchart, penyusun laporan, dan mengelola github |
| 3. | Maika Izano Filzan | 2609116099 | Penyusun laporan |
| 4. | Firza Aulia Syahlin | 26091160107 | Pembuat flowchart dan penyusun laporan |

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

## 1. Penggunaan Library, Modul, dan Konstanta

<img width="749" height="202" alt="Screenshot 2026-11-03 155159" src="https://github.com/user-attachments/assets/244c8612-ccfa-44c7-b860-fd81203ef1fe" />

Di awal program kami menggunakan beberapa library dan modul, yaitu json, os, time, pwinput, dan prettytable. json untuk membaca dan menulis data dalam format JSON. os untuk membersihkan tampilan layar terminal. time untuk mengambil tanggal dan waktu transaksi serta menghitung selisih jam saat refund. pwinput untuk mengubah karakter password menjadi tanda *. prettytable untuk menampilkan data dalam bentuk tabel.

Selain itu, terdapat konstanta FILE_TIKET, FILE_USER, dan FILE_TRANSAKSI sebagai lokasi file penyimpanan, serta konstanta aturan bisnis MAKS_BELI = 4, SANKSI_CEPAT = 5, SANKSI_LAMBAT = 10, dan BATAS_JAM_REFUND = 24. Dengan konstanta ini, aturan dapat diubah di satu tempat tanpa mengubah logika fungsi.

## 2. Fungsi Bersihkan Layar, Baca Data, dan Simpan Data

<img width="623" height="304" alt="Screenshot 2026-11-03 154936" src="https://github.com/user-attachments/assets/21a96e6e-2cab-4389-9674-1f71c3cfb381" />

Fungsi bersihkan_layar() menjalankan perintah cls pada windows atau clear pada sistem lain. Fungsi baca_data(nama_file) membuka file JSON dan mengembalikan list kosong [] agar program tidak error. Fungsi simpan_data(nama_file, data) membuka file dalam mode tulis ( w ) lalu menyimpan data dalam format JSON dengan indentasi 4. Fungsi ini mengembalikan True jika berhasil dan False (disertai pesan "Gagal menyimpan data!") jika gagal, sehingga fungsi lain dapat memastikan data benar benar tersimpan sebelum menampilkan pesan berhasil.

## 3. Fungsi Validasi Password

<img width="508" height="131" alt="Screenshot 2026-11-03 160441" src="https://github.com/user-attachments/assets/fc3fa697-b326-4834-ad3b-e279f5a89965" />

Fungsi validasi_password(password) memeriksa setiap karakter pada password. Variabel angka bernilai True jika ada karakter digit, dan variabel unik bernilai True jika ada karakter yang bukan huruf maupun angka (simbol). Fungsi mengembalikan True hanya jika kedua syarat terpenuhi.

## 4. Fungsi Tampilkan Tiket

<img width="757" height="403" alt="Screenshot 2026-11-03 162937" src="https://github.com/user-attachments/assets/1cd8a213-c5b0-454a-a3fa-cb36addcef7f" />

Fungsi tampilkan_tiket() dipakai oleh admin maupun user. Program membaca tiket.json, jika kosong, tampil pesan "Belum ada tiket" lalu fungsi berhenti. Jika ada data, program membuat tabel PrettyTable dengan kolom ID, Nama Konser, Tanggal, Lokasi, Harga, dan Kuota Tiket. Harga diformat dengan pemisah titik (contoh Rp150.000), dan kuota bernilai 0 ditampilkan sebagai SOLD OUT.

## 5. Menu Registrasi

<img width="831" height="403" alt="Screenshot 2026-11-03 164033" src="https://github.com/user-attachments/assets/da1eb40a-4482-41a5-96aa-3117325837f7" />

<img width="773" height="346" alt="Screenshot 2026-11-03 164103" src="https://github.com/user-attachments/assets/1e83d610-c2e6-4161-b391-fbecbbcf1134" />

Fungsi registrasi() dijalankan ketika pengguna memilih 2 opsi pada menu utama. Program membaca admin.json dan user.json. Pengguna diminta memasukkan username, program menolak jika kosong atau kurang dari 8 karakter. Selanjutnya pengguna memasukkan password (disembunyikan dengan pwinput) dalam perulangan while True sampai valid tidak boleh kosong, tidak boleh mengandunf spasi, dan harus lolos validasi_password(). Setelah itu program memeriksa apakah username sudah dipakai oleh akun admin maupun user. Jika belum, program membuat akun baru berisi username, password, role = "user", dan saldo = 0, menyimpannya ke user.json, lalu menampilkan "Selamat, Registrasi berhasil!".

## 6. Menu Login

<img width="787" height="389" alt="Screenshot 2026-11-03 164802" src="https://github.com/user-attachments/assets/703d067c-04c8-49b8-9668-ca446fd2052a" />

Fungsi login() dijalankan ketika pengguna memilih opsi 1 pada menu utama. Pengguna memasukkan username dan password (disembunyikan dengan pwinput). Program mencocokkan data terlebih dahulu dengan daftar admin di admin.json, jika cocok, menampilkan "Login user berhasil!" dan menjalankan menu_user(username). Jika tidak ada yang cocok, program menampilkan "Username atau password salah!".

## 7. Fungsi Tambah Tiket

<img width="764" height="406" alt="Screenshot 2026-11-03 165146" src="https://github.com/user-attachments/assets/b098597c-3c30-47f4-8d49-58460512f766" />

<img width="750" height="331" alt="Screenshot 2026-11-03 165205" src="https://github.com/user-attachments/assets/88f2cb0c-4573-404a-9b20-5d11c84d1105" />

Fungsi tambah_tiket() meminta admin memasukkan nama konser, tanggal, lokasi, harga, dan kuota. Nama, tanggal, dan lokasi tidak boleh kosong. Harga dan kuota harus berupa angka (dicek dengan try-except ValueError) dan tidak boleh negatif. ID tiket dibuat otomatis, program mencariangka ID terbesar yang sudah ada lalu menambahkannya 1, dengan format T001, T002, dan seterusnya. Tiket baru ditambahkan ke list, disimpan ke tiket.json, dan program menampilkan "Tiket berhasil ditambahkan!".

## 8. Fungsi Ubah Tiket

<img width="829" height="391" alt="Screenshot 2026-11-03 165948" src="https://github.com/user-attachments/assets/f74c3cdb-3a2c-4953-a428-5d929b488873" />

<img width="797" height="375" alt="Screenshot 2026-11-03 170018" src="https://github.com/user-attachments/assets/e101f53b-8b8d-41ed-88af-00c3411726eb" />

Fungsi ubah_tiket() menampilkan daftar tiket lalu meminta admin memasukkan nomor ID (angka saja, misalnya 1 untuk T001), yang diubah program menjadi format T001. Jika ID ditemukan, data lama ditampilkan di dalam tanda kurung siku dan admin dapat mengisi data baru atau menekan Enter untuk mempertahankan data lama. Harga dan kuota divalidasi harus angka dan tidak negatif. Setelah itu data diperbarui, disimpan ke tiket.json, dan muncul "Data tiket berhasil diubah". Jika ID tidak ada, muncul "ID tiket tidak ditemukan!".

## 9. Fungsi Hapus Tiket

<img width="745" height="246" alt="Screenshot 2026-11-03 170543" src="https://github.com/user-attachments/assets/97732fcd-4a4b-42ac-8cab-e7863e18ab5c" />

<img width="723" height="202" alt="Screenshot 2026-11-03 170607" src="https://github.com/user-attachments/assets/981c5b34-3aa0-446f-b92e-cb37bebb2bac" />

Fungsi hapus_tiket() menampilkan daftar tiket dan meminta nomor ID tiket yang ingin dihapus. Jika ditemukan, program meminta konfirmasi (y/n). Jika admin memilih y, tiket dihapus dari list, file tiket.json diperbarui, dan muncul "Tiket berhasil dihapus!". Jika memilih n, penghapusan dibatalkan. Jika ID tidak ada, muncul "ID tiket tidak ditemukan!".

## 10. Fungsi Cek Saldo dan Ambil Saldo

<img width="622" height="188" alt="Screenshot 2026-11-03 171050" src="https://github.com/user-attachments/assets/40b4ebb4-3b41-4578-85a0-7c6b0b6844f6" />

Fungsi ambil_saldo(username) mencari akun di user.json dan mengembalikan nilai saldonya (0 jika tidak ditemukan). Fungsi ini dipakai untuk menampilkan saldo terbaru pada header Menu User. Fungsi cek_saldo(username) memiliki cara kerja serupa, tetapi langsung mencetak saldo dengan format rupiah.

## 11. Fungsi Top Up

<img width="790" height="362" alt="Screenshot 2026-11-03 172255" src="https://github.com/user-attachments/assets/9749bdec-6b3e-4899-97f7-3a864ddcc552" />

Fungsi top_up(username) meminta user memasukkan nominal. Nominal harus berupa angka dan lebih dari 0, jika tidak, muncul pesan kesalahan. Jika valid, program mencari akun user, menambahkan nominal ke saldo, menyimpan ke user.json, lalu menampilkan "Top up berhasil!" beserta saldo terbaru.

## 12. Fungsi Cetak Invoice

<img width="674" height="173" alt="Screenshot 2026-11-03 172727" src="https://github.com/user-attachments/assets/d22435b5-396a-4926-b666-a06669bf0797" />

Fungsi cetak_invoice(transaksi) menampilkan struk pembelian berisi No Invoice, waktu, pembeli, konser, jumlah dan harga satuan, total, serta sisa saldo. Fungsi ini dipanggil otomatis setelah pembelian berhasil.

## 13. Fungsi Beli Tiket

<img width="797" height="405" alt="Screenshot 2026-11-03 172816" src="https://github.com/user-attachments/assets/30ba6417-b69d-4783-a796-fe2588cfabce" />

<img width="779" height="387" alt="Screenshot 2026-11-03 172856" src="https://github.com/user-attachments/assets/2818ed25-ac03-4638-a239-cc2377bdf827" />

<img width="802" height="363" alt="Screenshot 2026-11-03 173003" src="https://github.com/user-attachments/assets/507cdf34-b2a0-418d-abac-70dae55e218a" />

<img width="731" height="44" alt="Screenshot 2026-11-03 173018" src="https://github.com/user-attachments/assets/e2632e5f-624d-4597-ba6b-2de845804de4" />

Fungsi beli_tiket(username) menampilkan daftar tiket, lalu meminta ID tiket dan jumlah yang ingin dibeli. Program melakukan pengecekan secara berurutan, jumlah harus lebih dari 0 dan tidak melebihi MAKS_BELI (4), ID tiket harus ada, kuota tidak boleh 0 (SOLD OUT), kuota harus cukup untuk jumlah yang dibeli, dan saldo harus cukup untuk total harga. Jika semua terpenuhi, program menampilkan total harga dan meminta konfirmasi (y/n). Setelah dikonfirmasi, kuota tiket dan saldo user dikurangin, lalu transaksi baru dibuat berisi nomor invoice (INV0001, dst.), ID  tiket, status "Berhasil", waktu, username, nama konser, jumlah, harga, total dan sisa saldo. Data tiket, user, dan transaksi disimpan ke masing masing file JSON, lalu program menampilkan "Pembelian berhasil!" dan mencetak invoice.

## 14. Fungsi Riwayat Transaksi

<img width="833" height="402" alt="Screenshot 2026-11-03 174204" src="https://github.com/user-attachments/assets/ff5acbf6-1fb7-41f6-bada-74e99ae4bd4a" />

<img width="748" height="41" alt="Screenshot 2026-11-03 174220" src="https://github.com/user-attachments/assets/c4e4ce4e-bca6-417f-a709-7c98ae8a601d" />

Fungsi riwayat_transaksi(username) membaca transaksi.json lalu menyaring hanya transaksi milik user yang sedang login. Jika belum ada, menampilkan pesan "Belum ada transaksi". Jika ada, data ditampilkan dalam tabel berisi No invoice, waktu, konser, jumlah, total, dan status (Berhasil atau Refund).

## 15. Fungsi Laporan Penjualan

<img width="786" height="377" alt="Screenshot 2026-11-03 174354" src="https://github.com/user-attachments/assets/d2c8cdab-43a4-49e6-9d20-82eac0aee6fc" />

<img width="823" height="359" alt="Screenshot 2026-11-03 181354" src="https://github.com/user-attachments/assets/ade9081e-a555-4801-a735-f2f0ab4c3637" />

Fungsi laporan_penjualan() membaca transaksi.json. Transaksi berstatus Refund tidak dihitung sebagai penjualan, tetapi nilai sanksinya dijumlahkan ke total_sanksi. Untuk transaksi lainnya, program mengelompokkan data per nama konser dalam dictionary per_konser (jumlah tiket terjual dan pendapatan) sambil menghitung total transaksi, total tiket, dan total pendapatan. Hasilnya ditampilkan dalam tabel (Nama Konser, Tiket Terjual, Pendapatan) diikuti ringkasan total transaksi, total tiket, sanksi refund, dan total pendapatan (pendapatan penjualan ditambah sanksi refund).

## 16. Fungsi Daftar User

<img width="797" height="289" alt="Screenshot 2026-11-03 185248" src="https://github.com/user-attachments/assets/bb916375-e508-4441-93f7-c2396b7f79e8" />

Fungsi daftar_user() membaca user.json. Jika kosong, tampil "Belum ada user terdaftar". Jika ada, program menampilkan tabel berisi nomor urut, username, dan saldo setiap user.

## 17. Fungsi Hitung Sanksi Refund

<img width="739" height="161" alt="Screenshot 2026-11-03 185307" src="https://github.com/user-attachments/assets/e4850ad4-bc6d-4f25-ab7b-dc1f22b5b7f2" />

Fungsi hitung_sanksi_persen(trx) mengubah waktu pembelian pada transaksi menjadi waktu epoch, lalu menghitung selisih jam antara sekarang dan waktu pembelian. Jika selisih tidak lebih dari BATAS_JAM_REFUND (24 jam), sanksi yang dikenakan adalah SANKSI_CEPAT (5%), jika lebih, SANKSI_LAMBAT (10%). Jika format waktu tidak terbaca, fungsi memakai sanksi 10%.

## 18. Fungsi Refund Tiket

<img width="783" height="388" alt="Screenshot 2026-11-03 185326" src="https://github.com/user-attachments/assets/a3d7aa7b-d9ef-4136-b989-9a3b89f35a76" />

<img width="838" height="374" alt="Screenshot 2026-11-03 185351" src="https://github.com/user-attachments/assets/6b3b6630-d7e9-4fa3-9d10-fff7d38894b3" />

<img width="815" height="303" alt="Screenshot 2026-11-03 185409" src="https://github.com/user-attachments/assets/0de74b97-91e6-4cd1-ab6d-cdde96b91823" />

Fungsi refund_tiket(username) menampilkan tabel transaksi milik user yang berstatus "Berhasil". Jika tidak ada, tampil "Tidak ada transaksi yang bisa direfund". User kemudian memasukkan No Invoice. Program menghitung sanksi (total x persen ÷ 100) dan dana yang dikembalikan (total - sanksi), menampilkan ketiganya, dan meminta konfirmasi (y/n). Jika dikonfirmasi, kuota tiket konser terkait ditambah kembali, saldo user ditambah sebesar dana kembali, dan transaksi diubah menjadi status "Refund" lengkap dengan catatan sanksi_persen, sanksi, dan dikembalikan. Ketiga file JSON disimpan, lalu program menampilkan pesan refund berhasil beserta presentase sanksinya.

## 19. Menu Admin

<img width="697" height="188" alt="Screenshot 2026-11-03 185633" src="https://github.com/user-attachments/assets/980aaac1-32c2-41a6-a5a9-d12fa1e5654a" />

<img width="754" height="303" alt="Screenshot 2026-11-03 185651" src="https://github.com/user-attachments/assets/d659f5b6-a968-4079-97f6-0671766c7a5f" />

Fungsi menu_user(username) berjalan ketika login sebagai user. Di bagian atas menu, program menampilkan nama pengguna dan saldo terkini (diambil dengan ambil_saldo() ). Pilihan yang tersedia adalah 1. lihat Data Tiket, 2. Tambah Tiket, 3. Ubah Data Tiket, 4. Hapus Tiket, 5. Laporan Penjualan, 6. Daftar User, dan 7. Logout. Perulangan while True membuat menu terus tampil sampai admin memilih Logout. Setelah setiap fitur selesai, program meminta admin menekan Enter agar hasil tidak langsung tertimpa menu. Pilihan di luar 1-7 menampilkan "Pilihan tidak valid!".

## 20. Menu User

<img width="772" height="218" alt="Screenshot 2026-11-03 185706" src="https://github.com/user-attachments/assets/ae07caa2-1fb1-4704-aba7-6c6725f24a26" />

<img width="767" height="278" alt="Screenshot 2026-11-03 185724" src="https://github.com/user-attachments/assets/ba8b4b44-8bf6-412d-b46d-14c40536e497" />

Fungsi menu_user(username) berjalan ketika login sebagai user. Di bagian atas menu, program menampilkan nama pengguna dan saldo terkini (diambil dengan ambil_saldo() ). Pilihan yang tersedia 1. Lihat Data Tiket, 2. Top up, 3. Beli Tiket, 4. Riwayat Transaksi, 5. Refund Tiket, dan 6. Logout. Setiap pilihan memanggil fungsi yang sesuai dan menu terus tampil sampai user memilih Logout. Pilihan di luar 1-6 menampilkan "Pilihan tidak valid!".

## 21. Halaman Menu Utama

<img width="816" height="373" alt="Screenshot 2026-11-03 185743" src="https://github.com/user-attachments/assets/19058f94-5826-4df0-ba77-1538c63b3ff5" />

Fungsi menu_utama() menampilkan tiga pilihan: Login, Registrasi dan Keluar. Pilihan 1 memanggil login(), pilihan 2 memanggil registrasi(), dan pilihan 3 menampilkan pesan terimakasih lalu menghentikan perulangan. Input selain 1-3 menampilkan "Pilihan tidak valid!". Menu dijalankan dalam perulangan while True sehingga terus tampil sampai pengguna memilih Keluar, dan layar dibersihkan setiap kali menu tampil. Di bagian paling bawah program, pemanggilan menu_utama() dibungkus try-except KeyboardInterrupt agar jika pemgguna menekan Ctrl+C, program tidak berhenti paksa tetapi kembali ke menu utama.
