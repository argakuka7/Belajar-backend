# Manifest coverage Bab 21: Containerization, Docker, Kubernetes & CI/CD

Sumber: `public/21.Containerization-and-Deployment-Docker-Kubernetes-and-CICD/html_notes/notes.html` (21 bagian). Analogi induk: kit dapur portable. Membuka cabang baru dulu berarti mengirim tukang, membeli peralatan, menebak kompor cabang cocok dengan resep. Sekarang: seluruh dapur dikirim dalam satu peti siap pakai, kompor apa pun hasilnya sama. Petugas pusat (Kubernetes) yang mengawasi berapa peti berjalan dan mengganti peti yang rusak.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|
| Masalah yang dipecahkan container | CORE | "Di dapur lamaku resepnya jadi!" Hilang: resep dan kompor dikirim bersama dalam satu peti. |
| Container vs mesin virtual | RINGAN | Peti berisi dapur mini vs membangun gedung baru utuh. |
| Apa sebenarnya container itu | CORE ringan | Peti tertutup berisi resep, alat, dan bahan kering. Jalan di kompor mana saja. |
| Image, layer & union filesystem | RINGAN | Peti disusun dari tumpukan kotak standar, kotak dasar dipakai bersama. |
| Dockerfile | RINGAN | Resep merakit peti: masukkan apa saja, urutannya bagaimana. |
| Multi-stage build | RINGAN | Dapur perakitan berantakan boleh kotor; peti akhir hanya berisi hasil bersihnya. |
| Optimasi image & layer caching | RINGAN | Kotak yang jarang berubah disusun di bawah, kotak yang sering di atas. |
| Runtime, registry & tag | NAMED | |
| Networking & volume | RINGAN | Peti butuh jendela pesanan dan laci bahan segar di luar peti. |
| Docker Compose | RINGAN | Satu lembar daftar: peti dapur + peti gudang + peti kasa, jalankan semuanya sekaligus. |
| Kenapa orkestrasi | CORE | Lima puluh peti tidak bisa diawasi tangan. Butuh manajer pusat. |
| Arsitektur Kubernetes | RINGAN | Manajer pusat dengan buku keinginan: beginilah kondisi dapur yang harus dijaga. |
| Pod | RINGAN | Satu unit kerja terkecil: satu atau dua peti yang selalu bersama. |
| Deployment & ReplicaSet | CORE | "Saya mau 5 peti identik jalan terus." Manajer menuruti dan mengganti yang mati. |
| Service & Ingress | RINGAN | Papan nama cabang dan pintu tamu: tamu tak perlu tahu peti mana yang melayani. |
| Config, secret & environment | RINGAN | Catatan lokasi dan kunci kas dari bab 14, kini diberikan ke peti saat mulai bekerja. |
| Health probe & resource | RINGAN | Manajer mencicipi tiap peti dan membatasi listriknya. |
| Scaling & rollout | CORE | Tamu ramai? Tambah peti. Resep baru? Ganti peti satu per satu tanpa tutup cabang. |
| Pipeline CI/CD | CORE | Dari resep berubah ke peti terkirim: otomatis, tanpa diangkut tangan. |
| Strategi deployment & GitOps | RINGAN | Ganti-semua, sedikit-demi-sedikit, atau coba dulu ke sebagian kecil tamu. |
| Crib-sheet produksi | DEFERRED | |

Pertanyaan pemahaman dari CORE:
1. Apa yang diselesaikan peti (container) soal "di dapur lamaku jadi"?
2. Apa tugas manajer pusat (Kubernetes) terhadap lima puluh peti?
3. Apa yang dikerjakan pipeline CI/CD setelah resep berubah?

Ilustrasi (di `public/assets/illustrations/21-container/`):
- `01-peti.png` utama: Kuka berdiri di samping satu peti besar tertutup bergambar kompor dan panci, siap dikirim; tumpukan peti serupa di belakangnya.
- `02-manajer.png` pendukung: mesin manajer berkepala satu berdiri di atas panggung mengawasi lima peti identik yang tersusun rapi.
- `03-pipeline.png` pendukung: tiga meja berjajar: meja resep, meja rakit peti, meja kirim; peti bergerak melewatinya lewat konveyor.
