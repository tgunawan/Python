import turtle

t = turtle.Turtle()
screen = turtle.Screen()

# Flag tombol
gerak_kiri = False
gerak_kanan = False
gerak_maju = False
gerak_mundur = False

def tekan_kiri():
    global gerak_kiri
    gerak_kiri = True

def lepas_kiri():
    global gerak_kiri
    gerak_kiri = False

def tekan_kanan():
    global gerak_kanan
    gerak_kanan = True

def lepas_kanan():
    global gerak_kanan
    gerak_kanan = False

def tekan_maju():
    global gerak_maju
    gerak_maju = True

def lepas_maju():
    global gerak_maju
    gerak_maju = False

def update():
    if gerak_kiri:
        t.left(5)
    if gerak_kanan:
        t.right(5)
    if gerak_maju:
        t.forward(5)
    if gerak_mundur:
        t.backward(5)

    screen.ontimer(update, 20)  # 50 FPS


screen.listen()
screen.onkeypress(tekan_kiri, "a")
screen.onkeyrelease(lepas_kiri, "a")

screen.onkeypress(tekan_kanan, "d")
screen.onkeyrelease(lepas_kanan, "d")

screen.onkeypress(tekan_maju, "w")
screen.onkeyrelease(lepas_maju, "w")


update()
screen.mainloop()
