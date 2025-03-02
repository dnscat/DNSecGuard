# File: security.py
from cryptography.fernet import Fernet
import os

class SecurityModule:
    def __init__(self):
        self.key = self.load_key()
        self.cipher = Fernet(self.key)
        
    def load_key(self):
        try:
            with open("secret.key", "rb") as key_file:
                return key_file.read()
        except FileNotFoundError:
            print("[!] Kunci enkripsi tidak ditemukan. Membuat kunci baru...")
            self.generate_key()
            return self.load_key()

    def generate_key(self):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("[*] Kunci enkripsi berhasil dibuat.")

    def encrypt_file(self, filename):
        try:
            with open(filename, "rb") as f:
                content = f.read()
            encrypted = self.cipher.encrypt(content)
            with open(filename + ".enc", "wb") as f:
                f.write(encrypted)
            print(f"[+] File '{filename}' berhasil dienkripsi.")
        except Exception as e:
            print(f"[!] Gagal mengenkripsi file: {e}")

    def decrypt_file(self, filename):
        try:
            with open(filename, "rb") as f:
                content = f.read()
            decrypted = self.cipher.decrypt(content)
            with open(filename[:-4], "wb") as f:
                f.write(decrypted)
            print(f"[+] File '{filename}' berhasil didekripsi.")
        except Exception as e:
            print(f"[!] Gagal mendekripsi file: {e}")
