# Manifest coverage Bab 8: Database dengan Backend

Sumber: `public/8.Database-with-backend/html_notes/notes.html` (14 bagian). Analogi induk: masuk ke dalam gudang restoran dari bab 6. Database adalah buku besar gudang yang tertata dan berpenjaga: tidak hilang saat listrik mati, tiap laci khusus satu jenis bahan, ada penjaga yang menolak bahan tanpa label, dan transfer bahan antar rak dicatat lengkap atau dibatalkan semua.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Kenapa database ada | CORE | Buku besar gudang yang tidak hilang saat listrik mati. Tutup hari ini, besok buka lagi, catatan tetap utuh. |
| 2 | Disk vs RAM | RINGAN | Rak gudang permanen vs meja kerja yang kosong begitu gudang tutup. |
| 3 | DBMS & kenapa bukan file teks | CORE | Buku besar beraturan dengan penjaga dan aturan, bukan tumpukan kertas lepas yang mudah robek atau tertukar. |
| 4 | Relasional vs non-relasional | RINGAN | Laci berkolom rapi vs kotak serbaguna. Pilih sesuai barangnya. |
| 5 | Kenapa Postgres | NAMED | |
| 6 | Tipe data | CORE ringan | Tiap laci khusus satu jenis bahan. Angka di laci angka, tanggal di laci tanggal. |
| 7 | Migrasi | RINGAN | Rencana renovasi rak bertahap, gudang tetap buka. |
| 8 | Memodelkan hubungan | CORE ringan | Kartu pemasok terhubung kartu bahan lewat garis penghubung. |
| 9 | Constraint & integritas | CORE | Penjaga laci menolak bahan tanpa label, dan menolak catatan yang menunjuk pemasok yang tidak ada. |
| 10 | Query & join | CORE ringan | Satu laporan gabungan dari beberapa rak, tanpa berjalan rak ke rak. |
| 11 | Index | RINGAN | Daftar isi di sampul buku besar. Cari langsung, tanpa bolak-balik halaman. |
| 12 | Trigger | RINGAN | Bel otomatis yang berbunyi saat stok tertentu berubah. |
| 13 | Transaksi & ACID | CORE | Pindah bahan antar rak: kedua catatan jadi bersama, atau dibatalkan bersama. Tidak ada setengah jalan. |
| 14 | Esensi produksi | NAMED | |

Hasil: 4 CORE, 3 CORE ringan, 5 RINGAN, 2 NAMED.

Pertanyaan pemahaman dari CORE:
1. Kenapa gudang butuh buku besar (database), bukan sekadar tumpukan kertas (file)?
2. Aturan apa yang dijaga penjaga laci (constraint)?
3. Apa yang terjadi jika satu dari dua catatan transfer bahan gagal?

Ilustrasi (di `public/assets/illustrations/08-database/`):
- `01-gudang.png` utama: Kuka berdiri di depan lemari arsip besar berlaci banyak, buku besar tebal terbuka di meja kecil di sampingnya.
- `02-transaksi.png` pendukung: Kuka memindahkan satu bola dari laci kiri ke laci kanan, kedua laci masing-masing punya papan catatan kembar.
- `03-constraint.png` pendukung: mesin penjaga di depan laci menolak satu kotak tanpa tanda apa pun, tanda blok kecil muncul di antara mereka.
