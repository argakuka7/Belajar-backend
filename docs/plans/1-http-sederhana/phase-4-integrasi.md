# Fase 4: Integrasi dan verifikasi penuh

Kembali ke [overview.md](overview.md).

## Goal

Semua bagian menyambung: gambar terpasang dengan label HTML, diagram alur hidup, index.html menandai bab yang punya versi sederhana. Situs dalam keadaan bisa di-push.

## Changes

- `public/1.HTTP-AND-CORS/sederhana/notes.html` (edit). Pasang 4 gambar di `.ilustrasi-frame` dengan caption HTML 2-6 kata di sekitar gambar, bukan di dalamnya. Selesaikan bagian `alur` dengan SVG inline bergaya situs (stroke `#1A1A1A`, aksen `#E68A3C`). Rapikan `.istilah` details di bagian `konsep` untuk 6 istilah: request, respons, method, status code, header, HTTPS.
- `public/index.html` (edit kecil). Satu chip `Sederhana` di kartu bab 1, link ke `1.HTTP-AND-CORS/sederhana/notes.html`. Bab lain tidak berubah.

## Data structures

Tidak ada data baru. Nama file gambar diambil persis dari shot list fase 3.

## Verification

- Static: `python3 tools/verify.py` OK untuk kedua file yang disentuh.
- Runtime via `agent_browser`, server `python3 -m http.server 8124` dari `public/`:
  - Sederhana dan teknis terbuka, link dua arah jalan.
  - 4 gambar termuat (`naturalWidth > 0`), tidak ada 404 di network.
  - Chip di index.html menuju halaman yang benar.
  - Viewport 390px: gambar tidak meluber, diagram terbaca.
  - Console tanpa error.
- Commit di root project setelah verifikasi lulus. Push ke `main` setelah user melihat hasil.
