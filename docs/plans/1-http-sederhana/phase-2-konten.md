# Fase 2: Konten Versi Sederhana Bab 1

Kembali ke [overview.md](overview.md).

## Goal

Sembilan bagian terisi. Pembaca pemula selesai membaca dalam 10-15 menit dan bisa menjawab tiga pertanyaan pemahaman. Semua klaim selaras dengan versi teknis, tanpa menyalin kodenya.

## Changes

- `public/1.HTTP-AND-CORS/sederhana/notes.html` (isi). Peta bagian ke manifest:
  1. `masalah` — skenario harian: buka link, halaman muncul. Apa yang sebenarnya terjadi.
  2. `analogi` — Arga mengirim surat ke loket kantor pos: surat, label sampul, tanda terima bercap, loket yang tidak mengingat siapa pun.
  3. `ilustrasi` — placeholder untuk fase 3, jangan diisi gambar di fase ini.
  4. `konsep` — CORE dari manifest (`konsep-bab1.md`): lingkaran request/respons, anatomi pesan sebagai surat, method sebagai kata kerja, status code sebagai cap, HTTPS sebagai amplop tersegel. RINGAN: stateless-kartu identitas, caching fotokopi, keep-alive jalur terbuka.
  5. `alur` — diagram alur SVG inline: browser ke server, request, respons, status.
  6. `contoh` — satu contoh mini: request GET dan respons 200 yang ditulis seperti kartu pos, bukan kode Go/Python. Pseudocode maksimal 8 baris.
  7. `ringkasan` — 5 butir, masing-masing satu kalimat.
  8. `tanya` — 3 pertanyaan dari CORE: (a) apa isi request dan respons, (b) kenapa server tidak ingat kamu dan apa akibatnya, (c) apa beda 200, 404, 500.
  9. `lanjut` — link ke versi teknis dengan janji apa yang ditemukan di sana (header, CORS, caching dalam).
- NAMED dan DEFERRED dari manifest ditulis sebagai satu daftar "kalau mau lebih dalam" di bagian `lanjut`. Semua link menuju `../html_notes/notes.html` tanpa anchor, karena h2 versi teknis tidak punya id dan menambah id berarti menyentuh file teknis di luar scope.

Prosa mengikuti `tools/STYLE_GUIDE.md`: bahasa Indonesia wajar, tanpa em-dash, istilah teknis tetap Inggris, sentence case.

## Data structures

Struktur konten mengikuti id section tetap dari fase 1. Tidak ada data baru.

## Verification

- `python3 tools/verify.py` OK.
- Browser: halaman terbaca penuh, daftar `lanjut` punya anchor valid ke notes.html teknis (tiap link target benar-benar ada, dicek dengan grep id di teknis).
- Pembanding coverage: tiap baris CORE dan RINGAN di `konsep-bab1.md` punya tempat di halaman; tiap NAMED muncul di `lanjut`.
