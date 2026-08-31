# Manifest coverage Bab 18: Scaling & Performance (Bagian 1)

Sumber: `public/18. Backend Scaling and Performance Engineering-part-1/html_notes/notes.html` (19 bagian). Analogi induk: restoran yang mulai ramai. Pertanyaannya bukan "buat cepat", tapi "cepat di ukuran apa". Ukur dulu: berapa lama tamu menunggu rata-rata, dan terburuknya. Baru cari meja atau juru masak mana yang jadi kemacetan.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|
| Apa maksudnya "cepat"? | CORE | "Cepat" harus ada angkanya. Tiga menit itu cepat atau lambat? Tergantung janji di papan. |
| Selami latensi | CORE | Latensi = waktu tunggu tamu dari pesan sampai piring datang. |
| Persentil P50, P90, P99 | CORE | Tamu biasa dilayani cepat. Yang penting tamu paling sial: jangan sampai satu jam. |
| Throughput | CORE ringan | Berapa piring keluar per jam dari dapur. |
| Utilisasi & antrean | RINGAN | Dapur penuh = antrean panjang. Lihat antreannya, bukan hanya kecepatan masaknya. |
| Menemukan bottleneck | CORE | Meja mana yang selalu menumpuk? Di situlah masalahnya, bukan di meja yang kosong. |
| Profiling & flame graph | RINGAN | Kamera waktu yang menunjukkan juru masak mana paling lama di satu resep. |
| Distributed tracing | RINGAN | Nomor tiket dari bab 15, kini untuk mengukur tiap meja. |
| Masalah query N+1 | CORE | Pelayan berjalan ke gudang untuk satu bahan, kembali, jalan lagi untuk satu bahan lagi. Satu trip bawa daftarnya sekalian. |
| Index & query plan | RINGAN | Daftar isi buku besar dari bab 8. |
| Connection pooling | RINGAN | Pintu gudang dibuka sekali dan dipakai bergantian, bukan dibuka-tutup tiap ambil bahan. |
| Fundamental caching | RINGAN | Rak dekat dapur dari bab 9. |
| Invalidasi cache | RINGAN | Resep berubah? Fotokopi di rak harus diganti, kalau tidak tamu menerima menu basi. |
| Pola caching | NAMED | |
| Cache hit rate | RINGAN | Berapa persen ambilan yang cukup dari rak dekat, tanpa jalan ke gudang. |
| Vertical scaling | CORE | Beli kompor lebih besar untuk dapur yang sama. |
| Horizontal scaling | CORE | Buka meja dan juru masak tambahan, satu resep untuk semua. |
| Load balancing | CORE | Resepsionis yang membagi tamu ke meja yang kosong, seperti bab 2. |
| Ringkasan & prinsip kunci | RINGAN | |

Pertanyaan pemahaman dari CORE:
1. Kenapa "cepat" harus punya angka dan persentil, bukan kata-kata?
2. Apa itu query N+1 dan kenapa melelahkan gudang?
3. Apa beda membeli kompor lebih besar dan membuka cabang tambahan?

Ilustrasi (di `public/assets/illustrations/18-scaling1/`):
- `01-papan-angka.png` utama: Kuka berdiri di depan papan pantau berisi tiga meter dan grafik, menunjuk satu meter yang penuh.
- `02-n-plus-1.png` pendukung: pelayan berlari bolak-balik ke gudang tiga kali membawa satu bahan kecil per trip, alih-alih satu keranjang.
- `03-load-balancer.png` pendukung: resepsionis mesin membagi tiga tamu ke tiga meja kosong yang sama jaraknya.
