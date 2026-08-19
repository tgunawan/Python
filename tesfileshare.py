# def profile(**data):
#     print(data)

# profile(nama="Tedi", umur=20)
'''
print("Tulis file")


listNama=["Andi","Budi","Charlie","Danur"]
with open("datauser.txt", "w") as file:
    # nama=input("Masukkan nama: ")
    # file.write("\nNama : ") 
    # file.write(nama)
    for nama in listNama:
        file.write(f"\nNama : {nama}")

with open("datauser.txt", "r") as file:
    hasil=file.readlines()
    print(hasil)'''


''' # get screen width and height
import tkinter as tk

root = tk.Tk()

# Mendapatkan lebar dan tinggi layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Mengatur ukuran jendela sesuai lebar layar, dan tinggi misal 600 piksel
root.geometry(f"{screen_width}x600")

# Atau jika ingin full screen
# root.geometry(f"{screen_width}x{screen_height}")

root.title("Window menyesuaikan lebar layar OS")

root.mainloop()
'''

#get screen width and height plus position to center the window
import tkinter as tk

root = tk.Tk()

# Dapatkan ukuran layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Hitung ukuran jendela setengah layar
window_width = screen_width // 2
window_height = screen_height // 2

# Hitung posisi agar jendela berada di tengah layar
position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2

# Set ukuran dan posisi jendela
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

root.title("Jendela Setengah Layar dan Tengah")

root.mainloop()
