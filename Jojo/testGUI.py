import tkinter as tk

window=tk.Tk() #object jendela
window.title("Table")
window.geometry("400x400")

#============= Top==========
top_Frame=tk.Frame(window)
top_Frame.pack(fill=tk.X)

judul=tk.Label(top_Frame,text="Judul Top", fg="blue", font=("Arial",16))
judul.pack(pady=10)

center_Frame=tk.Frame(window, borderwidth=2, relief="raised")
center_Frame.pack(fill="both", pady=10)

#=============== left =============
left_center_Frame=tk.Frame(center_Frame)
left_center_Frame.pack(side="left", fill="both", pady=10)

center=tk.Label(left_center_Frame,text="Judul center", fg="yellow", font=("Arial",16),relief="raise")
center2=tk.Label(left_center_Frame,text="Judul center", fg="yellow", font=("Arial",16))
center.pack(fill=tk.BOTH, pady=10)
center2.pack(fill=tk.BOTH, pady=10)

#=============right==============
right_center_Frame=tk.Frame(center_Frame)
right_center_Frame.pack(side="right", fill="both", pady=20, expand=True)
fotter=tk.Label(right_center_Frame,text="Judul bottom", fg="green", font=("Arial",16))
fotter.pack(pady=10)

#============= bottom ==============
bottom_Frame1=tk.Frame(window)
bottom_Frame1.pack(side="bottom", fill="both", pady=20)
fotter1=tk.Label(bottom_Frame1,text="Judul bottom", fg="green", font=("Arial",16))
fotter1.pack(pady=10)

window.mainloop()