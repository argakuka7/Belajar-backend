# Manifest coverage Bab 19: Scaling & Performance (Bagian 2)

Sumber: `public/19.Backend Scaling and Performance Engineering - Part-2/html_notes/notes.html` (12 bagian). Analogi induk: lanjutan restoran ramai. Satu gedung tidak cukup lagi: buka cabang-cabang, tiap cabang punya gudang sendiri, papan pusat mengatur pembagian, dan pesanan berat dikirim ke dapur belakang.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|
| Statelessness: kunci pemicunya | CORE | Cabang baru bisa dibuka asal kasirnya tidak menyimpan ingatan; buku tamu ada di pusat, seperti bab 4. |
| Algoritma load balancer | CORE ringan | Cara resepsionis memilih meja: giliran, terpendek, atau acak. |
| Health check | RINGAN | Cabang yang sakit tidak diberi tamu sampai sehat. |
| Read replica | RINGAN | Buku besar disalinkan ke beberapa meja: yang mau membaca boleh ke salinan mana saja. |
| Sharding & partisi | CORE | Buku besar dipecah per huruf awal: cabang A menjaga tamu A, cabang B menjaga tamu B. |
| Database terdistribusi | NAMED | |
| CDN & kecepatan cahaya | RINGAN | Fotokopi menu diletakkan di setiap kota, tamu membaca yang terdekat. |
| Edge computing | RINGAN | Meja kasir kecil di dekat tamu untuk pesanan yang simple. |
| Pemrosesan asinkron & antrean | RINGAN | Papan tiket dapur dari bab 10. |
| Monolit vs microservice | RINGAN | Satu dapur besar semua juru masak, atau banyak dapur kecil per jenis hidangan. |
| Serverless computing | RINGAN | Sewa juru masak per pesanan, tanpa rawat dapur. |
| Model mental scaling | CORE ringan | Semua pilihan itu adalah jawaban atas satu pertanyaan: bagian mana yang kewalahan dulu? |

Pertanyaan pemahaman dari CORE:
1. Kenapa kasir tanpa ingatan (stateless) membuat membuka cabang jadi mudah?
2. Apa itu memecah buku besar per huruf awal (sharding)?
3. Apa pertanyaan yang dijawab oleh semua strategi scaling?

Ilustrasi (di `public/assets/illustrations/19-scaling2/`):
- `01-cabang.png` utama: tiga gedung restoran kembar berjajar, masing-masing dengan papan kecil yang sama; Kuka di depan gedung tengah.
- `02-sharding.png` pendukung: satu buku besar tebal dipecah jadi dua buku lebih tipis, Kuka memegang satu.
- `03-cdn.png` pendukung: satu lemari pusat dan tiga rak kecil di tiga sudut berbeda, isinya sama, garis putus-putus dari pusat ke tiap rak.
