# Kontrak ilustrasi Kuka (untuk worker)

Kamu membuat ilustrasi untuk satu bab memakai tool `codex_generate_image` di sesimu. Bila tool itu tidak ada di sesimu, berhenti dan laporkan segera, jangan mengarang gambar. Jangan sentuh file di luar folder ilustrasi babmu.

## Bahan

1. Baca shot list di manifest babmu, mis. `docs/plans/11-search-sederhana/konsep-bab11.md` (kolom Ilustrasi di bawah).
2. Baca `docs/plans/1-http-sederhana/kontrak-kuka.md` untuk character lock.

## Prompt (tiap gambar)

Bangun prompt bahasa Inggris dengan kerangka ini, adegan diganti sesuai shot list:

```
16:9 horizontal hand-drawn minimalist illustration, pure white background,
black ink line art slightly wobbly, no shadows no gradients no textures except
one soft elliptical shadow under the floating creature, no text no letters no
words no numbers no labels no title no writing of any kind.
[adegan dari shot list, subjek tunggal satu aksi].
Lots of empty white space. Strange but clean, not cute, not mascot, not
children's cartoon, not PPT infographic.
```

Character lock wajib menempel di tiap prompt (GANTI [adegan]):

```
A small round soft-white bean-shaped creature with EXACTLY ONE single small
solid dark circular eye (only one lens contains the eye, the other lens stays
empty), the single eye peeking above thin round dark-framed eyeglasses, a
crew-cut flat-top short dark hair patch on its head, two short stubby arms,
no legs, hovering above a soft elliptical shadow, friendly curious slightly
confused expression.
```

Parameter: `outputFormat: png`, `save: custom`, `saveDir:` folder ilustrasi babmu.

## QA tiap hasil (lihat gambar yang dikirim tool)

- Satu mata saja. Dua mata = GAGAL, regenerate.
- Tubuh putih solid, kacamata bulat + rambut cepak utuh, tanpa kaki, bayangan elips, tanpa antena.
- Tanpa teks/huruf/angka. Latar putih bersih. Bukan PPT, tidak penuh, tidak lucu.
- Gagal dua kali berturut-turut untuk gambar yang sama: biarkan, catat di laporan, gambar itu akan dibuatkan pihak lain.

## Penamaan

Setiap hasil lahir di subfolder UUID di dalam folder babmu. Pindahkan (`mv`) ke folder babmu dengan nama file dari shot list, lalu `rmdir` subfolder UUID. Cek dimensi dengan `sips -g pixelWidth -g pixelHeight` harus 16:9.

## Laporan

Daftar file final + dimensi + gambar yang gagal QA beserta alasan singkatnya.
