# Manifest coverage Bab 2: Routing

Sumber: `public/2.Routing-in-backend/html_notes/notes.html` (13 bagian). Analogi induk: Kuka tiba di gedung kantor dengan satu meja resepsionis dan banyak pintu. Kertas permintaan dibaca, satu pintu ditunjuk.

Nama tampilan karakter: Kuka. Kontrak visual tetap `docs/plans/1-http-sederhana/kontrak-kuka.md`, ilustrasi sama persis gayanya.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Apa itu routing | CORE | Resepsionis gedung membaca kertas Kuka lalu menunjuk satu pintu. |
| 2 | Method + Path -> Handler | CORE | Kertas berisi kata kerja dan nama pintu. Keduanya bersama menentukan petugas mana yang bekerja. |
| 3 | Route statis | RINGAN | Pintu dengan nama tetap, selalu ke ruangan yang sama. |
| 4 | Route dinamis & parameter path | CORE | Satu pintu berpola menerima banyak nomor kamar. Bingkai pintunya satu, daun pintunya berganti. |
| 5 | Parameter query | RINGAN | Catatan tambahan di peniti kertas, bukan bagian nama pintu. |
| 6 | Path vs query | RINGAN | Nama pintu vs catatan tempelan. |
| 7 | Route bertingkat | RINGAN | Lorong dalam lorong, pintu di ujung lorong. |
| 8 | Siklus hidup routing | NAMED | |
| 9 | Versioning & deprecation | NAMED | |
| 10 | Route catch-all | RINGAN | Alamat tak dikenal digiring ke ruang tunggu, bukan diusir. |
| 11 | Router di Go | DEFERRED | |
| 12 | Router di Python | DEFERRED | |
| 13 | Glosarium routing | DEFERRED | |

Hasil: 2 CORE, 5 RINGAN, 2 NAMED, 4 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Apa tugas router saat request tiba di server?
2. Apa beda pintu bernama tetap dan pintu berpola yang menerima banyak nama?
3. Kapan informasi ditaruh di path, kapan di query?

Ilustrasi (di `public/assets/illustrations/02-routing/`):
- `01-router.png` utama: Kuka menyerahkan kertas di meja resepsionis gedung, lengan meja menunjuk satu pintu di deretan pintu bermotif berbeda.
- `02-param.png` pendukung: satu bingkai pintu dengan daun pintu yang berganti-ganti bentuk, Kuka mengganti daunnya.
- `03-catchall.png` pendukung: lorong buntu berbangku empuk, Kuka duduk di bangku, tanda arah patah.
