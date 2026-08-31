# Manifest coverage Bab 16: Graceful Shutdown

Sumber: `public/16.Graceful Shutdown/html_notes/notes.html` (8 bagian). Analogi induk: restoran yang harus tutup. Cara kasar: matikan lampu, usir semua orang, pesanan hilang. Cara santun: papan "tutup sebentar lagi" dipasang di pintu, tamu yang sudah duduk dilayani sampai selesai, tamu baru tidak diterima, setelah semua meja kosong lampu dimatikan.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| Konsep | Perlakuan | Catatan analogi |
|---|---|---|
| Skenario (kenapa server berhenti) | CORE ringan | Gedung butuh tutup: renovasi, pindah, atau listrik diperbarui. |
| Apa itu graceful shutdown | CORE | Papan "tutup sebentar lagi", tamu lama dilayani tuntas, tamu baru ditolak sopan. |
| Manajemen siklus hidup proses | RINGAN | Ada urutan resmi menutup: pasang papan, berhenti terima, selesaikan, bersihkan, kunci. |
| Signal & komunikasi antar-proses | RINGAN | Petugas gedung mengetuk pintu dapur memberi tanda tutup. |
| Connection draining | CORE | Tamu yang sudah duduk dilayani sampai habis, tamu baru disuruh datang besok. |
| Pembersihan resource | CORE ringan | Cuci panci, rapikan rak, catat buku besar sebelum kunci pintu. |
| Contoh kode | DEFERRED | |
| Bacaan lanjutan | DEFERRED | |

Pertanyaan pemahaman dari CORE:
1. Apa beda matikan lampu langsung dengan tutup secara santun?
2. Kenapa tamu baru ditolak lebih dulu sebelum tamu lama selesai dilayani?
3. Apa yang harus dibersihkan sebelum pintu dikunci?

Ilustrasi (di `public/assets/illustrations/16-shutdown/`):
- `01-papan.png` utama: Kuka memasang papan tutup di pintu restoran, tamu di dalam masih dilayani pelayan.
- `02-draining.png` pendukung: dua meja tamu yang masih punya piring, pelayan membawa piring terakhir ke salah satunya, pintu sudah ditutup setengah.
- `03-beres-beres.png` pendukung: Kuka mencuci panci terakhir di bak cuci, rak di sebelahnya sudah kosong dan rapi.
