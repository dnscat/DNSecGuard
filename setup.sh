# File: setup.sh (diubah)
#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Menginstall dependensi..."
pkg install python -y
pip install cryptography

echo "[*] Membuat kunci enkripsi..."
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())" > secret.key

echo "[*] Membuat direktori kerja..."
mkdir -p /data/data/com.termux/files/home/DNSecGuard  # Nama direktori diubah
