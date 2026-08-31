# Manifest coverage Bab 14: Production-grade Configuration Management

Sumber: `public/14.Production-grade Configuration Management/html_notes/notes.html` (10 bagian). Analogi induk: buku panduan meja staf yang tergantung di dinding dapur. Resepnya sama untuk semua shift, tapi ada catatan kecil yang berbeda per lokasi: alamat pemasok cabang, jam buka cabang, dan kunci lemari kas. Catatan itu bukan resep; resep boleh sama, catatan lokasi harus tepat per gedung.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Apa itu manajemen konfigurasi | CORE | Pisahkan resep (kode) dari catatan lokasi (config). Resep sama, catatan berbeda per gedung. |
| 2 | Contoh platform e-commerce | RINGAN | Satu resep roti, tiga cabang, tiga jam buka berbeda. |
| 3 | Tantangan sistem terdistribusi | NAMED | |
| 4 | Kekacauan konfigurasi | CORE ringan | Catatan tempel berserakan di mana-mana: satu lepas, semua kacau. |
| 5 | Jenis-jenis konfigurasi | RINGAN | Jam buka boleh dilihat siapa saja; kunci lemari kas tidak boleh. |
| 6 | Sumber config (penyimpanan) | RINGAN | Buku panduan terpusat, bukan tempelan acak. |
| 7 | Kenapa config berbeda per lingkungan | RINGAN | Dapur latihan, dapur uji coba, dan gedung asli punya catatan masing-masing. |
| 8 | Keamanan konfigurasi | CORE | Kunci lemari kas tidak pernah ditulis di papan umum. Kredensial bukan tempelan. |
| 9 | Contoh kode | DEFERRED | |
| 10 | Bacaan lanjutan & dokumentasi | DEFERRED | |

Hasil: 2 CORE, 1 CORE ringan, 4 RINGAN, 1 NAMED, 2 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Kenapa resep (kode) dan catatan lokasi (config) harus dipisah?
2. Apa beda catatan yang boleh terbuka dan kunci lemari kas (rahasia)?
3. Apa akibatnya kalau kunci lemari kas ditempel di papan umum?

Ilustrasi (di `public/assets/illustrations/14-config/`):
- `01-panduan.png` utama: Kuka membaca buku panduan besar terbuka yang tergantung di dinding dapur, tempelan kecil tersusun rapi di sampingnya.
- `02-tempelan.png` pendukung: dinding penuh tempelan acak miring-miring, Kuka bingung memilih satu.
- `03-kunci.png` pendukung: Kuka menyimpan satu kunci ke dalam kotak kecil tertutup, papan tempelan di belakangnya kosong dari kunci.
