'''
import tkinter as tk

root= tk.Tk()
root.title("Simple Form Input")
root.geometry("420x260")
root.configure(bg="lightblue")
root.resizable(True, False)

title= tk.Label(root,
                text="Form Input Sederhana",
                font=("Segoe UI", 16, "bold"),
                bg="lightblue")
title.pack(pady=(20, 10))

frame = tk.Frame(root, bg="white", bd=1, relief="groove")#,height=100,width=200
frame.pack(padx=20, pady=10,fill="both" , expand=True)

root.mainloop()

# angka=int(input("Input: "))
# for i in range(1,angka+1,2):
#     print(f'{"*"*i:^{angka+5}}')'''

'''import tkinter as tk


#---------------
# Main Window
#---------------
window = tk.Tk()
window.title("Bebas")
window.geometry("420x260") #width x height
window.configure(bg="lightblue")

#---------------
#
#---------------

judul = tk.Label(window,
                text="Form Input Sederhana",
                font=("Segoe UI", 16, "bold"),
                bg="lightblue")
judul.pack(pady=(20, 10))

window.mainloop()'''

import time

list1D=["apel","jeruk","mangga","pisang"]

print(*list1D, sep="\n")

text = "Welcome to Bookworms!"
for char in text:
    print(char, end="", flush=True)
    time.sleep(0.2)