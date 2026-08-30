# Kontrak gaya ilustrasi Kuka

Sumber resmi: `~/.dsh/skills/kuka-ilustrasi-skill/` (SKILL.md + `references/`). File ini meringkas bagian yang bisa ditegakkan saat implementasi bab 1.

## Karakter pemandu: Kuka

Kuka adalah avatar pembuat, pemandu pembaca di Versi Sederhana.

Kunci visual (wajib, dari `references/character-arga.md`):
- Tubuh kacang lonjong, PUTIH solid, flat ink, tanpa outline tambahan.
- Satu mata kecil gelap, mengintip di atas kacamata.
- Kacamata bulat frame tipis gelap, rambut cepak gelap. Keduanya selalu utuh, tidak pernah terpotong.
- Dua lengan pendek gempal. Tanpa kaki, melayang di atas bayangan elips abu-abu lembut.
- Ekspresi ramah, penasaran, sedikit bingung. Tanpa antena.

Prompt lock (tempel mentah di tiap prompt):
```
small round soft-white bean-shaped creature with a crew-cut flat-top short
dark hair patch on its head, wearing round eyeglasses with thin dark frames,
one small solid dark circular eye peeking above the glasses, two short stubby
arms, no legs, hovering above a soft elliptical shadow, friendly curious
slightly confused expression
```

Pemeran lain: server dan objek teknis digambar sebagai objek (loket, mesin, amplop), bukan karakter kedua. Tanpa Noko atau Si Hitam di bab 1 supaya beban visual rendah.

## Gaya halaman (dari `references/style-dna.md` + SKILL.md)

- 16:9 horizontal, 1600x900, latar putih bersih.
- Garis tinta hitam sedikit goyang, tanpa bayangan, tanpa gradien, tanpa tekstur.
- Aksen merah/oranye/biru jarang. Ruang kosong 35-40%.
- Aneh tapi bersih. Bukan maskot lucu, bukan infografis PPT, bukan kartun anak.

## Aturan teks (Kuka's rule)

Gambar tanpa teks apa pun. Setiap prompt wajib memuat:
```
no text no letters no words no labels no title no writing of any kind
```
Semua label Bahasa Indonesia ditulis di HTML sekitar gambar, 2-6 kata per label.

## Pipeline generate

1. Utama: `codex_generate_image` (gpt-image-2), prompt bahasa Inggris + prompt lock + klausa tanpa teks.
2. Fallback: hand-coded SVG inline sesuai resep SVG di SKILL.md (viewBox 1600x900, stroke `#1A1A1A` 2.5-3.5, aksen oranye `#E68A3C`).
3. QA tiap hasil memakai `references/qa-checklist.md` dan character lock di atas. Gagal = regenerate, jangan dipaksa.
