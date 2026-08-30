# Fase 1: Scaffold halaman sederhana

Kembali ke [overview.md](overview.md).

## Goal

Halaman `public/1.HTTP-AND-CORS/sederhana/notes.html` ada dan bisa dibuka. Shell berisi kerangka 9 bagian yang masih kosong, komponen CSS bersama, dan link dua arah ke versi teknis. Fase ini berdiri sendiri: setelah fase ini, pola navigasi sudah bisa diuji meski konten belum ada.

## Changes

- `public/1.HTTP-AND-CORS/sederhana/notes.html` (baru). Struktur: head dengan font dan token warna yang sama seperti notes.html teknis, hero dengan kicker `BAB 1 / VERSI SEDERHANA`, sembilan section kosong bernomor sesuai struktur yang disepakati, tombol `Versi Teknis` di hero dan di nav bawah, footer `bfp-footer` dengan link www.argakuka.com.
- `public/assets/sederhana.css` (baru). Komponen bersama bab 2-3: `.step-card`, `.flow-diagram`, `.istilah` (details/summary), `.ilustrasi-frame`, `.tanya` (blok pertanyaan pemahaman). Semua dari token warna situs, tanpa framework.
- `public/1.HTTP-AND-CORS/html_notes/notes.html` (edit kecil). Satu chip link `Versi Sederhana` di hero meta.

Tanpa JS baru. Istilah interaktif memakai `<details>` native.

## Data structures

Tidak ada tipe baru. Kontrak halaman: sembilan `<section>` dengan id tetap (`masalah`, `analogi`, `ilustrasi`, `konsep`, `alur`, `contoh`, `ringkasan`, `tanya`, `lanjut`) supaya bab 2-3 menyalin kerangka yang sama persis.

## Verification

- `python3 tools/verify.py public/1.HTTP-AND-CORS/sederhana/notes.html` mencetak `OK`.
- `python3 -m http.server 8124` dari `public/`, drive browser: shell terbuka, link dua arah jalan ke dua arah, viewport 390px tidak rusak, console bersih.
