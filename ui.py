# File: ui.py
class Interface:
    def __init__(self):
        self.script_info = {
            "name": "DNSecGuard",
            "version": "2.1",
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
