import re
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class RegistrationForm(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Form Pendaftaran")
        self.geometry("520x620")
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        self.create_widgets()

    def create_widgets(self):
        title_label = ctk.CTkLabel(
            self,
            text="Form Pendaftaran",
            font=ctk.CTkFont(size=26, weight="bold"),
        )
        title_label.pack(pady=(0, 20))

        form_frame = ctk.CTkFrame(self, corner_radius=15)
        form_frame.pack(fill="both", expand=True, padx=10, pady=10)
        form_frame.grid_columnconfigure(1, weight=1)

        self.name_entry = self.add_row(form_frame, "Nama Lengkap", 0)
        self.email_entry = self.add_row(form_frame, "Email", 1)
        self.password_entry = self.add_row(form_frame, "Password", 2, show="*")
        self.birth_entry = self.add_row(form_frame, "Tanggal Lahir", 3, placeholder="YYYY-MM-DD")

        gender_label = ctk.CTkLabel(form_frame, text="Jenis Kelamin:")
        gender_label.grid(row=4, column=0, sticky="w", padx=10, pady=(10, 3))
        self.gender_var = ctk.StringVar(value="Laki-laki")
        gender_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        gender_frame.grid(row=4, column=1, sticky="ew", padx=10, pady=(10, 3))
        ctk.CTkRadioButton(gender_frame, text="Laki-laki", variable=self.gender_var, value="Laki-laki").pack(side="left", padx=(0, 10))
        ctk.CTkRadioButton(gender_frame, text="Perempuan", variable=self.gender_var, value="Perempuan").pack(side="left")

        self.program_var = ctk.StringVar(value="Pilih Program Studi")
        program_label = ctk.CTkLabel(form_frame, text="Program Studi:")
        program_label.grid(row=5, column=0, sticky="w", padx=10, pady=(10, 3))
        program_options = ["Teknik Informatika", "Sistem Informasi", "Desain Grafis", "Manajemen", "Lainnya"]
        self.program_menu = ctk.CTkOptionMenu(
            form_frame,
            values=program_options,
            variable=self.program_var,
            width=280,
        )
        self.program_menu.grid(row=5, column=1, sticky="ew", padx=10, pady=(10, 3))

        alamat_label = ctk.CTkLabel(form_frame, text="Alamat:")
        alamat_label.grid(row=6, column=0, sticky="nw", padx=10, pady=(10, 3))
        self.address_text = ctk.CTkTextbox(form_frame, width=320, height=110)
        self.address_text.grid(row=6, column=1, sticky="ew", padx=10, pady=(10, 3))

        self.terms_var = ctk.BooleanVar(value=False)
        self.terms_check = ctk.CTkCheckBox(
            form_frame,
            text="Saya menyetujui syarat dan ketentuan",
            variable=self.terms_var,
        )
        self.terms_check.grid(row=7, column=0, columnspan=2, sticky="w", padx=10, pady=(15, 0))

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(fill="x", padx=10, pady=(20, 0))

        submit_button = ctk.CTkButton(
            button_frame,
            text="Submit",
            width=140,
            command=self.submit_form,
        )
        submit_button.pack(side="left", expand=True, padx=(0, 10))

        reset_button = ctk.CTkButton(
            button_frame,
            text="Reset",
            width=140,
            fg_color="#888888",
            hover_color="#777777",
            command=self.reset_form,
        )
        reset_button.pack(side="left", expand=True)

    def add_row(self, parent, label_text, row, show=None, placeholder=None):
        label = ctk.CTkLabel(parent, text=label_text + ":")
        label.grid(row=row, column=0, sticky="w", padx=10, pady=(10, 3))

        entry = ctk.CTkEntry(parent, show=show, width=280)
        entry.grid(row=row, column=1, sticky="ew", padx=10, pady=(10, 3))
        if placeholder:
            entry.insert(0, placeholder)
            entry.bind("<FocusIn>", lambda event, e=entry, p=placeholder: self._clear_placeholder(e, p))
            entry.bind("<FocusOut>", lambda event, e=entry, p=placeholder: self._restore_placeholder(e, p))
        return entry

    @staticmethod
    def _clear_placeholder(entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, "end")

    @staticmethod
    def _restore_placeholder(entry, placeholder):
        if entry.get().strip() == "":
            entry.insert(0, placeholder)

    def validate_email(self, email: str) -> bool:
        return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$", email))

    def validate_password(self, password: str) -> bool:
        return len(password) >= 6

    def submit_form(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        birth = self.birth_entry.get().strip()
        gender = self.gender_var.get()
        program = self.program_var.get()
        address = self.address_text.get("1.0", "end").strip()
        terms_accepted = self.terms_var.get()

        if not name:
            messagebox.showwarning("Validasi", "Nama lengkap wajib diisi.")
            return
        if not self.validate_email(email):
            messagebox.showwarning("Validasi", "Masukkan email yang valid.")
            return
        if not self.validate_password(password):
            messagebox.showwarning("Validasi", "Password harus minimal 6 karakter.")
            return
        if program == "Pilih Program Studi":
            messagebox.showwarning("Validasi", "Pilih program studi.")
            return
        if not address:
            messagebox.showwarning("Validasi", "Alamat tidak boleh kosong.")
            return
        if not terms_accepted:
            messagebox.showwarning("Validasi", "Setujui syarat dan ketentuan terlebih dahulu.")
            return

        messagebox.showinfo(
            "Terdaftar",
            f"Pendaftaran berhasil!\n\nNama: {name}\nEmail: {email}\nJenis Kelamin: {gender}\nProgram Studi: {program}",
        )

    def reset_form(self):
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.birth_entry.delete(0, "end")
        self.birth_entry.insert(0, "YYYY-MM-DD")
        self.gender_var.set("Laki-laki")
        self.program_var.set("Pilih Program Studi")
        self.address_text.delete("1.0", "end")
        self.terms_var.set(False)


if __name__ == "__main__":
    app = RegistrationForm()
    app.mainloop()
