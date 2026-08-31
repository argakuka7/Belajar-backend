# Manifest coverage Bab 12: Error Handling & Sistem Tahan Gagal

Sumber: `public/12. Error Handling and Building Fault Tolerant Systems/html_notes/notes.html` (15 bagian). Analogi induk: dapur yang tetap tenang saat piring pecah. Dapur hebat bukan dapur yang tak pernah pecah piring, tapi yang tahu harus berbuat apa ketika pecah: beri tahu siapa, bersihkan, lanjut melayani.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Pola pikir tahan gagal | CORE | Piring pasti pecah sesekali. Yang menentukan adalah reaksi dapur, bukan kebetulan. |
| 2 | Ringkasan kerentanan | NAMED | |
| 3 | Logic error: pembunuh senyap | CORE ringan | Rasa asin yang tidak dikeluhkan tamu: tidak ada suara, tapi pelanggan pergi. |
| 4 | Error database | RINGAN | Gudang terkunci: pesanan tidak bisa diselesaikan sampai gudang dibuka. |
| 5 | Error layanan eksternal | RINGAN | Pemasok tidak angkat telepon: jangan buat tamu ikut menunggu. |
| 6 | Error validasi input | RINGAN | Pesanan aneh dari tamu: kembalikan dengan sopan, itu 400. |
| 7 | Error konfigurasi | RINGAN | Resep di dinding tertulis salah: semua hidangan ikut salah. |
| 8 | Health check | CORE ringan | Manajer mencicipi setiap panci tiap jam, sebelum tamu mengeluh. |
| 9 | Monitoring & observabilitas | RINGAN | Buku harian dapur + kamera. Baca bukunya, jangan tunggu keluhan. |
| 10 | Strategi pemulihan | CORE | Juru masak kedua mengambil alih panci yang bermasalah. Coba lagi dengan cara lain. |
| 11 | Global error handler: jaring pengaman terakhir | CORE | Jaring di bawah rak. Piring apa pun yang jatuh tertangkap di sini, tidak sampai lantai. |
| 12 | Go: global error handler | DEFERRED | |
| 13 | Python: global error handler | DEFERRED | |
| 14 | Keamanan: yang diekspos, yang disembunyikan | RINGAN | Kepada tamu cukup "pesanan gagal"; detail kerusakan hanya untuk dapur. |
| 15 | Referensi & bacaan lanjutan | DEFERRED | |

Hasil: 3 CORE, 2 CORE ringan, 6 RINGAN, 1 NAMED, 3 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Kenapa error harus segera ketahuan, bukan disembunyikan?
2. Apa beda pesan untuk tamu dan pesan untuk dapur saat pesanan gagal?
3. Apa fungsi jaring pengaman (global error handler)?

Ilustrasi (di `public/assets/illustrations/12-error/`):
- `01-jaring.png` utama: Kuka berdiri di samping rak tinggi dengan jaring pengaman besar direntang di bawahnya, satu piring jatuh tertangkap jaring.
- `02-health.png` pendukung: mesin manajer bertopi mencicipi dari panci besar sambil memegang papan kecil bertanda centang.
- `03-sapu.png` pendukung: Kuka menyapu pecahan piring dengan sikap tenang, dapur dan panci lain tetap berasap di belakang.
