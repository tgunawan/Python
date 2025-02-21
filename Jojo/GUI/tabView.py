import tkinter as tk
from tkinter import ttk

def buatTab(mainFrame, titleTab):
    frame=ttk.Frame(mainFrame)
    mainFrame.add(frame, text=titleTab)
    return frame


#main Root / window
root=tk.Tk()
root.title("Simple Tab Window Example Python")
root.geometry("500x300")

# Main Tab Control , Main frame dari tab
notebook=ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Create tab
tab1=buatTab(notebook, "Tab 1")
tab2=buatTab(notebook, "Tab 2")
tab3=buatTab(notebook, "Tab 3")

#Content / isi tab
isitab1=tk.Label(tab1, text="Tab 1")
isitab1.pack(padx=20, pady=20)

isitab2=tk.Label(tab2, text="Tab 2")
isitab2.pack(padx=20, pady=20)

isitab3=tk.Label(tab3, text="Tab 3")
isitab3.pack(padx=20, pady=20)

root.mainloop()