import customtkinter as ctk
import tkinter as tk
import datetime as dt

# ----------variable----------
directory = './Jojo/Feedback/Console'

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
    umpan_balik = umpan_balik_textbox.get("1.0", ctk.END).strip()

    if not nama or not email or not umpan_balik:
        ctk.CTkMessageBox(title="Peringatan", message="Semua item harus diisi!!!").show()  # Use CTkMessageBox
        return

    try:
        with open(f'{directory}/feedback.txt', 'a') as file:
            waktu = dt.datetime.now().strftime("%d-%m-%Y\t%H:%M:%S")
            file.write(f'Waktu: {waktu}\n')
            file.write(f'Nama: {nama}\n')
            file.write(f'Email: {email}\n')
            file.write(f'Note: {umpan_balik}\n')
            file.write(f'{"="*50}\n')

        ctk.CTkMessageBox(title="Terima Kasih", message="Terima kasih atas feedback Anda!").show()  # Use CTkMessageBox
        nama_entry.delete(0, ctk.END)
        email_entry.delete(0, ctk.END)
        umpan_balik_textbox.delete("1.0", ctk.END)

    except Exception as e:
        ctk.CTkMessageBox(title="Error", message=f"Terjadi error: {e}").show()  # Use CTkMessageBox

def display_feedback():
    daftarFeedback = bacaData()
    feedback_listbox.delete(0, ctk.END)
    if not daftarFeedback:
        feedback_listbox.insert(ctk.END, "Belum ada Feedback")
    else:
        for fb in daftarFeedback:
            feedback_listbox.insert(ctk.END, fb.strip())


# ----------main----------
root = ctk.CTk() # Use CTk
root.title("Feedback Form App")
root.geometry('600x400')

# Set appearance mode and color theme (optional)
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"


# --- Form Frame ---
form_frame = ctk.CTkFrame(root)
form_frame.pack(padx=20, pady=20)

nama_label = ctk.CTkLabel(form_frame, text="Nama:")
nama_label.grid(row=0, column=0, sticky="w")
nama_entry = ctk.CTkEntry(form_frame)
nama_entry.grid(row=0, column=1, sticky="ew", padx=(5,0))

email_label = ctk.CTkLabel(form_frame, text="Email:")
email_label.grid(row=1, column=0, sticky="w")
email_entry = ctk.CTkEntry(form_frame)
email_entry.grid(row=1, column=1, sticky="ew", padx=(5,0))

umpan_balik_label = ctk.CTkLabel(form_frame, text="Feedback:")
umpan_balik_label.grid(row=2, column=0, sticky="w")
umpan_balik_textbox = ctk.CTkTextbox(form_frame, height=80)  # Use CTkTextbox
umpan_balik_textbox.grid(row=2, column=1, sticky="nsew", padx=(5,0))

submit_button = ctk.CTkButton(form_frame, text="Submit", command=simpan_feedback)
submit_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))


# --- Display Frame ---
display_frame = ctk.CTkFrame(root)
display_frame.pack(padx=20, pady=(0, 20))

# feedback_listbox = ctk.CTkListbox(display_frame)  # Use CTkListbox
# feedback_listbox.pack(fill=ctk.BOTH, expand=True)
feedback_listbox = tk.Listbox(display_frame,width=200)  # Use tk.Listbox (standard Tkinter)
feedback_listbox.pack(fill=tk.BOTH, expand=True) # Use tk.BOTH for fill

display_feedback()

root.mainloop()