import tkinter as tk
from tkinter import ttk, messagebox
import os

# --- 1. Konsep OOP (Materi 10 & 11) ---
class Produk:
    def __init__(self, nama, stok, harga):
        self.nama = nama
        self.__stok = stok  # Enkapsulasi (Private Attribute)
        self.harga = harga

    def get_stok(self):
        return self.__stok

    def info_produk(self):
        return f"{self.nama} | Stok: {self.__stok} | Harga: Rp{self.harga:,}"

# --- 2. Logika Aplikasi & File Handling (Materi 8 & 9) ---
class WarehouseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Warehouse Manager Pro - GUI Edition")
        self.root.geometry("500x450")
        self.file_name = "gudang_gui.txt"
        self.inventaris = self.muat_dari_file()

        # --- 3. Antarmuka GUI (Materi 12 & 13) ---
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Tab 1: Input Data
        self.tab_input = tk.Frame(self.notebook)
        self.notebook.add(self.tab_input, text="Tambah Barang")
        self.setup_tab_input()

        # Tab 2: Daftar Inventaris
        self.tab_list = tk.Frame(self.notebook)
        self.notebook.add(self.tab_list, text="Lihat Inventaris")
        self.setup_tab_list()

    def setup_tab_input(self):
        # LabelFrame untuk mengelompokkan input (Materi 13)
        self.frame_input = tk.LabelFrame(self.tab_input, text="Formulir Barang Baru", padx=20, pady=20)
        self.frame_input.pack(padx=10, pady=10)

        tk.Label(self.frame_input, text="Nama Barang:").grid(row=0, column=0, sticky="w")
        self.ent_nama = tk.Entry(self.frame_input, width=30)
        self.ent_nama.grid(row=0, column=1, pady=5)

        tk.Label(self.frame_input, text="Jumlah Stok:").grid(row=1, column=0, sticky="w")
        self.ent_stok = tk.Entry(self.frame_input, width=30)
        self.ent_stok.grid(row=1, column=1, pady=5)

        tk.Label(self.frame_input, text="Harga Unit:").grid(row=2, column=0, sticky="w")
        self.ent_harga = tk.Entry(self.frame_input, width=30)
        self.ent_harga.grid(row=2, column=1, pady=5)

        self.btn_tambah = tk.Button(self.frame_input, text="Simpan ke Gudang", 
                                    command=self.tambah_barang, bg="lightgreen")
        self.btn_tambah.grid(row=3, column=0, columnspan=2, pady=15)

    def setup_tab_list(self):
        self.txt_display = tk.Text(self.tab_list, height=15, width=55)
        self.txt_display.pack(pady=10, padx=10)
        
        self.btn_refresh = tk.Button(self.tab_list, text="Refresh Daftar", command=self.tampilkan_daftar)
        self.btn_refresh.pack()

    # --- Fungsi Kontrol ---
    def tambah_barang(self):
        try:
            nama = self.ent_nama.get()
            stok = int(self.ent_stok.get())
            harga = float(self.ent_harga.get())

            if not nama: raise ValueError("Nama tidak boleh kosong")

            baru = Produk(nama, stok, harga)
            self.inventaris.append(baru)
            self.simpan_ke_file()
            
            messagebox.showinfo("Sukses", f"Berhasil menambahkan {nama}")
            self.ent_nama.delete(0, tk.END)
            self.ent_stok.delete(0, tk.END)
            self.ent_harga.delete(0, tk.END)
            self.tampilkan_daftar()

        except ValueError as e:
            messagebox.showerror("Input Error", "Pastikan Stok dan Harga adalah angka!")

    def tampilkan_daftar(self):
        self.txt_display.delete('1.0', tk.END)
        # Sorting dengan Lambda (Materi 5)
        self.inventaris.sort(key=lambda x: x.harga)
        
        if not self.inventaris:
            self.txt_display.insert(tk.END, "Gudang masih kosong.")
            return

        for i, b in enumerate(self.inventaris, 1):
            self.txt_display.insert(tk.END, f"{i}. {b.info_produk()}\n")

    def simpan_ke_file(self):
        with open(self.file_name, "w") as f:
            lines = [f"{b.nama},{b.get_stok()},{b.harga}\n" for b in self.inventaris]
            f.writelines(lines)

    def muat_dari_file(self):
        data_list = []
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        data_list.append(Produk(parts[0], int(parts[1]), float(parts[2])))
        return data_list

if __name__ == "__main__":
    root = tk.Tk()
    app = WarehouseApp(root)
    root.mainloop()