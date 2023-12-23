import turtle
import math

screen = turtle.Screen()
screen.setup(800, 800)
screen.setworldcoordinates(-2, -2, 2, 2)

pen = turtle.Turtle()
screen.tracer(0)
pen.hideturtle()
pen.penup()

# def mandelbrot(c, max_iter):
#     z = 0
#     n = 0
#     while abs(z) <= 2 and n < max_iter:
#         z = z*z + c
#         n += 1
#     return n

# max_iter = 20
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         c = complex(x / 100, y / 100)
#         m = mandelbrot(c, max_iter)
#         if m == max_iter:
#             pen.goto(x / 100, y / 100)
#             pen.dot(2, "black")

# screen.mainloop()


def julia(c, z, max_iter):
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

c = complex(-1, 0)
max_iter = 50
for x in range(-200, 200):
    for y in range(-200, 200):
        z = complex(x / 100, y / 100)
        m = julia(c, z, max_iter)
        if m == max_iter:
            pen.goto(x / 100, y / 100)
            pen.dot(2, "black")

screen.mainloop()


