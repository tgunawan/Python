import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class SimpleNotebookApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Notebook")
        self.geometry("750x550")
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

        ttk.Button(toolbar, text="Buat Catatan", command=self.new_note).pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Simpan", command=self.save_note).pack(side="left", padx=6)
        ttk.Button(toolbar, text="Buka", command=self.open_note).pack(side="left", padx=6)
        ttk.Button(toolbar, text="Tentang", command=self.show_about).pack(side="left", padx=6)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        self.tabs = []
        self.current_file = None

        self.add_new_tab("Catatan 1")

    def add_new_tab(self, title):
        frame = ttk.Frame(self.notebook)
        text_widget = tk.Text(frame, wrap="word", font=("Segoe UI", 11), undo=True)
        text_widget.pack(fill="both", expand=True, padx=6, pady=6)
        self.notebook.add(frame, text=title)
        self.tabs.append({"frame": frame, "text": text_widget, "file": None})
        return self.tabs[-1]

    def get_active_tab(self):
        index = self.notebook.index("current")
        return self.tabs[index]

    def new_note(self):
        active_tab = self.get_active_tab()
        if active_tab["text"].get("1.0", tk.END).strip():
            if not messagebox.askyesno("Catatan Baru", "Anda memiliki isi catatan. Buat catatan baru?"):
                return
        active_tab["text"].delete("1.0", tk.END)
        active_tab["file"] = None

    def save_note(self):
        active_tab = self.get_active_tab()
        path = active_tab["file"]
        if not path:
            path = filedialog.asksaveasfilename(
                title="Simpan Catatan",
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("Semua File", "*.*")],
            )
            if not path:
                return
            active_tab["file"] = path
            self.notebook.tab(self.notebook.index("current"), text=path.rsplit("/", 1)[-1])

        try:
            content = active_tab["text"].get("1.0", tk.END)
            with open(path, "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("Sukses", f"Catatan berhasil disimpan: {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan catatan:\n{e}")

    def open_note(self):
        path = filedialog.askopenfilename(
            title="Buka Catatan",
            filetypes=[("Text Files", "*.txt"), ("Semua File", "*.*")],
        )
        if not path:
            return

        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            active_tab = self.get_active_tab()
            active_tab["text"].delete("1.0", tk.END)
            active_tab["text"].insert(tk.END, content)
            active_tab["file"] = path
            self.notebook.tab(self.notebook.index("current"), text=path.rsplit("/", 1)[-1])
            messagebox.showinfo("Sukses", f"Catatan berhasil dibuka: {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuka catatan:\n{e}")

    def show_about(self):
        messagebox.showinfo(
            "Tentang",
            "Simple Notebook\n\nAplikasi catatan sederhana berbasis ttk tkinter."
        )


if __name__ == "__main__":
    app = SimpleNotebookApp()
    app.mainloop()
