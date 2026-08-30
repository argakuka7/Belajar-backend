# Manifest coverage Bab 10: Task Queues & Background Jobs

Sumber: `public/10.Task queues and background job/html_notes/notes.html` (19 bagian). Analogi induk: restoran yang sibuk. Pesanan kue yang butuh tiga puluh menit tidak dimasak di depan tamu. Kasir menempelkan tiket kue ke papan dapur, juru masak kue mengambilnya satu per satu, dan staf mengantar kue ke meja begitu jadi. Tamu cukup duduk dengan nomor dan minuman.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Apa itu tugas latar | CORE | Pesanan kue dikerjakan di dapur belakang, tamu tidak berdiri menunggu di kasir. |
| 2 | Kenapa kita butuh | CORE | Kalau kasir memasak kue sendiri, kasir macet, semua tamu keluar. |
| 3 | Sinkron vs asinkron | CORE | Menunggu di kasir (sinkron) vs duduk dengan nomor (asinkron). |
| 4 | Cara kerja antrean | CORE | Papan tiket di dapur. Tiket diambil satu per satu, selesai, ambil berikutnya. |
| 5 | Producer & consumer | CORE ringan | Kasir menempel tiket, juru masak kue mengambilnya. Dua peran berbeda. |
| 6 | Broker & teknologi | NAMED | |
| 7 | SQS standard vs FIFO | NAMED | |
| 8 | Retry & exponential backoff | CORE ringan | Kue gagal jadi, coba lagi nanti. Jeda makin panjang, bukan diulang terus-menerus. |
| 9 | Visibility timeout & acknowledgment | RINGAN | Tiket yang diambil terlalu lama boleh diambil staf lain. Tiket dibuang setelah kue selesai. |
| 10 | Jenis-jenis background task | RINGAN | Kirim email, buat laporan, proses foto. Semua masuk papan yang sama. |
| 11 | Kasus pemakaian dunia nyata | RINGAN | |
| 12 | Contoh kode: Go & Python | DEFERRED | |
| 13 | Pertimbangan desain di skala | NAMED | |
| 14 | Pola idempotensi | RINGAN | Kue yang sama dipesan dua kali tetap satu kue, seperti bab 7. |
| 15 | Rate limiting di worker | NAMED | |
| 16 | Monitoring Prometheus & Grafana | NAMED | |
| 17 | Praktik terbaik | NAMED | |
| 18 | Perbandingan framework | NAMED | |
| 19 | Temporal & orkestrasi workflow | NAMED | |

Hasil: 4 CORE, 2 CORE ringan, 4 RINGAN, 8 NAMED, 1 DEFERRED. Bab paling lebar; versi sederhana sengaja hanya membawa inti papan tiket.

Pertanyaan pemahaman dari CORE:
1. Kenapa kue dikirim ke dapur belakang, tidak dimasak di depan tamu?
2. Siapa yang menempel dan siapa yang mengambil tiket di papan dapur?
3. Apa yang terjadi kalau juru masak gagal membuat kue?

Ilustrasi (di `public/assets/illustrations/10-antrean/`):
- `01-papan-tiket.png` utama: papan tiket besar di dapur penuh kertas tergantung, juru masak mesin mengambil satu tiket, Kuka menempelkan satu tiket lagi.
- `02-nomor.png` pendukung: Kuka duduk santai di meja memegang nomor kecil, secangkir cangkir di dekatnya, dapur di kejauhan.
- `03-coba-lagi.png` pendukung: satu tiket terjatuh di lantai, Kuka membungkuk memungutnya kembali ke papan.
