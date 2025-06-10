import tkinter as tk
from GUI.main_window import MainWindow
from Data.contact_manager import ContactManager

if __name__=="__main__":
    root=tk.Tk()
    contact_manager = ContactManager()
    app=MainWindow(root,contact_manager)

    root.mainloop()