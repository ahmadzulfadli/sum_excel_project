# Sum Data Excel Project

Skrip ini digunakan untuk memproses file Excel yang berisi data dan menghasilkan output dalam bentuk file Excel baru serta grafik.

Berikut adalah link website: https://excel.ahmadzulfadli.online

## Fitur

- Menghitung total kolom yang relevan.
- Menyimpan hasil setiap file dan total akumulasi seluruh file ke dalam file Excel baru.
- Menangani kesalahan dan mencatat file yang gagal diproses.
- Memberikan hasil file Excel (`.xlsx`) dan grafik (`.png`) yang dapat diunduh.

## Kebutuhan

Sebelum menjalankan skrip ini, pastikan Anda telah menginstal paket berikut:

```
flask==2.3.3
flask-sqlalchemy==3.0.5
PyMySQL==1.1.0
SQLAlchemy==2.0.20
matplotlib==3.10.0
numpy==2.2.2
openpyxl==3.1.5
pandas==2.2.3
cryptography
python-dotenv
sympy
```

## Cara Menjalankan Project:

### **1. Menjalankan dengan Flask**
#### **Buat Virtual Environment**
```bash
python3 -m venv env
```
#### **Aktifkan Virtual Environment**
**Linux/macOS:**
```bash
source env/bin/activate
```
**Windows (Command Prompt):**
```bash
env\Scripts\activate
```
**Windows (PowerShell):**
```powershell
env\Scripts\Activate.ps1
```

#### **Install Library yang Dibutuhkan**
```bash
pip install -r requirements.txt
```

#### **Jalankan Program**
```bash
flask run
```

---

### **2. Menjalankan dengan Docker-Compose**
Pastikan konfigurasi **Dockerfile** dan **docker-compose.yml** sudah benar sebelum menjalankan.

#### **Jalankan Docker Compose**
```bash
docker compose up -d
```
#### **Pastikan Container Berjalan**
```bash
docker ps
```
#### **Menghentikan dan Menghapus Container, Image, serta Network**
```bash
docker compose down --rmi all
```