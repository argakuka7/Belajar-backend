# Manifest coverage Bab 3: Serialisasi & Deserialisasi

Sumber: `public/3.Serialization-and-Deserialization-or-backend-engineers/html_notes/notes.html` (11 bagian). Analogi induk: Kuka ingin mengirim mainan berbentuk lewat celah surat yang pipih. Mainan dibongkar jadi potongan datar berurutan, lalu dipasang kembali utuh di seberang.

Nama tampilan karakter: Kuka. Kontrak visual tetap `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Hambatan bahasa | CORE | Dua pihak beda bahasa tidak bisa menyampaikan mainan langsung. |
| 2 | Serialize & deserialize | CORE | Bongkar mainan jadi potongan datar sebelum masuk celah. Pasang kembali jadi utuh setelah keluar. |
| 3 | Menyepakati standar bersama | CORE ringan | Keduanya memegang buku pegangan yang sama persis. |
| 4 | Format teks vs biner | RINGAN | Potongan berlabel panjang yang mudah dibaca vs potongan kecil padat yang hemat tempat. |
| 5 | JSON: standar industri | RINGAN | Buku pegangan yang paling banyak dipinjam. |
| 6 | Aturan sintaks JSON | NAMED | |
| 7 | Model mental OSI | NAMED | |
| 8 | Alur kerja end-to-end | RINGAN | Perjalanan utuh mainan dari rak ke rak. |
| 9 | Serialisasi di Go | DEFERRED | |
| 10 | Serialisasi di Python | DEFERRED | |
| 11 | Glosarium | DEFERRED | |

Hasil: 3 CORE, 3 RINGAN, 2 NAMED, 3 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Kenapa dua program tidak bisa saling berkirim objek langsung?
2. Apa yang terjadi saat serialize, dan apa kebalikannya?
3. Kenapa dua pihak harus memegang standar yang sama?

Ilustrasi (di `public/assets/illustrations/03-serialisasi/`):
- `01-kirim-bentuk.png` utama: Kuka menekan mainan kursi kecil menjadi potongan datar berjajar yang masuk celah surat, panah oranye menelusuri potongan.
- `02-standar.png` pendukung: dua buku pegangan bersampul identik di satu meja, satu lembar datar di atasnya.
- `03-biner.png` pendukung: dua tumpukan potongan, satu berlabel pita panjang, satu padat kecil, Kuka menimbang keduanya.
