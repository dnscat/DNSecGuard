# File: ui.py (diubah)
class Interface:
    def __init__(self):
        self.script_info = {
            "name": "DNSecGuard",  # Nama diubah
            "version": "2.0",
            "developer": "Dimas Narendra Sudibyo",
            "team": "dnsCat"
        }
        
    def show_header(self):
        print(f"""
\033[1;31m{self.script_info['name']} v{self.script_info['version']}\033[0m
Developed by {self.script_info['developer']} ({self.script_info['team']})
Hak Cipta © 2024 dnsCat Team
Instagram: @dimas.n.sudibyo
------------------------------------------
""")
