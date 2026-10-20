# DevSecOps P5 - Flask Calculator App

## 1. Nama Aplikasi & Fungsinya
Aplikasi ini bernama **Flask Calculator App**. Fungsinya adalah menyediakan API sederhana untuk melakukan operasi matematika (penjumlahan) serta mensimulasikan koneksi backend.

## 2. Bahasa/Framework yang Digunakan
- **Bahasa:** Python 3.10
- **Framework:** Flask
- **Testing:** Pytest
- **SAST Tool:** Bandit

## 3. Cara Menjalankan Aplikasi
1. Clone repository ini.
2. Buat virtual environment (opsional): `python -m venv venv` dan aktifkan.
3. Install dependencies: `pip install -r requirements.txt`
4. Jalankan aplikasi: `python app.py`
5. Akses melalui browser di `http://localhost:5000`

## 4. Overview Pipeline CI/CD
Pipeline ini dijalankan menggunakan GitHub Actions. Terdiri dari 2 job utama:
- **Build:** Melakukan setup environment Python, menginstal dependencies, dan menjalankan unit test dengan `pytest`.
- **SAST Scan:** Bergantung (`needs`) pada job build. Job ini menggunakan **Bandit** untuk memindai source code Python dan mencari celah keamanan (seperti hardcoded credentials).