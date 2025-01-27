# Skrip Pengolahan Data Excel

Skrip ini digunakan untuk memproses file Excel yang berisi data dari inverter solar. Skrip ini menghitung total daya DC dari beberapa file Excel dan menyimpan hasilnya dalam file Excel baru.

## Fitur

- Membaca file Excel dari folder yang ditentukan.
- Menghitung total daya DC dari kolom yang relevan.
- Menyimpan hasil harian dan total bulanan ke dalam file Excel baru.
- Menangani kesalahan dan mencatat file yang gagal diproses.

## Prasyarat

Sebelum menjalankan skrip ini, pastikan Anda telah menginstal paket berikut:

- `blinker` 1.6.2
- `cffi` 1.16.0
- `click` 8.1.7
- `contourpy` 1.3.1
- `cryptography` 41.0.4
- `cycler` 0.12.1
- `et_xmlfile` 2.0.0
- `Flask` 2.3.3
- `Flask-SQLAlchemy` 3.0.5
- `fonttools` 4.55.6
- `greenlet` 2.0.2
- `gunicorn` 21.2.0
- `importlib-metadata` 6.8.0
- `itsdangerous` 2.1.2
- `Jinja2` 3.1.2
- `kiwisolver` 1.4.8
- `MarkupSafe` 2.1.3
- `matplotlib` 3.10.0
- `numpy` 2.2.2
- `openpyxl` 3.1.5
- `packaging` 23.1
- `pandas` 2.2.3
- `pillow` 11.1.0
- `pycparser` 2.21
- `PyMySQL` 1.1.0
- `pyparsing` 3.2.1
- `python-dateutil` 2.9.0.post0
- `pytz` 2024.2
- `setuptools` 59.6.0
- `six` 1.17.0
- `SQLAlchemy` 2.0.20
- `typing_extensions` 4.7.1
- `tzdata` 2025.1
- `Werkzeug` 2.3.7
- `zipp` 3.16.2

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