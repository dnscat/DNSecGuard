# File: security.py
from cryptography.fernet import Fernet
import os

class SecurityModule:
    def __init__(self):
        self.key = self.load_key()
        self.cipher = Fernet(self.key)
        
    def load_key(self):
        return open("secret.key", "rb").read()
        
    def encrypt_file(self, filename):
        with open(filename, "rb") as f:
            content = f.read()
        encrypted = self.cipher.encrypt(content)
        with open(filename + ".enc", "wb") as f:
            f.write(encrypted)
            
    def decrypt_file(self, filename):
        with open(filename, "rb") as f:
            content = f.read()
        decrypted = self.cipher.decrypt(content)
        with open(filename[:-4], "wb") as f:
            f.write(decrypted)
