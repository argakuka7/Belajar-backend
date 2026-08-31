# Manifest coverage Bab 15: Logging, Monitoring & Observability

Sumber: `public/15.Logging, Monitoring and Observability/html_notes/notes.html` (daftar bagian di halaman teknis). Analogi induk: buku harian dapur dan papan pantau. Setiap kejadian penting dicatat satu baris di buku harian (log). Papan pantau di dinding menampilkan angka penting saat ini (metrics). Saat tamu bertanya kenapa pesananannya lambat, dari buku harian dan papan itu kita bisa menjawab tanpa menebak (tracing).

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

Catatan: daftar h2 bab ini kosong di ekstraksi (struktur berbeda). Worker halaman wajib membaca notes.html teknisnya langsung dan menyusun cakupan berikut sebagai patokan: apa itu logging, level log, structured logging, apa itu metrics, apa itu tracing, centralized logging, alerting, dasbor. Perlakuan: logging dan metrics CORE, tracing CORE ringan, level log dan structured logging CORE ringan, centralized logging dan alerting RINGAN, sisanya NAMED/RINGAN mengikuti bobot di teknis.

| Konsep | Perlakuan | Catatan analogi |
|---|---|---|
| Logging | CORE | Buku harian: satu baris per kejadian, waktunya jelas. |
| Level log (info/warn/error) | CORE ringan | Catatan biasa, catatan waspada, catatan darurat. |
| Structured logging | CORE ringan | Ditulis dengan pola rapi supaya bisa dihitung, bukan coretan bebas. |
| Metrics | CORE | Papan pantau: jumlah pesanan hari ini, rasa menunggu rata-rata. |
| Distributed tracing | CORE ringan | Nomor tiket mengikuti pesanan dari pintu sampai rak, jadi tahu meja mana yang lambat. |
| Centralized logging | RINGAN | Buku harian semua cabang dikumpulkan di satu rak. |
| Alerting | RINGAN | Bel bunyi saat angka melewati batas, bukan menunggu tamu protes. |
| Dasbor | RINGAN | Papan pantau yang dilihat sekilas tiap pagi. |

Pertanyaan pemahaman dari CORE:
1. Apa beda buku harian (log) dan papan pantau (metrics)?
2. Kenapa catatan harus berpola rapi (structured)?
3. Apa gunanya nomor tiket (tracing) saat tamu komplain pesanan lambat?

Ilustrasi (di `public/assets/illustrations/15-logging/`):
- `01-buku-harian.png` utama: Kuka menulis satu baris di buku harian tebal di meja dapur, papan pantau kecil bergambar grafik tergantung di dinding.
- `02-papan.png` pendukung: papan pantau dengan tiga jarum meter dan satu grafik naik, Kuka melihat sekilas.
- `03-tiket.png` pendukung: satu tiket dengan nota terklip berpindah meja ke meja, garis putus-putus menghubungkan meja-meja itu.
