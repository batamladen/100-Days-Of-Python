import turtle
import random

wn = turtle.Screen()
wn.setup(width=800, height=600)

COLORS = ["blue", "red", "yellow", "green", "black", "orange", "pink", "purple"]
SPEED = [0, 1, 3, 6, 10]
NUM_TURTLES = 8

def create_turtle(color, y_position):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(-350, y_position)
    t.showturtle()
    return t

# Initialize turtles
turtles = []
start_y = -250
for i in range(NUM_TURTLES):
    color_picker = COLORS[i]
    speed_picker = random.choice(SPEED)
    t = create_turtle(color_picker, start_y + i * 50)
    t.speed(speed_picker)
    turtles.append(t)

# Start the race
race_on = True
while race_on:
    for t in turtles:
        t.forward(random.randint(1, 20))
        # Check if any turtle has crossed the finish line
        if t.xcor() >= 350:
            race_on = False
            print(f"The {t.color()[0]} turtle wins!")
            break

wn.exitonclick()
