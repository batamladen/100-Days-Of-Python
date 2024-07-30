import turtle
import random
from circle import draw_circle

COLORS = [(236, 69, 96), (220, 50, 10), (180, 43, 96), (157, 128, 36), (20, 156, 51), (100,150,200)]
turtle.colormode(255)

t = turtle.Turtle()

start_x = -250
start_y = -250
x_axis = start_x
y_axis = start_y

t.speed(0)
t.hideturtle()

for row in range(10):
    for col in range(10):
        color_picker = random.choice(COLORS)
        t.up()
        t.goto(x_axis, y_axis)
        t.down()
        t.begin_fill()
        t.fillcolor(color_picker)
        draw_circle(t)
        t.end_fill()
        x_axis += 50
    x_axis = start_x
    y_axis += 50

turtle.done()
