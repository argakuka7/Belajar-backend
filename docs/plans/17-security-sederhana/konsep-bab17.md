# Manifest coverage Bab 17: Backend Security

Sumber: `public/17.Backend Security - Everything You Need to Know/html_notes/notes.html` (20 bagian). Analogi induk: protokol keamanan gedung. Pikirkan seperti pencuri: pintu mana yang lemah? Lalu tutup satu per satu: kata sandi tidak pernah ditulis polos, kartu palsu ditolak, tamu tidak boleh masuk lewat jendela, dan setiap lapisan menjaga lapisan di bawahnya.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|
| Pola pikir keamanan: berpikir seperti penyerang | CORE | Sebelum menjaga gedung, pikirkan cara kamu akan mencurinya. |
| Ringkasan kerentanan | NAMED | |
| SQL injection | CORE | Tamu menulis catatan yang sebenarnya perintah ke gudang. Jangan pernah dibaca langsung sebagai perintah. |
| Command injection | RINGAN | Trik yang sama lewat pintu lain. |
| Penyimpanan kata sandi: tiga evolusi | CORE | Kata sandi tidak pernah ditulis polos di buku. Yang disimpan hasil olahannya. |
| Sesi, cookie & flag kritis | RINGAN | Kartu tamu punya tanda: hanya lewat jalur terkunci. |
| JWT: autentikasi stateless | RINGAN | Kartu bersegel dari bab 4. Segelnya bisa dipalsukan kalau kunci bocor. |
| Rate limiting endpoint autentikasi | RINGAN | Batasi tebakan: lima kali gagal, pintu pending sebentar. |
| BOLA & BFLA | RINGAN | Kartu tamu biasa tidak boleh membuka pintu gudang meski nomornya ditebak. |
| XSS | RINGAN | Tamu menempel catatan yang sebenarnya perintah ke tamu lain. |
| CSRF | RINGAN | Orang lain memesan atas nama kamu tanpa kamu tahu. |
| Salah konfigurasi | RINGAN | Pintu samping yang lupa dikunci. |
| Pertahanan berlapis | CORE ringan | Satu gembok tidak cukup; lapisan menjaga lapisan. |
| Go: pola aman | DEFERRED | |
| Python: pola aman | DEFERRED | |
| OAuth 2.0 & OIDC | RINGAN | Menitipkan pemeriksaan identitas ke penjaga profesional. |
| Internal HTTPS & TLS | RINGAN | Jalur antar ruangan juga disegel, bukan hanya pintu depan. |
| Pola pikir penetration testing | NAMED | |
| Studi kasus insiden nyata | RINGAN | Cerita gedung yang kecurungan: pelajarannya sama. |
| Referensi & bacaan lanjutan | DEFERRED | |

Pertanyaan pemahaman dari CORE:
1. Kenapa kata sandi tidak boleh disimpan dalam bentuk aslinya?
2. Apa bahaya menempel catatan tamu (input) langsung jadi perintah (SQL injection)?
3. Kenapa satu gembok (satu lapisan keamanan) tidak cukup?

Ilustrasi (di `public/assets/illustrations/17-security/`):
- `01-gembok.png` utama: pintu gedung dengan tiga lapis pengaman berjajar: gembok, pembaca kartu, dan penjaga mesin; Kuka melewati lapisan pertama.
- `02-sandi.png` pendukung: buku besar terbuka berisi halaman-halaman pola tak terbaca (hasil olahan), Kuka menutup halaman yang bertuliskan polos. Tanpa huruf: halaman polos digambarkan lembar kosong bersih vs halaman bergaris tak beraturan.
- `03-injection.png` pendukung: Kuka menyerahkan kertas catatan, mesin penerima memasukkannya ke rongga "perintah" yang terpisah dari rongga "catatan".
