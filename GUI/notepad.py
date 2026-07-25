import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class SimpleNotepadApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Notepad")
        self.geometry("700x500")
        self.resizable(True, True)

        self._build_ui()

    def _build_ui(self):
        self.configure(bg="#f3f4f6")
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TButton", padding=6, font=("Segoe UI", 10))
        self.style.configure("TLabel", font=("Segoe UI", 10), background="#f3f4f6")

        toolbar = ttk.Frame(self, padding=8)
        toolbar.pack(fill="x")

        ttk.Button(toolbar, text="Buka", command=self.open_file).pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Simpan", command=self.save_file).pack(side="left", padx=6)
        ttk.Button(toolbar, text="Bersihkan", command=self.clear_text).pack(side="left", padx=6)
        ttk.Button(toolbar, text="Tentang", command=self.show_about).pack(side="left", padx=6)

        self.text_area = tk.Text(self, wrap="word", font=("Segoe UI", 11), undo=True)
        self.text_area.pack(fill="both", expand=True, padx=8, pady=(0, 8))

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Buka File",
            filetypes=[("Text Files", "*.txt"), ("Semua File", "*.*")],
        )
        if not file_path:
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, content)
            messagebox.showinfo("Sukses", f"File berhasil dibuka: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuka file:\n{e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            title="Simpan File",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("Semua File", "*.*")],
        )
        if not file_path:
            return

        try:
            content = self.text_area.get("1.0", tk.END)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("Sukses", f"File berhasil disimpan: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan file:\n{e}")

    def clear_text(self):
        if messagebox.askyesno("Bersihkan", "Apakah Anda ingin menghapus isi teks?"):
            self.text_area.delete("1.0", tk.END)

    def show_about(self):
        messagebox.showinfo(
            "Tentang",
            "Simple Notepad\n\nAplikasi catatan sederhana berbasis Tkinter dan ttk."
        )


if __name__ == "__main__":
    app = SimpleNotepadApp()
    app.mainloop()
