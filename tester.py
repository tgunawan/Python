'''import time,os
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

t.mainloop()'''



import turtle
import time

# deklarasi pen dan screen
__Pen = turtle.Pen()
screen = turtle.Screen()

# mengatur setting dari sceeen
screen.title("Program Menggambar")
screen.bgcolor("lightblue")
screen.setup(width=1280, height=960)

# agar saat pertama kali program dijalankan fill juga dimulai
__Pen.begin_fill()

# fungsi go to untuk memindahkan turtle
def goto(x,y):
    __Pen.penup()
    __Pen.goto(x, y)
    __Pen.begin_fill()
    __Pen.pendown()

# fungsi fill color untuk memilih warna fill
def changeFillColor(color):
    __Pen.fillcolor(color)
    __Pen.pencolor(color)

# fungsi maju untuk menggerakkan turltle untuk maju dengan default majunya 100 step
def maju(satuan=100):
    __Pen.forward(satuan)

# fungsi mundur untuk menggerakkan turltle untuk mundur dengan default mundurnya 100 step
def mundur(satuan=100):
    __Pen.backward(satuan)

# fungsi right untuk mengubah arah turtle ke kanan dengan default angle nya 45
def right(deg=45):
    __Pen.right(deg)

# fungsi left untuk mengubah arah turtle ke kiri dengan default angle nya 45
def left(deg=45):
    __Pen.left(deg)

# fungsi untuk menandakan akhir dari fill shape
def endfill():
    __Pen.end_fill()

# fungsi untuk membuat awan 
def cloud(x,y):
    # untuk mengetahui current x position dan current circle
    curr_x = x
    curr_circle = 1
    # for loop untuk membuat 3 lingkaran membentuk awan
    for __count in range(3):
        __Pen.penup()
        __Pen.goto((curr_x), y)
        __Pen.pendown()
        __Pen.begin_fill()
        # untuk cek jika genap maka lingkaran yang dibuat lebih besar radiusnya
        if curr_circle%2 == 0:
            __Pen.circle(75)
        else:
            __Pen.circle(55)
        __Pen.end_fill()
        # mengupdate status current
        curr_x += 85
        curr_circle +=1

# fungsi untuk membuat circle
def circle():
    __Pen.begin_fill()
    __Pen.circle(55)
    __Pen.end_fill()

#fungsi untuk menulis keterangan
def show_message(text):
    __Pen.penup()
    __Pen.goto(-600, 300)
    __Pen.clear()
    __Pen.write(text, font=("Arial", 16, "bold"))
    __Pen.pendown()

# fungsi untuk menangkap error jika salah input keyboard
def wrong_key(expected):
    show_message(f"apakah yang kamu maksud '{expected}'?")
    time.sleep(1)
    show_message("")

show_message("""- klik kiri mana saja untuk mengganti posisi turtle
- maju = w, mundur = s, kiri = a, kanan = d
- pilih warna fill r = red, y=yellow, b=blue
- block atau fill warna dengan menekan space 
- tekan c untuk membuat circle 
- klik kanan untuk membuat awan
""")

screen.listen()

# Deteksi tombol click untuk mengubah posisi turtle dengan klik kiri
screen.onclick(goto, 1)
# membuat awan dengan klik kanan
screen.onclick(cloud, 3)
# mengubah warna fill dengan menekan tombol r = red, y = yellow, b = blue
screen.onkey(lambda: changeFillColor("red"), "r")
screen.onkey(lambda: changeFillColor("yellow"), "y")
screen.onkey(lambda: changeFillColor("blue"), "b")
# menggerakkan turtle untuk membuat garis(w=maju, s=mundur, a=kiri, d=kanan)
screen.onkey(maju, "w")
screen.onkey(mundur, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
# membuat circle dengan menekan tombol c
screen.onkey(circle, "c")
screen.onkey(lambda: wrong_key("c"), "v")
screen.onkey(lambda: wrong_key("c"), "x")
# menyelesaikan fill shape dengan space
screen.onkey(endfill, "space")

turtle.done()