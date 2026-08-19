import tkinter as tk

class AplikasiSaya(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contoh Tkinter OOP")
        self.geometry("300x180")

        # Atribut data / State
        self.counter = 0

        # Widget GUI
        self.label = tk.Label(self, text="Klik tombol di bawah!", font=("Arial", 11))
        self.label.pack(pady=20)

        self.tombol = tk.Button(self, text="Klik Saya", command=self.tambah_angka)
        self.tombol.pack()

    # Method untuk menangani aksi (event handler)
    def tambah_angka(self):
        self.counter += 1
        self.label.config(text=f"Tombol diklik: {self.counter} kali")

if __name__ == "__main__":
    app = AplikasiSaya()
    app.mainloop()