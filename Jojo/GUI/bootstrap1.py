import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox

class Aplikasi(ttk.Window):
    def __init__(self):
        super().__init__(themename="flatly")  # Anda bisa mencoba tema lain seperti "darkly", "solar"
        self.title("Aplikasi Sederhana")
        #self.geometry("400x300")
        self.resizable(True, False) # Mengizinkan pengguna menyesuaikan ukuran jendela (Horizontal, Vertikal)

        #Frame => setiap halaman / page di aplikasi
        self.login_frame = LoginFrame(self, self.show_signup_frame, self.show_landing_frame)
        self.signup_frame = SignupFrame(self, self.show_login_frame)
        self.landing_frame = LandingFrame(self, self.show_login_frame)

        self.show_login_frame()

    def show_frame(self, frame):
        frame.tkraise()

    def show_login_frame(self):
        self.show_frame(self.login_frame)

    def show_signup_frame(self):
        self.show_frame(self.signup_frame)

    def show_landing_frame(self):
        self.show_frame(self.landing_frame)

class LoginFrame(ttk.Frame):
    def __init__(self, parent, show_signup, show_landing):
        super().__init__(parent, padding=20)
        self.grid(row=0, column=0, sticky="nsew")

        ttk.Label(self, text="Login", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        ttk.Label(self, text="Username:").grid(row=1, column=0, sticky="w")
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(self, text="Password:").grid(row=2, column=0, sticky="w")
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, sticky="ew", pady=5)

        login_button = ttk.Button(self, text="Login", command=self.login_action, bootstyle="primary")
        login_button.grid(row=3, column=0, columnspan=2, pady=(10, 5))

        signup_button = ttk.Button(self, text="Signup", command=show_signup, bootstyle="link")
        signup_button.grid(row=4, column=0, columnspan=2, pady=(0, 5))

        self.show_landing = show_landing

    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Di sini Anda bisa menambahkan logika otentikasi
        if username == "user" and password == "pass":
            messagebox.showinfo("Sukses", "Login berhasil!")
            self.show_landing()
        else:
            messagebox.showerror("Gagal", "Username atau password salah.")

class SignupFrame(ttk.Frame):
    def __init__(self, parent, show_login):
        super().__init__(parent, padding=20)
        self.grid(row=0, column=0, sticky="nsew")

        ttk.Label(self, text="Signup", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        ttk.Label(self, text="Username:").grid(row=1, column=0, sticky="w")
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(self, text="Email:").grid(row=2, column=0, sticky="w")
        self.email_entry = ttk.Entry(self)
        self.email_entry.grid(row=2, column=1, sticky="ew", pady=5)

        ttk.Label(self, text="Password:").grid(row=3, column=0, sticky="w")
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=3, column=1, sticky="ew", pady=5)

        signup_button = ttk.Button(self, text="Signup", command=self.signup_action, bootstyle="success")
        signup_button.grid(row=4, column=0, columnspan=2, pady=(10, 5))

        login_button = ttk.Button(self, text="Sudah punya akun? Login", command=show_login, bootstyle="link")
        login_button.grid(row=5, column=0, columnspan=2, pady=(0, 5))

    def signup_action(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Di sini Anda bisa menambahkan logika penyimpanan data pendaftaran
        messagebox.showinfo("Sukses", f"Akun dengan username {username} berhasil dibuat!")
        # Setelah berhasil signup, mungkin Anda ingin mengarahkan pengguna ke halaman login
        # self.master.show_login_frame()

class LandingFrame(ttk.Frame):
    def __init__(self, parent, show_login):
        super().__init__(parent, padding=20)
        self.grid(row=0, column=0, sticky="nsew")

        ttk.Label(self, text="Selamat Datang!", font=("Arial", 24)).pack(pady=20)
        ttk.Label(self, text="Ini adalah halaman landing setelah login.").pack(pady=10)

        logout_button = ttk.Button(self, text="Logout", command=show_login, bootstyle="danger")
        logout_button.pack(pady=20)

if __name__ == "__main__":
    app = Aplikasi()
    app.mainloop()