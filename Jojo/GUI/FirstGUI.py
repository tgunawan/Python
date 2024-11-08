import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("My GUI")
window.geometry("800x300")

def display():
    global text2
    print('Hello tKinter')
    text2.pack_forget()
    text2=tk.Label(window,text="adeade", font=("Arial", 30, "bold", "italic"), fg="orange", bg="blue")
    text2.pack()
    # window.destroy()


text2=tk.Label(window,text="Hello", font=("Arial", 30, "bold", "italic"), fg="orange", bg="blue")
text2.pack()


tombol1=tk.Button(window, text="function", font=("Arial", 20),relief="ridge", bg="green",command=display)
tombol1.pack()

tombol2=tk.Button(window, text="lambda", font=("Arial", 20),relief="ridge", bg="green",command=lambda: print("tes lambda"))
tombol2.pack()

window.mainloop()