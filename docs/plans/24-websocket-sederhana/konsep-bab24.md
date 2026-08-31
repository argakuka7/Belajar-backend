# Manifest coverage Bab 24: WebSockets & Real-Time Communication

Sumber: `public/24.Web-Sockets-And-Real-time-Communication-with-WebSockets/html_notes/notes.html` (21 bagian). Analogi induk: pelayan yang berdiri di samping meja. Cara lama: tamu mengangkat tangan bertanya "sudah jadi?" berulang-ulang. Cara baru: pelayan tinggal di samping meja, begitu kue mati ia langsung menyodorkan, dan tamu juga bisa berbisik kapan saja tanpa berdiri.

Nama tampilan karakter: Kuka. Kontrak visual: `docs/plans/1-http-sederhana/kontrak-kuka.md`.

| Konsep (bagian teknis) | Perlakuan | Catatan analogi |
|---|---|---|
| Masalah yang dipecahkan WebSocket | CORE | Bertanya "sudah jadi?" sepuluh kali itu melelahkan untuk tamu dan pelayan. |
| Spektrum real-time | RINGAN | Dari menunggu dipanggil, bertanya berkala, sampai pelayan menetap. |
| Apa sebenarnya WebSocket itu | CORE | Pelayan menetap di samping meja: dua arah, kapan saja, tanpa tamu berdiri. |
| Handshake upgrade | CORE ringan | Tamu bertanya sekali: "boleh pelayan menetap?" Pelayan menjawab boleh. |
| Frame: format wire | RINGAN | Bisikan dipecah jadi potongan pendek berurutan. |
| Siklus hidup koneksi | RINGAN | Duduk, mengobrol, pamit: ada awal, isi, dan akhir yang rapi. |
| Ping/pong & heartbeat | RINGAN | Pelayan sesekali bertanya "masih di sini?" dan tamu menjawab. |
| Server WebSocket | RINGAN | Meja khusus untuk pelayan yang menetap; jumlah tamunya dibatasi. |
| Klien WebSocket | RINGAN | Cara tamu memulai duduk bersama pelayan. |
| Manajemen koneksi | RINGAN | Buku daftar tamu yang sedang ditemani pelayan. |
| Broadcast & room | RINGAN | Pengumuman ke seluruh ruangan, atau bisikan ke satu meja saja. |
| Backpressure & consumer lambat | RINGAN | Tamu lambat mencatat: jangan banjir dia dengan bisikan, tahan dulu. |
| Autentikasi | RINGAN | Kartu identitas dicek sebelum pelayan menetap di samping tamu. |
| Keamanan | RINGAN | Bisikan hanya lewat jalur tersegel. |
| Scaling: backplane | NAMED | |
| Load balancing & sticky session | NAMED | |
| Reconnection & ketahanan | RINGAN | Pelayan pergi? Tamu minta pelayan baru, pesanan yang terlewat diantar kemudian. |
| WebSocket vs SSE vs streaming vs polling | RINGAN | Empat cara menunggu kabar, pilih sesuai pesanan. |
| Jebakan umum | RINGAN | Pelayan yang menetap di semua meja sekaligus = pelayan lelah, semua tamu lambat. |
| Mendesain sistem real-time | NAMED | |
| Crib-sheet | DEFERRED | |

Pertanyaan pemahaman dari CORE:
1. Kenapa bertanya "sudah jadi?" berulang itu masalah, dan apa solusinya?
2. Apa yang terjadi saat handshake upgrade?
3. Kenapa pelayan perlu bertanya "masih di sini?" sesekali?

Ilustrasi (di `public/assets/illustrations/24-websocket/`):
- `01-pelayan-menetap.png` utama: pelayan mesin berdiri di samping meja Kuka yang duduk santai; keduanya saling menghadap, garis bisikan dua arah di antara mereka.
- `02-handshake.png` pendukung: Kuka mengulurkan kartu ke pelayan di pintu, pelayan mengangguk menyambut; pintu terbuka lebar.
- `03-broadcast.png` pendukung: satu pelayan di tengah ruangan menyampaikan piring ke empat meja sekaligus lewat garis bercabang.
