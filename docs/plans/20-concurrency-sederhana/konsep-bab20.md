# Manifest coverage Bab 20: Concurrency & Parallelism

Sumber: `public/20.Concurrency & Parallelism - IO Bound vs CPU Bound/html_notes/notes.html` (14 bagian). Analogi induk: satu juru masak dan banyak panci. Selama panci merebus (menunggu, IO-bound), juru masak boleh memotong sayur di meja lain (mengerjakan pesanan lain). Tapi menumbuk bumbu (CPU-bound) butuh tangan penuh; satu tangan tidak bisa menumbuk dua cobek. Jadi: menunggu boleh diselingi, menghitung butuh tangan tambahan.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|
| Kenapa konkurensi penting | CORE | Tamu tidak boleh menunggu rebusan selesai hanya karena juru masak berdiri menunggu. |
| Biaya duduk menganggur | CORE | Setiap detik juru masak menunggu panci adalah detik tamu lain tidak dilayani. |
| IO-bound vs CPU-bound | CORE | Menunggu rebusan (IO) vs menumbuk bumbu (CPU). Dua jenis kerja, dua solusi. |
| Konkurensi vs paralelisme | CORE | Menyelingi banyak resep sendirian (konkurensi) vs banyak juru masak memasak bersamaan (paralelisme). |
| Thread OS | RINGAN | Asisten kecil yang boleh memegang satu panci. |
| Overhead thread & context switching | RINGAN | Pindah asisten juga butuh waktu: terlalu banyak asisten, lama ganti-gantian. |
| Model event loop | RINGAN | Satu juru masak cepat dengan bel per panci, mengerjakan yang belnya bunyi. |
| Async/await | RINGAN | Catatan "nanti kembali ke sini" ditinggal di panci, lanjut meja lain. |
| Goroutine & virtual thread | RINGAN | Asisten yang sangat murah, bisa banyak sekali. |
| Scheduler M:N | NAMED | |
| Race condition & state bersama | CORE | Dua juru masak menuang gula ke panci yang sama bersamaan: manisnya dobel. |
| Lock, mutex & channel | RINGAN | Satu kunci panci: yang memegang kunci boleh mengaduk. Aturan antar asisten lewat tiket antar. |
| Memilih model yang tepat | RINGAN | Banyak menunggu? Selingi. Banyak menghitung? Tambah tangan. |
| Bacaan lanjutan | DEFERRED | |

Pertanyaan pemahaman dari CORE:
1. Apa beda pekerjaan yang menunggu (IO-bound) dan yang menghitung (CPU-bound)?
2. Apa beda konkurensi dan paralelisme?
3. Apa yang terjadi kalau dua juru masak menuang ke panci yang sama tanpa aturan?

Ilustrasi (di `public/assets/illustrations/20-concurrency/`):
- `01-dua-panci.png` utama: Kuka mengaduk satu panci sambil tangan lainnya menunjuk dua panci lain yang merebus, bel kecil di tiap panci.
- `02-paralel.png` pendukung: tiga juru masak mesin kembar mengaduk tiga panci di tiga kompor, benar-benar bersamaan.
- `03-gula.png` pendukung: dua lengan menuang dari dua tempurung gula ke satu panci yang sama, tetesan bertabrakan.
