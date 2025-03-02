# File: main.py
import security
import ai_core
import ui

def main():
    interface = ui.Interface()
    interface.show_header()
    
    sec = security.SecurityModule()
    ai = ai_core.AISecurity()
    
    ai.start_ai()
    print("[*] AI Security Engine Aktif")
    
    try:
        while True:
            # Logika utama program
            pass
    except KeyboardInterrupt:
        print("\n\033[93mProgram dimatikan\033[0m")

if __name__ == "__main__":
    main()
