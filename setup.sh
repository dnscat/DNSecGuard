#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Mengupdate paket sistem..."
pkg update -y && pkg upgrade -y

echo "[*] Menginstall dependensi sistem..."
pkg install python build-essential libffi libffi-dev openssl openssl-dev -y

echo "[*] Mengupgrade pip dan setuptools..."
pip install --upgrade pip setuptools wheel

echo "[*] Menginstall dependensi Python..."
pip install --no-cache-dir -r requirements.txt

echo "[*] Membuat direktori kerja..."
mkdir -p /data/data/com.termux/files/home/DNSecGuard

echo "[*] Setup selesai. Jalankan program dengan 'python main.py'"
