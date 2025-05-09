import tkinter as tk
import ttkbootstrap as ttk

class AplikasiTabbed(ttk.Window):
    def __init__(self):
        super().__init__(title="Aplikasi Tabbed dengan TTKBootstrap (OOP)", themename="flatly")
        self.geometry("600x400")
        self.resizable(False, False)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)
        self.buat_tab("Tab 1", "Ini adalah konten untuk Tab 1.")
        self.buat_tab("Tab 2", "Konten berbeda untuk Tab 2.")
        self.buat_tab("Tab 3", "Lebih banyak konten di Tab 3.")

    def buat_tab(self, judul, konten_teks):
        tab = ttk.Frame(self.notebook)
        label = ttk.Label(tab, text=konten_teks, padding=20)
        label.pack(fill="both", expand=True)
        self.notebook.add(tab, text=judul)

if __name__ == "__main__":
    app = AplikasiTabbed()
    app.mainloop()