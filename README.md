# Belajar Prinsip-Prinsip Backend

Dokumentasi backend engineering dalam bahasa Indonesia, seri 24 bab.

Seri ini membedah topik backend dari fondasinya: bukan sekadar menyebut fungsi tiap bagian, tetapi mengapa ia ada dan bagaimana ia bekerja di bawahnya. Setiap bab berisi penjelasan plus contoh kode **Go** dan **Python** yang ditampilkan berdampingan.

## Daftar Isi (24 Bab)

1. **HTTP & CORS** — protokol fondasi web dan Cross-Origin Resource Sharing
2. **Routing di Backend** — bagaimana request diarahkan ke handler yang tepat
3. **Serialisasi & Deserialisasi** — mengonversi data ke/dari format seperti JSON
4. **Autentikasi & Otorisasi** — mengamankan aplikasi dan mengelola akses pengguna
5. **Validasi & Transformasi** — menjaga integritas dan kebersihan data
6. **Controller, Service & Middleware** — pola arsitektur berlapis dan request context
7. **Desain API (REST)** — praktik terbaik merancang REST API yang intuitif
8. **Database** — konsep inti integrasi database di sistem backend
9. **Caching** — rahasia di balik aplikasi yang sangat cepat (Redis, dll.)
10. **Antrean Tugas & Pekerjaan Latar** — mengelola beban kerja asinkron
11. **Full-Text Search (Elasticsearch)** — pencarian cepat untuk data dalam jumlah besar
12. **Penanganan Error & Toleransi Kegagalan** — membangun sistem yang resilien
13. **gRPC & Komunikasi Antar-Layanan** — protokol komunikasi efisien untuk microservice
14. **Manajemen Konfigurasi** — mengelola environment variable dan konfigurasi dengan aman
15. **Logging & Observabilitas** — menjaga kesehatan sistem dan debugging di produksi
16. **Graceful Shutdown** — menghentikan aplikasi dengan aman tanpa kehilangan data
17. **Keamanan Backend** — SQL injection, XSS, CSRF, dan lainnya
18. **Scaling & Performa (Bagian 1)** — strategi scaling vertikal dan horizontal
19. **Scaling & Performa (Bagian 2)** — teknik scaling lanjutan
20. **Konkurensi & Paralelisme** — tugas IO-bound vs CPU-bound dan cara mengoptimalkannya
21. **Docker, Kubernetes & CI/CD** — mengemas dan mengirim aplikasi secara konsisten
22. **Pengujian Otomatis** — unit, integrasi, dan end-to-end yang efektif
23. **Message Broker & Kafka** — arsitektur berbasis event dan streaming
24. **WebSocket & Real-Time** — fitur real-time menggunakan WebSocket

## Cara Menjalankan Secara Lokal

Situs ini statis murni (HTML/CSS/JS, tanpa build step):

```bash
cd ~/Projects/Backend-from-first-Principle-id
python3 -m http.server 8124
# buka http://127.0.0.1:8124/
```

## Deploy ke Netlify

1. Pindahkan isi situs (index.html + folder bab + assets) ke folder `public/`
2. Tambah `netlify.toml` di root dengan `[build] publish = "public"`
3. Tarik folder `public/` ke Netlify Drop, atau push ke GitHub lalu import dari Netlify

## Struktur Proyek

```
├── index.html              ← landing page
├── 1.HTTP-AND-CORS/ … 24.Web-Sockets.../   ← bab (html_notes/notes.html + kode Go/Python)
├── translations/           ← file terjemahan per bab (JSON)
├── tools/                  ← pipeline terjemahan (extract / apply / verify)
└── assets/                 ← CSS & JS situs
```

## Catatan

- Kode contoh (Go/Python) dibiarkan utuh; hanya teks penjelasan yang diterjemahkan.
- Label diagram/infografis tertentu dibiarkan dalam bahasa aslinya demi menjaga tata letak visual.
