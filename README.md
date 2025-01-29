# Skrip Pengolahan Data Excel

Skrip ini digunakan untuk memproses file Excel yang berisi data dari inverter solar. Skrip ini menghitung total daya DC dari beberapa file Excel dan menyimpan hasilnya dalam file Excel baru.

## Fitur

- Membaca file Excel dari folder yang ditentukan.
- Menghitung total daya DC dari kolom yang relevan.
- Menyimpan hasil harian dan total bulanan ke dalam file Excel baru.
- Menangani kesalahan dan mencatat file yang gagal diproses.

## Prasyarat

Sebelum menjalankan skrip ini, pastikan Anda telah menginstal paket berikut:

- flask==2.3.3
- flask-sqlalchemy==3.0.5
- PyMySQL==1.1.0
- SQLAlchemy==2.0.20
- matplotlib==3.10.0
- numpy==2.2.2
- openpyxl==3.1.5
- pandas==2.2.3
- python-dotenv

## Cara Menjalankan Project:

Buat env
```bash
python3 -m venv env
```
Aktifkan env
```bash
source env/bin/activate
```
Aktifkan env
```bash
source env/bin/activate
```
Install library yang dibutuhkan
```bash
pip install -r requirements.txt
```
Jalankan Program
```bash
python main.py
```