# File: main.py
import security
import ai_core
import ui
import sys

def main():
    interface = ui.Interface()
    interface.show_header()
    
    try:
        sec = security.SecurityModule()
        ai = ai_core.AISecurity()
        
        ai.start_ai()
        print("[*] Memulai operasi keamanan...")
        
        while True:
            command = input("\n[>] Masukkan perintah (encrypt/decrypt/exit): ").strip().lower()
            if command == "encrypt":
                filename = input("[>] Nama file untuk dienkripsi: ").strip()
                sec.encrypt_file(filename)
            elif command == "decrypt":
                filename = input("[>] Nama file untuk didekripsi: ").strip()
                sec.decrypt_file(filename)
            elif command == "exit":
                print("[*] Menutup DNSecGuard...")
                sys.exit(0)
            else:
                print("[!] Perintah tidak valid.")
                
    except KeyboardInterrupt:
        print("\n\033[93m[*] Program dimatikan\033[0m")
    except Exception as e:
        print(f"\n[!] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
