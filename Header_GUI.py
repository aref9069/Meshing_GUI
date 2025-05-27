import tkinter as tk
from tkinter.font import BOLD, Font
from PIL import Image, ImageTk
import sys
from os import path

class Header(tk.Frame):
    def __init__(self, root, width=800, image_path="./", logo_filename="Logo.png", title="Application Title") -> None:
        super().__init__(root, width=width, pady=3, background="gray")

        if getattr(sys, 'frozen', False):
            folder_path = path.dirname(sys.executable)
        else:
            folder_path = path.dirname(path.realpath(__file__))

        # Load logo image
        logo_file = path.join(image_path, logo_filename)
        try:
            self.Logo_Image = Image.open(logo_file)
            self.Logo_Image_TK = ImageTk.PhotoImage(self.Logo_Image)
            self.Header_Label = tk.Label(self, image=self.Logo_Image_TK, background="gray")
        except Exception:
            self.Header_Label = tk.Label(self, text="[Logo]", font=("Arial", 20, "bold"), background="gray")

        self.Header_Label.grid(column=0, row=0, sticky="nw")

        # Title
        self.bold_font = Font(self.master, size=25, weight=BOLD)
        self.Header_Text = tk.Label(self, text=title, font=self.bold_font, background="gray")
        self.Header_Text.grid(column=1, row=0, sticky="w", padx=10)

        # Column configuration
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, minsize=80)
