import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from datetime import datetime

class RegistrationFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Form Pendaftaran - Aplikasi Modern")
        self.root.geometry("700x800")
        self.root.resizable(False, False)
        
        # Set style
        self.setup_style()
        
        # Create main canvas with background
        self.create_canvas_background()
        
        # Create form frame
        self.create_form()
        
    def setup_style(self):
        """Setup ttk style untuk tema modern"""
        self.style = ttk.Style()
        
        # Define colors
        self.primary_color = "#2E86AB"
        self.secondary_color = "#A23B72"
        self.success_color = "#06A77D"
        self.light_bg = "#F0F0F0"
        self.dark_text = "#2C3E50"
        
        # Configure ttk styles
        self.style.theme_use('clam')
        
        # Configure label style
        self.style.configure('TLabel', 
                           background=self.light_bg,
                           foreground=self.dark_text,
                           font=('Segoe UI', 10))
        
        # Configure title label
        self.style.configure('Title.TLabel',
                           background=self.light_bg,
                           foreground=self.primary_color,
                           font=('Segoe UI', 18, 'bold'))
        
        # Configure entry style
        self.style.configure('TEntry',
                           fieldbackground='white',
                           background='white',
                           foreground=self.dark_text,
                           borderwidth=1)
        
        # Configure button style
        self.style.configure('TButton',
                           font=('Segoe UI', 10, 'bold'),
                           padding=10)
        
        self.style.map('TButton',
                      background=[('active', self.secondary_color)])
        
        # Configure success button
        self.style.configure('Success.TButton',
                           font=('Segoe UI', 10, 'bold'),
                           padding=10,
                           background=self.success_color)
        
        # Configure combobox
        self.style.configure('TCombobox',
                           fieldbackground='white',
                           background='white',
                           foreground=self.dark_text)
        
    def create_canvas_background(self):
        """Buat canvas untuk background dengan design modern"""
        # Main canvas
        self.canvas = tk.Canvas(
            self.root,
            bg=self.light_bg,
            highlightthickness=0,
            height=800,
            width=700
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Draw header background
        self.canvas.create_rectangle(
            0, 0, 700, 120,
            fill=self.primary_color,
            outline=""
        )
        
        # Draw decorative circle
        self.canvas.create_oval(
            500, -50, 750, 100,
            fill=self.secondary_color,
            outline=""
        )
        
        # Title on canvas
        self.canvas.create_text(
            350, 40,
            text="📝 FORM PENDAFTARAN PENGGUNA",
            font=('Segoe UI', 16, 'bold'),
            fill='white',
            anchor='center'
        )
        
        # Subtitle
        self.canvas.create_text(
            350, 75,
            text="Silahkan isi data diri Anda dengan lengkap",
            font=('Segoe UI', 10),
            fill='white',
            anchor='center'
        )
        
    def create_form(self):
        """Buat form dengan fields"""
        # Frame untuk form (di atas canvas)
        form_frame = ttk.Frame(self.canvas, style='TFrame')
        form_frame.place(x=50, y=150, width=600)
        
        # Configure frame style
        self.style.configure('TFrame', background=self.light_bg)
        
        # Entry fields dengan label
        self.fields = {}
        
        # Row 1: Nama Lengkap
        ttk.Label(form_frame, text="Nama Lengkap *").grid(row=0, column=0, sticky='w', pady=(20, 5))
        self.fields['nama'] = ttk.Entry(form_frame, width=40)
        self.fields['nama'].grid(row=0, column=1, sticky='ew', pady=(20, 5), padx=10)
        
        # Row 2: Email
        ttk.Label(form_frame, text="Email *").grid(row=1, column=0, sticky='w', pady=5)
        self.fields['email'] = ttk.Entry(form_frame, width=40)
        self.fields['email'].grid(row=1, column=1, sticky='ew', pady=5, padx=10)
        
        # Row 3: No. Telepon
        ttk.Label(form_frame, text="No. Telepon *").grid(row=2, column=0, sticky='w', pady=5)
        self.fields['telepon'] = ttk.Entry(form_frame, width=40)
        self.fields['telepon'].grid(row=2, column=1, sticky='ew', pady=5, padx=10)
        
        # Row 4: Tanggal Lahir
        ttk.Label(form_frame, text="Tanggal Lahir *").grid(row=3, column=0, sticky='w', pady=5)
        self.fields['tgl_lahir'] = ttk.Entry(form_frame, width=40)
        self.fields['tgl_lahir'].grid(row=3, column=1, sticky='ew', pady=5, padx=10)
        self.canvas.create_text(420, 225, text="(dd-mm-yyyy)", font=('Segoe UI', 8, 'italic'), fill='gray')
        
        # Row 5: Jenis Kelamin
        ttk.Label(form_frame, text="Jenis Kelamin *").grid(row=4, column=0, sticky='w', pady=5)
        self.fields['jk'] = ttk.Combobox(
            form_frame,
            values=['Laki-laki', 'Perempuan', 'Lainnya'],
            state='readonly',
            width=37
        )
        self.fields['jk'].grid(row=4, column=1, sticky='ew', pady=5, padx=10)
        
        # Row 6: Alamat
        ttk.Label(form_frame, text="Alamat *").grid(row=5, column=0, sticky='nw', pady=5)
        self.fields['alamat'] = tk.Text(form_frame, width=40, height=4, font=('Segoe UI', 9))
        self.fields['alamat'].grid(row=5, column=1, sticky='ew', pady=5, padx=10)
        
        # Row 7: Kota
        ttk.Label(form_frame, text="Kota *").grid(row=6, column=0, sticky='w', pady=5)
        self.fields['kota'] = ttk.Entry(form_frame, width=40)
        self.fields['kota'].grid(row=6, column=1, sticky='ew', pady=5, padx=10)
        
        # Row 8: Provinsi
        ttk.Label(form_frame, text="Provinsi *").grid(row=7, column=0, sticky='w', pady=5)
        self.fields['provinsi'] = ttk.Combobox(
            form_frame,
            values=['Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'DKI Jakarta', 'Sumatera Utara', 'Lainnya'],
            state='readonly',
            width=37
        )
        self.fields['provinsi'].grid(row=7, column=1, sticky='ew', pady=5, padx=10)
        
        # Row 9: Password
        ttk.Label(form_frame, text="Password *").grid(row=8, column=0, sticky='w', pady=5)
        self.fields['password'] = ttk.Entry(form_frame, width=40, show='*')
        self.fields['password'].grid(row=8, column=1, sticky='ew', pady=5, padx=10)
        
        # Row 10: Confirm Password
        ttk.Label(form_frame, text="Konfirmasi Password *").grid(row=9, column=0, sticky='w', pady=5)
        self.fields['konfirm_password'] = ttk.Entry(form_frame, width=40, show='*')
        self.fields['konfirm_password'].grid(row=9, column=1, sticky='ew', pady=5, padx=10)
        
        # Row 11: Terms and Conditions
        self.agree_var = tk.BooleanVar()
        ttk.Checkbutton(
            form_frame,
            text="Saya setuju dengan Syarat & Ketentuan",
            variable=self.agree_var
        ).grid(row=10, column=0, columnspan=2, sticky='w', pady=15)
        
        # Configure column weight
        form_frame.columnconfigure(1, weight=1)
        
        # Button frame
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=11, column=0, columnspan=2, sticky='ew', pady=20)
        
        # Submit button
        submit_btn = ttk.Button(
            button_frame,
            text="✓ DAFTAR",
            command=self.submit_form,
            style='Success.TButton'
        )
        submit_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Reset button
        reset_btn = ttk.Button(
            button_frame,
            text="↻ BERSIHKAN",
            command=self.reset_form
        )
        reset_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
    def submit_form(self):
        """Validasi dan submit form"""
        # Validasi field kosong
        required_fields = ['nama', 'email', 'telepon', 'tgl_lahir', 'jk', 'alamat', 'kota', 'provinsi', 'password', 'konfirm_password']
        
        for field in required_fields:
            if field == 'alamat':
                if not self.fields[field].get("1.0", tk.END).strip():
                    messagebox.showerror("Error", f"Field {field.replace('_', ' ')} tidak boleh kosong!")
                    return
            else:
                if not self.fields[field].get():
                    messagebox.showerror("Error", f"Field {field.replace('_', ' ')} tidak boleh kosong!")
                    return
        
        # Validasi email
        email = self.fields['email'].get()
        if '@' not in email or '.' not in email:
            messagebox.showerror("Error", "Format email tidak valid!")
            return
        
        # Validasi password
        if self.fields['password'].get() != self.fields['konfirm_password'].get():
            messagebox.showerror("Error", "Password tidak cocok!")
            return
        
        if len(self.fields['password'].get()) < 6:
            messagebox.showerror("Error", "Password minimal 6 karakter!")
            return
        
        # Validasi terms and conditions
        if not self.agree_var.get():
            messagebox.showerror("Error", "Anda harus setuju dengan Syarat & Ketentuan!")
            return
        
        # Collect data
        data = {
            'nama': self.fields['nama'].get(),
            'email': self.fields['email'].get(),
            'telepon': self.fields['telepon'].get(),
            'tgl_lahir': self.fields['tgl_lahir'].get(),
            'jenis_kelamin': self.fields['jk'].get(),
            'alamat': self.fields['alamat'].get("1.0", tk.END).strip(),
            'kota': self.fields['kota'].get(),
            'provinsi': self.fields['provinsi'].get(),
            'terdaftar': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Save to file
        self.save_data(data)
        
        # Show success message
        messagebox.showinfo("Sukses", f"Selamat datang {data['nama']}!\nData Anda telah berhasil terdaftar.")
        
        # Reset form
        self.reset_form()
        
    def reset_form(self):
        """Reset semua field"""
        for field_name, field_widget in self.fields.items():
            if field_name == 'alamat':
                field_widget.delete("1.0", tk.END)
            else:
                field_widget.delete(0, tk.END)
        
        self.agree_var.set(False)
        
    def save_data(self, data):
        """Simpan data ke file JSON"""
        try:
            # Load existing data
            try:
                with open('registrations.json', 'r') as f:
                    registrations = json.load(f)
            except FileNotFoundError:
                registrations = []
            
            # Add new data
            registrations.append(data)
            
            # Save to file
            with open('registrations.json', 'w') as f:
                json.dump(registrations, f, indent=4, ensure_ascii=False)
            
            print(f"✓ Data {data['nama']} berhasil disimpan!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan data: {e}")


def main():
    root = tk.Tk()
    app = RegistrationFormApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
