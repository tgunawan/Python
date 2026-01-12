import time,os
import turtle as t
'''
def hapus():
    os.system("clear")

def wait(n):
    time.sleep(n)

def tulis(teks):
    print(teks)'''

print("Selamat datang di program penghapusan file!")
kura=t.Turtle()
kura.shape("turtle")
kura.color("green")
kura.speed(1)

def kanan(deg=90):
    kura.right(deg)

def kiri(deg=90):
    kura.left(deg)

def maju(steps=100):
    kura.forward(steps)

def mundur(steps=100):
    kura.backward(steps)

def penaTurun():
    kura.pendown()

def penaNaik():
    kura.penup()


t.mainloop()