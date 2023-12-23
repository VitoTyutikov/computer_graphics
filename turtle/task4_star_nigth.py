import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("navy")
screen.setup(width=800, height=600)
screen.tracer(0)

def draw_star(x, y):
    star = turtle.Turtle()
    star.hideturtle()
    star.color("white")
    star.penup()
    star.goto(x, y)
    star.begin_fill()
    size = 10
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()
   

for _ in range(100):
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    draw_star(x, y)


moon = turtle.Turtle()
moon.shape("circle")
moon.color("white")
moon.penup()


def move_moon(frame):
    x = frame - 400
    y = -0.001 * x ** 2 + 200
    moon.goto(x, y)

    phase = (frame // 50) % 2
    if phase == 0:
        moon.fillcolor("white")
    else:
        moon.fillcolor("grey")


screen.tracer(1)
moon.hideturtle()
for frame in range(800):
    move_moon(frame)
    moon.showturtle()
    screen.update()

turtle.done()
