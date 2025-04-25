import tkinter as tk
from tkinter import ttk

class EntryField(ttk.Frame):
    def __init__(self,parent,label_text):
        super().__init__(parent)
        self.label = ttk.Label(self,text=label_text)
        self.label.pack(side=tk.LEFT)
        self.entry = ttk.Entry(self)
        self.entry.pack(side=tk.LEFT, fill=tk.X , expand=True)

    def get(self):
        return self.entry.get()
        
    def clear(self):
        self.entry.delete(0,tk.END)

class ContactList(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.listbox = tk.Listbox(self, height=10, width=50)
        self.listbox.pack(fill=tk.BOTH, expand=True)
    
    def update_contact(self,contacts):
        self.listbox.delete(0,tk.END)
        for name, phone in contacts:
            self.listbox.insert(tk.END,f"{name} - {phone}")