import tkinter as tk

window = tk.Tk()
window.title("Listbox")

listbox = tk.Listbox(window)
listbox.pack()

listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")

window.mainloop()

