import tkinter as tk
from tkinter import scrolledtext

class MainScreen(tk.Frame):
    def __init__(self, root, title="Output Log", width=80, height=20) -> None:
        super().__init__(root, padx=10, pady=10)
        
        # Optional title label
        self.title_label = tk.Label(self, text=title, font=("Helvetica", 12, "bold"))
        self.title_label.pack(anchor='w', pady=(0, 5))

    def log(self, text):
        self.outputBox.insert(tk.END, text + "\n")
        self.outputBox.see(tk.END)

    def clear(self):
        self.outputBox.delete('1.0', tk.END)
