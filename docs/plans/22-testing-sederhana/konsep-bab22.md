# Manifest coverage Bab 22: Automated Testing

Sumber: `public/22.Automated-Testing-Unit-Integration-and-E2E/html_notes/notes.html` (21 bagian). Analogi induk: uji rasa sebelum buka pintu. Juru masak hebat tidak menebak; ia mencicipi tiap bahan (unit), mencicipi satu hidangan utuh (integrasi), dan sesekali duduk sebagai tamu biasa dari pintu depan sampai bayar (end-to-end). Cicipi ulang setiap kali resep berubah.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|
| Kenapa tes ada | CORE | Menangkap rasa asin di dapur jauh lebih murah daripada dari keluhan tamu. |
| Piramida pengujian | CORE | Banyak cicipan bahan, sedikit cicipan hidangan utuh, sangat jarang sekali sewa tamu tiruan. |
| Anatomi sebuah tes | CORE ringan | Siapkan bahan, olah, cicip, putuskan lulus atau tidak. |
| Tes unit | CORE | Cicip satu bahan: gula itu manis, garam itu asin. Cepat dan murah. |
| Test double | RINGAN | Garam tiruan untuk latihan: rasanya bisa diatur, tidak menghabiskan stok. |
| Dependency injection | RINGAN | Sediakan celah supaya bahan tiruan bisa dipasang tanpa membongkar dapur. |
| Table-driven testing | RINGAN | Satu daftar cicipan: baris demi baris bahan dengan hasil yang diharapkan. |
| Tes integrasi | CORE | Cicip satu hidangan utuh: bahan-bahan sudah bercampur di panci. |
| Database nyata | RINGAN | Cicip dengan gudang sungguhan kecil, bukan gudang khayalan. |
| HTTP handler & API | RINGAN | Uji pelayan: pesan lewat pintu depan, lihat apa yang keluar. |
| Contract testing | NAMED | |
| Tes end-to-end | RINGAN | Sewa tamu tiruan dari pintu depan: pesan, makan, bayar. Lambat tapi paling mirip kenyataan. |
| Test coverage | RINGAN | Peta bahan mana yang sudah dicicip dan yang belum. |
| Tes flaky | RINGAN | Cicipan yang kadang asin kadang tidak: tidak boleh dipercaya, cari penyebabnya. |
| Fixture & factory | RINGAN | Bahan siap pakai yang disiapkan sama setiap kali mencicip. |
| TDD: red/green/refactor | RINGAN | Tentukan rasanya dulu, pastikan gagal, lalu masak sampai lulus, lalu rapikan. |
| Mocking waktu & keacakan | RINGAN | Jam dan dadu palsu supaya cicipan bisa diulang hasilnya. |
| Performance & load testing | RINGAN | Uji jam sibuk: seratus tamu datang bersamaan, dapur tetap hidup? |
| Tes di CI/CD | RINGAN | Setiap resep baru otomatis dicicip sebelum boleh ke cabang. |
| Strategi pengujian | NAMED | |
| Crib-sheet | DEFERRED | |

Pertanyaan pemahaman dari CORE:
1. Kenapa menangkap rasa asin di dapur lebih baik daripada dari keluhan tamu?
2. Apa beda mencicip bahan (unit) dan mencicip hidangan utuh (integrasi)?
3. Kenapa piramida: banyak cicipan murah, sedikit cicipan mahal?

Ilustrasi (di `public/assets/illustrations/22-testing/`):
- `01-uji-rasa.png` utama: Kuka mencicipi dari sendok kecil di depan banyak mangkuk kecil tersusun, muka berpikir.
- `02-piramida.png` pendukung: tumpukan mangkuk membentuk piramida: banyak di bawah, satu di puncak.
- `03-flaky.png` pendukung: satu mangkuk yang isinya berubah-ubah (digambar dua wajah cicip berbeda di sisi mangkuk), Kuka menggeleng.
