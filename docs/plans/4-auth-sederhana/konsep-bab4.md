# Manifest coverage Bab 4: Autentikasi & Otorisasi

Sumber: `public/4.Authentication and authorization for backend engineers/html_notes/notes.html` (18 bagian). Analogi induk: masih di gedung bab 2. Pintu kini terkunci. Masuk butuh dua hal: kartu identitas (autentikasi, kamu siapa) dan gelang bertanda (otorisasi, ruangan mana yang boleh).

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Ringkasan dua kalimat | CORE | Autentikasi: tunjukkan kartu siapa kamu. Otorisasi: gelang menentukan pintu mana yang terbuka. |
| 2 | Sejarah autentikasi | NAMED | |
| 3 | Tiga komponen inti | CORE ringan | Kartu, mesin pemeriksa, catatan siapa punya akses ke apa. |
| 4 | Sesi | CORE | Buku tamu di meja gedung. Kuka dapat penanda nomor, gedung mengingat lewat bukunya. |
| 5 | JWT | CORE | Kartu bersegel yang isi identitasnya ditulis di kartu sendiri. Gedung tidak perlu buku tamu, cukup cek segelnya. |
| 6 | Cookie | RINGAN | Saku di browser tempat penanda atau kartu disimpan. |
| 7 | Autentikasi ber-state | RINGAN | Cara buku tamu: gedung simpan catatan, tamu cukup bawa penanda. |
| 8 | Autentikasi stateless | RINGAN | Cara kartu bersegel: gedung tidak simpan apa-apa, semua info di kartu. |
| 9 | Ber-state vs stateless: memilih | RINGAN | Buku tamu gampang dicoret saat tamu diusir. Kartu praktis kalau ada banyak gedung. |
| 10 | Autentikasi API key | RINGAN | Kartu khusus mesin, bukan kartu tamu. |
| 11 | Masalah delegasi | NAMED | |
| 12 | OAuth 1.0 | NAMED | |
| 13 | OAuth 2.0 | NAMED | |
| 14 | OpenID Connect | NAMED | |
| 15 | Memilih jenis auth | RINGAN | Pilih buku tamu atau kartu bersegel sesuai gedungnya. |
| 16 | Otorisasi & RBAC | CORE | Gelang bermotif: motif segitiga buka pintu segitiga, motif lingkaran buka pintu lingkaran. Peran menentukan pintu. |
| 17 | Pesan error & serangan timing | NAMED | |
| 18 | Crib-sheet debug | DEFERRED | |

Hasil: 4 CORE, 6 RINGAN, 6 NAMED, 1 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Apa beda autentikasi dan otorisasi?
2. Kenapa sesi butuh buku tamu di server, dan JWT tidak?
3. Setelah identitasmu sah, apa yang menentukan ruangan mana yang boleh kamu masuki?

Ilustrasi (di `public/assets/illustrations/04-auth/`):
- `01-pintu.png` utama: Kuka menempelkan kartu bertanda ke mesin pembaca di pintu berpalang, palang mulai naik.
- `02-buku-tamu.png` pendukung: resepsionis mesin menulis di buku tamu tebal, Kuka memegang penanda kecil.
- `03-kartu-segel.png` pendukung: Kuka menunjukkan kartu bersegel lilin, meja di belakangnya kosong tanpa buku.
- `04-gelang.png` pendukung: Kuka memakai gelang bermotif segitiga, satu pintu bermotif segitiga terbuka, dua pintu bermotif lain tertutup.
