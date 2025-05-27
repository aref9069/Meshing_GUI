""""
Abaqus script for displaying the mesh refinement after getting all the results

Aref Aasi, May 2025

"""
from Header_GUI import Header
from MainScreen_GUI import MainScreen
from CommandBar_GUI import CommandBar
import tkinter as tk
from tkinter import messagebox

class GeneralApp:
    def __init__(self, root, title="General Application", header_image_path="./", header_logo="Logo.png", header_title="App Title"):
        root.title(title)

        # Header
        self.header = Header(root, width=800, image_path=header_image_path, logo_filename=header_logo, title=header_title)
        self.header.pack(fill=tk.X)

        # Main Frame
        self.mainFrame = tk.Frame(root)
        self.mainFrame.pack(fill=tk.BOTH, expand=True)

        # Output Log Screen
        self.screen = MainScreen(self.mainFrame, title="Output Log")
        self.screen.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Command Bar
        self.command = CommandBar(self.mainFrame, run_callback=self.run_callback)
        self.command.pack(side=tk.TOP, fill=tk.X)

    def run_callback(self, input1, input2):
        """ Replace this with custom logic for your application. """
        try:
            inputs = [float(s.strip()) for s in input2.split(',') if s.strip()]
        except ValueError:
            messagebox.showerror("Invalid Input", "Input2 must be numbers separated by commas.")
            return

        self.screen.clear()
        self.screen.log(f"Running task for: {input1}")
        self.screen.log(f"Processed values: {inputs}")
        for val in inputs:
            self.screen.log(f"Processing value {val} ... [mock result]")

# Entry point
if __name__ == '__main__':
    root = tk.Tk()
    app = GeneralApp(
        root,
        title="Custom App GUI",
        header_image_path="./assets",
        header_logo="logo.png",
        header_title="My Analysis Tool"
    )
    root.mainloop()
