import tkinter as tk

# Buat jendela utama
window = tk.Tk()
window.title("Jendela Terbagi")

# Frame utama di atas (topheading)
topheading_frame = tk.Frame(window, bg="lightblue")
topheading_frame.pack(fill="x")
label_top = tk.Label(topheading_frame, text="Ini adalah bagian atas", font=("Arial", 16))
label_top.pack(pady=10)

# Frame kiri dan kanan di bawah topheading
left_frame = tk.Frame(window, bg="lightgreen", width=window.winfo_screenwidth() // 3)
left_frame.pack(side="left", fill="both")

right_frame = tk.Frame(window, bg="pink", width=window.winfo_screenwidth() // 3 * 2)
right_frame.pack(side="right", fill="both", expand=True)

# Bagi frame kiri menjadi atas dan bawah
left_top_frame = tk.Frame(left_frame, bg="yellow")
left_top_frame.pack(fill="both", expand=True)
label_left_top = tk.Label(left_top_frame, text="Kiri Atas")
label_left_top.pack(pady=10)

left_bottom_frame = tk.Frame(left_frame, bg="orange")
left_bottom_frame.pack(fill="both", expand=True)
label_left_bottom = tk.Label(left_bottom_frame, text="Kiri Bawah")
label_left_bottom.pack(pady=10)

# Contoh isi untuk frame kanan (bisa diganti dengan komponen lain)
label_right = tk.Label(right_frame, text="Ini adalah bagian kanan yang lebih besar", font=("Arial", 12))
label_right.pack(pady=10)

window.mainloop()