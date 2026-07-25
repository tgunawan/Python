import tkinter as tk
from tkinter import messagebox, ttk

window = tk.Tk()
window.title("Aplikasi Perpustakaan Sederhana")
window.geometry("760x520")

judul = tk.Label(window,text="Perpustakaan Mandiri",)
judul.pack()

buku=tk.Entry()

window.mainloop()

