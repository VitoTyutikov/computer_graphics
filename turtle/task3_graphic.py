import turtle
import random


def draw_chart():
    turtle.speed('fastest')
    turtle.pensize(3)
    turtle.color("black")
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(600)


def draw_line(price):
    turtle.penup()
    turtle.goto(-300, -200+4*price)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()


def draw_grapf(price):
    draw_chart()
    draw_line(price)
    x = range(-300, 300, 7)
    y = {}
    for i in range(600):
        y[i] = random.randint(-180, 220)
    turtle.goto(-300, -200+4*price)
    turtle.pendown()
    for i in range(len(x)-1):
        k = (y[i]-y[i+1])/(x[i]-x[i+1])

        b = y[i]-k*x[i]
        if y[i] >= -200+4*price and y[i + 1] > -200+4*price:
            turtle.color("green")
            turtle.goto(x[i+1], y[i+1])
        elif y[i] >= -200+4*price and y[i + 1] < -200+4*price:
            turtle.color("green")
            turtle.goto((-200+4*price - b)/k, -200+4*price)
            turtle.color("red")
            turtle.goto(x[i+1], y[i+1])
        elif y[i] < -200+4*price and y[i + 1] > -200+4*price:
            turtle.color("red")
            turtle.goto((-200+4*price - b)/k, -200+4*price)
            turtle.color("green")
            turtle.goto(x[i+1], y[i+1])
        elif y[i] < -200+4*price and y[i + 1] < -200+4*price:
            turtle.color("red")
            turtle.goto(x[i+1], y[i+1])


draw_grapf(50)
turtle.done()


