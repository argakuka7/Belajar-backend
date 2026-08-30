# Inventaris konsep Bab 1 + manifest coverage

Sumber: `public/1.HTTP-AND-CORS/html_notes/notes.html` (22 bagian, h2). Kolom perlakuan menentukan apa yang ditulis di Versi Sederhana dan apa yang hanya dapat link.

Perlakuan:
- **CORE** = dijelaskan dengan analogi Arga di Versi Sederhana.
- **RINGAN** = disebut satu-dua kalimat dengan analogi, tanpa detail.
- **NAMED** = disebut namanya saja sebagai jalan setumpuk ke versi teknis.
- **DEFERRED** = tidak disentuh, hanya ada di versi teknis.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Prinsip inti: request/respons, client-server, stateless, TCP | CORE | Arga kirim surat ke loket, terima tanda terima. Loket tidak mengingat siapa pun. Jalur pos = TCP. |
| 2 | Evolusi HTTP (0.9, 1.1, 2, 3) | NAMED | Satu kalimat: aturan main ini ikut naik versi. |
| 3 | Anatomi pesan (start line, header, body) | CORE ringan | Surat punya baris perintah, label di sampul, dan isi. |
| 4 | Kenapa header ada | CORE ringan | Label sampul: tanpa membuka isi, kurir sudah tahu kemana dan apa isinya. |
| 5 | Jenis-jenis header (termasuk security header) | NAMED | Ditunda ke teknis. |
| 6 | Method HTTP (GET/POST/PUT/PATCH/DELETE) | CORE ringan | Kata kerja di kertas permintaan: ambil, titip, ganti, hapus. |
| 7 | Idempotensi | RINGAN | Tekan tombol ambil berkali-kali, hasilnya sama. |
| 8 | Cookie, sesi, JWT | RINGAN | Loket lupa, jadi setiap kunjungan bawa kartu identitas. |
| 9 | CORS & preflight | NAMED | Punya bab konsep sendiri nanti; di sini hanya nama. |
| 10 | Status code (2xx/3xx/4xx/5xx) | CORE | Cap warna di tanda terima: hijau berhasil, kuning pindah alamat, merah salah, abu-abu mesin rusak. 200, 404, 500 dipakai sebagai contoh. |
| 11 | Redireksi | RINGAN | Tanda terima berisi alamat baru. |
| 12 | Caching (Cache-Control, ETag) | RINGAN | Simpan salinan fotokopi supaya tidak minta ulang ke loket. |
| 13 | Request kondisional & penguncian optimistis | NAMED | Ditunda ke teknis. |
| 14 | Negosiasi konten & kompresi | NAMED | Ditunda ke teknis. |
| 15 | Range request | NAMED | Ditunda ke teknis. |
| 16 | Koneksi persisten & keep-alive | RINGAN | Jalur pos tetap terbuka untuk beberapa surat, tidak buka-tutup tiap surat. |
| 17 | Upload multipart & stream | DEFERRED | |
| 18 | Proxy, tunneling, Forwarded | DEFERRED | |
| 19 | Upgrade protokol & WebSocket | DEFERRED | Ada bab 24. |
| 20 | SSL, TLS, HTTPS | CORE ringan | Amplop tersegel: tukang pos tidak bisa membaca atau mengubah isinya. |
| 21 | Crib-sheet debugging | DEFERRED | Alat kerja, bukan konsep. |

Hasil: 4 CORE (intinya satu lingkaran request/respons), 6 RINGAN, 7 NAMED, 4 DEFERRED. Tiga pertanyaan pemahaman diambil dari CORE: anatomi request/respons, stateless, arti method dan status code.
