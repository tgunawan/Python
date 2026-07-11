"""
Project Concept / Long Explanation:
Aplikasi ini adalah contoh sederhana proyek GUI Warehouse Inventory menggunakan Python dengan library tkinter ttk.
Konsep yang dipakai adalah kombinasi antara layout form, widget ttk, dan penyimpanan data sementara di memori.

1. Window utama (root)
   - Digunakan sebagai container utama agar semua komponen tampil di satu layar.
   - Title window diubah menjadi "Warehouse Inventory" agar sesuai judul proyek.

2. Ttk widgets
   - ttk.Label digunakan untuk menampilkan judul dan label teks.
   - ttk.Entry digunakan untuk menerima input dari pengguna.
   - ttk.Combobox digunakan untuk memilih kategori barang secara cepat.
   - ttk.Button digunakan untuk menambah, membersihkan, dan menghapus data.
   - ttk.Treeview digunakan untuk menampilkan daftar barang dalam bentuk tabel.

3. Layout management
   - Metode grid() dipakai agar form dan tabel tersusun rapi.
   - Frame kiri digunakan untuk form input, sementara frame kanan digunakan untuk daftar stok.

4. Event handling
   - Saat tombol Add Item ditekan, program membaca data dari form lalu menyimpan ke list.
   - Saat tombol Clear ditekan, semua field input dikosongkan.
   - Saat tombol Delete Selected ditekan, item yang dipilih di Treeview akan dihapus.

5. Note implementasi
   - Data yang ditambahkan bersifat sementara karena disimpan di variabel Python, bukan database.
   - Program ini cocok dijadikan contoh pembelajaran dasar GUI sebelum lanjut ke database dan CRUD.

Versi yang baru ini dibuat agar tampil lebih mirip desain form warehouse inventory modern,
memiliki form di sisi kiri, tabel di sisi kanan, warna profesional, serta tombol dengan styling yang lebih bagus.
"""

import tkinter as tk
from tkinter import ttk, messagebox


# ===== Variabel global sementara =====
# Data barang disimpan dalam list agar mudah dipahami untuk pembelajaran dasar.
# Di versi lanjutan, list ini bisa diganti dengan database seperti SQLite.
inventory_data = []


# ===== Fungsi bantuan =====
def clear_form():
    """Membersihkan semua field input agar user bisa mengisi data baru."""
    entry_name.delete(0, tk.END)
    combo_category.set("")
    entry_stock.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_supplier.delete(0, tk.END)
    status_var.set("Form has been cleared.")


# ===== Fungsi menambah data =====
def add_item():
    """Mengambil data dari form dan menambahkannya ke tabel inventory."""
    product_name = entry_name.get().strip()
    category = combo_category.get().strip()
    stock = entry_stock.get().strip()
    price = entry_price.get().strip()
    supplier = entry_supplier.get().strip()

    # Note: validasi sederhana agar field tidak kosong.
    if not all([product_name, category, stock, price, supplier]):
        messagebox.showwarning("Warning", "Semua field harus diisi terlebih dahulu.")
        status_var.set("Please complete all input fields.")
        return

    # Note: data disimpan dalam bentuk dictionary agar mudah dibaca.
    item = {
        "name": product_name,
        "category": category,
        "stock": stock,
        "price": price,
        "supplier": supplier,
    }
    inventory_data.append(item)

    # Note: Treeview di-update setiap kali item baru ditambahkan.
    tree.insert("", tk.END, values=(product_name, category, stock, price, supplier))
    status_var.set(f"Added item: {product_name}")
    clear_form()
    messagebox.showinfo("Success", "Data barang berhasil ditambahkan.")


# ===== Fungsi hapus item =====
def delete_selected_item():
    """Menghapus item yang dipilih dari tabel inventory."""
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showwarning("Warning", "Pilih item yang ingin dihapus terlebih dahulu.")
        status_var.set("No item selected for deletion.")
        return

    # Note: item dihapus dari Treeview dan juga dari list data.
    item_values = tree.item(selected_item, "values")
    for item in inventory_data:
        if (
            item["name"] == item_values[0]
            and item["category"] == item_values[1]
            and item["stock"] == item_values[2]
            and item["price"] == item_values[3]
            and item["supplier"] == item_values[4]
        ):
            inventory_data.remove(item)
            break

    tree.delete(selected_item)
    status_var.set("Selected item removed.")
    messagebox.showinfo("Success", "Item berhasil dihapus.")


# ===== Setup window utama =====
root = tk.Tk()
root.title("Warehouse Inventory")
root.geometry("1080x680")
root.configure(bg="#f3f6fb")
root.resizable(False, False)

# Note: theme clam dipilih agar tampilan ttk lebih rapi dan konsisten.
style = ttk.Style(root)
style.theme_use("clam")

# Note: konfigurasi warna dibuat agar UI terlihat lebih profesional.
style.configure("Header.TLabel", font=("Segoe UI", 22, "bold"), foreground="#0f172a", background="#f3f6fb")
style.configure("SubHeader.TLabel", font=("Segoe UI", 10), foreground="#475569", background="#f3f6fb")
style.configure("Field.TLabel", font=("Segoe UI", 10, "bold"), foreground="#334155")
style.configure("TLabelframe", background="#ffffff")
style.configure("TLabelframe.Label", font=("Segoe UI", 10, "bold"), foreground="#111827")
style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), background="#2563eb", foreground="#ffffff")
style.map("Accent.TButton", background=[("active", "#1d4ed8")], foreground=[("active", "#ffffff")])
style.configure("Soft.TButton", font=("Segoe UI", 10, "bold"), background="#f59e0b", foreground="#111827")
style.map("Soft.TButton", background=[("active", "#d97706")], foreground=[("active", "#111827")])
style.configure("Danger.TButton", font=("Segoe UI", 10, "bold"), background="#dc2626", foreground="#ffffff")
style.map("Danger.TButton", background=[("active", "#b91c1c")], foreground=[("active", "#ffffff")])
style.configure("TEntry", fieldbackground="#ffffff")
style.configure("TCombobox", fieldbackground="#ffffff")
style.configure("Treeview", background="#ffffff", foreground="#0f172a", fieldbackground="#ffffff")
style.map("Treeview", background=[("selected", "#bfdbfe")], foreground=[("selected", "#0f172a")])

# ===== Judul utama =====
header_frame = ttk.Frame(root, padding=(20, 18, 20, 6))
header_frame.pack(fill="x")
header = ttk.Label(header_frame, text="Warehouse Inventory", style="Header.TLabel")
header.pack(anchor="w")
sub_header = ttk.Label(header_frame, text="Professional inventory management form and stock list", style="SubHeader.TLabel")
sub_header.pack(anchor="w", pady=(2, 0))

# ===== Frame pembungkus =====
main_frame = ttk.Frame(root, padding=(20, 10, 20, 20))
main_frame.pack(fill="both", expand=True)

# ===== Frame kiri untuk form input =====
left_frame = ttk.LabelFrame(main_frame, text="Item Form", padding=16)
left_frame.grid(row=0, column=0, padx=(0, 12), pady=8, sticky="nsew")

# Note: label dan entry dibuat satu per satu agar mudah dipelajari.
field_name = ttk.Label(left_frame, text="Product Name", style="Field.TLabel")
field_name.grid(row=0, column=0, sticky="w", pady=(0, 5))
entry_name = ttk.Entry(left_frame, width=34)
entry_name.grid(row=1, column=0, pady=(0, 10), sticky="ew")

field_category = ttk.Label(left_frame, text="Category", style="Field.TLabel")
field_category.grid(row=2, column=0, sticky="w", pady=(0, 5))
combo_category = ttk.Combobox(left_frame, values=["Electronics", "Stationery", "Furniture", "Food"], width=31, state="readonly")
combo_category.grid(row=3, column=0, pady=(0, 10), sticky="ew")

field_stock = ttk.Label(left_frame, text="Stock", style="Field.TLabel")
field_stock.grid(row=4, column=0, sticky="w", pady=(0, 5))
entry_stock = ttk.Entry(left_frame, width=34)
entry_stock.grid(row=5, column=0, pady=(0, 10), sticky="ew")

field_price = ttk.Label(left_frame, text="Price", style="Field.TLabel")
field_price.grid(row=6, column=0, sticky="w", pady=(0, 5))
entry_price = ttk.Entry(left_frame, width=34)
entry_price.grid(row=7, column=0, pady=(0, 10), sticky="ew")

field_supplier = ttk.Label(left_frame, text="Supplier", style="Field.TLabel")
field_supplier.grid(row=8, column=0, sticky="w", pady=(0, 5))
entry_supplier = ttk.Entry(left_frame, width=34)
entry_supplier.grid(row=9, column=0, pady=(0, 12), sticky="ew")

# ===== Tombol aksi =====
button_add = ttk.Button(left_frame, text="Add Item", style="Accent.TButton", command=add_item)
button_add.grid(row=10, column=0, pady=(0, 8), sticky="ew")

button_clear = ttk.Button(left_frame, text="Clear Form", style="Soft.TButton", command=clear_form)
button_clear.grid(row=11, column=0, pady=(0, 8), sticky="ew")

button_delete = ttk.Button(left_frame, text="Delete Selected", style="Danger.TButton", command=delete_selected_item)
button_delete.grid(row=12, column=0, sticky="ew")

# ===== Frame kanan untuk daftar tabel =====
right_frame = ttk.LabelFrame(main_frame, text="Inventory List", padding=12)
right_frame.grid(row=0, column=1, padx=(0, 0), pady=8, sticky="nsew")

# Note: Treeview ditentukan kolomnya agar data tampil seperti tabel.
tree = ttk.Treeview(right_frame, columns=("Product", "Category", "Stock", "Price", "Supplier"), show="headings", height=18)

# Note: heading untuk judul tabel agar mudah dibaca.
tree.heading("Product", text="Product")
tree.heading("Category", text="Category")
tree.heading("Stock", text="Stock")
tree.heading("Price", text="Price")
tree.heading("Supplier", text="Supplier")

tree.column("Product", width=170, anchor="center")
tree.column("Category", width=130, anchor="center")
tree.column("Stock", width=100, anchor="center")
tree.column("Price", width=105, anchor="center")
tree.column("Supplier", width=155, anchor="center")

tree.pack(fill="both", expand=True)

# ===== Status bar =====
status_var = tk.StringVar(value="Ready to manage inventory.")
status_label = ttk.Label(root, textvariable=status_var, font=("Segoe UI", 9), foreground="#475569")
status_label.pack(anchor="w", padx=20, pady=(0, 12))

# ===== Data contoh untuk memperlihatkan tampilan tabel =====
# Note: data dummy dibuat agar user langsung melihat struktur tabel ketika program pertama kali dijalankan.
initial_items = [
    ("Laptop", "Electronics", "12", "$780", "TechSupply"),
    ("Notebook", "Stationery", "45", "$4", "OfficeHub"),
    ("Desk Chair", "Furniture", "8", "$120", "ComfortCo"),
    ("Rice Pack", "Food", "25", "$18", "FreshMarket"),
]

for item in initial_items:
    inventory_data.append(
        {
            "name": item[0],
            "category": item[1],
            "stock": item[2],
            "price": item[3],
            "supplier": item[4],
        }
    )
    tree.insert("", tk.END, values=item)

# ===== Pengaturan agar layout responsif =====
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=2)
main_frame.rowconfigure(0, weight=1)
left_frame.columnconfigure(0, weight=1)
right_frame.columnconfigure(0, weight=1)

# ===== Jalankan aplikasi =====
root.mainloop()
