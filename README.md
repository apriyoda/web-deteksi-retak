# Web Deteksi Retak Infrastruktur
Deskripsi Project 
Web Deteksi Retak Infrastruktur merupakan aplikasi berbasis web yang dirancang untuk membantu proses identifikasi keretakan pada infrastruktur melalui analisis citra digital.
Sistem ini memanfaatkan model Convolutional Neural Network (CNN) yang dilatih menggunakan dataset berjumlah ±40.000 citra, terdiri dari gambar infrastruktur dengan kondisi retak dan tidak retak.
Model CNN yang telah dilatih diintegrasikan ke dalam aplikasi web menggunakan framework Flask, 
sehingga pengguna dapat dengan mudah mengunggah gambar infrastruktur dan memperoleh hasil prediksi secara langsung melalui antarmuka web. 
Sistem ini bertujuan untuk mendukung proses inspeksi visual agar menjadi lebih cepat, objektif, dan konsisten dibandingkan dengan pemeriksaan manual.

## Manfaat Sistem
Sistem deteksi retak ini memberikan beberapa manfaat, antara lain:
Membantu proses inspeksi infrastruktur secara otomatis berbasis citra digital.
Mengurangi ketergantungan terhadap inspeksi manual yang memerlukan waktu dan tenaga lebih besar.
Mempercepat proses identifikasi kerusakan awal pada infrastruktur.
Dapat digunakan sebagai alat bantu pendukung pengambilan keputusan dalam pemeliharaan dan perawatan infrastruktur.

## Kelebihan Sistem
Adapun kelebihan dari sistem yang dikembangkan, yaitu:
Menggunakan model Deep Learning (CNN) yang mampu mengenali pola retakan dengan baik.
Berbasis web, sehingga mudah diakses.
Antarmuka sederhana dan mudah digunakan oleh pengguna.
Proses prediksi dilakukan secara real-time setelah gambar diunggah.
Sistem dapat dikembangkan lebih lanjut untuk jenis kerusakan atau dataset yang lebih beragam

## Fitur Utama
- Upload gambar infrastruktur
- Deteksi retak dan tidak retak
- Menampilkan hasil prediksi melalui web

## Teknologi yang Digunakan
- Python
- Flask
- TensorFlow / Keras
- OpenCV
- NumPy

## Library / Dependency
Semua library yang digunakan tercantum pada file:
requirements.txt

## Cara Instalasi
1. Clone repository:
git clone https://github.com/apriyoda/web-deteksi-retak.git

2. Masuk ke folder project:
cd web-deteksi-retak

3. Install dependency:
pip install -r requirements.txt

## Cara Menjalankan Aplikasi
python app.py

Aplikasi akan berjalan di browser melalui:
http://localhost:5000

## Anggota Kelompok
-  Apriyoda Pratama (https://github.com/apriyoda)
-  Sae Al Chaq      (https://github.com/ALCHAQ)
-  Faiq Akhmad      (https://github.com/Fa-svg48)
