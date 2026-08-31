# Manifest coverage Bab 23: Message Brokers & Event Streaming dengan Kafka

Sumber: `public/23.Message-Brokers-and-Event-Streaming-with-Kafka/html_notes/notes.html` (21 bagian). Analogi induk: papan tiket raksasa yang buku-catatannya tidak pernah dihapus. Tiket yang sudah diambil tetap menempel berurutan; juru masak mana pun boleh membaca ulang dari tiket lama. Berbeda dengan papan bab 10 yang tiketnya hilang setelah diambil.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|
| Apa sebenarnya Kafka itu | CORE | Papan tiket raksasa antar banyak dapur, catatannya berurutan dan tidak dihapus. |
| Antrean vs log: kenapa Kafka berbeda | CORE | Papan bab 10: tiket diambil hilang. Papan ini: tiket tinggal menempel, siapa pun boleh membaca ulang. |
| Commit log | CORE ringan | Catatan bertuliskan nomor urut: nomor 1, 2, 3, tanpa bolak-balik. |
| Topik & partisi | CORE ringan | Papan dibagi per jenis pesanan, dan tiap jenis dipecah ke beberapa jalur supaya muat. |
| Broker, replikasi & daya tahan | RINGAN | Papan punya kembaran di dapur lain; satu papan rusak, catatan tetap ada. |
| Producer | RINGAN | Yang menempel tiket baru selalu di ujung bawah. |
| Consumer & consumer group | RINGAN | Banyak juru masak membagi pembacaan; tiap tiket dibaca satu juru masak per kelompok. |
| Offset & manajemen offset | RINGAN | Pembatas buku tiap juru masak: sampai nomor berapa ia sudah baca. |
| Semantik pengiriman | RINGAN | Bisa jadi tiket terbaca dua kali saat sibuk; juru masak harus kebal itu. |
| Jaminan urutan | RINGAN | Urutan dijamin dalam satu jalur, tidak dijamin antar jalur. |
| Retensi & kompaksi log | RINGAN | Tiket lama disimpan berminggu-minggu; tiket terbaru per kata kunci menggantikan yang lama. |
| Skema & schema registry | RINGAN | Buku kode tiket supaya semua dapur membaca sama, seperti bab 13. |
| Pola event-driven | RINGAN | Meja lain bereaksi setiap tiket baru menempel, tanpa diminta. |
| Event sourcing & CQRS | NAMED | |
| Outbox & change data capture | NAMED | |
| Stream processing | RINGAN | Membaca aliran tiket sambil berjalan: hitung, saring, rangkum. |
| Kafka vs antrean tradisional | RINGAN | Kapan papan permanen lebih baik daripada papan tiket hilang. |
| Jebakan consumer | RINGAN | Pembatas buku lupa digeser: tumpukan tiket membengkak diam-diam. |
| Operasi & monitoring | NAMED | |
| Mendesain dengan Kafka | NAMED | |
| Crib-sheet | DEFERRED | |

Pertanyaan pemahaman dari CORE:
1. Apa beda papan tiket bab 10 (diambil = hilang) dengan papan Kafka (tetap menempel)?
2. Apa gunanya nomor urut (offset) dan pembatas buku tiap juru masak?
3. Kenapa satu jalur menjamin urutan, tapi antar jalur tidak?

Ilustrasi (di `public/assets/illustrations/23-kafka/`):
- `01-papan-log.png` utama: papan raksasa berisi barisan tiket bernomor panjang yang tersusun atas ke bawah dan tidak ada yang kosong; Kuka membaca dari tiket atas.
- `02-offset.png` pendukung: tiga juru masak mesin berdiri di depan papan yang sama, tiap juru masak memegang pembatas buku di tingkat berbeda.
- `03-jalur.png` pendukung: papan dengan tiga jalur tiket terpisah, tiket bernomor mengalir turun di tiap jalur secara berurutan.
