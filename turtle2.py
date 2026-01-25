import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def on_click(x, y):
    t.goto(x, y)

screen.onclick(on_click)
screen.mainloop()


import turtle

t = turtle.Turtle()

def turtle_clicked(x, y):
    t.color("red")

t.onclick(turtle_clicked)
turtle.mainloop()


import turtle

t = turtle.Turtle()
t.speed(0)

def drag(x, y):
    t.goto(x, y)

t.ondrag(drag)
turtle.mainloop()


import turtle

t = turtle.Turtle()

def drag(x, y):
    t.goto(x, y)

def release(x, y):
    t.ondrag(None)
    t.ondrag(drag)

t.ondrag(drag)
t.onrelease(release)
turtle.mainloop()

