"""
=====================================================================
 WAREHOUSE INVENTORY APP - Contoh Aplikasi GUI dengan Tkinter + ttk
=====================================================================

Penjelasan Project:
--------------------
Aplikasi ini adalah CONTOH tampilan (mockup) untuk sistem manajemen
gudang (warehouse). Tujuannya untuk menunjukkan bagaimana kita bisa
membuat GUI desktop yang terlihat modern menggunakan Python bawaan
(tkinter) tanpa perlu install library tambahan.

Konsep yang dipakai:
1. ttk (themed tkinter) -> versi tkinter yang lebih modern, dipakai
   untuk widget seperti Notebook (tab), Treeview (tabel), Button, dll.
2. ttk.Style -> dipakai untuk mengatur warna/tema agar mirip tampilan
   dark mode seperti pada gambar referensi.
3. Sidebar (menu kiri) -> dibuat dengan Frame + Label yang disusun
   vertikal, berfungsi seperti navigasi menu.
4. Notebook (tab) -> untuk tab "Inventory", "Products", "Suppliers",
   "Reports" di bagian atas.
5. Treeview -> dipakai untuk membuat tabel "Current Stock" dan
   "Incoming Shipments", karena Treeview mendukung kolom & baris data.
6. Search bar -> Entry (kotak input teks) untuk mencari item.

Struktur file (dari atas ke bawah):
- Konfigurasi window utama & warna tema
- Sidebar (menu navigasi kiri)
- Header (judul "Warehouse Inventory")
- Notebook / Tab menu (Inventory, Products, Suppliers, Reports)
- Search bar
- Tabel Current Stock
- Tabel Incoming Shipments
- Tombol aksi (Simpan / Batal)

Catatan: Data pada tabel di bawah ini hanya data contoh (dummy data),
belum terhubung ke database asli. Jika mau dipakai untuk project nyata,
data ini bisa diganti dengan hasil query dari database (misal SQLite).
=====================================================================
"""

import tkinter as tk
from tkinter import ttk

# ---------------------------------------------------------------
# 1. KONFIGURASI WARNA (supaya tampilannya mirip dark theme di gambar)
# ---------------------------------------------------------------
BG_DARK = "#1e2430"       # warna background utama (gelap)
BG_SIDEBAR = "#161b26"    # warna background sidebar (lebih gelap)
BG_CARD = "#2a3242"       # warna background "kartu" / panel
ACCENT_BLUE = "#3b82f6"   # warna biru untuk tombol / tab aktif
TEXT_LIGHT = "#e5e7eb"    # warna teks terang
TEXT_MUTED = "#9ca3af"    # warna teks abu-abu (kurang menonjol)


class WarehouseInventoryApp(tk.Tk):
    """
    Class utama aplikasi. Semua tampilan (sidebar, tab, tabel, dll)
    dibuat di dalam class ini agar rapi dan mudah dikembangkan.
    """

    def __init__(self):
        super().__init__()

        # --- Pengaturan dasar window ---
        self.title("Warehouse Inventory")
        self.geometry("1200x750")
        self.configure(bg=BG_DARK)

        # Siapkan style ttk sebelum membuat widget lain
        self._setup_style()

        # Susun tampilan: sidebar di kiri, konten utama di kanan
        self._build_sidebar()
        self._build_main_content()

    # -----------------------------------------------------------
    # PENGATURAN STYLE (tema warna untuk widget ttk)
    # -----------------------------------------------------------
    def _setup_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")  # tema dasar yang gampang di-custom

        # Style untuk Notebook (tab)
        style.configure("TNotebook", background=BG_DARK, borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            background=BG_CARD,
            foreground=TEXT_LIGHT,
            padding=(20, 10),
            font=("Segoe UI", 10, "bold"),
        )
        print(f"DEBUG: Current theme is {style.theme_use()}")
        print(ttk.Style().lookup("TNotebook", "font"))
        style.map(
            "TNotebook.Tab",
            background=[("selected", ACCENT_BLUE)],
            foreground=[("selected", "white")],
        )

        # Style untuk Treeview (tabel)
        style.configure(
            "Treeview",
            background=BG_CARD,
            fieldbackground=BG_CARD,
            foreground=TEXT_LIGHT,
            rowheight=28,
            borderwidth=0,
        )
        style.configure(
            "Treeview.Heading",
            background=BG_DARK,
            foreground=TEXT_LIGHT,
            font=("Segoe UI", 10, "bold"),
        )
        style.map("Treeview", background=[("selected", ACCENT_BLUE)])

        # Style untuk tombol biru (aksi utama)
        style.configure(
            "Accent.TButton",
            background=ACCENT_BLUE,
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=8,
        )
        style.map("Accent.TButton", background=[("active", "#2563eb")])

        # Style untuk tombol netral (aksi sekunder / batal)
        style.configure(
            "Muted.TButton",
            background=BG_CARD,
            foreground=TEXT_LIGHT,
            padding=8,
        )

    # -----------------------------------------------------------
    # SIDEBAR (menu navigasi di sebelah kiri)
    # -----------------------------------------------------------
    def _build_sidebar(self):
        sidebar = tk.Frame(self, bg=BG_SIDEBAR, width=200)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)  # supaya lebar sidebar tetap 200px

        # Judul kecil di atas sidebar
        tk.Label(
            sidebar, text="🐍  LabelFrame", bg=BG_SIDEBAR, fg=TEXT_LIGHT,
            font=("Segoe UI", 12, "bold"), anchor="w"
        ).pack(fill="x", padx=15, pady=(15, 25))

        # Daftar menu di sidebar. Nama menu di sini sudah dibuat
        # bermakna (bukan teks acak seperti pada gambar referensi),
        # supaya sesuai konteks aplikasi Warehouse Inventory.
        menu_items = [
            ("📦", "Inventory"),
            ("🧾", "Products"),
            ("🚚", "Suppliers"),
            ("📊", "Reports"),
            ("📍", "Locations"),
            ("👤", "Users"),
        ]

        for icon, name in menu_items:
            self._add_sidebar_item(sidebar, icon, name)

    def _add_sidebar_item(self, parent, icon, text):
        """Membuat satu baris menu di sidebar (icon + teks)."""
        row = tk.Frame(parent, bg=BG_SIDEBAR)
        row.pack(fill="x", padx=10, pady=6)

        tk.Label(
            row, text=f"{icon}  {text}", bg=BG_SIDEBAR, fg=TEXT_MUTED,
            font=("Segoe UI", 11), anchor="w", cursor="hand2"
        ).pack(fill="x", padx=10, pady=6)

    # -----------------------------------------------------------
    # KONTEN UTAMA (header + tab + tabel)
    # -----------------------------------------------------------
    def _build_main_content(self):
        main = tk.Frame(self, bg=BG_DARK)
        main.pack(side="left", fill="both", expand=True)

        # --- Header / Judul halaman ---
        header = tk.Frame(main, bg=BG_DARK)
        header.pack(fill="x", padx=25, pady=20)
        tk.Label(
            header, text="Warehouse Inventory", bg=BG_DARK, fg=TEXT_LIGHT,
            font=("Segoe UI", 22, "bold")
        ).pack(side="left")

        # --- Tab menu: Inventory / Products / Suppliers / Reports ---
        notebook = ttk.Notebook(main)
        notebook.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        tab_inventory = tk.Frame(notebook, bg=BG_DARK)
        tab_products = tk.Frame(notebook, bg=BG_DARK)
        tab_suppliers = tk.Frame(notebook, bg=BG_DARK)
        tab_reports = tk.Frame(notebook, bg=BG_DARK)

        notebook.add(tab_inventory, text="Inventory")
        notebook.add(tab_products, text="Products")
        notebook.add(tab_suppliers, text="Suppliers")
        notebook.add(tab_reports, text="Reports")

        # Isi tab "Inventory" dibuat lengkap dengan data dummy.
        # Tab lain sengaja dikosongkan / diberi placeholder karena hanya untuk contoh GUI.
        self._build_inventory_tab(tab_inventory)

        for tab, label in [
            (tab_products, "Products"),
            (tab_suppliers, "Suppliers"),
            (tab_reports, "Reports"),
        ]:
            tk.Label(
                tab, text=f"Halaman {label} belum dibuat (contoh saja)",
                bg=BG_DARK, fg=TEXT_MUTED, font=("Segoe UI", 11)
            ).pack(pady=40)

    # -----------------------------------------------------------
    # ISI TAB "INVENTORY"
    # -----------------------------------------------------------
    def _build_inventory_tab(self, parent):
        # --- Search bar ---
        search_frame = tk.Frame(parent, bg=BG_CARD)
        search_frame.pack(fill="x", pady=(10, 15))

        search_entry = ttk.Entry(search_frame, font=("Segoe UI", 10))
        search_entry.insert(0, "Cari nama produk...")
        search_entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        ttk.Button(search_frame, text="Filter", style="Muted.TButton").pack(
            side="left", padx=5
        )
        ttk.Button(search_frame, text="Tambah Item", style="Accent.TButton").pack(
            side="right", padx=10
        )

        # --- Tabel 1: Current Stock ---
        tk.Label(
            parent, text="Current Stock", bg=BG_DARK, fg=TEXT_LIGHT,
            font=("Segoe UI", 13, "bold")
        ).pack(anchor="w", pady=(5, 5))

        self.tree_stock = self._create_table(
            parent,
            columns=("item_name", "quantity", "last_updated"),
            headers=("Item Name", "Quantity", "Last Updated Date"),
        )

        # Data contoh (dummy) untuk tabel Current Stock
        stock_data = [
            ("Kabel USB Type-C", 2300, "2025-01-10"),
            ("Mouse Wireless", 4300, "2025-01-11"),
            ("Keyboard Mekanik", 2500, "2025-01-09"),
            ("Charger 65W", 1000, "2025-01-08"),
            ("Casing Laptop", 2000, "2025-01-12"),
            ("Speaker Bluetooth", 2500, "2025-01-07"),
        ]
        for row in stock_data:
            self.tree_stock.insert("", "end", values=row)

        # --- Tabel 2: Incoming Shipments ---
        tk.Label(
            parent, text="Incoming Shipments", bg=BG_DARK, fg=TEXT_LIGHT,
            font=("Segoe UI", 13, "bold")
        ).pack(anchor="w", pady=(15, 5))

        self.tree_shipment = self._create_table(
            parent,
            columns=("item_name", "quantity", "last_updated"),
            headers=("Item Name", "Quantity", "Last Updated Date"),
        )

        # Data contoh (dummy) untuk tabel Incoming Shipments
        shipment_data = [
            ("Unit Server Rack", 23000, "2025-01-10"),
            ("Unit Server Rack", 122000, "2025-01-15"),
            ("Modul RAM Corsair", 34000, "2025-01-14"),
            ("Modul RAM Kingston", 99000, "2025-01-16"),
            ("Kabel Fiber Optik", 152000, "2025-01-17"),
            ("Router Cisco", 222000, "2025-01-18"),
        ]
        for row in shipment_data:
            self.tree_shipment.insert("", "end", values=row)

        # --- Tombol aksi bawah (Simpan / Batal) ---
        button_frame = tk.Frame(parent, bg=BG_DARK)
        button_frame.pack(fill="x", pady=15)

        ttk.Button(button_frame, text="Batal", style="Muted.TButton").pack(
            side="right", padx=(0, 10)
        )
        ttk.Button(button_frame, text="Simpan", style="Accent.TButton").pack(
            side="right"
        )

    # -----------------------------------------------------------
    # FUNGSI BANTUAN: membuat tabel (Treeview) dengan scrollbar
    # -----------------------------------------------------------
    def _create_table(self, parent, columns, headers):
        """
        Membuat satu tabel Treeview lengkap dengan scrollbar vertikal.
        columns -> id kolom (dipakai internal)
        headers -> teks judul kolom yang tampil ke user
        """
        table_frame = tk.Frame(parent, bg=BG_CARD)
        table_frame.pack(fill="both", expand=True, pady=(0, 5))

        tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=6
        )

        for col_id, header_text in zip(columns, headers):
            tree.heading(col_id, text=header_text)
            tree.column(col_id, anchor="w", width=200)

        # Scrollbar vertikal di sisi kanan tabel
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=tree.yview
        )
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return tree


# ---------------------------------------------------------------
# JALANKAN APLIKASI
# ---------------------------------------------------------------
if __name__ == "__main__":
    app = WarehouseInventoryApp()
    app.mainloop()