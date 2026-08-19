import tkinter as tk

class AplikasiUtama(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Multi-Halaman Tkinter")
        self.geometry("400x300")

        # Container utama untuk menampung semua frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary untuk menyimpan instance tiap halaman
        self.frames = {}

        # Inisialisasi dan tumpuk semua kelas halaman
        for PageClass in (HalamanUtama, HalamanProfil, HalamanPengaturan):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            
            # Tumpuk semua frame di sel grid (0, 0) yang sama
            frame.grid(row=0, column=0, sticky="nsew")

        # Tampilkan halaman awal
        self.tampilkan_frame("HalamanUtama")

    def tampilkan_frame(self, page_name):
        """Menaikkan frame ke tumpukan paling atas"""
        frame = self.frames[page_name]
        frame.tkraise()


class HalamanUtama(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Halaman Utama", font=("Arial", 14, "bold"))
        label.pack(pady=20)

        btn_profil = tk.Button(
            self, 
            text="Ke Profil", 
            command=lambda: controller.tampilkan_frame("HalamanProfil")
        )
        btn_profil.pack(pady=5)

        btn_setting = tk.Button(
            self, 
            text="Ke Pengaturan", 
            command=lambda: controller.tampilkan_frame("HalamanPengaturan")
        )
        btn_setting.pack(pady=5)


class HalamanProfil(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Halaman Profil Pengguna", font=("Arial", 14, "bold"))
        label.pack(pady=20)

        btn_kembali = tk.Button(
            self, 
            text="Kembali ke Utama", 
            command=lambda: controller.tampilkan_frame("HalamanUtama")
        )
        btn_kembali.pack(pady=5)


class HalamanPengaturan(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Halaman Pengaturan", font=("Arial", 14, "bold"))
        label.pack(pady=20)

        btn_kembali = tk.Button(
            self, 
            text="Kembali ke Utama", 
            command=lambda: controller.tampilkan_frame("HalamanUtama")
        )
        btn_kembali.pack(pady=5)


if __name__ == "__main__":
    app = AplikasiUtama()
    app.mainloop()