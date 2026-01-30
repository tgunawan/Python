import tkinter as tk
from tkinter import messagebox

def welcome():
    return "Selamat datang di Aplikasi Kasir Sederhana \nSilahkan masukkan data barang!"

def hitung_total():
    """Hitung total harga berdasarkan input jumlah, harga, dan member diskon."""
    try:
        kuantitas = int(entry_qty.get())
        harga = float(entry_harga.get())
        total = kuantitas * harga

        if member_var.get() == 1:
            total *= 0.8  # diskon 20%
            label_total.config(text=f"Total (Member 20% Off): Rp {total:,.2f}")
        else:
            label_total.config(text=f"Total: Rp {total:,.2f}")

    except ValueError:
        messagebox.showerror("Error", "Jumlah harus integer dan harga harus angka!")

# Window Setup
root = tk.Tk()
root.title("Kasir Sederhana")
root.geometry("350x400")

# Widgets
label_welcome = tk.Label(root, text=welcome(), fg="darkred", font=("Arial", 10), justify="center")
label_welcome.pack(pady=10)

# Nama Barang
label_nama = tk.Label(root, text="Nama Barang:")
label_nama.pack(pady=5)
entry_nama = tk.Entry(root)
entry_nama.pack(pady=5)

# Jumlah
label_qty = tk.Label(root, text="Jumlah:")
label_qty.pack(pady=5)
entry_qty = tk.Entry(root)
entry_qty.pack(pady=5)

# Harga
label_harga = tk.Label(root, text="Harga Satuan (Rp):")
label_harga.pack(pady=5)
entry_harga = tk.Entry(root)
entry_harga.pack(pady=5)

# Member Checkbutton
member_var = tk.IntVar()
check_member = tk.Checkbutton(root, text="Member? Diskon 20%", variable=member_var)
check_member.pack(pady=5)

# Button Hitung
btn_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
btn_hitung.pack(pady=10)

# Label Total
label_total = tk.Label(root, text="Total: Rp 0")
label_total.pack(pady=10)

# Jalankan aplikasi
root.mainloop()