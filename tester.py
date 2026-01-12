import time,os
import turtle as t

screen = t.Screen()
screen.title("Program Kura Sederhana")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)


kura=t.Turtle()
kura.shape("turtle")
kura.color("green")
kura.speed(1)

def kembali():
    kura.home()
    kura.setheading(0)

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


screen.listen()

# Deteksi tombol
screen.onkey(maju, "w")
screen.onkey(mundur, "s")
screen.onkey(lambda: kiri(45), "a")
screen.onkey(lambda: kanan(45), "d")
screen.onkey(kembali, "space")

t.mainloop()