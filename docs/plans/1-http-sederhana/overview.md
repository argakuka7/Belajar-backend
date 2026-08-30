# Plan: Versi Sederhana Bab 1 HTTP + ilustrasi Kuka

## Context

Situs ini punya 24 bab versi teknis yang padat. Pembaca pemula (dewasa, non-backend) tidak punya pintu masuk. Keputusan desain sudah disepakati di sesi sebelumnya dan digrill habis: tiap bab dapat dua versi, teknis (yang sekarang) dan Versi Sederhana. Bab 1 jadi pembuktian pola; bab 2-3 menyusul kalau polanya terbukti. Belum ada satu baris implementasi pun. Plan ini adalah deliverable sesi ini.

Untuk siapa: pembaca pemula mendapat halaman masuk yang bisa dipahami tanpa istilah backend. Pemilik situs mendapat pola yang bisa diulang untuk 23 bab berikutnya tanpa kerja ulang.

## Scope

**Masuk.**
- Halaman `public/1.HTTP-AND-CORS/sederhana/notes.html` dengan struktur 9 bagian yang sudah disepakati.
- `public/assets/sederhana.css` sebagai komponen bersama (dipakai ulang bab 2-3).
- Ilustrasi Kuka: 1 utama 16:9 + 3 pendukung, disimpan di `public/assets/illustrations/01-http/`.
- Link dua arah antara kedua versi, plus satu link penanda di `public/index.html` untuk bab yang punya versi sederhana.
- Inventaris konsep Bab 1 dan manifest coverage di `konsep-bab1.md`.

**Keluar.**
- Konten bab 2-3 (pola saja, belum dieksekusi).
- Perubahan apa pun pada isi versi teknis, kecuali satu link ke versi sederhana.
- Framework, build step, atau library baru.
- Animasi dekoratif yang tidak menjelaskan.

## Constraints

- Situs statis murni. Halaman baru adalah HTML+CSS+sedikit JS vanilla, konsisten dengan design token yang sudah ada (paper, ink, rust, gold, teal).
- Ilustrasi lokal di `public/assets/illustrations/`, bukan gambar runtime atau URL eksternal.
- Gaya Kuka terkunci oleh `kontrak-kuka.md`. Gambar tanpa teks; semua label hidup di HTML.
- Prosa mengikuti `tools/STYLE_GUIDE.md`: bahasa Indonesia wajar, tanpa em-dash, istilah teknis tetap Inggris.
- Repo git ada di root project. Commit dari root.

## Alternatives

1. **HTML statis per bab + CSS bersama (dipilih).** Nol dependensi, bisa direview per file, persis pola situs sekarang. Biaya: menyalin header/nav antar bab, diterima karena frekuensi bab baru rendah.
2. **Shell HTML + konten JSON yang dirender JS.** Satu template untuk semua bab, tapi menambah runtime requirement dan menyulitkan share link tanpa JS. Melanggar constraint statis murni.
3. **SSG (Astro/Eleventy).** Template bersih dan scaling bagus untuk 24 bab, tapi menambah build step dan framework baru yang user tolak secara eksplisit.

## Applicable skills

- `kuka-ilustrasi-skill` (`~/.dsh/skills/kuka-ilustrasi-skill/`) untuk kontrak visual dan QA ilustrasi.
- `frontend-design` untuk komponen step cards, diagram alur, istilah interaktif.
- `stop-slop` dan `tools/STYLE_GUIDE.md` untuk semua prosa halaman.
- `pi-pstack`: `how` sebelum menyentuh notes.html, `unslop` untuk tiap diff prosa, `deslop` sebelum commit, `technical-writing` untuk dokumen plan.

## Phases

1. [phase-1-scaffold.md](phase-1-scaffold.md): shell halaman sederhana, CSS bersama, link dua arah.
2. [phase-2-konten.md](phase-2-konten.md): isi 9 bagian sesuai manifest coverage.
3. [phase-3-ilustrasi.md](phase-3-ilustrasi.md): shot list, generate, QA, simpan ilustrasi Kuka.
4. [phase-4-integrasi.md](phase-4-integrasi.md): pasang ilustrasi + diagram + istilah, link index.html, verifikasi penuh.

Urutan ini menaruh scaffold dan kontrak (yang dipakai semua fase berikutnya) lebih dulu. Ilustrasi sebelum integrasi supaya fase 4 hanya menyambung, tidak menunggu.

## Verification

- Static: `python3 tools/verify.py <file>` mencetak `OK` untuk tiap HTML yang disentuh.
- Runtime: `python3 -m http.server 8124` dari `public/`, lalu drive `agent_browser` ke kedua halaman: link dua arah jalan, gambar termuat (`naturalWidth > 0`), nav bawah utuh, viewport 390px tidak rusak, console bersih.

## Implementation guidance

- Jalankan `how` atas notes.html sebelum edit (sudah dieksekusi sesi ini; temuan hidup di plan ini).
- `unslop` tiap diff prosa sebelum commit, termasuk dokumen plan ini.
- `deslop` atas diff sebelum tiap commit.
- `show-me-your-work`: keputusan penting dicatat di file plan ini, bukan di kepala.
- Tidak ada PR. Sesuai pola situs ini, commit langsung ke `main` dan push setelah user melihat hasilnya di browser.

 ## Worker

 Delegasi kerja memakai `subagent({ agent: "worker", model: "openai-codex/gpt-5.6-luna" })` (arah user, sesi ini). Slug polos `gpt-5.6-luna` gagal 402 OpenRouter karena credit key kurang; slug kualified `openai-codex/gpt-5.6-luna` sudah diprobe dan jalan. Tiap task ke worker memuat pointer file, bukan konten inline, dan selalu menyebut `docs/plans/1-http-sederhana/` sebagai kontrak yang wajib dibaca dulu.
