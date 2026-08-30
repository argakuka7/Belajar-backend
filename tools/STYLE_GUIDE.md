# Panduan Terjemahan (Gaya Unslop, Bahasa Indonesia)

Proyek: ~/Projects/Backend-from-first-Principle-id (versi Indonesia dari dokumentasi backend open source (24 bab)). Tugas Anda: terjemahkan bab yang ditugaskan.

## Aturan Gaya

1. Terjemahkan ke bahasa Indonesia yang wajar dan "manusiawi". Bukan terjemahan harfiah kaku.
2. Tidak ada em-dash (—). Gunakan titik atau koma.
3. Tidak ada kata kosong/puffery ("delve", "pivotal", "testament", "sejalan", "menggugah", dll). Sebutkan hal konkretnya.
4. Kalimat pendek dan panjang bervariasi. Kalimat langsung, suara aktif.
5. Istilah teknis TETAP bahasa Inggris: GET/POST/PUT/PATCH/DELETE, ETag, JWT, status code, header, index, join, query, handler, middleware, session, Redis, Postgres, dll. Terjemahkan kata sambung dan kalimatnya; biarkan jargon teknis.
6. Judul bagian: sentence case (jangan Title Case berlebihan).
7. Perbaiki typo/artefak asli bila jelas (mis. "the protocolyour" → "protokol yang Anda pakai").
8. Jangan menambahkan emoji dekoratif, bold berlebihan, atau tanda kutip melengkung.

## Sintaks Penanda (WAJIB)

Gunakan penanda ini di TEKS TERJEMAHAN — alat apply.py akan mengubahnya kembali ke tag HTML:

- `«teks»` = <code>teks</code> (kode inline / istilah teknis dalam font kode). JANGAN pakai backtick `.
- `**teks**` = <strong>teks</strong> (penekanan).
- `_teks_` = <em>teks</em> (miring).
- `[url|teks]` = <a href="url">teks</a> (tautan; biarkan url aslinya).
- Jangan menumpuk penanda di dalam penanda lain kalau bisa.
- Jangan pernah menulis backtick (`) di manapun dalam terjemahan.
- Pertahankan entitas HTML seperti &amp;, &lt;, &gt;, &#8594; apa adanya.
- Baris tabel (tr): terjemahan = sel-sel dipisah persis dengan ` | ` (spasi-pipe-spasi), JUMLAH SEL HARUS SAMA dengan jumlah sel asli.

## Alur Kerja per Bab

Untuk bab di folder `N.<nama-bab>/html_notes/notes.html`:

1. Jalankan: `python3 tools/extract.py "N.<nama-bab>/html_notes/notes.html" /tmp/chBLOCK.json`
2. Baca /tmp/chBLOCK.json. Blok yang `"skip": true` TIDAK diterjemahkan (infografis/kode — biarkan).
3. Untuk setiap blok prosa (skip=false), baca `"marked"`-nya (teks dengan penanda) lalu tulis terjemahan dengan penanda ke file translations: `~/Projects/Backend-from-first-Principle-id/translations/chN.json` — format: objek JSON ber-`"id": "terjemahan"` (kunci STRING).
4. Jalankan: `python3 tools/apply.py /tmp/chBLOCK.json translations/chN.json "N.<nama-bab>/html_notes/notes.html"`
5. Jalankan: `python3 tools/verify.py "N.<nama-bab>/html_notes/notes.html"` — harus mencetak `OK`. Jika ada mismatch tag atau marker bocor: perbaiki file translations (atau hapus marker yang bocor) lalu ulangi apply+verify. Catatan: backtick/`**` yang muncul DI DALAM `<pre>` (blok kode) adalah sah, jangan disentuh.
6. Jika ada blok bersarang (marked mengandung banyak baris yang dulu terpotong), terjemahkan sebagai satu blok utuh.

## Contoh Gaya (dari bab 1 yang sudah disetujui)

- "The server keeps **no session memory between two requests**." → "Server **tidak menyimpan memori sesi antar dua request**."
- "GET should **only retrieve** data..." → "GET seharusnya **hanya mengambil** data..."
- "«Content-Type» wrong is a common bug" → "Salah mengisi «Content-Type» adalah bug umum"

## Larangan (kesalahan yang pernah terjadi)

- Jangan pakai backtick untuk kode — pakai «».
- Jangan menulis `**` yang ganjil (tidak berpasangan).
- Jangan mengubah jumlah sel tabel saat menerjemahkan (split ` | ` harus sama banyak).
- Jangan menerjemahkan blok `"skip": true`.
- Jangan sentuh file bab lain / index.html / tools / translations bab lain.
- JANGAN mengubah file terjemahan bab lain.
- Setelah selesai: lapor jumlah blok diterjemahkan + hasil verify + bab mana yang masih infografis (dilewati).

## Selesai = verify.py mencetak OK
