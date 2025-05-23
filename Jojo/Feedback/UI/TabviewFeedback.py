import tkinter as tk
from tkinter import messagebox, ttk
import datetime as dt

# ----------variable----------
directory = './Jojo/Feedback/UI'

# ----------function----------
def bacaData():
    try:
        with open(f'{directory}/feedback.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        with open(f'{directory}/feedback.txt', 'w') as file:
            return []

def simpan_feedback():
    nama = nama_entry.get()
    email = email_entry.get()
    umpan_balik = umpan_balik_text.get("1.0", tk.END).strip()

    if not nama or not email or not umpan_balik:
        messagebox.showerror("Peringatan", "Semua item harus diisi!!!")
        return

    try:
        with open(f'{directory}/feedback.txt', 'a') as file:
            waktu = dt.datetime.now().strftime("%d-%m-%Y\t%H:%M:%S")
            file.write(f'Waktu: {waktu}\n')
            file.write(f'Nama: {nama}\n')
            file.write(f'Email: {email}\n')
            file.write(f'Note: {umpan_balik}\n')
            file.write(f'{"="*50}\n')

        messagebox.showinfo("Terima Kasih", "Terima kasih atas feedback Anda!")
        nama_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        umpan_balik_text.delete("1.0", tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi error: {e}")


def displayData():
    daftarFeedback = bacaData()
    if not daftarFeedback:
        feedback_listbox.delete(0, tk.END)
        feedback_listbox.insert(tk.END, "Belum ada Feedback")
    else:
        feedback_listbox.delete(0, tk.END)
        for fb in daftarFeedback:
            feedback_listbox.insert(tk.END, fb.strip())


# ----------main----------
root = tk.Tk()
root.title("Feedback Form App")

# Main Tab Control
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# --- Tab 1: Form Feedback ---
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Submit Feedback")

form_frame = tk.LabelFrame(tab1, text="Form Feedback")
form_frame.pack(padx=20, pady=20)

nama_label = tk.Label(form_frame, text="Nama:")
nama_label.grid(row=0, column=0, sticky="w")
nama_entry = tk.Entry(form_frame)
nama_entry.grid(row=0, column=1, sticky="ew")

email_label = tk.Label(form_frame, text="Email:")
email_label.grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(form_frame)
email_entry.grid(row=1, column=1, sticky="ew")

umpan_balik_label = tk.Label(form_frame, text="Feedback:")
umpan_balik_label.grid(row=2, column=0, sticky="w")
umpan_balik_text = tk.Text(form_frame, height=5)
umpan_balik_text.grid(row=2, column=1, sticky="nsew")

submit_button = tk.Button(form_frame, text="Submit", command=simpan_feedback)
submit_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))


# --- Tab 2: Display Feedback ---
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Current Feedback")

display_frame = tk.LabelFrame(tab2, text="Current Feedback")
display_frame.pack(padx=20, pady=20)

feedback_listbox = tk.Listbox(display_frame, height=10)
feedback_listbox.pack(fill=tk.BOTH, expand=True)

displayData()  # Initial display of feedback


root.mainloop()