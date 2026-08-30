# Manifest coverage Bab 5: Validasi & Transformasi

Sumber: `public/5. Validations and transformations for backend engineers/html_notes/notes.html` (15 bagian). Analogi induk: masih di gedung. Sebelum barang dari laporan masuk rak, petugas pemeriksa memeriksa paketnya: bentuknya benar, labelnya sesuai format, isinya masuk akal, lalu dirapikan sebelum diserahkan ke rak.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Apa itu & kenapa ada | CORE | Petugas periksa paket di pintu sebelum barang menyentuh rak. |
| 2 | Di mana ia tinggal: tiga lapisan | NAMED | |
| 3 | Siklus hidup request | NAMED | |
| 4 | Titik eksekusi | NAMED | |
| 5 | Kenapa kritis: kisah 500 vs 400 | CORE | Paket rusak karena pengirim: sapa ramah "kembalikan ke pengirim", 400. Rak jebol karena kesalahan gedung: 500. Salam yang tepat menyelamatkan hari. |
| 6 | Di dalam pipeline: langkah demi langkah | CORE ringan | Barisan meja pemeriksa, tiap meja satu tugas, ada urutannya. |
| 7 | Validasi tipe | CORE | Cek bentuk barang: yang bulat bukan kotak, yang angka bukan huruf. |
| 8 | Validasi sintaksis | CORE ringan | Cek label: alamat ditulis dalam format yang disepakati. |
| 9 | Validasi semantik | CORE ringan | Cek isi masuk akal: jumlah tidak minus, tanggal pulang tidak sebelum tanggal datang. |
| 10 | Validasi kompleks / dependen | RINGAN | Aturan antar barang: kupon hanya berlaku jika ada belanjaan. |
| 11 | Transformasi sebagai type casting | RINGAN | Ganti kemasan, isi tetap sama: kotak jadi kaleng. |
| 12 | Transformasi sebagai normalisasi | RINGAN | Rapikan sebelum simpan: huruf kecil semua, spasi rapi, format seragam. |
| 13 | Satu pipeline gabungan | RINGAN | Pemeriksa dan perapian jadi satu barisan. |
| 14 | Validasi frontend vs backend | RINGAN | Penjaga toko menolong tamu, penjaga gudang yang wajib paling ketat. |
| 15 | Controller beranotasi lengkap | DEFERRED | |

Hasil: 3 CORE, 3 CORE ringan, 5 RINGAN, 3 NAMED, 1 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Kenapa server harus memeriksa request lagi padahal halaman frontend sudah memeriksa?
2. Apa beda 400 dan 500, dan kenapa beda itu penting?
3. Apa beda cek bentuk (tipe), cek format (sintaksis), dan cek masuk akal (semantik)?

Ilustrasi (di `public/assets/illustrations/05-validasi/`):
- `01-periksa.png` utama: Kuka menyerahkan satu paket ke meja mesin pemeriksa yang mengamatinya dengan lup besar.
- `02-400-500.png` pendukung: paket dengan tanda seru didorong kembali lewat jalur balik ke arah Kuka, mesin di sampingnya tetap utuh.
- `03-tipe.png` pendukung: tiga paket berbentuk bulat, kotak, dan tabung di depan tiga celah berbentuk sama, Kuka mencocokkan satu.
- `04-rapi.png` pendukung: barang berantakan di meja disusun Kuka menjadi barisan lurus seragam.
