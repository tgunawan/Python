import tkinter as tk

window=tk.Tk()
window.title("Multiplication table")
window.geometry("800x500")  

title = tk.Label(window, text="Multiplication table", font=("Arial", 30, "bold", "italic"), fg="orange", bg="blue")
title.grid(row=0, column=0, columnspan=11)

for i in range(1, 11):
  headercolumn=tk.Label(window,text=i, font=("Arial", 10, "bold", "italic"), fg="orange")
  headercolumn.grid(row=1, column=i)

for i in range(2,12):
  headerrow=tk.Label(window,text=i-1, font=("Arial", 10, "bold", "italic"), fg="orange")
  headerrow.grid(row=i, column=0)

for i in range(2,12):
  for j in range(1,11):
    result=(i-1)*j
    label=tk.Label(window,text=result, font=("Arial", 10, "bold", "italic"), fg="green")
    label.grid(row=i, column=j)

for i in range(0,24):
  label=tk.Label(window,text=" ", background="green")
  label.grid(row=i, column=13)
label=tk.Label(window,text=f"{"-":10}"*24,background="red")
label.grid(row=14, column=0,columnspan=24)



window.mainloop()