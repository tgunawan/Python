import tkinter as tk

window = tk.Tk()
window.title("Contoh Listbox dengan data")

datalist = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

listbox = tk.Listbox(window)
listbox.pack()

#insert data to listbox
for data in datalist:
    listbox.insert(tk.END, data)

window.mainloop()
