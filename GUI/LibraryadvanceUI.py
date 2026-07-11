import tkinter as tk
from tkinter import ttk, messagebox
import os

# --- 1. Konsep OOP (Materi 10, 11) ---
class ItemPerpustakaan:
    def __init__(self, judul, kategori, stok):
        self.judul = judul
        self.kategori = kategori
        self.__stok = stok  # Enkapsulasi: Private Attribute

    def get_stok(self):
        return self.__stok

# Class turunan (Inheritance)
class Buku(ItemPerpustakaan):
    def __init__(self, judul, kategori, stok, harga):
        super().__init__(judul, kategori, stok)
        self.harga = harga

    def info_singkat(self):
        return f"[{self.kategori}] {self.judul} - Stok: {self.get_stok()} - Rp{self.harga:,}"

# --- 2. Aplikasi Utama dengan Tkinter (Materi 12, 13) ---
class BeeLibApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BeeLib - Sistem Manajemen Perpustakaan")
        self.root.geometry("500x500")
        self.file_name = "perpustakaan.txt"
        self.koleksi_buku = self.muat_data()

        # Pembuatan Notebook/Tab (Materi 13)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill="both")

        self.tab_tambah = tk.Frame(self.notebook)
        self.tab_daftar = tk.Frame(self.notebook)

        self.notebook.add(self.tab_tambah, text="Tambah Buku")
        self.notebook.add(self.tab_daftar, text="Daftar Koleksi")

        self.setup_ui_tambah()
        self.setup_ui_daftar()

    def setup_ui_tambah(self):
        # LabelFrame (Materi 13)
        frame = tk.LabelFrame(self.tab_tambah, text="Input Data Buku Baru", padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        # Grid Layout (Materi 12)
        tk.Label(frame, text="Judul:").grid(row=0, column=0, sticky="w")
        self.ent_judul = tk.Entry(frame, width=30)
        self.ent_judul.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Kategori:").grid(row=1, column=0, sticky="w")
        self.ent_kategori = tk.Entry(frame, width=30)
        self.ent_kategori.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Stok:").grid(row=2, column=0, sticky="w")
        self.ent_stok = tk.Entry(frame, width=30)
        self.ent_stok.grid(row=2, column=1, pady=5)

        tk.Label(frame, text="Harga:").grid(row=3, column=0, sticky="w")
        self.ent_harga = tk.Entry(frame, width=30)
        self.ent_harga.grid(row=3, column=1, pady=5)

        tk.Button(frame, text="Simpan Data", command=self.simpan_buku, bg="orange").grid(row=4, columnspan=2, pady=10)

    def setup_ui_daftar(self):
        self.listbox = tk.Text(self.tab_daftar, height=15, width=55)
        self.listbox.pack(pady=10, padx=10)
        
        btn_refresh = tk.Button(self.tab_daftar, text="Refresh & Sortir Harga", command=self.tampilkan_data)
        btn_refresh.pack()

    # --- 3. Logika & Error Handling (Materi 6, 7, 8, 9) ---
    def simpan_buku(self):
        try:
            # Validasi Input
            judul = self.ent_judul.get()
            kat = self.ent_kategori.get()
            stok = int(self.ent_stok.get())
            harga = float(self.ent_harga.get())

            if not judul or not kat:
                raise ValueError("Judul dan Kategori tidak boleh kosong!")

            baru = Buku(judul, kat, stok, harga)
            self.koleksi_buku.append(baru)

            # File Handling: Menulis (Materi 9)
            with open(self.file_name, "a") as f:
                data = [judul, kat, str(stok), str(harga)]
                f.write(",".join(data) + "\n")

            messagebox.showinfo("Sukses", f"Buku '{judul}' berhasil disimpan!")
            self.bersihkan_form()
            
        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")

    def muat_data(self):
        temp_list = []
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                for baris in f.readlines():
                    # Split String (Materi 9)
                    d = baris.strip().split(",")
                    if len(d) == 4:
                        temp_list.append(Buku(d[0], d[1], int(d[2]), float(d[3])))
        return temp_list

    def tampilkan_data(self):
        self.listbox.delete('1.0', tk.END)
        # Sorting dengan Lambda (Materi 5)
        self.koleksi_buku.sort(key=lambda x: x.harga)
        
        for i, b in enumerate(self.koleksi_buku, 1):
            self.listbox.insert(tk.END, f"{i}. {b.info_singkat()}\n")

    def bersihkan_form(self):
        self.ent_judul.delete(0, tk.END)
        self.ent_kategori.delete(0, tk.END)
        self.ent_stok.delete(0, tk.END)
        self.ent_harga.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BeeLibApp(root)
    root.mainloop()