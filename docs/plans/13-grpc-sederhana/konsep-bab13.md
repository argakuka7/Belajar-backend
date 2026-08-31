# Manifest coverage Bab 13: gRPC & Komunikasi Antar Layanan

Sumber: `public/13.gRPC-and-Inter-Service-Communication-for-Microservices/html_notes/notes.html` (21 bagian). Analogi induk: cabang restoran yang harus saling kirim pesanan. Mengirim surat (REST) rapi tapi lambat bolak-balik; mengangkat telepon langsung ke dapur cabang lain (gRPC) jauh lebih cepat, asal kedua pihak memegang buku kode yang sama persis.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Apa sebenarnya gRPC itu | CORE | Telepon langsung antar dapur cabang untuk pesanan antar cabang. |
| 2 | Kenapa gRPC ada | CORE ringan | Surat bolak-balik terlalu lambat saat cabang harus bertanya-jawab ratusan kali. |
| 3 | Model mental RPC | CORE ringan | Terasa seperti memanggil resep di buku sendiri, padahal yang memasak dapur sebelah. |
| 4 | Protocol Buffers: kontraknya | CORE | Buku kode pesanan yang ditulis rapat dan disepakati kedua cabang. Tidak ada pesanan di luar buku. |
| 5 | Cara protobuf meng-encode | RINGAN | Tulisan dalam buku kode dipadatkan jadi sandi pendek biar hemat bicara. |
| 6 | HTTP/2: transport di bawahnya | RINGAN | Satu jalur telepin bisa membawa banyak pembicaraan sekaligus. |
| 7 | RPC unary | CORE ringan | Tanya satu, jawab satu. Seperti bertanya stok gula. |
| 8 | Server streaming | RINGAN | Dapur menyebutkan daftar panjang sambil dihangatkan, tamu mendengar bertahap. |
| 9 | Client streaming | RINGAN | Kuka menyebutkan daftar belanja panjang tanpa diputus, dapur mendengar sampai selesai. |
| 10 | Streaming dua arah | NAMED | |
| 11 | Alur kerja .proto -> kode | NAMED | |
| 12 | Channel, stub & satu panggilan | RINGAN | Nosambungan dan cara memanggilnya sudah disiapkan di setiap meja. |
| 13 | Metadata, deadline & pembatalan | RINGAN | Nota membawa batas waktu. Kalau habis, panggilan diputus, jangan menunggu selamanya. |
| 14 | Status code & penanganan error | RINGAN | Dapur sebelah juga punya cara standar bilang gagal. |
| 15 | Interceptor: middleware-nya gRPC | RINGAN | Barisan pintu pemeriksa seperti bab 6, kini di jalur telepon. |
| 16 | Autentikasi & keamanan | RINGAN | Hanya cabang resmi yang boleh menelpon. |
| 17 | Ketahanan & load balancing | NAMED | |
| 18 | gRPC vs REST: memilih | RINGAN | Surat untuk tamu, telepon untuk antar cabang. |
| 19 | gRPC-Web & interop browser | NAMED | |
| 20 | Observabilitas & debugging | NAMED | |
| 21 | Crib-sheet debug | DEFERRED | |

Hasil: 2 CORE, 3 CORE ringan, 10 RINGAN, 5 NAMED, 1 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Apa beda mengangkat telepon (gRPC) dan mengirim surat (REST)?
2. Apa isi buku kode (protobuf) dan kenapa kedua cabang harus memegang yang sama?
3. Apa gunanya batas waktu (deadline) yang dibawa nota?

Ilustrasi (di `public/assets/illustrations/13-grpc/`):
- `01-telepon.png` utama: dua meja dapur di kiri dan kanan, Kuka di kiri berbicara lewat telepon meja; garis telepon lurus menghubungkan kedua meja; buku kode tebal terbuka di meja Kuka.
- `02-protokol.png` pendukung: dua buku kode bersampul identik terbuka di dua meja berseberangan.
- `03-deadline.png` pendukung: Kuka menelpon sambil menunjuk jam dinding besar; pasir di jam pasir menipis.
