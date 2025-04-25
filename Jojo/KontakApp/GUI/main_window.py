import tkinter as tk
from tkinter import ttk
from .widget import EntryField,ContactList

class MainWindow(ttk.Frame):
    def __init__(self,parent,contact_manager):
        super().__init__(parent)
        self.parent = parent
        self.contact_manager = contact_manager
        self.parent.title("Buku kontak simple")
        self.grid(row=0,column=0,sticky=(tk.N,tk.W,tk.E,tk.S))
        # self.grid_columnconfigure(0,weight=1)
        # self.grid_rowconfigure(0,weight=1)
    
        self.create_widgets()
        self.load_contacts()
    
    def create_widgets(self):
        #frame
        input_frame = ttk.LabelFrame(self,text="Tambah Kontak")
        input_frame.grid(row=0,column=0, pady=10, padx=10,sticky=(tk.N,tk.W,tk.E))

        #entry field
        self.name_entry= EntryField(input_frame,"Nama: ")
        self.name_entry.grid(row=0,column=0, pady=5,padx=5,sticky=(tk.W, tk.E))

        self.phone_entry= EntryField(input_frame,"Telepon: ")
        self.phone_entry.grid(row=1,column=0, pady=5,padx=5,sticky=(tk.W, tk.E))

        #button
        self.add_button = ttk.Button(input_frame,text="Tambah",command=self.add_contact).grid(row=2,column=0,pady=5,padx=5,sticky=(tk.W))

        #frame
        List_frame = ttk.LabelFrame(self,text="Daftar Kontak")
        List_frame.grid(row=1,column=0,pady=10,padx=10,sticky=(tk.N,tk.W,tk.E, tk.S))

        #contact list
        self.contact_list = ContactList(List_frame)
        self.contact_list.grid(row=0,column=0,sticky=(tk.N,tk.W,tk.E))

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contact_manager.add_contact(name,phone)
            self.load_contacts()
            self.name_entry.clear()
            self.phone_entry.clear()
        


    def load_contacts(self):
        contacts = self.contact_manager.get_all_contact()
        self.contact_list.update_contact(contacts)