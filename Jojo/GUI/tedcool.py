#===============================library==========================================#
import tkinter as tk
#===============================main==========================================#
root = tk.Tk()
root.title("Ted counting table")
root.geometry('400x500')
kali=tk.Label(root,text='Perkalian(x)')
kali.grid(row=0,column=0,columnspan=11)

for i in range(1,11):
    sigma=tk.Label(root,text=i)
    sigma.grid(row=1,column=i)
for i in range(2,12):
    rizzler=tk.Label(root,text=i-1)
    rizzler.grid(row=i,column=0)

for i in range(2,12):
    for j in range(1,11):
        result=(i-1)*(j)
        x=tk.Label(root,text=result)
        x.grid(row=i,column=j)

for i in range(0,24):
    side1=tk.Label(root,text='',bg='black')
    side1.grid(row=i,column=13,)
bagi=tk.Label(root,text='Pembagian(:)')
bagi.grid(row=0,column=14,columnspan=11)
for i in range(1,11):
    up=tk.Label(root,text=i)
    up.grid(row=1,column=i+14)
for i in range(2,12):
    sdie=tk.Label(root,text=i-1)
    sdie.grid(row=i,column=14)
for i in range(1,11):#pembagian
    for j in range(2,12):
        result=round((j-1)/(i),2)
        res=tk.Label(root,text=result)
        res.grid(row=j,column=i+14)

for i in range(0,24):#batas
    side2=tk.Label(root,text=f'\t',bg='black')
    side2.grid(row=12,column=i,columnspan=2)
plus=tk.Label(root,text='Penjumlahan(+)')
plus.grid(row=13,column=0,columnspan=11)
for i in range(1,11):
    down=tk.Label(root,text=i)
    down.grid(row=14,column=i)
for i in range(2,12):
    down1=tk.Label(root,text=i-1)
    down1.grid(row=i+13,column=0)
for i in range(1,11):
    for j in range(2,12):
        result=((j-1)+(i))
        res=tk.Label(root,text=result)
        res.grid(row=j+13,column=i)
min=tk.Label(root,text='Pengurangan(-)')
min.grid(row=13,column=14,columnspan=11)


root.mainloop()