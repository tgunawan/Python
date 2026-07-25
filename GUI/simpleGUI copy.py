import tkinter as tk
from tkinter import messagebox

def tombol_kirim():
    nama = entry_nama.get().strip()
    email = entry_email.get().strip()
    pesan = entry_pesan.get().strip()

    if not nama or not email or not pesan:
        messagebox.showwarning("Input Tidak Lengkap", "Silakan isi semua field.")
        return

    with open("simpan.txt", "a", encoding="utf-8") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Pesan: {pesan}\n")
        file.write("-" * 30 + "\n")

    messagebox.showinfo("Berhasil", f"Halo {nama}!\nData Anda berhasil disimpan ke simpan.txt.")


def tombol_baca():
    try:
        with open("simpan.txt", "r", encoding="utf-8") as file:
            isi = file.read()
        if isi:
            messagebox.showinfo("Isi File", isi)
        else:
            messagebox.showinfo("Isi File", "File masih kosong.")
    except FileNotFoundError:
        messagebox.showwarning("File Tidak Ditemukan", "Belum ada file simpan.txt yang dibuat.")


# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Simple Form Input")
root.geometry("420x300")
root.configure(bg="#f2f4f7")
root.resizable(False, False)

# Membuat judul tampilan
judul = tk.Label(
    root,
    text="Form Input Sederhana",
    font=("Brush Script MT", 16, "bold"),
    bg="#f2f4f7",
    fg="#1f2937",
)
judul.pack(pady=(20, 10))

# Membuat frame untuk menampung form
frame = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Label dan Entry untuk input nama
label_nama = tk.Label(frame, text="Nama:", font=("Segoe UI", 11), bg="#ffffff")
label_nama.grid(row=0, column=0, sticky="w", padx=10, pady=8)
entry_nama = tk.Entry(frame, width=30, font=("Segoe UI", 11))
entry_nama.grid(row=0, column=1, padx=10, pady=8)

# Label dan Entry untuk input email
label_email = tk.Label(frame, text="Email:", font=("Segoe UI", 11), bg="#ffffff")
label_email.grid(row=1, column=0, sticky="w", padx=10, pady=8)
entry_email = tk.Entry(frame, width=30, font=("Segoe UI", 11))
entry_email.grid(row=1, column=1, padx=10, pady=8)

# Label dan Entry untuk input pesan
label_pesan = tk.Label(frame, text="Pesan:", font=("Segoe UI", 11), bg="#ffffff")
label_pesan.grid(row=2, column=0, sticky="w", padx=10, pady=8)
entry_pesan = tk.Entry(frame, width=30, font=("Segoe UI", 11))
entry_pesan.grid(row=2, column=1, padx=10, pady=8)

# Tombol submit
button_kirim = tk.Button(
    frame,
    text="Kirim",
    width=15,
    bg="#2563eb",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=tombol_kirim,
)
button_kirim.grid(row=3, column=0, pady=(12, 8), sticky="e")

# Tombol baca file
button_baca = tk.Button(
    frame,
    text="Baca File",
    width=15,
    bg="#16a34a",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=tombol_baca,
)
button_baca.grid(row=3, column=1, pady=(12, 8), sticky="w")

# Menjalankan aplikasi Tkinter
root.mainloop()
