# Kontrak verifikasi browser (untuk worker)

Kamu memverifikasi satu atau dua halaman Versi Sederhana memakai tool `agent_browser` native di sesimu. Jangan pakai CLI agent-browser lewat bash; lingkungan memblokirnya. Jangan sentuh file apa pun.

## Persiapan

1. `cd public` lalu jalankan server di port yang ditugaskan: `python3 -m http.server <PORT>` di background (`nohup ... &`). Tunggu 1 detik, cek `curl -s -o /dev/null -w "%{http_code}"` harus 200. Matikan server di akhir (`pkill -f "http.server <PORT>"`).
2. Buka halaman sederhana dengan `agent_browser` open (URL-encode spasi dengan %20).

## Checklist per bab (laporkan pass/fail tiap butir + bukti URL)

1. **Struktur.** Eval: `document.title` sesuai bab; `main section` punya 9 id: masalah, analogi, ilustrasi, konsep, alur, contoh, ringkasan, tanya, lanjut.
2. **Gambar.** Set semua `.ilustrasi img` loading=eager, lalu `await i.decode()` per gambar. Semua harus `naturalWidth > 0` dan `complete`.
3. **Overflow.** `document.documentElement.scrollWidth <= clientWidth` pada viewport 390x844.
4. **Link dua arah.** Klik teks "Versi Teknis" sampai URL pindah ke `html_notes/notes.html`. Lalu klik "Versi Sederhana" sampai kembali ke `sederhana/notes.html`. Bila klik tertutup elemen melayang (dock tema), naikkan viewport ke 1440x1000 lalu ulangi; bila tetap gagal, buktikan link lewat snapshot (href ada di DOM) dan catat sebagai pass-dengan-catatan.
5. **Chip teknis.** Di halaman teknis, cari teks link "Versi Sederhana" (snapshot atau grep lewat eval). Harus ada satu.
6. **Console.** QA preset: `expectedSelector: ".simple-shell"`, checkConsole, checkErrors. Harus lulus.
7. **Index.** Buka `/index.html`, pastikan ada link `Sederhana` dengan href menuju folder bab tugasmu.

## Laporan

Kirim tabel pass/fail per butir, URL bukti, dan daftar masalah apa pun. Jika butir gagal, jangan memperbaiki apa pun; cukup laporkan dengan detail elemen yang bermasalah.
