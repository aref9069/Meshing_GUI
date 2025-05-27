from abaqus import mdb
import tkinter as tk

class CommandBar(tk.Frame):
    def __init__(self, root, run_callback) -> None:
        super().__init__(root, padx=10, pady=10)

        tk.Label(self, text="Part Name:").grid(row=0, column=0, sticky='e')

        # Get part names from the current model
        model_name = list(mdb.models.keys())[0]  # assumes one model is active
        self.part_names = list(mdb.models[model_name].parts.keys())

        self.selected_part = tk.StringVar()
        self.selected_part.set(self.part_names[0])  # default

        self.partMenu = tk.OptionMenu(self, self.selected_part, *self.part_names)
        self.partMenu.config(width=30)
        self.partMenu.grid(row=0, column=1, padx=5)

        tk.Label(self, text="Scale Factors:").grid(row=1, column=0, sticky='e')
        self.sfEntry = tk.Entry(self, width=30)
        self.sfEntry.insert(0, "2.0, 1.5, 1.0, 0.75, 0.675")
        self.sfEntry.grid(row=1, column=1, padx=5)

        self.runBtn = tk.Button(self, text="Run Mesh Refinement", command=lambda: run_callback(
            self.selected_part.get(), self.sfEntry.get()))
        self.runBtn.grid(row=2, column=0, columnspan=2, pady=10)
