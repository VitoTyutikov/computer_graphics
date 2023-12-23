import turtle


def draw_yinyang(radius):
    # turtle.tracer(0, 0)
    turtle.pensize(3)
    turtle.speed(10)

    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()

    turtle.circle(radius)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(radius, 180)
    # turtle.left(180)
    turtle.end_fill()

    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(radius/2, -180)
    turtle.left(180)
    turtle.end_fill()

    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(radius/2, 180)
    turtle.left(180)
    turtle.end_fill()

    turtle.penup()

    turtle.goto(radius / 15, radius / 2 + 25)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(radius / 15, -radius / 25 - 75)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()


draw_yinyang(200)
