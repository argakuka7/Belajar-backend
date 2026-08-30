# Manifest coverage Bab 6: Controller, Service, Repository, Middleware, Request Context

Sumber: `public/6.controllers-services-repositories-middlewares-and-request-context/html_notes/notes.html` (15 bagian). Analogi induk: restoran. Pelayan menerima pesanan tamu dan menulis tiket (controller). Juru masak memutuskan cara memasak (service). Petugas gudang satu-satunya yang boleh ambil dan letakkan bahan (repository). Sebelum pesanan sampai ke pelayan, ia melewati barisan pintu restoran (middleware). Nota kecil menempel pada pesanan dan ikut ke mana-mana (request context).

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Klien & server | RINGAN | Tamu dan restoran. Recap bab 1, satu kalimat. |
| 2 | Siklus hidup request di dalam server | CORE ringan | Pesanan masuk: pintu, pelayan, dapur, gudang, lalu kembali ke meja. |
| 3 | Titik masuk & routing | RINGAN | Resepsionis mengarahkan tamu ke pelayan yang tepat, seperti bab 2. |
| 4 | Kenapa tiga lapisan? | CORE | Kalau satu orang merangkap pelayan, juru masak, dan petugas gudang, dia kewalahan. Tugas dipisah supaya resep bisa berganti tanpa mengganti meja. |
| 5 | Lapisan controller / handler | CORE | Pelayan: dengar pesanan, tulis tiket rapi, antar ke dapur, bawa hasil ke tamu. Ia tidak memasak. |
| 6 | Lapisan service | CORE | Juru masak: semua aturan resep ada di sini. Pelayan dan gudang tidak boleh memutuskan rasa. |
| 7 | Lapisan repository | CORE | Petugas gudang: satu-satunya yang boleh masuk gudang. Dapur tidak peduli bahan disimpan di mana. |
| 8 | Siklus lengkap end to end | RINGAN | Satu pesanan berjalan dari pintu sampai kembali ke meja. |
| 9 | Apa itu middleware | CORE | Barisan pintu restoran yang dilewati setiap pesanan sebelum sampai ke pelayan. |
| 10 | Fungsi next() | CORE ringan | Kalimat "selesai, teruskan ke petugas berikutnya". Tanpa itu, barisan macet. |
| 11 | Kenapa urutan penting | RINGAN | Cek reservasi dulu, baru serah jaket. Salah urutan, tamu dipulangkan saat mejanya sudah diambil orang lain. |
| 12 | Middleware yang umum | NAMED | Logging, autentikasi, parsing, compression, error handler. |
| 13 | Apa itu request context | CORE | Nota kecil yang menempel pada pesanan dan ikut ke semua meja: siapa tamunya, nomor meja, batas waktu. |
| 14 | Meneruskan data autentikasi | RINGAN | Identitas tamu yang dicek di pintu terbaca dapur tanpa perlu bertanya ulang. |
| 15 | Tracing & pembatalan | RINGAN | Nomor pesanan untuk melacak keluhan, dan tamu bisa membatalkan pesanan sehingga dapur berhenti memasak. |

Hasil: 6 CORE, 2 CORE ringan, 5 RINGAN, 1 NAMED. Recaps dan kode Go/Python penuh terserah versi teknis.

Pertanyaan pemahaman dari CORE:
1. Apa tugas controller, dan apa yang tidak boleh ia kerjakan?
2. Kenapa gudang (database) hanya boleh diakses lewat repository?
3. Apa fungsi next() dan apa yang terjadi jika satu middleware lupa memanggilnya?

Ilustrasi (di `public/assets/illustrations/06-lapisan/`):
- `01-restoran.png` utama: Kuka di meja restoran menyerahkan kertas pesanan kepada pelayan mesin, jendela dapur dan rak bahan di kejauhan.
- `02-tiga-lapis.png` pendukung: tiket berjalan melewati tiga meja bertanda bentuk berbeda: pelayan, panci juru masak, rak gudang.
- `03-middleware.png` pendukung: Kuka melewati barisan dua gerbang berbentuk berbeda sebelum sampai ke meja pelayan.
- `04-nota.png` pendukung: tiket pesanan dengan nota kecil terklip, Kuka memasangkan klip itu.
