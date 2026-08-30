# Testing

Kembali ke [overview.md](overview.md).

## Static

Jalan setelah tiap fase yang menyentuh HTML:

```
python3 tools/verify.py public/1.HTTP-AND-CORS/sederhana/notes.html
python3 tools/verify.py public/1.HTTP-AND-CORS/html_notes/notes.html
python3 tools/verify.py public/index.html
```

Semua harus mencetak `OK`. verify.py memeriksa keseimbangan tag dan kebocoran marker terjemahan; cukup untuk halaman statis tanpa JS baru.

## Runtime

```
cd public && python3 -m http.server 8124
```

Drive `agent_browser` (bukan screenshot manual):

1. `http://localhost:8124/1.HTTP-AND-CORS/sederhana/notes.html` terbuka, sembilan section terlihat.
2. Klik `Versi Teknis` sampai notes.html teknis terbuka. Klik `Versi Sederhana` kembali.
3. Keempat gambar punya `naturalWidth > 0`. Network tanpa 404.
4. Anchor di daftar `lanjut` mengarah ke id yang benar-benar ada di notes.html teknis.
5. Index.html: chip `Sederhana` di kartu bab 1 menuju halaman sederhana.
6. Viewport 390x844: tidak ada overflow horizontal, diagram masih terbaca.
7. Console kosong dari error.

## Bukti lulus

Tiap fase mencatat hasil check-nya di pesan balasan sesi, bukan hanya klaim. Fase 4 menutup dengan commit di root project:

```
git add public docs && git commit -m "bab 1: tambah halaman Versi Sederhana + ilustrasi Arga"
```

Push ke `main` menunggu persetujuan user setelah melihat hasilnya.
