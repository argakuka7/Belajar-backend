# Fase 3: Ilustrasi Kuka

Kembali ke [overview.md](overview.md). Kontrak visual: [kontrak-kuka.md](kontrak-kuka.md).

## Goal

Empat gambar siap pakai di `public/assets/illustrations/01-http/`, lolos QA character lock, tanpa teks di dalam gambar.

## Shot list

| File | Peran | Konsep | Adegan |
|---|---|---|---|
| `01-request-respons.png` | Utama, 16:9 | Lingkaran request/respons | Kuka mengantre di loket kantor pos berbentuk mesin raksasa. Ia menyerahkan satu surat, mesin mengeluarkan tanda terima bercap lewat celah lain. Dua arah, dua celah. |
| `02-stateless.png` | Pendukung | Server stateless | Loket yang sama, meja kosong tanpa catatan. Kuka mengulang menunjukkan kartu identitas ke mesin yang wajahnya kosong. |
| `03-status-code.png` | Pendukung | Status code | Tiga tanda terima dengan cap bentuk berbeda: centang, panah melengkung ke alamat baru, tanda seru. Kuka menatap bingung satu cap aneh. |
| `04-https.png` | Pendukung | HTTPS | Amplop dengan segel lilin di tangan Kuka, jalur troli di atasnya digambar sebagai perut ular yang menelan amplop utuh. |

Semua prompt: bahasa Inggris, 16:9, prompt lock Kuka dari kontrak, klausa `no text no letters no words no labels no title no writing of any kind`, satu subjek satu aksi, aksen oranye tunggal untuk arah aliran.

## Changes

- 4 file PNG baru di `public/assets/illustrations/01-http/`, 1600x900.
- Tidak menyentuh HTML apa pun. Integrasi ada di fase 4.

Generator: `codex_generate_image` per gambar, satu per satu, bukan komposit. Fallback SVG sesuai kontrak bila generator gagal dua kali untuk gambar yang sama.

## Verification

- Tiap PNG dibuka lewat `read`: Kuka putih, satu mata, kacamata dan cepak utuh, melayang, tanpa teks, latar bersih. Cek juga `references/qa-checklist.md`: bukan dekorasi, tidak penuh, tidak PPT, tidak lucu.
- Dimensi 1600x900 (cek `sips -g pixelWidth -g pixelHeight`).
- Gagal character lock = regenerate gambar itu, jangan diedit paksa.
