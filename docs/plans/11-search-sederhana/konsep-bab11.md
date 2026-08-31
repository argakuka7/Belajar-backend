# Manifest coverage Bab 11: Full-Text Search & Elasticsearch

Sumber: `public/11.Full text search using Elasticsearch for blazingly fast search/html_notes/notes.html` (12 bagian). Analogi induk: gudang restoran punya ribuan kertas resep. Mencari satu resep dengan membuka satu per satu = gila. Pustakawan menyelesaikannya dengan kartu katalog: satu kartu per kata, berisi daftar resep yang memuat kata itu.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| # | Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|---|
| 1 | Kisah asal: kenapa pencarian jadi sulit | CORE | Mencari resep di tumpukan sepuluh ribu kertas dengan membuka satu per satu. Butuh hari. |
| 2 | Analogi pustakawan | CORE | Pustakawan menyiapkan kartu katalog: bukan menyimpan resep, ia menyimpan petunjuk ke resep. |
| 3 | Inverted index: penemuan inti | CORE | Kartu terbalik: satu kata, daftar semua resep yang memuatnya. Cari sekali, langsung dapat daftar. |
| 4 | Elasticsearch: apa itu & cara kerjanya | CORE ringan | Petugas katalog super cepat yang menyimpan semua kartu di memori dan membagi tugas ke banyak meja. |
| 5 | BM25: cara kerja skor relevansi | RINGAN | Petugas menilai jawaban mana yang paling cocok, bukan sekadar daftar asal. |
| 6 | Toleransi typo: fuzzy search | RINGAN | Ketik "kopi" jadi "kpi" pun kartunya tetap ketemu. |
| 7 | ELK stack: log & observabilitas | NAMED | |
| 8 | Full-text search Postgres di Go | DEFERRED | |
| 9 | Elasticsearch di Python | DEFERRED | |
| 10 | Benchmark: ILIKE vs Elasticsearch | NAMED | |
| 11 | Kapan memakai apa | RINGAN | Rak kecil cukup kartu sederhana; ribuan resep baru butuh pustakawan. |
| 12 | Referensi & bacaan lanjutan | DEFERRED | |

Hasil: 3 CORE, 2 CORE ringan, 3 RINGAN, 2 NAMED, 2 DEFERRED.

Pertanyaan pemahaman dari CORE:
1. Kenapa mencari di tumpukan besar dengan membuka satu per satu itu lambat?
2. Apa isi kartu katalog terbalik (inverted index)?
3. Kenapa ketikan yang salah sedikit tetap bisa menemukan resep?

Ilustrasi (di `public/assets/illustrations/11-search/`):
- `01-katalog.png` utama: Kuka membuka satu laci kabinet kartu katalog perpustakaan raksasa, rak buku tinggi di kejauhan.
- `02-inverted.png` pendukung: satu kartu besar di dinding dengan tiga garis penghubung ke tiga buku di rak.
- `03-fuzzy.png` pendukung: Kuka menyerahkan kartu dengan satu goresan bergelombang, petugas mesin mengangguk menerimanya.
