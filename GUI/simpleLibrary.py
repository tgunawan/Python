import tkinter as tk
from tkinter import messagebox, ttk


class Book:
    def __init__(self, title, author, year, status="Tersedia"):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_line(self):
        return f"{self.title}|{self.author}|{self.year}|{self.status}\n"

    @classmethod
    def from_line(cls, line):
        title, author, year, status = line.strip().split("|", 3)
        return cls(title, author, int(year), status)


class LibraryDataManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_books(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                lines = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write("")
            return []

        return [Book.from_line(line) for line in lines]

    def save_books(self, books):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for book in books:
                file.write(book.to_line())


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Perpustakaan Sederhana")
        self.geometry("760x520")
        self.resizable(False, False)

        self.data_manager = LibraryDataManager("library_books.txt")
        self.books = self.data_manager.load_books()

        self._build_ui()
        self.refresh_list()

    def _build_ui(self):
        self.configure(bg="#f3f4f6")
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="#f3f4f6", font=("Segoe UI", 10))
        self.style.configure("Title.TLabel", font=("Segoe UI", 15, "bold"), foreground="#1d4ed8")
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"))
        self.style.configure("TEntry", padding=4)
        self.style.configure("TCombobox", padding=4)

        title_label = ttk.Label(self, text="Daftar Buku Perpustakaan", style="Title.TLabel")
        title_label.pack(pady=(12, 6))

        content_frame = ttk.Frame(self, padding=10)
        content_frame.pack(fill="both", expand=True)

        left_frame = ttk.Frame(content_frame)
        left_frame.grid(row=0, column=0, padx=(0, 10), sticky="nsew")

        ttk.Label(left_frame, text="Daftar Buku").pack(anchor="w", pady=(0, 6))
        self.book_list = tk.Listbox(
            left_frame,
            width=50,
            height=15,
            font=("Segoe UI", 10),
            bg="white",
            activestyle="dotbox",
        )
        self.book_list.pack(fill="both", expand=True)
        self.book_list.bind("<<ListboxSelect>>", self.on_select)

        right_frame = ttk.Frame(content_frame)
        right_frame.grid(row=0, column=1, sticky="nsew")

        ttk.Label(right_frame, text="Tambah / Edit Buku").pack(anchor="w", pady=(0, 6))

        fields_frame = ttk.Frame(right_frame)
        fields_frame.pack(fill="x")

        self.title_var = tk.StringVar()
        self.author_var = tk.StringVar()
        self.year_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Tersedia")

        ttk.Label(fields_frame, text="Judul").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(fields_frame, textvariable=self.title_var, width=30).grid(row=0, column=1, pady=4)

        ttk.Label(fields_frame, text="Penulis").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Entry(fields_frame, textvariable=self.author_var, width=30).grid(row=1, column=1, pady=4)

        ttk.Label(fields_frame, text="Tahun").grid(row=2, column=0, sticky="w", pady=4)
        ttk.Entry(fields_frame, textvariable=self.year_var, width=30).grid(row=2, column=1, pady=4)

        ttk.Label(fields_frame, text="Status").grid(row=3, column=0, sticky="w", pady=4)
        ttk.Combobox(
            fields_frame,
            textvariable=self.status_var,
            values=["Tersedia", "Dipinjam"],
            state="readonly",
            width=27,
        ).grid(row=3, column=1, pady=4)

        button_frame = ttk.Frame(right_frame)
        button_frame.pack(fill="x", pady=(10, 0))

        ttk.Button(button_frame, text="Tambah", command=self.add_book).pack(side="left", padx=(0, 6))
        ttk.Button(button_frame, text="Hapus", command=self.delete_book).pack(side="left", padx=6)
        ttk.Button(button_frame, text="Ubah Status", command=self.toggle_status).pack(side="left", padx=6)
        ttk.Button(button_frame, text="Bersihkan", command=self.clear_form).pack(side="left", padx=6)

        self.info_label = ttk.Label(right_frame, text="", foreground="#0f766e")
        self.info_label.pack(anchor="w", pady=(12, 0))

        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)

    def refresh_list(self):
        self.book_list.delete(0, tk.END)
        for book in self.books:
            display = f"{book.title} | {book.author} | {book.year} | {book.status}"
            self.book_list.insert(tk.END, display)
        self.info_label.config(text=f"Jumlah buku: {len(self.books)}")

    def add_book(self):
        title = self.title_var.get().strip()
        author = self.author_var.get().strip()
        year_text = self.year_var.get().strip()
        status = self.status_var.get().strip()

        if not title or not author or not year_text:
            messagebox.showwarning("Input belum lengkap", "Judul, penulis, dan tahun wajib diisi.")
            return

        try:
            year = int(year_text)
        except ValueError:
            messagebox.showwarning("Input tidak valid", "Tahun harus berupa angka.")
            return

        book = Book(title, author, year, status)
        self.books.append(book)
        self.data_manager.save_books(self.books)
        self.refresh_list()
        self.clear_form()
        messagebox.showinfo("Berhasil", f"Buku '{title}' berhasil ditambahkan.")

    def delete_book(self):
        selected = self.book_list.curselection()
        if not selected:
            messagebox.showwarning("Belum ada buku yang dipilih", "Pilih buku dari daftar terlebih dahulu.")
            return

        index = selected[0]
        removed_book = self.books.pop(index)
        self.data_manager.save_books(self.books)
        self.refresh_list()
        self.clear_form()
        messagebox.showinfo("Berhasil", f"Buku '{removed_book.title}' berhasil dihapus.")

    def toggle_status(self):
        selected = self.book_list.curselection()
        if not selected:
            messagebox.showwarning("Belum ada buku yang dipilih", "Pilih buku dari daftar terlebih dahulu.")
            return

        index = selected[0]
        book = self.books[index]
        book.status = "Dipinjam" if book.status == "Tersedia" else "Tersedia"
        self.data_manager.save_books(self.books)
        self.refresh_list()
        messagebox.showinfo("Berhasil", f"Status buku '{book.title}' diubah menjadi {book.status}.")

    def on_select(self, event):
        selected = self.book_list.curselection()
        if not selected:
            return

        index = selected[0]
        book = self.books[index]
        self.title_var.set(book.title)
        self.author_var.set(book.author)
        self.year_var.set(str(book.year))
        self.status_var.set(book.status)

    def clear_form(self):
        self.title_var.set("")
        self.author_var.set("")
        self.year_var.set("")
        self.status_var.set("Tersedia")
        self.book_list.selection_clear(0, tk.END)


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
