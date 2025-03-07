import getpass

password = getpass.getpass("Masukkan password Anda: ") #hide saat ketik password
print(password)
print("Password Anda:", "*" * len(password))  # Menampilkan * sejumlah panjang password