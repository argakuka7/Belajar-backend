# Manifest coverage Bab 9: Caching

Sumber: `public/9.Caching, the secret behind it all/html_notes/notes.html` (11 bagian). Analogi induk: masih di gedung restoran. Chef menyimpan bahan favorit di rak dekat dapur. Mengambil dari rak dekat itu cepat; hanya kalau rak kosong ia berjalan ke gudang. Salinan di rak dekat adalah cache, gudang adalah database dari bab 8.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Apa itu caching | CORE | Simpan fotokopi bahan favorit di rak dekat dapur. Ambil dari sana dulu, gudang hanya kalau rak kosong. |
| 2 | Contoh dunia nyata | RINGAN | Google dan Netflix: dapur dengan rak dekat yang raksasa. |
| 3 | Tingkat caching | CORE ringan | Ada beberapa rak: di meja kerja, di dapur, di gudang. Semakin dekat, semakin cepat. |
| 4 | Caching tingkat jaringan | RINGAN | Cabang restoran punya raknya sendiri, tidak selalu tanya pusat. |
| 5 | Caching tingkat perangkat keras | NAMED | |
| 6 | Database key-value dalam memori (Redis) | CORE ringan | Lemari cepat di samping dapur. Isinya hilang kalau listrik mati, kecuali diselamatkan. |
| 7 | Strategi caching | RINGAN | Kapan menyalin ke rak, dan kapan tamu disajikan salinan tanpa bertanya ke gudang. |
| 8 | Kebijakan eviction | CORE | Rak penuh. Buang yang paling lama tidak dipakai supaya ada tempat. |
| 9 | Kasus pemakaian Redis | RINGAN | Lemari cepat dipakai untuk stok, sesi login, dan antrean ringan. |
| 10 | Contoh kode | DEFERRED | |
| 11 | Bacaan lanjutan & dokumentasi | DEFERRED | |

Hasil: 2 CORE, 2 CORE ringan, 4 RINGAN, 1 NAMED, 2 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Apa untungnya menyimpan salinan di rak dekat dapur?
2. Apa yang dilakukan chef saat rak penuh dan ada bahan baru?
3. Kapan salinan di rak jadi bahaya, dan apa namanya masalah itu?

Ilustrasi (di `public/assets/illustrations/09-caching/`):
- `01-rak-dekat.png` utama: Kuka mengambil toples dari rak kecil dekat dapur, pintu gudang terlihat jauh di kejauhan.
- `02-eviction.png` pendukung: rak penuh sesak, Kuka mengeluarkan satu toples bersarang debu dari raknya.
- `03-cabang.png` pendukung: dua dapur cabang berhadapan, masing-masing punya rak kecil yang isinya sama.
