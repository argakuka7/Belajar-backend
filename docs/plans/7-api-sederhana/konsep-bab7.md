# Manifest coverage Bab 7: Desain REST API

Sumber: `public/7.API-DESIGN-RestAPI/html_notes/notes.html` (15 bagian). Analogi induk: masih di restoran bab 6. REST adalah menu restoran yang tertulis konsisten. Kontrak antara tamu dan dapur: nama hidangan selalu sama, kata kerjanya jelas, kalau gagal dapur menyebut alasannya, dan menu punya nomor edisi.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Apa sebenarnya REST itu | CORE | Menu yang tertulis konsisten. Tamu baru bisa memesan tanpa dituntun, karena semua hidangan punya pola nama yang sama. |
| 2 | Enam batasan | NAMED | |
| 3 | Kenapa REST membingungkan sekarang | NAMED | |
| 4 | Anatomi sebuah route | CORE | Nama benda di menu: /menu/kopi, bukan /buat-kopi. Kata kerjanya lewat method. |
| 5 | Method & idempotensi | CORE ringan | Tekan tombol pesan dua kali, tidak jadi dua piring. Ulang aman itu penting saat jaringan gagal. |
| 6 | Aksi kustom: melampaui CRUD | RINGAN | Permintaan spesial di luar menu boleh, tapi seminimal mungkin. |
| 7 | API daftar: page/sort/filter | CORE ringan | Menu panjang dibaca per halaman, bisa minta urutan dan saringan. |
| 8 | Status code: yang benar | CORE | Dapur punya cara standar menyampaikan: jadi, habis, pesananmu salah, dapur kacau. |
| 9 | Contoh kerja: platform PM | DEFERRED | |
| 10 | Aturan emas | NAMED | |
| 11 | Versioning | RINGAN | Menu edisi baru terbit, pesanan edisi lama tetap dilayani. |
| 12 | Respons error: separuh lainnya dari kontrak | CORE ringan | Kalau gagal, dapur menyerahkan slip berisi alasan yang bisa dibaca, bukan piring kosong diam-diam. |
| 13 | Batasan vs konvensi | NAMED | |
| 14 | Delapan prinsip | NAMED | |
| 15 | Kode kerja: API task di Go | DEFERRED | |

Hasil: 3 CORE, 3 CORE ringan, 2 RINGAN, 5 NAMED, 2 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Apa itu REST dalam satu kalimat?
2. Kenapa pesanan yang sama dikirim dua kali tidak boleh menghasilkan dua piring?
3. Apa gunanya status code bagi pengirim request?

Ilustrasi (di `public/assets/illustrations/07-api/`):
- `01-menu.png` utama: Kuka membaca papan menu besar dengan deretan gambar hidangan tersusun rapi berkelompok, pelayan mesin menunggu di samping.
- `02-idempoten.png` pendukung: Kuka menekan tombol panggil dua kali dengan dua tangan, hanya satu piring di meja.
- `03-menu-versi.png` pendukung: dua papan menu di dinding, satu diberi bendera kecil; Kuka memegang papan kecil lama, pelayan mengangguk.
