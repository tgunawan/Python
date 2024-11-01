from tkinter import *

def show_entry_fields():
  print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
  
master = Tk()
master.title("Introduction")
master.geometry('350x200') 

btn5=Button(master, text="Test", command="").grid(row=0)
e1 = Entry(master)
btn4=Button(master, text="Test", command="").grid(row=0, column=1)
btn3=Button(master, text="Test", command="").grid(row=0, column=2)

new_label2 = Label(master, 
         text="Last Name").grid(row=1)

e2 = Entry(master)

e2.grid(row=1, column=1)
c = Checkbutton(master, text="Keep me logged in")
c.grid(columnspan=1, column=1)
new_btn1 = Button(master, text='Quit', command=master.quit).grid(row=3, column=0,sticky=W, pady=4)


new_btn2 = Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

master.mainloop()